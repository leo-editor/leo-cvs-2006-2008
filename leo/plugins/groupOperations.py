#@+leo-ver=4-thin
#@+node:mork.20041018131258.1:@thin groupOperations.py
#@<< docstring >>
#@+node:ekr.20050912180223:<< docstring >>
'''A Leo Plugin that adds Group commands functionality. Restrictions currently
apply to using Leo with a Tk frontend. There are several commands in this
plugin:

-   Mark Node: marks a node for further operations such as copying, cloning and moving.

-   Mark Target: marks a node as the place where group operations are to target.

-   Operate On Marked: moves lassoed nodes to the spot where the roundup node is
    placed. Clones are maintained.

-   Clear Marked: unmarks all marked nodes and removes the roundup node.

-   Transfer Lassoed Nodes: this is a menu for inter-window communication.
    The windows must all be spawned from the same Leo instance. 
    It allows the user to move all node marked for copying and moving from another window to this one.
'''
#@nonl
#@-node:ekr.20050912180223:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

#@<< imports >>
#@+node:mork.20041018131258.2:<< imports >>
import leoPlugins 
import leoGlobals as g      
import leoNodes
import copy
import base64

sets    = g.importExtension('sets',   pluginName=__name__,verbose=True)
Tkinter = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
#@nonl
#@-node:mork.20041018131258.2:<< imports >>
#@nl
#@<< images >>
#@+node:mork.20041021094915:<< images >>
groupOps = r'''R0lGODlhZAAUAMZpAB8xvCAyvCEzvSIzvSM0vSM1vSQ2viU3viY3vig5vyk6vyo7vyo8vys8wCw9
wC0+wDJDwjVFwztLxDxMxT1MxT5NxUBPxkJRx0NSx0RTx0VUx0dVyEhXyEpZyUtZyU1byk5cyk9d
ylJgy1RhzFVizFVjzFdlzVhmzVpnzltozlxpzl5rz2Fu0GJu0GRw0GRx0WVy0WZy0Wh00ml10mp2
0mt202t302x4021502561HaB1nqF15Ga3pKb3p2l4qCo46Sr5Keu5aux5qyz5q2056+157O66LS6
6ba86bi+6rm+6rvB67zC673C677D7MLG7cLH7cPI7cnO78/T8dbZ89fa89nc9Nrd9Nve9Nzf9N3f
9ebo+Ofp+Ojq+Onr+Ors+ezt+e3u+fT1/Pj5/fr6/fv7/vv8/vz9/v7+////////////////////
/////////////////////////////////////////////////////////////////////////yH+
FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAAGQAFAAAB/6AaYKDhIWGh4iJiouMjY6PkJGSk5SV
lpeYmZqbl0ogBRA8aJxQJQgHJE+caQAAnEUAOmJVD1GbSAApXl4pAEiYrauDFgBfha0fYDcMDDZg
rK7B0CQGLVyDGABYglcAGtPVXF8yCQ0xVNAfSRcCET9pL60h0GnKzM7QHA4+aUYUBB5sISoAgAw0
INCu9GLSJBc9aa2YLAFwYpAAAGYElQEwAJpEiihatUKQEAYKKwAICILoamHDFNCqACC5AIAUFDMS
cQAwRdAKhK3QGABQZuOBh66glSEDoMCgC9oEYQGQQSnTAgTPEAoqpAMIlitdDS0K4GiwYENaIKjA
I5GTAJ4iwEQhANSVCQBOXqYhAABl0lZOmABAMegIABVfuoQ8Ai3w4BE2tcjoQY+gzL8AxtC7m9fh
WVc3dmSZqQhKCAIWdNRN84WGggU4wqThoWACyxMFWHghBIUaKlXQcOve4gJBgxy7g7kgIAFB1BoE
SNBr/To20jRBIgzYQETY1qSOpHkf/0h8I/Pk06tfz769+/fw48ufT7++/fv48xMKBAA7'''

bullseye=r'''R0lGODlhCgAKAKECAOcxcf/9/f///////ywAAAAACgAKAAACGpSBYIsRyMCTsMk36cR2084p1hc5
0CIkilEAADs='''

