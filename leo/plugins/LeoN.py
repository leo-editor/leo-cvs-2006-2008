#!/usr/bin/env python2.2
#@+leo-ver=4-thin
#@+node:ekr.20050402080206.8:@thin LeoN.py
#@@first

#@<< docstring >>
#@+node:ekr.20050402080206.9:<< docstring >>
"""
This code correspond to an implementation of a Concurrent Editable Text buffer.

The code is strictly based on the works of Chengzheng Sun.

Actually all the function were written in order to follow as much as possible the notation introduced in his papers. So most of the code is procedure oriented and not strictly pythonic.

Search at citeseer for the files:

    operational_transformation_issues_algorithms_achievements.djvu
    sun98achieving.pdf (<- the must)
    sun97generic.pdf (citeseer.nec.jp.com/sun97generic.htm)
    sun98operational.pdf
    sun98reversible.pdf

You need this documents to understand the code.

This file provide a unit test that execute an instance of the example proposed in the reference papers.

There is also a class named ConcurrentEditableServer that try to implement a 'star' configuration (one server <-> N clients) for the comunications.

I recomend using Leo to explore the code. http://leo.sf.net

Released under GNU GPL. http://www.gnu.org

Rodrigo Benenson. 2003. LeoN project. 

rodrigob at elo dot utfsm dot cl
"""
#@nonl
#@-node:ekr.20050402080206.9:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

#@<< version history >>
#@+node:ekr.20050402080235:<< version history >>
#@+at
# release version 0.0.1 (major, minor, release)
# 
# this version is not supposed to be error prone, but it is good code base.
# -------------------------------------------------------------------------
# 
# 25/06/03 Copying of the main algorithms into the code. RodrigoB.
# 01/07/03 Programming. RodrigoB.
# 02/07/03 Programming. RodrigoB.
# 05/07/03 Reading about the garbage collector stuff. RodrigoB.
# 07/07/03 Programming. RodrigoB.
# 08/07/03 Programming, operations herit from dict, support splitted ops, 
# working on tests, syntax debugging. RodrigoB.
# 09/07/03 Implementing operations relations, starting debug iterations based 
# on unittests.
#          Added another parameters form for receive_operation. RodrigoB.
# 10/07/03 Debugging conceptual aspects; management of timestamps on 
# transformed operations. minor bugs fixed. Splitted special cases 
# appears.RodrigoB.
# 12/07/03 Searching bugs. bugfixes. RodrigoB.
# 13/07/03 Implementing the garbage collector. Searching bugs. bugfixes. 
# Testing garbage collector. RA problems. RodrigoB.
# 14/07/03 (vive la France!) Testing an idea (__eq__). Little edit to the root 
# docustring. RodrigoB.
# 15/07/03 Hunting the Last Bug. Eureka. First successful execution. Code 
# cleanup. Using unittest module. Release 1. RodrigoB.
# 
# 5/4/05 EKR: Converted tabs to blanks.
# 
# Todo
# 
# - Find a good TestConcurrentEditable2 to test LostInformation cases
# 
# - LI is absolutelly not verified
# - Find the Recover_LI specifications.
# - Find a better way to quit the ambiguities on the 'if else {}' operation 
# pertenence. (save_RA, save_LI conditions ?)
# 
# - collect garbage do not work anymore exactly like in the example. (is this 
# a problem ?)
# 
# - Implement ConcurrentEditableServer
# - Implement the  client-server tests
# 
# - Debug.
#@-at
#@@c
#@-node:ekr.20050402080235:<< version history >>
#@nl

#@<<docs>>
#@+node:ekr.20050402080206.10:<<docs>>
#@+others
#@+node:ekr.20050402080206.13:Big picture
#@+at
# Big picture
# -----------
# 
# There is a concurrent editable object that receive commands (operations to 
# realize) associated with the State Vector of the emisor.
# 
# The received command are 'received and delayed to preserve causality' or 
# 'executed'.
# 
# When executed an undo/transform-do/transform-redo scheme is used.
# 
# The transformation of commands (operational transforms) is realized by the 
# GOT algorithm.
# 
# The GOT algorithm use two application specific transformation functions IT, 
# ET (inclusion and exclusion transform, respectively).
# 
# Tadaaa...
#@-at
#@@c
#@-node:ekr.20050402080206.13:Big picture
#@+node:ekr.20050402080206.14:Context (so what?)
#@+at
# so what? -> Why should you care about this code?
# 
# If you want to implement a collaborative text editing software.
# You will need to care about three aspects:
#     - network layer
#     - editor user interface
#     - core logic for collaborative editing
# 
# The python implementation allow a full cross platform usage and a very rapid 
# deployment; considering that there already exist solutions for the network 
# layer (Twisted) and tools to create easilly user interfaces (Tkinter, 
# wxWindows).
# 
# I will enjoy to know about anyone using this code, so please feel free to 
# mail me: <rodrigob at elo dot utfsm dot cl>.
# 
# This code is part of the devellopment of LeoN, the Collaborative Leo plugin. 
# http://leo.sf.net
#@-at
#@@c
#@-node:ekr.20050402080206.14:Context (so what?)
#@-others
#@nonl
#@-node:ekr.20050402080206.10:<<docs>>
#@nl

import types

dbg = 0 # debug level ;p

