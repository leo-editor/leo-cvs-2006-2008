#@+leo-ver=4-thin
#@+node:mork.20041022155742.1:@thin nodebar.py
"""nodebar adds buttons at the bottom of the tree canvas.

The buttons correspond to commands found in the Outline commands. It is intended
to speed up a new users ability to use the outline. Experienced users may find
value in being able to quickly execute commands they do not use very often"""

#@<< imports >>
#@+node:ekr.20041030084334:<< imports >>
import leoGlobals as g
import leoPlugins

load_ok=True
try:
    import Pmw
    import weakref
    import Tkinter as Tk
    import ConfigParser
    import os.path
except Exception, x:
    g.es( 'Could not load because of %s' % x )
    load_ok = False
#@nonl
#@-node:ekr.20041030084334:<< imports >>
#@nl
#@<<images>>
#@+node:mork.20041022160850:<<images>>

nodeup = r'''R0lGODlhEAAQAIABAENMzf///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAhqM
j6nL7QDcgVBS2u5dWqfeTWA4lqYnpeqqFgA7'''

nodeupPI = Tk.PhotoImage( data = nodeup )

nodedown = r'''R0lGODlhEAAQAIABAENMzf///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAhuM
j6nL7Q2inLTaGW49Wqa+XBD1YE8GnOrKBgUAOw=='''

nodedownPI = Tk.PhotoImage( data = nodedown )

nodeleft = r'''R0lGODlhEAAQAIABAENMzf///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAiOM
jwDIqd3Ug0dOam/MC3JdfR0jjuRHBWjKpUbmvlIsm65WAAA7'''

nodeleftPI = Tk.PhotoImage( data = nodeleft )

noderight = r'''R0lGODlhEAAQAIABAENMzf///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAiGM
A3DLltrag/FMWi+WuiK9WWD4gdGYdenklUnrwqX8tQUAOw=='''

noderightPI = Tk.PhotoImage( data = noderight )

clone = r'''R0lGODlhEAAQAIABAP8AAP///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAhaM
j6nL7Q8jBDRWG8DThjvqSeJIlkgBADs='''

clonePI = Tk.PhotoImage( data = clone )


copy = r'''R0lGODlhEAAQAMIEAAAAAI9pLOcxcaCclf///////////////ywAAAAAEAAQAAADLEi63P5vSLiC
vYHiq6+wXSB8mQKcJ2GNLAssr0fCaOyB0IY/ekn9wKBwSEgAADs='''

copyPI = Tk.PhotoImage( data = copy )

cut = r'''R0lGODlhEAAQAKECAAAAAKCclf///////yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAA
EAAAAiaUDad7yS8cnDNYi4A0t7vNaCLTXR/ZZSBFrZMLbaIWzhLczCxTAAA7'''

cutPI = Tk.PhotoImage( data = cut )


paste = r'''R0lGODlhEAAQAKECAAAAAB89vP///////yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAA
EAAAAiOUH3nLktHYm9HMV92FWfPugQcgjqVBnmm5dsD7gmsbwfEZFQA7'''

pastePI = Tk.PhotoImage( data = paste )


insert = r'''R0lGODlhEAAQAKECAAAAAB89vP///////ywAAAAAEAAQAAACKJRhqSvIDGJ8yjWa5MQ5BX4JwXdo
3RiYRyeSjRqKmGZRVv3Q4M73VAEAOw=='''

insertPI = Tk.PhotoImage( data = insert )

demote = r'''R0lGODlhEAAQAKECACMj3ucxcf///////yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAA
EAAAAiiUj2nBrNniW+G4eSmulqssgAgoduYWeZ+kANPkCsBM1/abxLih70gBADs='''

demotePI = Tk.PhotoImage( data = demote )

promote = r'''R0lGODlhEAAQAKECACMj3ucxcf///////yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAA
EAAAAiWUj6kX7cvcgy1CUU1ecvJ+YUGIbKSJAAlqqGQLxPI8t29650YBADs='''

promotePI = Tk.PhotoImage( data = promote )

pasteclone = r'''R0lGODlhEAAQAKEDACMj3v8AAP/9/f///ywAAAAAEAAQAAACOJSPaTPgoxBzgEVDM4yZbtU91/R8
ClkJzGqp7MK21rcG9tYedSCb7sDjwRLAGs7HsPF8khjzcigAADs='''

pasteclonePI = Tk.PhotoImage( data = pasteclone )