copy=r'''R0lGODlhCgAKAIABANupWv///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAAAoACgAAAhOM
A6eYy62AhGbai+WjZ7rKRUsBADs='''

clone=r'''R0lGODlhCgAKAIABADeHHv///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAAAoACgAAAhOM
A6eYy62AhGbai+WjZ7rKRUsBADs='''

move=r'''R0lGODlhCgAKAIABAB89vP///yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAAAoACgAAAhOM
A6eYy62AhGbai+WjZ7rKRUsBADs='''

move_Arrow=r'''R0lGODlhMgAUAIABAB89vP///ywAAAAAMgAUAAACToyPqcvtD6OctNqLs94WKOAZIPeMiRmg5KeK
YRqC3ju3kfwec8rTPSyj4Ia7Ik/0ywmJwZgR2dRVcB/kMWgFXrArjK0rBIvH5LL5jD4UAAA7'''

copy_Arrow=r'''R0lGODlhMgAUAIABANupWv///ywAAAAAMgAUAAACSYyPqcvtD6OctNqLs94WLAByUph4hik2IHoq
6/mi7LTO9uHJ+FX3JLzT5Xi+GEwYnFFqH9IrwGxlnrQS5zdCYKeprvcLDovHlwIAOw=='''

clone_Arrow=r'''R0lGODlhMgAUAIABADeHHv///ywAAAAAMgAUAAACTYyPqcvtD6OctNqLcwbcAC19iRh8JNh0yOl5
KkfClrwq5nGXJcw+/FjL6URCCu+Y6wiTulYISYu6iE7a5IfSWLMYFXfzDYvH5LL5/CgAADs='''

markSpot=r'''R0lGODlhZAAUAKECAOcxcf/9/f///////ywAAAAAZAAUAAACk5SPqcvtD6OctNqLs968+w+G4kiW
JIACCHqwj5qkqdmhQeAKed7Aiq8BjmxE2M630ymFyhVyOdOxokMA7madLptGw3MB7HJb0hkTlMWl
VeztytviwX/zp/D8Wa+57XHT/UbmZ0eG50GEpTboJfMnJshoFsdnZFiThUnTA6kZY6XYyUAV6ilH
eoqaqrrK2ur6CitRAAA7'''

markFor=r'''R0lGODlhZAAUAKU+AB8xvCEzvSM0vSM1vSQ2viU3vio7vz9OxUBPxk5dyk9dylBey1Ffy1Jgy1Nh
zFRhzFVizF9sz2h00m971HF81HJ91XR/1XiD13mE13yH2H2H2ICK2YiR24+Y3ZCZ3pKb3pSc35Wd
35eg4Jig4J2l4qOq46Wt5LW76bi+6rq/6sLH7cTJ7c7S8M/T8dTX8tXY8tbZ89ve9N3f9d/h9d/i
9uDj9uLk9uTm9/T1/Pn5/fr6/fv8/vz9/v7+/////////yH+FUNyZWF0ZWQgd2l0aCBUaGUgR0lN
UAAsAAAAAGQAFAAABtJAn3BILBqPyKRyyWw6n9CodEqtWq/YrHbL7Xq/4LD4CNAMNQBm2ghot8dh
QGLn2ynWSjxRDwcDOCo+KxxrLAcGH0IAHgI+AD0ZKXtENQ0EDjWOjI59VAAwFj4XL2sIKDYBiiQ5
jiIgRW5pDiU5JRCOq51Vjws4DT1pPCchI2sAdI4TFLBEAjo+OQOOyLpTaR4YHZwpADctAM94jxIu
k0MNJjolD5zVnj4zADGcORUFGw8X7ZwyEeZCNBgMaJBJnLuDCBMqXMiwocOHECNKnEhxTBAAOw=='''