#@+others
#@+node:ekr.20050402080206.15:ConcurrentEditable
class ConcurrentEditable:
    
    """
    This is the core class.
    It instanciate a Site that contain an editable text.
    Will receive and generate operations.
    The implementation is focused on simplicity and paper similarities.
    """

    #@    @+others
    #@+node:ekr.20050405135819: __init__
    def __init__(self, site_index, num_of_sites):
        
        """
        """
                
        self.site_index   = site_index
        self.state_vector = [0] * num_of_sites
                
        self.state_vector_table   = [[0]* num_of_sites]* num_of_sites # required by the garbage collector (SVT)
        self.minimum_state_vector = [0]*num_of_sites # required by the garbage collector (MSV)
    
        self.state_vector_table [self.site_index] = self.state_vector # link with local state_vector
    
        self.HB = [] # history buffer
        self.delayed_operations = [] 
    
        self.text_buffer = ""
        
        return
    #@-node:ekr.20050405135819: __init__
    #@+node:ekr.20050405135819.1:get_text
    def get_text(self):
        """
        """
    
        return self.text_buffer
    #@nonl
    #@-node:ekr.20050405135819.1:get_text
    #@+node:ekr.20050402080206.16:receive operation
    def receive_operation(self, t_op, *args, **kw):
        """
        can receive operations reciving an Operation object, or being called as : (type, pos, data, {extra args}) 
        receive an operation to execute
        check if it is causally ready
        if not delay it
        else execute it
        if executed check the delayed buffer to check for operation that now can be operated (and so on until no operation is executable)
        ---
        The workflow is receive->apply->execute
        """
    
        if not isinstance(t_op, Operation):
            try:
                assert len(args) == 2
                t_op = Operation(t_op, args[0], args[1])
                for k in kw:
                    t_op[k] = kw[k]
            except:
                raise "Error on receive_operation arguments"
                
        # receive an operation to execute
        if dbg >=1:
            print "Site %i;%s; '%s'; receiving %s"%(self.site_index, self.state_vector, self.get_text(), t_op)
    
        
        if is_causally_ready(t_op, self): 		# check if it is causally ready
            self.apply(t_op) # execute it (apply to local buffer)
                
            # if executed check the delayed buffer to check for operation that now can be operated
            # (and so on until no operation is executable)			
            
            while 1: # uhhh, dangerous
                for tt_op in self.delayed_operations:
                    if is_causally_ready(tt_op, self): 
                        self.apply(tt_op) 
                        self.delayed_operations.remove(tt_op)
                        break # break the 'for'; go back to 'while 1'
                break # end of while 1
    
        else: # if not delay it
            self.delayed_operations.append(t_op)
        
        if dbg >=1:
            print "Site %i; HB %s"%(self.site_index, self.HB)
            print "Site %i;%s; '%s'; delayed_ops: %s\n"%(self.site_index, self.state_vector, self.get_text(), self.delayed_operations)
    
                
        return
    
    receive_op = receive_operation # alias
        
    #@-node:ekr.20050402080206.16:receive operation
    #@+node:ekr.20050402080206.17:apply
    def apply(self, Onew):
        """
        Algorithm 3: The undo/transform-do/transform-redo scheme (sun98generic)
        
        Given a new causally-ready operation Onew , and HB = [EO1,..., EOm,..., EOn ], the following steps are executed:
        
        1. Undo operations in HB from right to left until an operation EOm is found such that EOm => Onew .
        2. Transform Onew into EOnew by applying the GOT control scheme. Then, do EOnew .
        3. Transform each operation EOm+i in HB[m+1,n] into the new execution form EO'm+i as follows:
            - EO'm+1 := IT (EOm+1, EOnew ).
            - For 2 <= i <= (n - m),
                (1) TO := LET (EOm+i, reverse(HB[m+1,m+i - 1]) );
                (2) EO'm+i := LIT (TO, [EOnew, EO'm+1,..., EO'm+i-1 ]).
            Then, redo EO'm+1, EO'm+2, ..., EO'n , sequentially.
        
        After the execution of the above steps, the contents of the history buffer becomes: HB = [EO1,..., EOm, EOnew, EO'm+1,..., EO'n ].
        ---
        This function manage the History Buffer.
        """
    
        assert T(Onew) in ["Insert", "Delete"], "Invalid operation request."
        
        if dbg >=1:
            print "Site %i;%s; '%s'; applying %s"%(self.site_index, self.state_vector, self.get_text(), Onew)
    
    
        HB = self.HB
    
        # 1.
        m = 0 # manage the case HB == []
        undoed = []
        for m in range(len(HB) -1, 0 -1, -1):	 # from right to left
            EOm = HB[m]
            #print "check_total_ordering(%s, %s) => %i"%(EOm, Onew, check_total_ordering(EOm, Onew)) # just for debugging
            if not check_total_ordering(EOm, Onew):
                self.undo(EOm)
                # operations do should not be erased from HB, because they will later be transformed !
                undoed.append(EOm)
            else:
                break
            
        if HB and len(undoed) == len(HB):
            if dbg>=2:
                print "No previous op found !"
            m = -1 # to indicate that no previous op was found
    
        # 2.
        EOnew = GOT( Onew, HB[:m+1]) # pass Onew and HB = [EO1, EO2, ..., EOm ]
        self.execute(EOnew)
        # EOnew will be inserted after step 3 to follow better the paper notation.
        if dbg>=2:
            print "m %i; [EO1, ..., EOm ] %s; HB[m+1:] %s"%(m,  HB[:m+1],  HB[m+1:])
    
        
        # 3.
        if undoed: # if there was an undo, then redo
            if dbg>=1:
                print "Site %i; '%s'; undoed %s; executed %s;"%(self.site_index, self.get_text(), undoed, EOnew) # just for debugging
            EOoL = [] # EO'm+1 List
    
            EOoL.append( IT( HB[m+1], EOnew ) ) 
            for i in range(1, len(undoed)):  # python indexes start from 'zero' (in the paper they start from 'one')
                TO = LET( HB[m+1+i], reverse(HB[m+1: m+i +1])) # paper [m+1,m+i - 1] -> python [m+1:m+i +1]
                EOoL.append( LIT( TO, [EOnew] + EOoL) )
    
            #print "m: %i; len(EOoL) %i;EOoL %s"%(m, len(EOoL), EOoL) # just for debugging
            for i in range(len(EOoL)):			
                t_op = EOoL[i]
                self.execute(t_op)
                HB[m+1+i] = t_op # python indexes start from 'zero'
    
    
        # After the execution of the above steps [...] HB = [EO1,..., EOm, EOnew, EO'm+1,..., EO'n ].
        HB.insert(m + 1, EOnew) # insert into the HB, just after EOm
            
            
        # Update local State vector
        t_index = Onew["source_site"]
        assert t_index < len(self.state_vector), "Received an operation from a source_site outside the state_vector range"
        self.state_vector[t_index] += 1
    
        if EOnew["source_site"] != self.site_index: # local SVT is linked to the local SV
            self.state_vector_table[EOnew["source_site"]] = EOnew["timestamp"] # update state_vector_table
    
        if (len(HB) % 10) == 0: # call the garbage collector (over a dummy periodic condition)
            self.collect_garbage()
    
        return
    #@-node:ekr.20050402080206.17:apply
    #@+node:ekr.20050402080206.18:execute
    def execute(self, EO, splitted_part=0):
        """
        Modify the text buffer.
        The lost information is stored into the operators for future undos.
        """
        
        if EO.get("is_splitted"):
            self.execute(EO["splitted_head"], splitted_part=1)
            self.execute(EO["splitted_tail"], splitted_part=1)
            return
            
        startpos = P(EO)
        data     = EO["data"]
        
        if T(EO) == "Insert":
            t_list = list(self.text_buffer)
            t_list.insert(startpos, data)	
            self.text_buffer = ''.join(t_list)
            
        elif T(EO) == "Delete":
            length = data
            t_text = self.text_buffer
            EO["deleted_text"] = t_text[startpos:(startpos+length)]
            self.text_buffer = ''.join(t_text[:startpos] + t_text[(startpos+length):])	
            
        else:
            raise " Tried to executed an Unmanaged Operation type"
            
        return
    #@nonl
    #@-node:ekr.20050402080206.18:execute
    #@+node:ekr.20050402080206.19:undo
    def undo(self, EO):
        """
        Undo an operation. Return the text to his previous state.
        The undo operation supose that EO is the last operation executed over the buffer.
        """
        
        if EO.get("is_splitted"):
            self.undo(EO["splitted_head"])
            self.undo(EO["splitted_tail"])
            return
    
        if T(EO) == "Delete":
            assert EO.has_key("deleted_text"), "Undoable operation (no undo info stored)"
            self.execute( op("Insert", P(EO), EO["deleted_text"]) ) # create the undo operation and execute it
            
        elif T(EO) == "Insert":
            self.execute( op("Delete", P(EO), len(S(EO)) ) ) # create the undo operation and execute it
            
        else:
            raise "Trying to undo an Unmanaged Operation."
        
        return
    #@nonl
    #@-node:ekr.20050402080206.19:undo
    #@+node:ekr.20050402080206.20:collect_garbage
    def collect_garbage(self):
        """
        Algorithm 4. The garbage collection procedure. sun98achieving (page 18, 19, 20).
        Scan HB from left to right. Let EO be the current operation under inspection.
        Suppose that EO was generated at site i and timestamped by SVEO.
            (1) If SVEO [i] <= MSVk[i], then EO is removed from HB and continue scanning.
            (2) Otherwise stop scanning and return.
            
        (The garbage collection procedure can be invoked periodically, or after processing each remote operation/message, or when the number of buffered operations in HB goes beyond a preset threshold value.)
        """
        # reference asignations (local aliases)
        HB  = self.HB 
        SVT = self.state_vector_table
        MSV = self.minimum_state_vector
        
        # compute the MSV
        for i in range(len(MSV)):
            MSV[i] = min( [ sv[i] for sv in SVT ] )
        
        if dbg >=1:
            print "Site %i; MSV %s; SVT %s;"%(self.site_index, MSV, SVT)
            
        # collect the garbage
        for EO in HB:
            i    = EO["source_site"]
            SVEO = EO["timestamp"]
            
            condition = reduce(lambda x,y: x+y, [ SVEO[i] <= MSV[i] for i in range(len(SVEO))]) == len(SVEO) # bizare but it works
            
            if condition:
                HB.remove(EO)
                if dbg>=1:
                    print "Site %i; removing %s"%(self.site_index, EO)
            else:
                break
    
        return
    
    def update_SVT(self, site_index, state_vector):
        """
        update_StateVectorTable
        
        sun98achievings.pdf, page 19 paragraph 2.
        If one site happens to be silent for an unusually long period of time, other sites will not know what its state is [a 'mostly observer' site]. Therefore, it is required for a site to broadcast a short state message containing its state vector when it has not generated an operation for a certain period of time and/or after executing a certain number of remote operations. Upon receiving a state message from a remote site r, site k simply updates its rth statve vecor in SVTk withe the piggybacked state vector.
        ---
        This function is used as a remote call to broadcast the state message.
        """
        
        self.state_vector_table[site_index] = state_vector
        
        return
    #@nonl
    #@-node:ekr.20050402080206.20:collect_garbage
    #@+node:ekr.20050402080206.21:generate operations
    def generate_operation(self, type, pos, data, **kws):
        """
        The site generate an operation, and apply it locally.
        """
        
        t_SV = list(self.state_vector) # copy the list
        t_SV[self.site_index] += 1
        
        t_op = Operation(type, pos, data, t_SV, self.site_index)
        
        for k in kws.keys():
            t_op[k] = kws[k]
            
        if dbg>=1:
            print "Site %i; generating %s"%(self.site_index, t_op)
        
        self.receive_op(t_op)
        
        return t_op
        
    gen_op = generate_operation # alias
        
    def gen_Op(self, type, data, pos, **kws):
        """
        Alias with another parameters order.
        """
        
        return self.gen_op(type, pos, data, **kws)
    #@-node:ekr.20050402080206.21:generate operations
    #@-others
