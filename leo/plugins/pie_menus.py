#@+leo-ver=4-thin
#@+node:ekr.20040828122150:@thin pie_menus.py
'''Adds pie menus: http://www.piemenus.com/'''

#@@language python
#@@tabwidth -4

#@<< pie_menus imports >>
#@+node:ekr.20040828122150.1:<< pie_menus imports >>
import leoGlobals as g
import leoTkinterTree
import leoTkinterFrame
import leoPlugins

Tk     = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
tkFont = g.importExtension('tkFont', pluginName=__name__,verbose=True)

import weakref
#@nonl
#@-node:ekr.20040828122150.1:<< pie_menus imports >>
#@nl
#@<< version history >>
#@+node:ekr.20050518065635:<< version history >>
#@+at
# 
# .28 EKR: Added import for tkFont.
#@-at
#@nonl
#@-node:ekr.20050518065635:<< version history >>
#@nl

timeids = weakref.WeakKeyDictionary()
fas = weakref.WeakKeyDictionary()

createCanvas = leoTkinterFrame.leoTkinterFrame.createCanvas

#@+others
#@+node:ekr.20040828122150.2:moving
def moving( event, c ):

    canvas = event.widget
    if timeids.has_key( canvas ):
        canvas.after_cancel( timeids[ canvas ] )
        del timeids[ canvas ]
    x = canvas.canvasx( event.x )
    y = canvas.canvasy( event.y ) 
    items = canvas.find_overlapping( x, y, x, y )
    if hasattr( c.frame.tree, 'icon_id_dict' ):
        idict = c.frame.tree.icon_id_dict
    else:
        idict = c.frame.tree.icon_id_dict = c.frame.tree.ids # EKR
        
    for z in items:
        if idict.has_key( z ):
            fa = fas[ canvas ]
            if fa.visible: return
            bbox = canvas.bbox( z )
            cx = x - event.x
            cy = y - event.y          
            x1 = bbox[ 0 ] - cx
            y1 = bbox[ 1 ] - cy
            fa.x1 = ( x1 + canvas.winfo_rootx() ) - 30
            fa.y1 = ( y1 + canvas.winfo_rooty() ) - 37
            id = canvas.after( 250, time_draw, fa, bbox, c.frame.tree.icon_id_dict[z], z )
            timeids[ canvas ] = id
            return
    if fas[ canvas ].visible: fas[ canvas ].leave( event )
#@nonl
#@-node:ekr.20040828122150.2:moving
#@+node:ekr.20040828122150.3:time_draw
def time_draw( fa, bbox, id, z ):
    if timeids.has_key( fa ):
        del timeids[ fa ]
    fa.draw( bbox[ 0 ], bbox[ 1 ], id , z)