hoist = r'''R0lGODlhEAAQAKECAAAAAENMzf/9/f/9/SwAAAAAEAAQAAACI5SPaRCtypp7S9rw4sVwzwQYW4ZY
JAWhqYqE7OG+QvzSrI0WADs='''

hoistPI = Tk.PhotoImage( data = hoist )

dehoist = r'''R0lGODlhEAAQAKECAAAAACMj3v/9/f/9/SH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAA
EAAAAiOUj6lrwOteivLQKi4LXCcOegJIBmIZLminklbLISIzQ9hbAAA7'''

dehoistPI = Tk.PhotoImage( data = dehoist )

question = r'''R0lGODlhEAAQAIABAB89vP///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAiCM
DwnHrNrcgzFQGuGrMnGEfdtnjKRJpt2SsuxZqqgaFQA7'''

sortchildren = r'''R0lGODlhEAAQAKECAAAAAB89vP/9/f/9/SwAAAAAEAAQAAACJJSPKcGt2NwzbKpqYcg68oN9ITde
UQCkKgCeCvutsDXPk/wlBQA7'''

sortchildrenPI = Tk.PhotoImage( data = sortchildren )

sortsiblings = r'''R0lGODlhEAAQAKECAAAAAB89vP/9/f/9/SH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAA
EAAAAiWUFalxbatcS7IiZh3NE2L+fOAGXpknal4JlAIAw2Br0Fksu1YBADs='''

sortsiblingsPI = Tk.PhotoImage( data = sortsiblings )

questionPI = Tk.PhotoImage( data = question )

delete = r'''R0lGODlhEAAQAMIEAAAAAB89vKCclbq3sv///////////////yH+FUNyZWF0ZWQgd2l0aCBUaGUg
R0lNUAAsAAAAABAAEAAAAzJIutwKELoGVp02Xmy5294zDSSlBAupMleAEhoYuahaOq4yCPswvYQe
LyT0eYpEW8iRAAA7'''

deletePI = Tk.PhotoImage( data = delete )

#@-node:mork.20041022160850:<<images>>
#@nl
#@<<images2>>
#@+node:mork.20041023210407:<<images2>>
moveup = r'''R0lGODlhEAAQAIABAENMzf///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAh6M
j6nL7QDcgVDWcFfGUW3zfVPHPZHoUeq6Su4LwwUAOw=='''

moveupPI = Tk.PhotoImage( data = moveup )

movedown = r'''R0lGODlhEAAQAIABAENMzf///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAh+M
j6nL7Q2inFS+EDFw2XT1eVsSHmGJdChpXesFx00BADs='''

movedownPI = Tk.PhotoImage( data = movedown )

moveleft = r'''R0lGODlhEAAQAIABAENMzf///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAiWM
jwDIqd3egueFSe2lF2+oGV41fkwoZmNJJlxXvbDJSbKI1l4BADs='''

moveleftPI = Tk.PhotoImage( data = moveleft )

moveright = r'''R0lGODlhEAAQAIABAENMzf///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAABAAEAAAAiWM
A3DLltqaSpFBWt3BFTovWeAyIiUinSNnkaf2Zagpo2x343IBADs='''

moverightPI = Tk.PhotoImage( data = moveright )
#@nonl
#@-node:mork.20041023210407:<<images2>>
#@nl
__version__ = ".7"
#@<<version>>
#@+node:mork.20041023091529:<<version>>
#@+at
# 
# .1 made initial icons
# 
# .15 eliminated most of the letter icons, made them node based icons.
# 
# .2 EKR:
#     - Fixed hang when help dialog selected.
#     - Write help string to status area on mouse over.
#     - Added test for if g.app.gui.guiName() == "tkinter"
# 
# .25 added movement arrows.  These contrast with the move node arrows by 
# being empty and on the other side of the nodebar.  A user may be able to do 
# all the manipulations he needs of the outline at this point.  Note:  the bar 
# is of such a size we may need to add some kind of scrolling mechanism.  Not 
# sure if I like the hoist and dehoist icons yet. ????
# 
# --tried out scrollbar idea, what a terrible idea.  The user is just going to 
# have to have a big enough screen to use it. :D
# 
# .3 Added balloon help.  Should help new users.  Added .config file machinery
# 
# .4 EKR:
#     - Put load_ok code in root.  Added string.atoi = int
# 
# .5 EKR
#     - Defined __version__
# .6 EKR:
#     - Changed 'new_c' logic to 'c' logic.
#     - Added init function.
# .7 EKR:
#     - Removed 'start2' hook.
#     - Removed haveseen dict.  It is no longer needed.
#@-at
#@nonl
#@-node:mork.20041023091529:<<version>>
#@nl
#@<<How To Configure>>
#@+node:mork.20041026092203:<<How To Configure>>
#@+at
# 
# 1rst there needs to be a config file in the plugins directory called 
# nodebar.ini
# 
# in this file there needs to be a section with this headline:
# [ nodebar ]
# 
# under this headline there needs to be these two options
# position
# usehelp
# 
# ----
# position should be set to 1 of 3 values:
# position=1
# position=2
# position=3
# 
# 1, means add the nodebar to the icon area of Leo( this is the default )
# 2, means add the nodebar underneath the tree area
# 3, means add the nodebar underneath the editor area
# 
# -----
# usehelp should be set to either 0 or 1:
# usehelp=0
# usehelp=1
# 
# 0, means do not use balloon help when the arrow goes over the nodebar( this 
# is the default )
# 1, means use the balloon help when the arrow goes over the nodebar
# 
# ------
# nodebar will create a .ini file for the user if there isn't one already.
# 
# If there are problems in the .ini file, nodebar should sail on using the 
# default values.
#@-at
#@nonl
#@-node:mork.20041026092203:<<How To Configure>>
#@nl