#@-node:ekr.20050402080206.15:ConcurrentEditable
#@+node:ekr.20050402080206.22:operations relations
#@+at
# Function defined over the operation that return boolean values
#@-at
#@@c
#@+node:ekr.20050402080206.23:causally-ready
def is_causally_ready(t_O, t_site):
    """
    Definition 5: Conditions for executing remote operations

    Let O be an operation generated at site s and timestamped by SVo . O is causally-ready for execution at site d (d != s) with a state vector SVd only if the following conditions are satisfied:
        1. SVo [s] = SVd [s] + 1, and
        2. SVo [i] <= SVd [i], for all i in {0,1, ..., N - 1} and i != s.
    """
    
    SVd = t_site.state_vector
    SVo = t_O["timestamp"]
    s   = t_O["source_site"]
    
    assert len(SVd) == len(SVo) 
    assert type(s) == types.IntType, "The operation has no source site (%s)"%(t_O)
    
    # 1.
    condition1 = ( SVo[s] == SVd[s] + 1 )
    
    #2.
    condition2 = 1
    for i in range(len(SVd)):
        if i == s: continue
        condition2 = condition2 and (SVo[i] <= SVd[i])
    
    
    return condition1 and condition2
#@-node:ekr.20050402080206.23:causally-ready
#@+node:ekr.20050402080206.24:total ordering relation
def check_total_ordering(Oa, Ob):
    """
    Check if Oa => Ob.
    Definition 6: Total ordering relation "=>"
    
    Given two operations Oa and Ob, generated at sites i and j and timestamped by SVOa and SVOb, respectively, then Oa => O b, iff:
        1. sum(SVOa) < sum(SVOb), or
        2. i < j when sum(SVOa) = sum(SVOb),
    
    where sum(SV) = $\sum_{i=0}^{N-1} SV[i]$.	
    """
    
    sum = lambda t_list: reduce(lambda x,y: x+y, t_list)
    
    SVOa = Oa["timestamp"]
    SVOb = Ob["timestamp"]
    
    assert SVOa and SVOb, "can not check operations without timestamp. (Oa:%s; Ob:%s)"%(Oa, Ob)
    
    # 1.
    condition1 = sum(SVOa) < sum(SVOb)
    
    #2.
    i = Oa["source_site"]
    j = Ob["source_site"]
    
    condition2 = (sum(SVOa) == sum(SVOb)) and (i < j)
        
    return condition1 or condition2
