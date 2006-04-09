#@+leo-ver=4-thin
#@+node:leo4u.20040924131405.1:@thin Tknotebook.py
'''A simple Tkinter notebook-like widget'''

#@@language python
#@@tabwidth -4

#@<< about this code >>
#@+node:ekr.20051109024443:<< About this code >>
#@+at 
#@nonl
# Out of envy of more advanced GUI toolkits, I wondered if it isn't possible 
# to
# simulate a notebook widget using standard Tkinter frames and radiobuttons. 
# It
# turns out that it is indeed, by the employment of some odd Tk corners, like 
# the
# "indicatoron" radiobutton option (which reverts the radiobutton default
# appearance to the normal button one) and the forget() frame method, which 
# allows
# easily swapping of "screens" (app frames) back and forth from the notebook
# "screen" area.
# 
# To convert an existing single-toplevel Tkinter app to a notebook-based one, 
# it
# is necessary to change only the master frame root (usually a toplevel) to 
# the
# one provided by the notebook (the 'n()' on the example code).
# 
# Since all references to the external frames are kept implicitly in closures
# (lambdas), it is not very easy to implement a frame exclusion method with 
# the
# current structure (apart from destroying radiobuttons, which isn't very
# elegant), but I think such method is not relevant in this case and would add
# unnecessary complexity. One alternative would be to keep the frames' 
# references
# on a list indexed by the radiobutton's binding var (self.choice), then
# destroy()ing the frames bound for exclusion and their companion 
# radiobuttons.
# 
# References:
# "An Introduction to Tkinter", Fredrik Lundh
# "Practical programming in Tcl and Tk", Brent Welsh
# 
#@-at
#@-node:ekr.20051109024443:<< About this code >>
#@nl
#@<< notes >>
#@+node:ekr.20051109024443.1:<< notes >>
#@+at
# 
# Last Updated: 2003/03/12 Version no: 1.2
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/188537
# Copyright 2003, Iuri Wickert (iwickert yahoo.com)
# 
# You have some single-toplevel Tkinter apps that you want to organize in a
# notebook-like fashion, associating each tab to an app, in a way which 
# requires
# minimal changes in your original apps. This simple notebook class allows 
# that,
# also supporting different tab orientations (TOP, BOTTOM, LEFT & RIGHT).
# 
# f04924a09:15:39 convert to Leo outline for TabbedLog use instead of PMW
# its add doesnt retrn anything and expects the frame to add
# doesnt have a pack method. URLLiaf and Leo Log use will require changes
# need to be able to ask for a list of tabs and to delete a tab
# send msg to tab
# 
# complicated by the fact PMW is way too hard to follow to copy
# and TKnotebook doesn't seem to keep refrences to its frames
# also it could use a wrap feature if more tab than can fit
# rearranging tabs should be possible drag & drop
# a tab of tabs should be supported with d&d between them
# 
# on the sholders of giants, as they say.
# e
#@-at
#@-node:ekr.20051109024443.1:<< notes >>
#@nl
#@<< imports >>
#@+node:leo4u.20040924131405.2:<< imports >>
import leoGlobals as g
import Tkinter as Tk
#@nonl
#@-node:leo4u.20040924131405.2:<< imports >>
#@nl

#@+others
#@+node:leo4u.20040924131405.3:class notebook
class notebook:

    #@	@+others
    #@+node:leo4u.20040924131405.4:__init__
    def __init__ (self,master,side='left'):
    
        self.active_fr = None
        self.count = 0
        self.choice = Tk.IntVar(0)
    
        # Set the positioning for radiobuttons. (seems backward)
        self.side = g.choose(side in ('top','bottom'),'left','top')
    
        # Creates notebook's frames structure
        self.rb_fr = Tk.Frame(master,bd=2,relief='ridge')
        self.rb_fr.pack(side=side,fill='both')
    
        self.screen_fr = Tk.Frame(master,bd=2,relief='ridge')
        self.screen_fr.pack(fill='both')
    #@nonl
    #@-node:leo4u.20040924131405.4:__init__
    #@+node:leo4u.20040924131405.5:__call__
    def __call__(self ):
    
        # return a master frame reference for the external frames (screens)
    
        return self.screen_fr
    #@-node:leo4u.20040924131405.5:__call__
    #@+node:leo4u.20040924131405.6:add_screen
    def add_screen (self,fr,title):
    
        '''Add a new frame (screen) to the (bottom/left) of the notebook.'''
    
        b = Tk.Radiobutton(self.rb_fr,text=title,indicatoron=0,
            variable = self.choice, value = self.count,
            command = lambda: self.display(fr))
    
        b.pack(expand=0,fill='y',side=self.side)
    
        # Ensure the first frame will be the first selected/enabled
        if not self.active_fr:
            fr.pack(expand=1,fill='both')
            self.active_fr = fr
    
        self.count += 1
    
    #@-node:leo4u.20040924131405.6:add_screen
    #@+node:leo4u.20040924135048:add
    def add (self,tabName):
    
        '''Add a new frame for compatibility w/TabbedLog.'''
    
        f = Tk.Frame(self.rb_fr)
        self.add_screen(f,tabName)
        return f
    #@nonl
    #@-node:leo4u.20040924135048:add
    #@+node:leo4u.20040924131405.7:display
    def display(self,fr):
        
        '''Hide the previous frame and show a new frame.'''
    
        # hides the former active frame and shows 
        # another one, 
    
        self.active_fr.forget()
        fr.pack(expand=1,fill='both')
        
        # keep its reference!
        self.active_fr = fr
    #@nonl
    #@-node:leo4u.20040924131405.7:display
    #@-others
#@nonl
#@-node:leo4u.20040924131405.3:class notebook
#@+node:leo4u.20040924133052:test
def test (parent=None):
    # simple demonstration of the Tkinter notebook
    
    a = parent or Tk.Tk()
    
    nb = notebook(a,'top')

    # uses the notebook's frame
    f1 = Tk.Frame(nb())
    b1 = Tk.Button(f1,text="Button 1")
    e1 = Tk.Entry(f1)

    # pack your widgets before adding the frame 
    # to the notebook (but not the frame itself)!
    b1.pack(fill='both',expand=1)
    e1.pack(fill='both',expand=1)

    f2 = Tk.Frame(nb())
    b2 = Tk.Button(f2,text='Button 2')
    b3 = Tk.Button(f2,text='Beep 2',command=lambda: Tk.Tk.bell(a))
    b2.pack(fill='both',expand=1)
    b3.pack(fill='both',expand=1)

    f3 = Tk.Frame(nb())

    nb.add_screen(f1,"Screen 1")
    nb.add_screen(f2,"Screen 2")
    nb.add_screen(f3,"dummy")
    a.mainloop()
#@nonl
#@-node:leo4u.20040924133052:test
#@-others
#@nonl
#@-node:leo4u.20040924131405.1:@thin Tknotebook.py
#@-leo