operateOnMarked=r'''R0lGODlhZAAUAMZjAB8xvCEzvSIzvSM0vSM1vSQ2viU3viY3vio7vz5NxT9OxUBPxkFRxkJRx0NS
x0RTx0VUx0ZVyEdWyEpZyU5cyk5dyk9dylBey1Ffy1Jgy1NhzFRhzFVizFdlzVxpzl9sz2Fu0GNv
0Gh00m971HF81HJ91XJ+1XR/1XiD13mE13yH2H2H2ICK2YKM2oON2oiR24+Y3ZCZ3pKb3pSc35Wd
35af4Jeg4Jig4J2l4p+n4qCo46Gp46Kp46Oq46Sr5KWt5K20566156+157W76bi+6rq/6rrA68LG
7cLH7cTJ7c7S8M/T8dDT8dHV8dLW8tTX8tXY8tbZ89nc9Nve9N3f9d/h9d/i9uDj9uLk9uTm9+bo
9/T1/Pj5/fn5/fr6/fv7/vv8/vz9/v7+////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////yH+
FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAAGQAFAAAB/6AY4KDhIWGh4iJiouMjY6PkJGSk5SV
lpeYmZqbnJ2en4VBDQQNQKCQACuDKwCMrYuvi0ERTV5NEEKWsZUAFWBjYBa7iMOHxYcMToNMD2MA
LAUVVlIVAxRHzjEDY0oKCDJjIAAJ1NbYglcZBRpXzikH4IQAL0hjSS+v3d+CANrOYiqKlLtmpYKB
FscMDfgyyMs2AD644OAgAYDFhzi6jFlABEsAfmMqXhykoUeXHhycEZmyTV6UE2NQQHnF0SO/jM5s
zAhpEcCADDm47EhYKNkgJxCcaeRCgAAXeb/CDKFx41Urpwq9jOlCwFkYZ4UAiLmwJYOYVlKpWv3l
bASJMZ1YBQ1YSpQQkAhOvjiRUMSZjy45NHio0YVHCLBjigDIsgSAVseDCx8WlOGHlx4bEA9rFSMF
DLCKGTtG/E/Ek8iGNejo4qOuXQYCIBjh56IABStaOhDYoAVxlxIGWGxAMWaCg9y7ewuygoFAhnZW
w46pAmAK2N/Bh5NuReUDct4FA5hwrYj8qfOUzKNfz769+/fw48ufT7++/fv47wcCADs='''

clearMarks=r'''R0lGODlhZAAUAMZoAB8xvCEzvSIzvSM0vSM1vSU3viY3vik6vyo7vy9AwTJDwjREwjVFwzZGwzlJ
xD9OxUBPxkdWyEtZyU5cyk5dyk9dylBey1Jgy1RhzFdlzVxpzl5rz19sz2Ju0GNv0GZy0Wh00mt3
02x402971HF81HJ91XR/1XiD13mE13yH2H2H2ICK2YGL2YKM2oiR24+Y3ZCZ3pKb3pSc35Wd35ae
35af4Jeg4Jig4Jmh4Zuj4Z2l4qKp46Oq46at5Keu5a6157O66LW76be96bi+6rm+6rq/6sLG7cLH
7cTJ7cbK7s7S8M/T8dDT8dTX8tXY8tbZ89fb89nc9Nve9N3f9d7g9d/h9eLk9uTm9+bo9+jq+Onr
+O3v+vP0+/T1/PX2/Pb3/Pf4/fj5/fn5/fr6/fv7/vv8/vz9/v7+////////////////////////
/////////////////////////////////////////////////////////////////////////yH+
FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAAGQAFAAAB/6AaIKDhIWGh4iJiouMjY6PkJGSk5SV
lpeYmZqbnJ2en4RnOQ0FHltoAJQAKoMqqYuvoJI4H1phPiGoqhRlaGUVsYnBso8LWIWpURQDE0Zo
Sg8IMYIAMAOEAC5HaEgur9DS1NaoZylFPw0GIl/EigJkyGgRAPTXEENWAdQ6YthPJmhOOHl1L9++
fgBsyEBzAEqWCEDaJZLARBAYB7oIhBlkJsiMG68A9MJ2xkKXC2dSdfwYciSAESTQEIlBg0USiYiE
SKDipQWrVBpqiNnhoQiAK0sAjNEVDwaKF7qMIlXKlByIJgyodOmAASciHgoKgOCiC0sGAhiwiClR
YAWGEyxVB6WqAkCKrrVt31ZNNYVDjwQFNlTxSriw4cOIEytezLix48eQI0ueTPlQIAA7'''