#@-node:ekr.20050402080206.24:total ordering relation
#@+node:ekr.20050402080206.25:dependent or independent
#@+at
# Definition 1: Causal ordering relation "->"
# 
# Given two operations Oa and Ob , generated at sites i and j, then Oa -> Ob , 
# iff:
#     1. i = j and the generation of Oa happened before the generation of Ob , 
# or
#     2. i != j and the execution of Oa at site j happened before the 
# generation of Ob , or
#     3. there exists an operation Ox, such that Oa -> Ox and Ox -> Ob.
# 
# Definition 2: Dependent and independent operations
# 
# Given any two operations Oa and Ob.
#     1. Ob is said to be dependent on Oa iff Oa -> Ob.
#     2. Oa and Ob are said to be independent (or concurrent) iff neither Oa 
# -> Ob , nor Ob -> Oa , which is expressed as Oa || Ob.
# 
# (nor == not or; 0,0 => 1 , 0 else)
# 
#@-at
#@@c

def are_dependent(Oa,Ob):
    """
    Implement a less than strict check. Will return true if (Oa->Ob) or if there is a Ox such as (Oa->Ox and Ox->Ob)
    
    After reading in detail the papers I propose:
    Oa -> Ob iff :
        if i==j: return SVoa[i] < SVob[i]
        else:    return SVoa[i] <= SVob[i]
    """
    
    i = Oa["source_site"]
    j = Ob["source_site"]
    
    
    if i == j:
        return Oa["timestamp"][i] <  Ob["timestamp"][i]
    else:
        return Oa["timestamp"][i] <= Ob["timestamp"][i]
    
    return

def are_concurrent(Oa,Ob):
    """
    Check if both operations are independent (or concurrent)
    
    return Oa->Ob nor Ob->Oa
    (nor == not or; 0,0 => 1 , 0 else)
    """	
    return not (are_dependent(Oa,Ob) or are_dependent(Ob,Oa) )
    
    
are_independent = are_concurrent # just an alias
#@nonl
#@-node:ekr.20050402080206.25:dependent or independent
#@-node:ekr.20050402080206.22:operations relations
#@+node:ekr.20050402080206.26:GOT
def GOT( Onew, HB):
    """
    Algorithm 2: The GOT control scheme (sun98generic)

    Given a new causally-ready operation Onew , and HB = [EO1 , EO2, ..., EOm ]. The following steps are executed to obtain EOnew :
    
    1. Scanning the HB from left to right to find the first operation EOk such that EOk || Onew (EOk and Onew are concurrent (or independent)). If no such an operation EOk is found, then EOnew := Onew.
    
    2. Otherwise, search the range of HB[k+1,m] to find all operations which are causally preceding Onew, and let EOL denote these operations. If EOL = [ ], then EOnew := LIT (Onew , HB[k,m]).
    
    3. Otherwise, suppose EOL = [EOc1, ..., EOcr ], the following steps are executed:
        (a) Get EOL' = [EO'c1, ..., EO'cr ] as follows:
            i. EO'c1 := LET (EOc1, reverse(HB[k, c1 - 1]) ):
            ii. For 2 <= i <= r,
                TO := LET (EOci , reverse(HB[k, ci - 1]) );
                EO'ci := LIT (TO, [EO'c1, ..., EO'ci-1]).
        (b) O'new := LET (Onew, reverse(EOL') ).
        (c) EOnew := LIT (O'new, HB[k,m]).
    """
    
    EOnew = Onew # the default result
    
    for k in range(len(HB)):
        EOk = HB[k]
        if are_concurrent(EOk, Onew): 
            EOL = HB[k+1:]; c1 = k+1 
            if EOL == []:
                EOnew = LIT(Onew, HB[k:])
            else:
                # (a) i.
                r = len(EOL) 
                
                EOLl = range(r) # EOLl <=> EOL'
                #print "GOT (a) i.; r %s; (k,c1 - 1) %s; len(HB) %s"%(r, (k,c1 - 1), len(HB)) # just for debugging
                
                EOLl[0] = LET(EOL[0], reverse(HB[k:c1 - 1 +1]))
                    # +1 because in paper notation ranges are incluse, incluse ('[]')
                    # while python they are incluse, exclusive ('[)')
                
                # (a) ii.
                for i in range(1,r):
                    TO = LET(EOL[i], reverse(HB[k: c1 + i - 1 + 1]))
                    EOLl[i] = LIT(TO, EOLl[1:i-1+1])
                
                # (b)
                Oonew = LET(Onew, reverse(EOLl))
                
                # (c)
                EOnew = LIT(Oonew, HB[k:])
            
    return EOnew
#@nonl
#@-node:ekr.20050402080206.26:GOT
#@+node:ekr.20050402080206.27:Transformations
def LIT(O, OL):
    if OL==[]:
        Oo = O
    else:
        Oo = LIT(IT(O, OL[0]), OL[1:])
    
    return Oo
    