#@-node:ekr.20040828122150.3:time_draw
#@+node:ekr.20040828122150.4:class PieMenu
class PieMenu:
    #@	@+others
    #@+node:ekr.20040828122150.5:__init__
    def __init__( self, can, c ):
    
        self.canvas = can
        self.c = c
        self.rmvgroup = {}
        self.visible = False
        self.x = 0
        self.y = 0
        self.help = weakref.WeakKeyDictionary()
        self.construct()
        self.bind()
        self.id = 0 
        self.sid = 0
    #@nonl
    #@-node:ekr.20040828122150.5:__init__
    #@+node:ekr.20040828122150.6:drawString
    def drawString( self, event ):
    
        self.message.after_cancel( self.sid )
        self.message_box.delete( 'help' )  
        x, y = self.l4.winfo_x(), self.l4.winfo_y()
        x = x + 16
        y = y + 16
        f = tkFont.Font( weight = tkFont.BOLD, size = -15, family = 'courier')
        hmes = self.help[ event.widget ]
        self.id = self.message_box.create_text( 1, 7, text = hmes, fill = 'blue',anchor = 'w' , font = f, tags = 'help' )
        self.message.geometry( '+%s+%s' %( x, y ) )
        self.message.deiconify()
        def rmv():
            self.message_box.delete( id )
            self.message.withdraw()
        self.sid = self.message.after( 2500, rmv )
    #@-node:ekr.20040828122150.6:drawString
    #@+node:ekr.20040828122150.7:construct
    def construct( self ):
    
        f = tkFont.Font( weight = tkFont.BOLD, size = -15, family = 'courier')
        
        for i in xrange(1,8):
            w = Tk.Toplevel()
            w.withdraw()
            exec("l%d = self.l%d = w" % (i,i))
            w.overrideredirect(1)
    
        fc = 'darkgreen'
        h = self.help
    
        #@    << create h1 area >>
        #@+node:ekr.20040828131454:<< create h1 area >>
        if 1: # old code
            self.copy = copy = Tk.Canvas( l1, background = 'orange', width = 15,height = 15 )
            h[ copy ] = 'copy'
            copy.create_text( 5, 6, text = 'C' , anchor = 'center', fill = 'white', font = f)
        
            self.paste = paste = Tk.Canvas( l1, background = 'white', width = 15,height = 15 )
            h[ paste ] = 'paste'
            paste.create_text( 5, 6, text = 'P' , anchor = 'center', fill = 'orange',font = f)
            
            self.iu = iu = Tk.Canvas( l1 , background = 'white' , width = 15, height= 15)
            h[ iu ] = 'up'
            iu.create_line( 0, 7, 8, 0, 15, 7, fill = fc, width = 2 )
            iu.create_line( 8, 0, 8, 15, fill = fc, width = 2 )
            
            self.hoist = hoist = Tk.Canvas( l1, background = 'yellow', width = 15,height = 15 )
            h[ hoist ] = 'hoist'
            hoist.create_text( 5, 6, text = 'H' , anchor = 'center', fill = 'green',font = f)
            
            self.insert = insert = Tk.Canvas( l1, background = 'blue', width = 15,height = 15 )
            h[ insert ] = 'insert'
            insert.create_text( 6, 6, text = 'In' , anchor = 'center', fill = 'white', font = f)
        
            for w in copy,paste,iu,hoist,insert:
                w.pack( side = 'left' ) 
                w.bind( '<Enter>', self.drawString )
        else:
            for (ivar,hval,background,fill,text,x,y) in (
                ('copy','copy','orange','white','C',5,6),
                ('paste','paste','white','orange','P',5,6),
                ('iu','up','white','white',None,0,0),
                ('hoist','hoist','yellow','green','H',5,6),
                ('insert','insert','blue','white','In',6,6),
            ):
                w = Tk.Canvas(l1,background=background,width=15,height=15)
                setattr(self,ivar,w)
                h[w] = hval
                if text:
                    w.create_text(x,y,text=text,anchor='center',fill=fill,font = f)
                else:
                    w.create_line( 0, 7, 8, 0, 15, 7, fill = fc, width = 2 )
                    w.create_line( 8, 0, 8, 15, fill = fc, width = 2 )
                w.pack( side = 'left' ) 
                w.bind( '<Enter>', self.drawString)
        #@nonl
        #@-node:ekr.20040828131454:<< create h1 area >>
        #@nl
        #@    << create h3 area >>
        #@+node:ekr.20040828131454.1:<< create h3 area >>
        self.dele = dele = Tk.Canvas( l3, background = 'red', width = 15, height = 15 )
        h[ dele ] = 'delete'
        dele.create_text( 5, 6, text = 'D' , anchor = 'center', fill = 'white',font = f)
        dele.bind( '<Enter>', self.drawString )
        
        dele.pack()
        self.il = il = Tk.Canvas( l3 , background = 'white' , width = 15, height= 15)
        h[ il ] = 'left'
        il.create_line( 7, 0, 0, 8, 7, 15, fill = fc, width = 2 )
        il.create_line( 0, 7, 15, 7 , fill = fc, width = 2 )
        il.pack()
        il.bind( '<Enter>', self.drawString )
        
        self.promote = promote = Tk.Canvas( l3, background = 'darkgreen', width= 15, height = 15 )
        h[ promote] = 'promote'
        promote.create_text( 5, 6, text = 'P' , anchor = 'center', fill = 'white',font = f)
        promote.pack()
        promote.bind( '<Enter>', self.drawString )
        #@nonl
        #@-node:ekr.20040828131454.1:<< create h3 area >>
        #@nl
        #@    << create h2 area >>
        #@+node:ekr.20040828131454.2:<< create h2 area >>
        self.iclone = iclone = Tk.Canvas( l2, background = 'white', width =15, height = 15 )
        h[ iclone ] = 'clone'
        iclone.create_text( 5, 6, text = 'C' , anchor = 'center', fill = 'red',font = f)
        iclone.pack( side = 'left' )
        iclone.bind( '<Enter>', self.drawString )
        
        self.cut = cut = Tk.Canvas( l2, background = 'orange', width = 15, height= 15 )
        h[ cut ] = 'cut'
        cut.create_text( 5, 6, text = 'X' , anchor = 'center', fill = 'white',font = f)
        cut.pack( side = 'left' )
        cut.bind( '<Enter>', self.drawString )
        
        self.ib = ib = Tk.Canvas( l2 , background = 'white' , width = 15, height= 15)
        h[ ib ] = 'down'
        ib.create_line( 0, 7, 8, 15, 15, 7, fill = fc, width = 2 )
        ib.create_line( 8, 0, 8, 15, fill = fc, width = 2 )
        ib.pack( side = 'left' ) 
        ib.bind( '<Enter>', self.drawString )
        
        self.mark = mark = Tk.Canvas( l2, background = 'red', width = 15, height= 15 )
        h[ mark ] = 'mark'
        mark.create_text( 5, 6, text = 'M' , anchor = 'center', fill = 'white',font = f)
        mark.pack( side = 'left' ) 
        mark.bind( '<Enter>', self.drawString )
        
        self.ichild = ichild = Tk.Canvas( l2, background = 'blue', width = 15,height = 15 )
        h[ ichild ] = 'child'
        ichild.create_text( 5, 6, text = 'C' , anchor = 'center', fill = 'white',font = f)
        ichild.pack( side = 'left' )
        ichild.bind( '<Enter>', self.drawString )
        #@nonl
        #@-node:ekr.20040828131454.2:<< create h2 area >>
        #@nl
        #@    << create h4 area >>
        #@+node:ekr.20040828131454.3:<< create h4 area >>
        self.uhoist = uhoist = Tk.Canvas( l4 , background = 'yellow', width= 15, height = 15 )
        h[ uhoist ] = 'unhoist'
        uhoist.create_text( 5, 6, text = 'U' , anchor = 'center', fill = 'green',font = f)
        uhoist.pack()
        uhoist.bind( '<Enter>', self.drawString )
        
        self.ir = ir = Tk.Canvas( l4 , background = 'white' , width = 15, height= 15 )
        h[ ir ] = 'right'
        ir.create_line( 7, 0, 15, 8, 7, 15, fill = fc, width = 2 )
        ir.create_line( 0, 7, 15, 7, fill = fc, width = 2 )
        ir.pack()
        ir.bind( '<Enter>', self.drawString )
        
        self.demote = demote = Tk.Canvas( l4, background = 'darkgreen', width= 15, height = 15 )
        h[ demote ] = 'demote'
        demote.create_text( 5, 6, text = 'D' , anchor = 'center', fill = 'white',font = f)
        demote.pack()
        demote.bind( '<Enter>', self.drawString )
        #@nonl
        #@-node:ekr.20040828131454.3:<< create h4 area >>
        #@nl
        #@    << create h5 area >>
        #@+node:ekr.20040828131454.4:<< create h5 area >>
        self.sorts = sorts = Tk.Canvas( l5 , background = 'red', width = 15,height = 15 )
        h[ sorts ] = 's_siblings'
        sorts.create_text( 5, 6, text = 'S' , anchor = 'center', fill = 'white',font = f)
        sorts.pack()
        sorts.bind( '<Enter>', self.drawString )
        #@nonl
        #@-node:ekr.20040828131454.4:<< create h5 area >>
        #@nl
        #@    << create h6 area >>
        #@+node:ekr.20040828131454.5:<< create h6 area >>
        self.sort = sort = Tk.Canvas( l6, background = 'red', width = 15, height= 15 )
        h[ sort ] = 's_children'
        sort.create_text( 5, 6, text = 's' , anchor = 'center', fill = 'white',font = f)
        sort.pack()
        sort.bind( '<Enter>', self.drawString )
        #@nonl
        #@-node:ekr.20040828131454.5:<< create h6 area >>
        #@nl
        #@    << create h7 area >>
        #@+node:ekr.20040828131454.6:<< create h7 area >>
        self.u1 =  u1 = Tk.Canvas( l7, background = 'grey', width = 15, height= 15 )
        h[ u1 ] = 'user one '
        u1.create_text( 5,6, text = '1', anchor = 'center', fill = 'black',font = f )
        u1.pack( side = 'left')
        u1.bind( '<Enter>', self.drawString )
        
        self.u2 =  u2 = Tk.Canvas( l7, background = 'grey', width = 15, height= 15 )
        h[ u2 ] = 'user two '
        u2.create_text( 5,6, text = '2', anchor = 'center', fill = 'black',font = f )
        u2.pack( side = 'left' )
        u2.bind( '<Enter>', self.drawString )
        
        self.u3 =  u3 = Tk.Canvas( l7, background = 'grey', width = 15, height= 15 )
        h[ u3 ] = 'user three'
        u3.create_text( 5,6, text = '3', anchor = 'center', fill = 'black',font = f )
        u3.pack( side = 'left' )
        u3.bind( '<Enter>', self.drawString )
        #@nonl
        #@-node:ekr.20040828131454.6:<< create h7 area >>
        #@nl
        #@    << create message area >>
        #@+node:ekr.20040828131454.7:<< create message area >>
        self.message = message =  Tk.Toplevel()
        self.message.withdraw()
        self.message.overrideredirect( 1 )
        
        self.message_box =Tk.Canvas( self.message , width = 95, height = 15,background = 'white' )
        self.message_box.bind( '<Enter>', lambda event, self = self: self.clean())
        self.message_box.pack()
        #@nonl
        #@-node:ekr.20040828131454.7:<< create message area >>
        #@nl
    #@nonl
    #@-node:ekr.20040828122150.7:construct
    #@+node:ekr.20040828122150.8:bind
    def bind( self ):
        c = self.c 
        def left( event ):           
            c.selectVnode( self.vnode )
            c.moveOutlineLeft()
        self.il.bind( '<Button-1>', left )
        def right( event ):
            c.selectVnode( self.vnode )
            c.moveOutlineRight()
        self.ir.bind( '<Button-1>', right )  
        def up( event ):
            c.selectVnode( self.vnode )
            c.moveOutlineUp()
        self.iu.bind( '<Button-1>', up ) 
        def down( event ):
            c.selectVnode( self.vnode )
            c.moveOutlineDown()
        self.ib.bind( '<Button-1>', down )
        def clone( event ):
            c.selectVnode( self.vnode )
            c.clone()
        self.iclone.bind( '<Button-1>', clone )
        def child( event ):
            c.selectVnode( self.vnode )
            c.insertHeadline()
            c.moveOutlineRight() 
        self.ichild.bind( '<Button-1>', child ) 
        def insert( event ):
            c.selectVnode( self.vnode )
            c.insertHeadline()
        self.insert.bind( '<Button-1>', insert )       
        def cp( event ):
            c.selectVnode( self.vnode )
            c.copyOutline()
        self.copy.bind( '<Button-1>', cp)
        def pst( event ):
            c.selectVnode( self.vnode )
            c.pasteOutline()
        self.paste.bind( '<Button-1>', pst)
        def ct( event ):
            c.selectVnode( self.vnode )
            c.cutOutline()
        self.cut.bind( '<Button-1>', ct)
        def dt( event ):
            c.selectVnode( self.vnode )
            c.deleteOutline()
        self.dele.bind( '<Button-1>', dt)
        def ht( event ):
            c.selectVnode( self.vnode )
            c.hoist()
        self.hoist.bind( '<Button-1>', ht)
        def uht( event ):
            c.selectVnode( self.vnode )
            c.dehoist()
        self.uhoist.bind( '<Button-1>', uht)
        def mk( event ):
            cv = c.currentVnode()
            c.selectVnode( self.vnode )
            c.markHeadline()
        self.mark.bind( '<Button-1>', mk)
        def pr( event ):
            cv = c.currentVnode()
            c.selectVnode( self.vnode )
            c.promote()
        self.promote.bind( '<Button-1>', pr)
        def dm( event ):
            cv = c.currentVnode()
            c.selectVnode( self.vnode )
            c.demote()
        self.demote.bind( '<Button-1>', dm)
        def srts( event ):
            c.selectVnode( self.vnode )
            c.sortSiblings()
        self.sorts.bind( '<Button-1>', srts)
        def srt( event ):
            c.selectVnode( self.vnode )
            c.sortChildren()
        self.sort.bind( '<Button-1>', srt)
    #@-node:ekr.20040828122150.8:bind
    #@+node:ekr.20040828122150.9:clean
    def clean( self ):
    
        if hasattr( self, 'ri2' ):
            self.l1.withdraw()
            self.l2.withdraw()
            self.l3.withdraw()
            self.l4.withdraw() 
            self.l5.withdraw()
            self.l6.withdraw()
            self.l7.withdraw()
            self.message.withdraw()
            self.canvas.delete( self.ri2 )
            self.canvas.delete( self.ri3 )
            self.canvas.delete( self.ri4 )
            self.canvas.delete( self.ri5 )
            self.visible = False
    #@-node:ekr.20040828122150.9:clean
    #@+node:ekr.20040828122150.10:leave
    def leave( self, event ):
    
        x, y = event.x, event.y
        can = self.canvas
        x = can.canvasx( x )
        y = can.canvasy( y )
        ol = can.find_overlapping( x, y, x, y )
        for z in ol:
            if self.rmvgroup.has_key( z ):
                return
        self.clean() 
    #@-node:ekr.20040828122150.10:leave
    #@+node:ekr.20040828122150.11:draw
    def draw( self, x, y, v, z ):
    
        if not v: return # EKR
        evdict = v.c.frame.tree.edit_text_dict  
        can = self.canvas
        self.clean()
        self.visible = True
        self.vnode = v
        self.x = x
        self.y = y 
        self.y1 = int( self.y1 )
        self.x1 = int( self.x1 )
        
        i = 1
        for (dx,dy) in (
            (0,0),  (0,64), (0,16),
            (68,16),
            (16,48),(52,48),(16,16)
        ):
            w = getattr(self,"l%d" %i)
            w.geometry('+%s+%s' % (self.x1+dx,self.y1+dy))
            w.deiconify()
            i += 1
        if 0:
            #@        << old code >>
            #@+node:ekr.20040828131759:<< old code >>
            self.l1.geometry( '+%s+%s' %( self.x1,      self.y1 ) )
            self.l3.geometry( '+%s+%s' %( self.x1,      self.y1 + 16 ) )
            self.l2.geometry( '+%s+%s' %( self.x1,      self.y1 + 64 ) )
            self.l4.geometry( '+%s+%s' %( self.x1 + 68, self.y1 + 16 ) )
            self.l5.geometry( '+%s+%s' %( self.x1 + 16, self.y1 + 48 ) )
            self.l6.geometry( '+%s+%s' %( self.x1 + 52, self.y1 + 48 ) )
            self.l7.geometry( '+%s+%s' %( self.x1 + 16, self.y1 + 16 ) )
            self.l1.deiconify()
            self.l3.deiconify() 
            self.l2.deiconify()
            self.l4.deiconify() 
            self.l5.deiconify()
            self.l6.deiconify()
            self.l7.deiconify()
            #@nonl
            #@-node:ekr.20040828131759:<< old code >>
            #@nl
        bb = can.bbox( z )
        bx, by, bx1, by1 = bb
        self.ri2 = can.create_rectangle( bx - 15, y - 16,  x + 31,   by + 1,   width = 0 )
        self.ri3 = can.create_rectangle( bx - 15, by1 -1,  x + 31,   by1 + 16, width = 0 )
        self.ri4 = can.create_rectangle( bx - 15, by1 -16, bx + 1,   by1 + 16, width = 0 )
        self.ri5 = can.create_rectangle( bx1 - 1, by1 -16, bx1 + 11, by1 +16 , width = 0)
        self.rmvgroup[ self.ri2 ] = None
        self.rmvgroup[ self.ri3 ] = None  
        self.rmvgroup[ self.ri4 ] = None
        self.rmvgroup[ self.ri5 ] = None
    #@nonl
    #@-node:ekr.20040828122150.11:draw
    #@-others
#@-node:ekr.20040828122150.4:class PieMenu
#@+node:ekr.20040828122150.12:addPMenu
def addPMenu( self, parentFrame ):

    can = createCanvas( self, parentFrame )
    c = self.c
    
    can.bind( '<Motion>', lambda event , c = c: moving( event, c ) )

    fa = PieMenu( can, c )
    fas[ can ] = fa
    return can
#@nonl
#@-node:ekr.20040828122150.12:addPMenu
#@-others

if Tk and not g.app.unitTesting:  # Changes Leo's core.
    leoTkinterFrame.leoTkinterFrame.createCanvas = addPMenu
    __version__ = ".28"
    g.plugin_signon( __name__ )
#@nonl
#@-node:ekr.20040828122150:@thin pie_menus.py
#@-leo
