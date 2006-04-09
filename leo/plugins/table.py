#@+leo-ver=4-thin
#@+node:ekr.20041017035937:@thin table.py
#@<< docstring >>
#@+node:ekr.20050912180921:<< docstring >>
'''This plugin puts the View Table command in the Outline menu.

This command checks the current node using the csv (comma separated values) mods
Sniffer. It tries to determine the format that is in the nodes data. If you had
excel data in it, it should be able to determine its excel data. It then creates
a dialog with the data presented as in a table for the user to see it.
 
Requires Pmw and the tktable widget at http://sourceforge.net/projects/tktable
'''
#@nonl
#@-node:ekr.20050912180921:<< docstring >>
#@nl

#@@language python
#@@tabwidth -4

#@<< imports >>
#@+node:ekr.20041017035937.1:<< imports >>
import leoGlobals as g
import leoPlugins
import leoNodes

Pmw    = g.importExtension("Pmw",    pluginName=__name__,verbose=True)
Tk     = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
tktab  = g.importExtension('tktable',pluginName=__name__,verbose=True)

import csv
import cStringIO
import weakref
#@nonl
#@-node:ekr.20041017035937.1:<< imports >>
#@nl

__version__ = ".13"
#@<< version history >>
#@+node:ekr.20050311103711:<< version history >>
#@@killcolor

#@+at
# 
# .13 EKR:
#     - Added init function.
#     - Use only 'new' and 'open2' hooks.
#@-at
#@nonl
#@-node:ekr.20050311103711:<< version history >>
#@nl

haveseen = weakref.WeakKeyDictionary()

#@+others
#@+node:ekr.20050311103711.1:init
def init ():
    
    ok = Pmw and Tk and tktab # Ok for unit testing.
    
    if ok: 
        leoPlugins.registerHandler(('new','open2'),addMenu )
        g.plugin_signon( __name__ )
        
    return ok
#@nonl
#@-node:ekr.20050311103711.1:init
#@+node:ekr.20041017035937.2:class CSVVisualizer
class CSVVisualizer:
    
    arrays = []
    
    #@    @+others
    #@+node:ekr.20041017035937.3:CSVVisualizer.__init__
    def __init__( self, c ):
        
        self.c = c
        self.arr = tktab.ArrayVar()
        CSVVisualizer.arrays.append( self.arr )
        self.rows = 0
        self.columns = 0
    #@-node:ekr.20041017035937.3:CSVVisualizer.__init__
    #@+node:ekr.20041017035937.4:addData
    def addData( self ):
    
        arr = self.arr
        reader = self.readData() 
        hc = False
        for n, d in enumerate( reader ):
            for n1, d2 in enumerate( d ):
                arr.set( "%s,%s" %( n, n1 ), str(d2) )
        
        self.columns = n1 + 1
        self.rows = n + 1
        return self.columns, self.rows
    #@-node:ekr.20041017035937.4:addData
    #@+node:ekr.20041017035937.5:readData
    def readData( self ):
        
        c = self.c
        pos = c.currentPosition()
        data = pos.bodyString()
        cS = cStringIO.StringIO()
        cS.write( data )
        cS.seek( 0 )
        sniff = csv.Sniffer()
        self.type = sniff.sniff( data ) 
        reader = csv.reader( cS, self.type ) 
        return reader
    #@-node:ekr.20041017035937.5:readData
    #@+node:ekr.20041017035937.6:writeData
    def writeData( self, save ):
        
        pos = self.c.currentPosition()
        n2 = self.rows
        n = self.columns
        data = []
        for z in xrange( n2 ):
            ndata = []
            for z2 in xrange( n ):
                ndata.append( self.arr.get( "%s,%s" % ( z, z2 ) ) )        
            data.append( ndata )
        cS = cStringIO.StringIO()
        csv_write = csv.writer( cS, self.type )
        for z in data:
            csv_write.writerow( z )
        cS.seek( 0 )
        self.c.beginUpdate() 
        if not save:
            tnd = leoNodes.tnode( cS.getvalue(), "Save of Edited " + str(pos.headString() ) )
            pos.insertAfter( tnd )
        else:
            pos.setTnodeText( cS.getvalue() )
        self.c.endUpdate()
    #@-node:ekr.20041017035937.6:writeData
    #@+node:ekr.20041017035937.7:addRow
    def addRow( self , tab ):
        
        self.rows = self.rows + 1
        tab.configure( rows = self.rows )
        rc =  '%s,0' % (self.rows -1 )
        for z in xrange( self.columns ):
            self.arr.set( '%s,%s' %( self.rows - 1, z ), "" ) 
        tab.activate( rc )
        tab.focus_set()
    #@-node:ekr.20041017035937.7:addRow
    #@+node:ekr.20041017035937.8:deleteRow
    def deleteRow( self, tab ):
        
        i = tab.index( 'active' )
        if i:
            tab.delete_rows( i[ 0 ], 1 )
            self.rows = self.rows - 1
    #@nonl
    #@-node:ekr.20041017035937.8:deleteRow
    #@-others