def LET(O, OL):
    if OL==[]:
        Oo = O
    else:
        Oo = LET(ET(O, OL[0]), OL[1:])
    
    return Oo
    

def reverse(in_list):
    """
    Helper function used to have a compact notation.
    """
    
    t_list = list(in_list) # create a copy
    t_list.reverse() # in place operator
    
    return t_list
#@nonl
#@+node:ekr.20050402080206.28:IT
def IT (Oa, Ob):
    """
    Inclusion Transform.
    Return a transformed Oa, named Ooa, such that the impact of the independent operation Ob (against Oa) is efectively included into Oa.
    Also define the timestamp of the virtual operation.
    """

    if Check_RA(Oa):
        #print "Check_BO(\n\t%s, \n\t%s \n)\t\t=> %s"%(Oa, Ob, Check_BO(Oa, Ob)) # just for debugging
        if Check_BO(Oa, Ob):
             Ooa = Convert_AA(Oa, Ob)
        else:
             Ooa = Oa 
    elif T(Oa) == "Insert" and T(Ob) == "Insert":
         Ooa = IT_II(Oa, Ob)
    elif T(Oa) == "Insert" and T(Ob) == "Delete":
        Ooa = IT_ID(Oa, Ob)
    elif T(Oa) == "Delete" and T(Ob) == "Insert":
        Ooa = IT_DI(Oa, Ob)
    else: # if T(Oa) == "Delete" and T(Ob) == "Delete"
        Ooa = IT_DD(Oa, Ob)
        
    
    Ooa["source_site"] = Oa["source_site"]
    Ooa["timestamp"]   = list(Oa["timestamp"]) # copy
    
    if dbg>=2:	
        print "IT(\n\t%s, \n\t%s\n)\t\t=> %s;"%(Oa, Ob,Ooa) # just for debugging
        
    return Ooa


def IT_II(Oa, Ob):

    if P (Oa) < P (Ob):
        Ooa = Oa
    else:
        Ooa = Op( "Insert", S(Oa), P(Oa) + L(Ob) )
        
    return Ooa


def IT_ID(Oa, Ob):

    if P(Oa) <= P(Ob):
        Ooa = Oa 
    elif P(Oa) > ( P(Ob) + L(Ob) ):
        Ooa = Op( "Insert",  S(Oa), P(Oa) - L(Ob) )
    else:
        Ooa = Op( "Insert",  S(Oa), P(Ob) )
        
        Save_LI(Ooa, Oa, Ob )
        
    return Ooa

def IT_DI(Oa, Ob):

    if P(Ob) >= (P(Oa) + L(Oa)):
        Ooa = Oa 
    elif P(Oa) >= P(Ob):
        Ooa = Op( "Delete",  L(Oa), P(Oa) + L(Ob) )
    else: 
        Ooa = Splitted( 
                        Op( "Delete", P(Ob) - P(Oa)          , P(Oa)         ),
                        Op( "Delete", L(Oa) - (P(Ob) - P(Oa)), P(Ob) + L(Ob) ) )
    return Ooa

def IT_DD(Oa, Ob):

    if P (Ob) >= (P(Oa) + L(Oa)):
        Ooa = Oa 
    elif P(Oa) >= (P(Ob) + L(Ob)):
        Ooa = Op( "Delete", L(Oa), P(Oa) - L(Ob) )
    else:
        if P(Ob) >= P(Oa) and (P(Oa) + L(Oa)) <= (P(Ob) + L(Ob)):
            Ooa = Op( "Delete", 0, P(Oa) )
        elif P(Ob) <= P(Oa) and (P(Oa) + L(Oa)) > (P(Ob) + L(Ob)):
            Ooa = Op( "Delete", P(Oa) + L(Oa) - (P(Ob)+ L(Ob)), P (Ob) )
        elif P(Ob) > P(Oa) and (P(Ob) + L(Ob)) >= (P(Oa) + L(Oa)):
            Ooa = Op( "Delete", P(Ob) - P (Oa), P(Oa) )
        else:
            Ooa = Op( "Delete", L(Oa) - L(Ob), P(Oa) )
            
        Save_LI(Ooa, Oa, Ob) # this is in the first 'else' # this is a guess
            
    return Ooa



#@-node:ekr.20050402080206.28:IT
#@+node:ekr.20050402080206.29:ET
def ET(Oa, Ob):
    """
    Exclusion Transform.
    Transform Oa against its causally preceding operation Ob to produce Ooa in such a way that Ob's impact on Oa is excluded.
    Also define the timestamp of the virtual operation.
    """
    
    if Check_RA(Oa):
        Ooa = Oa
    elif T(Oa) == "Insert" and T(Ob) == "Insert":
        Ooa = ET_II(Oa, Ob)
    elif T(Oa) == "Insert" and T(Ob) == "Delete":
        Ooa = ET_ID(Oa, Ob)
    elif T(Oa) == "Delete" and T(Ob) == "Insert":
        Ooa = ET_DI(Oa, Ob)
    else: # if T(Oa) == "Delete" and T(Ob) == "Delete":
        Ooa = ET_DD(Oa, Ob)
        
    
    Ooa["source_site"] = Oa["source_site"]
    Ooa["timestamp"]   = list(Oa["timestamp"]) # copy
    
    if dbg>=2:		
        print "ET(\n\t%s, \n\t%s\n)\t\t=> %s;"%(Oa, Ob,Ooa) # just for debugging
    
    return Ooa

def ET_II(Oa, Ob):

    if P(Oa) <= P(Ob) :
        Ooa = Oa
    elif P(Oa) >= (P(Ob) + L(Ob)):
        Ooa = Op( "Insert",  S(Oa), P(Oa) - L(Ob) )
    else:
        Ooa = Op( "Insert",  S(Oa), P(Oa) - P(Ob) )
        Save_RA(Ooa, Ob)
        
    return Ooa

def ET_ID(Oa, Ob):

    if Check_LI(Oa, Ob):
        Ooa = Recover_LI(Oa)
    elif P(Oa) <= P(Ob):
        Ooa= Oa
    else:
        Ooa= Op( "Insert", S(Oa), P(Oa) + L(Ob) )

    return Ooa
    
    