#@+others
#@+node:ekr.20050311090939.5:init
def init():
    
    if load_ok: # Ok for unit test.

        configureNodebar()
        
        if g.app.gui is None: 
            g.app.createTkGui(__file__)
    
        if g.app.gui.guiName() == "tkinter":
            leoPlugins.registerHandler(('open2',"new"),addNodeBar )
            g.plugin_signon(__name__)
            
    return load_ok
#@nonl
#@-node:ekr.20050311090939.5:init
#@+node:mork.20041026090227:determineFrame
def determineFrame( c ):
    '''Returns the area in Leo where the user wants the nodebar.  Default to are 1'''
    cpos = config[ pos ]
    
    if cpos == '2':
        frame = c.frame.split2Pane1
    elif cpos == '3':
        frame = c.frame.split1Pane2
    else: #Should be area 1.  If its something else we use area 1.
        frame = c.frame.iconFrame 

    return frame
#@nonl
#@-node:mork.20041026090227:determineFrame
#@+node:mork.20041022160305:addNodeBar
def addNodeBar( tag, keywords ):
    '''Add nodebar to new frame'''
    c = keywords.get( 'c' )
    if not c: return

    frame = determineFrame( c )
    mbox = Tk.Frame( frame )
    mbox.pack( side = 'bottom' , fill = 'x' )
    for z in frame.children.values():
        mbox.pack_configure( before = z )
        
    def goToChild( c = c ):
        pos = c.currentPosition()
        if pos.hasChildren():
            c.selectPosition( pos.nthChild( 0 ) )
            
    bcommands = ( 
                  ( c.moveOutlineUp, nodeupPI, 'Move Node Up' ),
                  ( c.moveOutlineDown, nodedownPI , 'Move Node Down' ),
                  ( c.moveOutlineLeft, nodeleftPI , 'Move Node Left' ),
                  ( c.moveOutlineRight, noderightPI, 'Move Node Right' ),
                  ( c.clone, clonePI , 'Clone Node' ),
                  ( c.copyOutline, copyPI, 'Copy Node' ),
                  ( c.cutOutline, cutPI, 'Cut Node' ),
                  ( c.deleteOutline, deletePI, 'Delete Node' ),
                  ( c.pasteOutline, pastePI , 'Paste Node' ),
                  ( c.pasteOutlineRetainingClones, pasteclonePI, 'Paste Retaining Clones' ),
                  ( c.insertHeadline, insertPI, 'Insert Node' ),
                  ( c.demote, demotePI, 'Demote' ),
                  ( c.promote, promotePI , 'Promote' ) ,
                  ( c.hoist, hoistPI, 'Hoist'),
                  ( c.dehoist, dehoistPI, 'De-Hoist' ),
                  ( c.sortChildren, sortchildrenPI, 'Sort Children' ),
                  ( c.sortSiblings, sortsiblingsPI, 'Sort Siblings' ),
                  ( c.goToPrevSibling, moveupPI, 'Goto Previous Sibling' ),
                  ( c.goToNextSibling, movedownPI, 'Goto Next Sibling' ),
                  ( c.goToParent, moveleftPI, 'Goto Parent' ),
                  ( goToChild, moverightPI, 'Goto Child' ),
                  )
    for i, z in enumerate( bcommands ):
        add( c, mbox ,i, *z )       
        
    #@    << Create the help button >>
    #@+node:mork.20041026100755:<< Create the help button >>
    ques = Tk.Button( mbox, image = questionPI, 
        command = lambda c = c, items = bcommands: view_help(c,items) )    
    ques.grid( column = i + 1, row = 1 ) 
    
    if int( config[ help ] ):
        addBalloon( mbox, ques, "Help" )
    
    def callback(event,c=c ):
        c.frame.clearStatusLine()
        c.frame.putStatusLine("Open Help Dialog")
    
    ques.bind("<Enter>",callback, '+' )
    #@nonl
    #@-node:mork.20041026100755:<< Create the help button >>
    #@nl