transferFrom = r'''R0lGODlhZAAUAMZUAB8xvCEzvSIzvSM0vSM1vSQ2viU3viY3vik6vyo7vy9AwTVFwzZGwzpKxD9O
xUBPxkdWyE5cyk5dylFfy1Jgy1NhzFRhzFVizFdlzVpnzlxpzl5rz2Ju0GNv0GRx0Wx402561HJ9
1XR/1XiD13mE14CK2YGL2YWP2ouU3JCZ3pKb3pWd35ae35af4Jig4J2l4qKp46Oq46Wt5Kat5K61
57O66LW76bi+6rm+6rq/6r3C67/E7MLG7cbK7s7S8M/T8dfb89nc9Nve9N3f9d7g9d/h9d/i9uDj
9uLk9uTm9+bo9+jq+PT1/Pb3/Pj5/fn5/fr6/fv8/vz9/v7+////////////////////////////
////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////////////////////////////////////////yH+
FUNyZWF0ZWQgd2l0aCBUaGUgR0lNUAAsAAAAAGQAFAAAB/6AVIKDhIWGh4iJiouMjY6PkJGSk5SV
lpeYmZqbnJ2en4QAoqIZliAOjaOioJYAmQBNqayvoSkDVD4OCSqCACQHvDQMBx9NHgANQRIDETxU
ALahhdADRxQFFUfPIgMoHAQnvbOugwAvT1QPN0gBvTdCtwhASxA1z1QQo7fm6OWjvecqxHgS48Kz
HUMA6BgiYFa5UFGoSLGxwgU5AFLu4VDBwkSPewScQJw2LeIAKFSeEHg2heU9hy/FUckBIMkPACgv
UllAhAkHC/c0tHgCo0PMh9KoUJABJQZQnUdZkZP5JISBEhZGvHQ1Q4GBDUXuKcFAwIKSqFHJGZlA
gII2qBhQYcqdS7eu3bt48+rdy7ev37+AAwvuFAgAOw=='''

groupOpPI = Tkinter.PhotoImage( data = groupOps )
bullseyePI = Tkinter.PhotoImage( data = bullseye )
copyPI = Tkinter.PhotoImage( data = copy )
clonePI = Tkinter.PhotoImage( data = clone )
movePI = Tkinter.PhotoImage( data = move )
move_arrowPI = Tkinter.PhotoImage( data = move_Arrow )
copy_arrowPI = Tkinter.PhotoImage( data = copy_Arrow )
clone_arrowPI = Tkinter.PhotoImage( data = clone_Arrow )
markSpotPI = Tkinter.PhotoImage( data = markSpot )
markForPI = Tkinter.PhotoImage( data = markFor )
operateOnMarkedPI = Tkinter.PhotoImage( data = operateOnMarked )
clearMarksPI = Tkinter.PhotoImage( data = clearMarks )
transferFromPI = Tkinter.PhotoImage( data = transferFrom )
#@nonl
#@-node:mork.20041021094915:<< images >>
#@nl

# globals
lassoers = {}

__version__ = ".5"
#@<<version history>>
#@+node:mork.20041021120027:<<version history>>
#@@killcolor
#@+at 
# .1 -- We have started almost from scratch from the previous group Move
# operations. Many things are easier. We have a new way of marking things for
# moving. Instead of marking all nodes and thugishly moving them as clones or
# copies, the user can specify what type of operation he wants on the node. 
# This
# apparently works with Chapters, but I havent tested it enough to verify 
# there
# aren't bugs involved. Marks across chapters do not apparently move very well 
# to
# another window. Will work on for next version.
# .2 EKR:
# - Use g.importExtension to import Pmw and sets.
# - Added init function.
# .3 EKR:
# - Removed start2 hook.
# - Use keywords to get c, not g.top().
# .4 EKR
# - Removed all calls to g.top().
# .5 EKR
# - Major cleanup of code.
# - Added support for minibuffer commands.
#@-at
#@nonl
#@-node:mork.20041021120027:<<version history>>
#@nl