def ET_DI(Oa, Ob):

    if(P(Oa) + L(Oa)) <= P(Ob):
        Ooa = Oa
    elif P(Oa) >= (P(Ob) + L(Ob)):
        Ooa = Op( "Delete", L(Oa), P(Oa) - L(Ob) )
    else:
        if P(Ob) <= P(Oa) and (P(Oa) + L(Oa))  <= (P(Ob) + L(Ob)):
            Ooa = Op( "Delete", L(Oa), P(Oa) - P(Ob) )
        elif P(Ob) <= P(Oa) and ((P(Oa) + L(Oa)) > (P(Ob) + L(Ob))):
            Ooa = Splitted ( Op( "Delete",  P(Ob) + L(Ob) - P(Oa)         ,(P(Oa) - P(Ob)) ),
                                         Op( "Delete", (P(Oa) + L(Oa))-(P(Ob) + L(Ob)), P(Ob)          ) )
        elif P(Oa) < P(Ob) and ((P(Ob) + L(Ob)) <= (P(Oa) + L(Oa))):
            Ooa = Splitted( Op( "Delete", L(Ob)        , 0     ), 
                            Op( "Delete", L(Oa) - L(Ob), P(Oa) ) )
        else:
            Ooa = Splitted( Op( "Delete", P(Oa) + L(Oa) - P(Ob), 0     ), 
                            Op( "Delete", P(Ob) - P(Oa)        , P(Oa) ) )
        
        Save_RA(Ooa, Ob) # this is in the first 'else' # this is a guess
            
    return Ooa



def ET_DD(Oa, Ob):

    if Check_LI(Oa, Ob):
        Ooa = Recover_LI(Oa)
    elif P(Ob) >= (P(Oa) + L(Oa)):
        Ooa = Oa
    elif P(Oa) >= P(Ob) :
        Ooa = Op( "Delete", L(Oa), P(Oa) + L(Ob))
    else :
        Ooa = Splitted( Op( "Delete", P(Ob) - P(Oa)         , P(Oa)         ),
                        Op( "Delete", L(Oa) -(P(Ob) - P(Oa)), P(Ob) + L(Ob) ) )
    return Ooa

#@-node:ekr.20050402080206.29:ET
#@-node:ekr.20050402080206.27:Transformations
#@+node:ekr.20050402080206.30:Operations
class Operation(dict):
    """
    simple object that encapsulate the information and methods related to the operations.
    it is a dictionary with extra methods.
    """
    
    def __init__(self, type=None, pos=None, data=None, timestamp=None, source_site=None):
        
        d = self
        
        d["type"] = str(type)
        d["pos"]  = pos
        d["data"] = data # text or len
            
        d["timestamp"]   = timestamp
        d["source_site"] = source_site
                    
        return

    def __eq__(self, other): 
        """
        The papers do not explain how to manage the TimeStamp of the operations during transforms and do not explain which operations are considered to be equivalents.
        Studying in detail the sequence of transformations that the example generate:
            LIT(ET(O4, ET(EO2, EO1)), [EO1, EO2])
        I deduce that the first approach of using Operations class instances is wrong. Doing that Transformation mutate the operators passed is wrong too.
        If during transform the timestamp are preserved then timestamp and source_site are the unique identifiers of a operation. Then IT(EO, EOx) == ET(EO, EOx) == EO; this is not intuitive but it works.
        ----
        x==y calls x.__eq__(y)
        """
        
        assert isinstance(other, Operation), "Only operations instances can be compared"
        
        return (self["source_site"] == other["source_site"]) and (self["timestamp"] == other["timestamp"])

    def __repr__(self):
        """
        """
        return "%s"%(self)
        
    def __str__(self):
        """
        """
        
        t_keys = filter(lambda x: x not in ["type", "pos", "data", "source_site", "timestamp"], self.keys())
        
        t_string = ""
        
        if self.has_key("source_site") and self.get("timestamp") :
            t_string += "from S%i%s "%(self["source_site"], self["timestamp"])
            
        if type(self["data"]) in types.StringTypes:
            t_data = "'%s'"%(self["data"])
        else:
            t_data = self["data"]
            
        t_string += "%s@%s:%s"%(self["type"], self["pos"], t_data)
         
        for k in t_keys:
                t_string += ", %s:'%s'"%(k, self[k])
            
        return "{%s}"%t_string
        
    def set_timestamp(self, t_SV):
        """
        Save a state vector as the timestamp.
        """
        
        self["timestamp"] = t_SV
        return
        
    def get_timestamp(self):
        """
        return the state vector used as the timestamp.
        """
        return self.get("timestamp")
    
        
# end of class Operation

#@+at
# Dummy function to shortcut the code.
#@-at
#@@c

def Op(type, data, pos): # this one has a diferent parameters order
    """
    Return an instance of the Operation Object.
    """
    return Operation(type, pos, data)
    
def op(type, pos, data):
    """
    Return an instance of the Operation Object.
    """
    return Operation(type, pos, data)


#@+at
# Simple function used in the algorithm (enhance readability and paper 
# notation matching)
#@-at
#@@c

def T(O):
    """
    Return the type of operation ("Insert" or "Delete")
    """
    return O["type"]
        
    
def P(O):
    """
    Return the position where the operation is executed.
    """
    return O["pos"]


def L(O):
    """
    Return length of the deletion operation.
    For safness if the operation is no a deletion it return the length of the inserted text. (stricly it should raise an error...)
    """
    
    data = O["data"] # speed-up
    assert data != None, "Operation has no data! (%s in %s)"%(data, O)
    
    if type(data) == types.IntType:
        return data
    else:
        return len(data)

def S(O):
    """
    Return the string that the insert operation is trying to insert.
    """
    
    assert type(O["data"]) in types.StringTypes, "S(O) is only valid for Insertion operation."
        
    return O["data"]
    
#@+node:ekr.20050402080206.31:Splitted
def Splitted(O1, O2):
    """
    Return an operation that is splitted. (this should considered in function 'execute' and 'undo')
    """
    
    assert T(O1) == T(O2), "Splitted operations are of different types, this is not sane."
    assert not (O1.get("is_splitted") or O1.get("is_splitted") ), "Recursive splitted operation not yet supported" 
        
    Oo = Operation(T(O1))
    Oo["is_splitted"] = 1
    Oo["splitted_head"] = O1
    Oo["splitted_tail"] = O2
    
    
    if P(O1) < P(O2):
        Oo["pos"] =  P(O1)
        Oo["data"] =  ( P(O2) + L(O2) ) - P(O1)
    elif P(O1) > P(O2):
        Oo["pos"] = P(O2)
        Oo["data"] = ( P(O1) + L(O1) ) - P(O2)
    else:
        raise "Weird split P(O1) == P(O2) (%s,%s)"%(O1, O2)
        
    return Oo