#@-node:ekr.20041017035937.2:class CSVVisualizer
#@+node:ekr.20041017035937.9:viewTable
def viewTable( c ):
    
    pos = c.currentPosition()
    dialog = Pmw.Dialog(
        title = "Table Editor for " + str( pos.headString()),
        buttons = [ 'Save To Current', 'Write To New', 'Close']
    )
    dbbox = dialog.component( 'buttonbox' )
    for z in xrange( dbbox.numbuttons() ):
        dbbox.button( z ).configure( background = 'white', foreground = 'blue')
    csvv = CSVVisualizer( c )
    sframe = Pmw.ScrolledFrame( dialog.interior() )
    sframe.pack()
    tab = createTable( sframe.interior(), csvv.arr )
    createBBox( dialog.interior(), csvv, tab )
    n = csvv.addData()
    tab.configure( cols = n[ 0 ], rows = n[ 1 ] )
    #@    << define fire_button callback >>
    #@+node:ekr.20041017035937.10:<< define fire_button callback >>
    def fire_button( name ):
        if name == "Close":
            dialog.deactivate()
            dialog.destroy()
        elif name == "Write To New":
            csvv.writeData( False )
        elif name == "Save To Current":
            csvv.writeData( True )
    #@nonl
    #@-node:ekr.20041017035937.10:<< define fire_button callback >>
    #@nl
    dialog.configure( command = fire_button )
    dialog.activate()
#@nonl
#@-node:ekr.20041017035937.9:viewTable
#@+node:ekr.20041017035937.11:createTable
def createTable( parent , arr ):
    
    tab = tktab.Table(
        parent,
        rows = 0, cols = 0, variable = arr,
        sparsearray=1,
        background = 'white', foreground = 'blue', selecttype = 'row' )

    tab.tag_configure( 'active', background = '#FFE7C6', foreground = 'blue' )
    tab.tag_configure( 'sel', background = '#FFE7C6', foreground = 'blue', bd=2 )
    tab.pack()
    return tab 
#@-node:ekr.20041017035937.11:createTable
#@+node:ekr.20041017035937.12:createBBox
def createBBox( parent, csvv, tab ):
    
    bbox = Pmw.ButtonBox( parent )
    bconfig = (
        ( "Add Row", lambda tab = tab : csvv.addRow( tab ) ),
        ( "Delete Row", lambda tab = tab: csvv.deleteRow( tab ) ) )

    for z in bconfig:
        bbox.add( z[ 0 ], command = z[ 1 ], background = 'white', foreground = 'blue' )
    bbox.pack()     

#@-node:ekr.20041017035937.12:createBBox
#@+node:ekr.20041017035937.13:addMenu
def addMenu( tag, keywords ):

    c = keywords.get(c)
    if not c or haveseen.has_key( c ):
        return

    haveseen[ c ] = None
    men = c.frame.menu
    men = men.getMenu( 'Outline' )
    men.add_command( label = "Edit Node With Table", command = lambda c = c: viewTable( c ) )
#@nonl
#@-node:ekr.20041017035937.13:addMenu
#@-others
#@nonl
#@-node:ekr.20041017035937:@thin table.py
#@-leo