#@+others
#@+node:ekr.20060325104949:Module level
#@+node:ekr.20050226114442:init
def init ():

    ok = Tkinter and sets
    if ok:
        leoPlugins.registerHandler(('open2',"new"),addMenu)
        leoPlugins.registerHandler("after-redraw-outline",drawImages)
        g.plugin_signon(__name__)
    return ok
#@nonl
#@-node:ekr.20050226114442:init
#@+node:mork.20041018131258.34:drawImages
def drawImages (tag,keywords):
    ''' draws a little yellow box on the node image to indicate selection'''

    c = keywords.get('c')
    if not c or not c.exists: return
    canvas = c.frame.tree.canvas
    global lassoers
    if not lassoers.has_key(c): return
    lassoer = lassoers [c]

    canvas.delete('lnodes')
    mc = ((lassoer.mvForM,movePI),(lassoer.mvForCopy,copyPI),(lassoer.mvForClone,clonePI))
    for l, col in mc:
        for z in l:
            if z.exists(c):
                drawArrowImages(z,col,canvas)

    canvas.delete('movenode')
    if lassoer.moveNode and lassoer.moveNode.isVisible():
        mN = lassoer.moveNode.v
        x = mN.iconx
        y = mN.icony
        if lassoer.moveNode.exists(c):
            canvas.create_image(x-5,y+7,image=bullseyePI,tag='movenode')
            #canvas.create_polygon( x -10 , y + 2  , x , y + 7, x -10, y + 12, fill = 'red', tag = 'movenode' )
    return None

#@-node:mork.20041018131258.34:drawImages
#@+node:mork.20041018131258.35:drawArrowImages
def drawArrowImages (p,image,canvas):

    if p.isVisible():
        x = p.v.iconx
        y = p.v.icony
        canvas.create_image(x-5,y+7,image=image,tag='lnodes')
#@nonl
#@-node:mork.20041018131258.35:drawArrowImages
#@+node:mork.20041018131258.36:addMenu & helper
def addMenu (tag,keywords):
   
    global lassoers
    c = keywords.get('c')
    if not c or not c.exists or c in lassoers.keys(): return
    lassoers [c] = las = Lassoer(c)
    table = (("Mark RoundUp Spot",None,las.markTarget),)
    men = c.frame.menu
    tp = c.frame.top
    mname = tp ['menu'].split('.') [ -1]
    men = tp.children [mname]
    nrumenu = Tkinter.Menu(men,tearoff=0)
    men.add_cascade(menu=nrumenu,label='GroupOps') # image=groupOpPI)
    nrumenu.add_command(image=markSpotPI,command=las.markTarget)
    mmenu = Tkinter.Menu(nrumenu,tearoff=0)
    nrumenu.add_cascade(menu=mmenu,image=markForPI)

    for label,command,image in (
        ('Moving', las.addForMove,move_arrowPI),
        ('Copying',las.addForCopy,copy_arrowPI),
        ('Cloning',las.addForClone,clone_arrowPI),
    ):
        mmenu.add_command(label=label,command=command,image=image)

    nrumenu.add_command(command=las.operateOnMarked,image=operateOnMarkedPI)
    nrumenu.add_command(command=las.reset,image=clearMarksPI)
    imenu = Tkinter.Menu(nrumenu,tearoff=0)
    nrumenu.add_cascade(menu=imenu,image=transferFromPI)
    imenu.config(postcommand=lambda nm=imenu: createCommandsMenu(nm))
    imenu.lassoer = las
#@nonl
#@+node:mork.20041018131258.33:createCommandsMenu
def createCommandsMenu (menu):

    menu.delete('1','end')

    global lassoers
    commanders = lassoers.keys()
    commanders.remove(menu.lassoer.c)
    mlas = lassoers [menu.lassoer.c]
    event = None
    for c in commanders:
        if hasattr(c,"frame") and len(lassoers[c]) != 0:
            las = lassoers [c]
            menu.add_command(
                label=c.frame.getTitle(),
                command=lambda frm=las,to=mlas: frm.transfer(event,to))