#@nonl
#@-node:ekr.20050402080206.31:Splitted
#@+node:ekr.20050402080206.32:Lost Information
# LI refers to "Lost Information".

def Check_LI(Oa, Ob):
    """
    Ob was involved in a information lossing operation that afected Oa ?
    """
    
    return 	Oaa.get("LI_reference_op") == Ob
    
    
def Save_LI(Oaa, Oa, Ob):
    """
    Store in Oaa the information related to the paremeters of Oa and the reference to Ob.
    
    One operation can only store one and only one information lose.
    """
    
    copy_Oa = op(Oa["type"], Oa["pos"], Oa["data"] )
    
    Oaa["lost_information"]     = copy_Oa
    Oaa["LI_reference_op"]      = Ob
    
    return


def Recover_LI(Oa):
    """
    >>>>>>>>>>>>>>>>>DID NOT FOUND SPECIFICATION (this could cause horrible errors)<<<<<<<<<<<<<<<<<<
    """
    
    return 	Oa["lost_information"]
#@nonl
#@-node:ekr.20050402080206.32:Lost Information
#@+node:ekr.20050402080206.33:Relative Address
def Check_RA(Oa):
    """
    Is Oa relatively addressed ?
    """
    
    return Oa.has_key("relatively_addressed") and Oa["relatively_addressed"]
    
def Save_RA(Oa, Ob):
    """
    Stores the information to mark Oa as having a relative address to over Ob.
    """
    
    #print "called Save_RA(%s, %s)"%(Oa, Ob) # just for debugging
    
    Oa["relatively_addressed"] = 1
    Oa["base_operation"] = Ob
    Oa["delta_pos"] = P(Oa) - P(Ob) # Abis = P(Obbis) + A.delta_pos
    
    return
    
def Check_BO(Oa, Ob):
    """
    Ob is the base operation of Oa ? (in the relative address context)
    """
    
    #Ox = Oa.get("base_operation")
    #return (Ox["source_site"] == Ob["source_site"]) and (Ox["timestamp"] == Ob["timestamp"])
    
    return Ob == Oa.get("base_operation") # look at the definition of __eq__ in the Operation class

def Convert_AA(Oa, Ob):
    """
    Obtain Oaa, which is an absolute address operation based on Oa, over the relative position of Ob.
    """
    
    assert Check_BO(Oa,Ob), "Convert_AA: Ob is not the base_operation of Oa"
    
    #print "called Convert_AA(%s, %s)"%(Oa, Ob) # just for debugging
    
    Oaa = op( Oa["type"],	Oa["delta_pos"] + Ob["pos"], Oa["data"] )
    
    return Oaa
#@nonl
#@-node:ekr.20050402080206.33:Relative Address
#@-node:ekr.20050402080206.30:Operations
#@+node:ekr.20050402080206.34:ConcurrentEditableServer
class ConcurrentEditableServer:
    """
    Manage the request from different client, giving them the ilussion that there are only two sites. Here and There.
    ---
    The server receive an operation, transform it and apply it. Send it show this new operation executed as if it was a locally executed operation and send it to all the users that are hearing it.
    """
    
    def __init__():
        """
        """
        # create state_vectors
        
        # create the local buffer
        
        return
        
        
    def add_client():
        """
        """
        return
        
    def del_client():
        """
        """
        return
#@-node:ekr.20050402080206.34:ConcurrentEditableServer
#@+node:ekr.20050402080206.35:Tests
#@+at
# The unit tests for concurrent editions.
#@-at
#@@c


def Tests():
    """
    run the tests
    """
    
    global dbg
    dbg = 0
    
    if 0: # hand made unittest 
        print "Starting tests"
        TestConcurrentEditable1()
        print "-"	* 30
        TestConcurrentEditable2()
        print "-"	* 30	
        TestConcurrentEditableServer()
        print "end of tests"
        return



    import unittest
    

    TestSuite = unittest.TestSuite()
    TestSuite.addTest(unittest.FunctionTestCase(TestConcurrentEditable1))
    TestSuite.addTest(unittest.FunctionTestCase(TestConcurrentEditable2))
    TestSuite.addTest(unittest.FunctionTestCase(TestConcurrentEditableServer))
    
    unittest.TextTestRunner().run(TestSuite)
    
    return