#@nonl
#@-node:mork.20041022160305:addNodeBar
#@+node:mork.20041022172156:add
def add( c, frame, column, command, image, text ):
    '''Add a button to the nodebar'''
    b = Tk.Button( frame, command = command , image = image )
    b.grid( column = column , row = 1)
    if int( config[ help ] ):
        addBalloon( frame, b, text )
    
    def callback(event,c=c,s=text):
        c.frame.clearStatusLine()
        c.frame.putStatusLine(s)
    
    b.bind("<Enter>",callback, '+' )
#@nonl
#@-node:mork.20041022172156:add
#@+node:mork.20041026083725:addBalloon
balloons = {}
def addBalloon( frame, widget, text ):
    '''Help ballon is added to a frame and text is bound to a specific widget'''
    if not balloons.has_key( frame ):
        balloons[ frame ] = Pmw.Balloon( frame )
    
    
    balloon = balloons[ frame ]
    balloon.bind( widget, text )
#@nonl
#@-node:mork.20041026083725:addBalloon
#@+node:mork.20041022175619:view_help
def view_help( c, items ):
    '''Opens the Help dialog up for the user to view'''
    dialog = Pmw.Dialog( c.frame.top, title = 'Button Help' )
    sf = Pmw.ScrolledFrame( dialog.interior() )
    
    sf.pack()
    sfi = sf.interior()
    
    for z in items:
        lw = Pmw.LabeledWidget( sfi , labelpos = 'e', label_text = z[ 2 ] )
        l = Tk.Button( lw.interior() , image = z[ 1 ] )
        lw.pack()
        l.pack()
        
    dialog.activate()

#@-node:mork.20041022175619:view_help
#@+node:mork.20041026084314:configureNodebar
config = {}
pos = 'position'
help = 'usehelp'
config[ pos ] = '1' #The default is to put the bar in the icon area
config[ help ] = '1' #The default is to see the help buttons

def configureNodebar():
    '''nodebar reads what the config file has in it and sets global state'''
    nbar = 'nodebar'
    cparser = readConfigFile()
    if not cparser: return None
    for z in cparser.sections():
        if z.strip() == nbar:
            nbar = z
            break
    if cparser.has_section( nbar ):
        if cparser.has_option( nbar, pos ):
            p = cparser.get( nbar, pos )
            if p.isdigit():
                config[ pos ] = p
            else:
                g.es( "Bad value in nodebar.ini: %s" % p, color= 'red' )
                g.es( "Was expecting a digit", color = 'red' )
        if cparser.has_option( nbar, help ):
            p = cparser.get( nbar, help )
            if p.isdigit():
                config[ help ] = p
            else:
                g.es( "Bad value in nodebar.ini: %s" % p, color= 'red' )
                g.es( "Was expecting a digit", color = 'red' )
#@nonl
#@-node:mork.20041026084314:configureNodebar
#@+node:mork.20041026084509:readConfigFile
def readConfigFile ():

    #reads the nodebar config file in.
    pth = os.path.split(g.app.loadDir)   
    aini = pth[0]+r"/plugins/nodebar.ini"
    if not os.path.exists(aini):
        try:
            cf = file( aini, 'w' )#creates config file for user, how nice.
            data='''
[ nodebar ]
position=1
usehelp=1
            '''
            cf.write( data )
            cf.close()
            g.es( "Added nodebar.ini to plugin directory", color='blue' )
        except Exception, x:
            g.es( "Could not create nodebar.init because of : %s" % x, color='red' )
            return None
    try:
        cp = ConfigParser.ConfigParser()
        cp.read(aini)
        return cp
    except Exception, x:
        g.es( "Could not read nodebar.ini because of : %s "%x, color='red' )
        return None
#@nonl
#@-node:mork.20041026084509:readConfigFile
#@-others
#@nonl
#@-node:mork.20041022155742.1:@thin nodebar.py
#@-leo