#@nonl
#@-node:mork.20041018131258.33:createCommandsMenu
#@-node:mork.20041018131258.36:addMenu & helper
#@-node:ekr.20060325104949:Module level
#@+node:mork.20041018131258.5:class Lassoer
class Lassoer(object):

    #@	@+others
    #@+node:mork.20041018131258.7:__init__
    def __init__( self , c ):
    
        self.nodes = []
        self.c = c
        self.k = k = c.k
        self.mover = []
        self.mvForM = []
        self.mvForCopy = []
        self.mvForClone = []
        self.moveNode = None
        self.canvases = sets.Set()
    
        for commandName,func in (
            ('group-operations-clear-marked',       self.clear),
            ('group-operations-mark-for-move',      self.addForMove),
            ('group-operations-mark-for-copy',      self.addForCopy),
            ('group-operations-mark-for-clone',     self.addForClone),
            ('group-operations-mark-target',        self.markTarget),
            ('group-operations-operate-on-marked',  self.operateOnMarked),
            ('group-operations-transfer',           self.transfer),
        ):
            k.registerCommand (commandName,None,func,pane='all',verbose=False)
    #@nonl
    #@-node:mork.20041018131258.7:__init__
    #@+node:mork.20041018131258.6:__lcmp__
    def __lcmp__ (p1,p2):
    
        if   p1.v.icony >  p2.v.icony: return  1
        elif p1.v.icony <  p2.v.icony: return -1
        elif p1.v.icony == p2.v.icony: return  0
    
    __lcmp__ = staticmethod(__lcmp__)
    #@nonl
    #@-node:mork.20041018131258.6:__lcmp__
    #@+node:mork.20041019124112:__len__
    def __len__( self ):
        
        return len( self.mvForClone ) + \
               len( self.mvForCopy ) + \
               len( self.mvForM )
    #@-node:mork.20041019124112:__len__
    #@+node:ekr.20060325094821:Commands
    #@+node:mork.20041018131258.9:addForMove
    def addForMove (self,event=None):
    
        c = self.c ; p = c.currentPosition()
        aList = self.mvForM ; justRmv = p in aList
        # g.trace(justRmv)
    
        self.remove(p)
        if not justRmv:
            aList.append(p)
            aList.sort(Lassoer.__lcmp__)
            self.canvases.add(c.frame.canvas)
            # if p.hasNext(): c.selectPosition(p.next())
        c.redraw()
    #@nonl
    #@-node:mork.20041018131258.9:addForMove
    #@+node:mork.20041019102247:addForCopy
    def addForCopy (self,event=None):
    
        c = self.c ; p = c.currentPosition()
        aList = self.mvForCopy ; justRmv = p in aList
    
        self.remove(p)
        if not justRmv:
            aList.append(p)
            aList.sort(Lassoer.__lcmp__)
            self.canvases.add(self.c.frame.canvas)
            # if p.hasNext(): c.selectPosition(p.next())
        c.redraw()
    #@nonl
    #@-node:mork.20041019102247:addForCopy
    #@+node:mork.20041019102247.1:addForClone
    def addForClone (self,event=None):
        
        c = self.c ; p = self.c.currentPosition()
        aList = self.mvForClone ; justRmv = p in aList
    
        self.remove(p)
        if not justRmv:
            aList.append(p)
            aList.sort(Lassoer.__lcmp__)
            self.canvases.add(c.frame.canvas)
            # if p.hasNext(): c.selectPosition(p.next())
        c.redraw()
    #@nonl
    #@-node:mork.20041019102247.1:addForClone
    #@+node:mork.20041018131258.11:clear
    def clear (self,event=None):
    
        self.mvForM = []
        self.mvForCopy = []
        self.mvForClone = []
        self.moveNode = None
        for z in self.canvases:
            z.delete('lnodes')
            z.delete('movenode')
        self.canvases.clear()
    #@-node:mork.20041018131258.11:clear
    #@+node:mork.20041019121125:markTarget
    def markTarget (self,event=None):
        
        c = self.c ; p = c.currentPosition()
    
        if p == self.moveNode:
            self.moveNode = None
        else:
            self.remove(p)
            self.moveNode = p
    
        c.redraw()
    #@nonl
    #@-node:mork.20041019121125:markTarget
    #@+node:ekr.20060325113340:operateOnMarked
    def operateOnMarked (self,event=None):
        
        c = self.c
    
        if self.validMove():
            c.beginUpdate()
            self.moveTo()
            self.copyTo()
            self.cloneTo()
            self.clear()
            c.endUpdate()
        else:
            g.es('No valid move',color='blue')
    #@nonl
    #@-node:ekr.20060325113340:operateOnMarked
    #@+node:mork.20041019125724.3:transfer
    def transfer (self,event=None,lassoer=None):
        
        '''Inter-window transfer.'''
    
        c = self.c
        if not lassoer.validMove():
            g.es('Transfer not valid',color='blue')
            return
        cpos = self.c.currentPosition()
        self.c.beginUpdate()
        lassoer.c.beginUpdate()
        mN = lassoer.moveNode
        for z in self.mvForCopy:
            self.copyTo(mN)
        for z in self.mvForM:
            self.moveTo(mN)
        self.clear()
        self.c.endUpdate()
        lassoer.c.endUpdate()
        c.selectPosition(cpos)
        self.c.redraw()
        lassoer.c.redraw()
    #@nonl
    #@-node:mork.20041019125724.3:transfer
    #@-node:ekr.20060325094821:Commands
    #@+node:ekr.20060325103727:Utils
    #@+node:mork.20041019125724:copyTo
    def copyTo( self, mN = None ):
    
        if not mN: mN = self.moveNode
        for z in self.mvForCopy:
            nn = mN.insertAfter()
            z.copyTreeFromSelfTo( nn )
            mN = nn
    #@nonl
    #@-node:mork.20041019125724:copyTo
    #@+node:mork.20041019125724.1:cloneTo
    def cloneTo (self,mN=None):
    
        if not mN: mN = self.moveNode
        for z in self.mvForClone:
            clo = z.clone(z)
            clo.moveAfter(mN)
            mN = clo
    #@-node:mork.20041019125724.1:cloneTo
    #@+node:mork.20041019125724.2:moveTo
    def moveTo (self,mN=None):
    
        if not mN: mN = self.moveNode
        for z in self.mvForM:
            if z.isRoot():
                continue
            if z.c != mN.c:
                z.c.selectPosition(z)
                s = z.c.fileCommands.putLeoOutline()
                p = mN.c.fileCommands.getLeoOutline(s,False)
                p.moveAfter(mN)
                z.doDelete()
            else:
                z.moveAfter(mN)
                mN = z
    
    
    #@-node:mork.20041019125724.2:moveTo
    #@+node:ekr.20060325113814:reset
    def reset (self):
        
        self.clear()
        self.c.redraw()
    #@nonl
    #@-node:ekr.20060325113814:reset
    #@+node:mork.20041018131258.10:remove
    def remove (self,p):
        
        c = self.c
        
        for aList in (self.mvForCopy, self.mvForClone, self.mvForM):
            if p in aList: aList.remove(p)
    
        if p == self.moveNode:
            self.moveNode = None
    #@nonl
    #@-node:mork.20041018131258.10:remove
    #@+node:mork.20041019121125.1:contains
    def contains (self,p):
        
        return p in self.mvForClone or p in self.mvForCopy or p in self.mvForM
    #@nonl
    #@-node:mork.20041019121125.1:contains
    #@+node:mork.20041019151511:validMove
    def validMove (self):
    
        return self.moveNode and self.moveNode.exists(self.c)
    #@nonl
    #@-node:mork.20041019151511:validMove
    #@-node:ekr.20060325103727:Utils
    #@-others
#@-node:mork.20041018131258.5:class Lassoer
#@-others
#@nonl
#@-node:mork.20041018131258.1:@thin groupOperations.py
#@-leo