#@nonl
#@+node:ekr.20050402080206.36:TestConcurrentEditable1
def TestConcurrentEditable1():
    """
    The test case that we gonna use for debugging is the same case presented at "A generic operation transformation scheme for consistency maintenance in real-time cooperative editing systems", Fig 1; wich suggest an interesing scenario.
    Here the operatations are:
        - O1 Insert 0 "ABC"
        - O2 Insert O "BCD"
        - O3 Delete 1 2
        - O4 Insert 2 "c"
    So the final result should be "ABCcD" in the three sites.
    
    Site 0: (generate O1) O1 O2 O4 O3
    Site 1: (gen O2) O2 O1 (gen O3) O3 O4
    Site 2: O2 (gen 04) 03 01
    
    The event sequence is:
        S0(O1);S1(O2);S2O2;S1O1;S0O2;S2(O4);S0O4;S1(03);S2O3;S0O3;S1O4;S2O1. 
        
    It also test the garbage collector as indicated in the figure 3 of sun98achieving.pdf, page 20.
    """
    
    print "-"*15
    print "Read docstring of TestConcurrentEditable for more info about this test.\n"
    
    # Create three site instances
    num_sites = 3
    site0 = ConcurrentEditable(0, num_sites) # site_index, num_of_sites
    site1 = ConcurrentEditable(1, num_sites)
    site2 = ConcurrentEditable(2, num_sites)
    
    # Apply the operations in each site (following the order of the picture)
    
    O1 = site0.gen_op("Insert", 0, "ABC", dbg_name="O1")  # generate and apply locally the operation
    O2 = site1.gen_Op("Insert", "BCD", 0, dbg_name="O2") # test the alias
    site2.receive_op(O2)
    site1.receive_op(O1)
    site0.receive_op(O2)
    O4 = site2.gen_op("Insert", 2, "c", dbg_name="O4") 
    site0.receive_op(O4)			
    #print "\ntest blocked..."; return # please erase this line
    O3 = site1.gen_op("Delete", 1, 2, dbg_name="O3")
    site2.receive_op(O3)
    site0.receive_op(O3)
    site1.receive_op(O4)			
    site2.receive_op(O1)
    
    
    if dbg>=4:
        for t_op in [ O1, O2, O3, O4]:
            print t_op
            
    if 1:
        # this messages are the same of figure 3. sun98achieving.pdf, page 20.
        site1.update_SVT(0, site0.state_vector) # message to put to date the other sites
        site2.update_SVT(0, site0.state_vector)

        site0.collect_garbage()
        site1.collect_garbage()
        site2.collect_garbage()

    if dbg>=1:
        print "\nFinal HBs"
        for t_site in [site0, site1, site2]:
            print "Site %i;%s;HB %s"%(t_site.site_index, t_site.state_vector, t_site.HB)
    
    # Show the final result at each site (expecting "ABCC'D")

    res_text = lambda x: "OK."*x or "FAILED."*(not x)

    print "\nFinal results:"	
    
    success = 1
    for t_site in [site0, site1, site2]:
        t_res = (t_site.get_text() == "ABCcD" and not t_site.delayed_operations)
        success = success and t_res
        print "Site %i;%s; '%s'; delayed_ops: %s; %s"%(
            t_site.site_index,
            t_site.state_vector,
            t_site.get_text(),
            t_site.delayed_operations,
            res_text(t_res))

    if success:
        print "\nTest successfull."
    else:
        print "\nTest FAILED. Expecting the same result at the three sites: 'ABCcD', and no delayed operations left in the buffer."

    return success
#@-node:ekr.20050402080206.36:TestConcurrentEditable1
#@+node:ekr.20050402080206.37:TestConcurrentEditable2
def TestConcurrentEditable2():
    """
    Second test is similar to Test1 but with other operations. Try to test other code areas (i.e. Lost Information cases)
    
    The test case that we gonna use for debugging is the same case presented at "A generic operation transformation scheme for consistency maintenance in real-time cooperative editing systems", Fig 1; wich suggest an interesing scenario.
    Here the operatations are:
        - O1 Insert 0 "ABC"
        - O2 Insert O "BCD"
        - O3 Insert 5 "c"
        - O4 Delete 0 3
    So the final result should be ABCc in the three sites.
    
    Site 0: (generate O1) O1 O2 O4 O3
    Site 1: (gen O2) O2 O1 (gen O3) O3 O4
    Site 2: O2 (gen 04) 03 01
    
    The event sequence is:
        S0(O1);S1(O2);S2O2;S1O1;S0O2;S2(O4);S0O4;S1(03);S2O3;S0O3;S1O4;S2O1. 
        
    It also test the garbage collector as indicated in the figure 3 of sun98achieving.pdf, page 20.
    """
    
    print "-"*15
    print "Read docstring of TestConcurrentEditable for more info about this test.\n"
    
    # Create three site instances
    num_sites = 3
    site0 = ConcurrentEditable(0, num_sites) # site_index, num_of_sites
    site1 = ConcurrentEditable(1, num_sites)
    site2 = ConcurrentEditable(2, num_sites)
    
    # Apply the operations in each site (following the order of the picture)
    
    O1 = site0.gen_op("Insert", 0, "ABC", dbg_name="O1")  # generate and apply locally the operation
    O2 = site1.gen_Op("Insert", "BCD", 0, dbg_name="O2") # test alias
    site2.receive_op(O2)
    site1.receive_op(O1)
    site0.receive_op(O2)
    O4 = site2.gen_op("Delete", 0, 3, dbg_name="O3")
    site0.receive_op(O4)			
    #print "\ntest blocked..."; return # please erase this line
    O3 = site1.gen_op("Insert", 5, "c", dbg_name="O4")
    site2.receive_op(O3)
    site0.receive_op(O3)
    site1.receive_op(O4)			
    site2.receive_op(O1)
    
    if 1:
        # this messages are the same of figure 3. sun98achieving.pdf, page 20.
        site1.update_SVT(0, site0.state_vector) # message to put to date the other sites
        site2.update_SVT(0, site0.state_vector)

        site0.collect_garbage()
        site1.collect_garbage()
        site2.collect_garbage()
    
    if dbg>=4:
        for t_op in [ O1, O2, O3, O4]:
            print t_op
    
    if dbg>=1:
        print "\nFinal HBs"
        for t_site in [site0, site1, site2]:
            print "Site %i;%s;HB %s"%(t_site.site_index, t_site.state_vector, t_site.HB)
    
    # Show the final result at each site (expecting "ABCC'D")

    res_text = lambda x: "OK."*x or "FAILED."*(not x)

    print "\nFinal results:"	
    
    success = 1
    for t_site in [site0, site1, site2]:
        t_res = (t_site.get_text() == "ABCc" and not t_site.delayed_operations)
        success = success and t_res
        print "Site %i;%s; '%s'; delayed_ops: %s; %s"%(
            t_site.site_index, t_site.state_vector,
            t_site.get_text(), t_site.delayed_operations,
            res_text(t_res))

    if success:
        print "\nTest successfull."
    else:
        print "\nTest FAILED. Expecting the same result at the three sites: 'ABCc', and no delayed operations left in the buffer."

    return success
#@nonl
#@-node:ekr.20050402080206.37:TestConcurrentEditable2
#@+node:ekr.20050402080206.38:TestConcurrentEditableServer
def TestConcurrentEditableServer():
    """
    """
    
    return 1
#@nonl
#@-node:ekr.20050402080206.38:TestConcurrentEditableServer
#@-node:ekr.20050402080206.35:Tests
#@-others

if __name__ == "__main__":

    Tests()

#@-node:ekr.20050402080206.8:@thin LeoN.py
#@-leo
