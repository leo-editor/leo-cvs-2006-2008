#@+leo-ver=4-thin
#@+node:ekr.20040107092135.2:@thin searchbox.py
#@<< doc string >>
#@+node:ekr.20040108060748:<< doc string >>
'''Add a quick search to Leo's toolbar.

A search box which behaves like a web site search is added, along with
a "GO" button to do quick searches right from the main Leo window. All the
current search options are retained except that "search body text" is
explicitely set - mainly because this is by far the most common use case.

Pressing <CR> while editing the text automatically does a search. Repeated
searches can be done by clicking the "GO" button.

The combo box also stores a list of previous searches, which can be
selected to quickly repeat a search. When activating a previous
search the original search mode is used.

Still to do:

- incremental search
- reverse search
- persist recent searches across Leo sessions
- use INI file to set options for list size etc
'''
#@nonl
#@-node:ekr.20040108060748:<< doc string >>
#@nl

#@@language python
#@@tabwidth -4

__version__ = "0.6"

#@<< version history >>
#@+node:ekr.20040908094021.3:<< version history >>
#@+at
# 0.4 EKR: Don't mess with button width on MacOS/darwin.
# 
# 0.5 EKR: Create a separate SearchBox instance for each open window.
#     This eliminates problems when multiple windows are open.
# 0.6 EKR: Changes required by revisions of leoFind.leoFind class in Leo 4.3:
#     - Removed '_flag' suffixes in OPTION_LIST.
#     - Added c arg to QuickFind ctor.
#         - We now have per-commander find panels.
#     - update_ivars
#         - Changed name from set_ivars.
#         - Call setattr(self,key,0), not setattr(c,key+'_flag',0)
#         - No more _flag hack.
#         - Set self ivars, not c ivars.
#     - Changed init_s_text to init_s_ctrl.
#         - Changed s_text to s_ctrl.
#@-at
#@nonl
#@-node:ekr.20040908094021.3:<< version history >>
#@nl
#@<< imports >>
#@+node:ekr.20040908093511.3:<< imports >>
import leoGlobals as g
import leoPlugins

import leoFind

Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)

import sys
#@nonl
#@-node:ekr.20040908093511.3:<< imports >>
#@nl
#@<< vars >>
#@+node:ekr.20040108054555.14:<< vars >>
# Set this to 0 if the sizing of the toolbar controls doesn't look good on 
# your platform 
USE_FIXED_SIZES = sys.platform != "darwin"

# Set this to the number of previous searches you want to remember 
SEARCH_LIST_LENGTH = 10

# Define the search option/find option matrix - we define as a list first 
# so we can keep a nice order. You can easily add options here if you 
# know what you are doing ;) 
# If an option is supposed to zero a flag then start the name with a !

# New in 4.3: removed the odious _flag hack.
OPTION_LIST = [
    ("Search text", ["search_body", "search_headline", "ignore_case"]), 
    ("Search word", ["search_body", "search_headline", "whole_word", "ignore_case"]), 
    ("Search headlines", ["search_headline","ignore_case"]), 
    ("Search body", ["search_body", "ignore_case"]), 
    ("Case sensitive", ["search_body", "search_headline"]), 
]

OPTION_DICT = dict(OPTION_LIST)
#@nonl
#@-node:ekr.20040108054555.14:<< vars >>
#@nl

#@+others
#@+node:ekr.20040909132007:onCreate
def onCreate(tag, keywords):
    
    # Not ok for unit testing: can't use unitTestGui.
    if g.app.unitTesting:
        return

    c = keywords.get("c")
    search = SearchBox(c)
    search.addWidgets()
#@nonl
#@-node:ekr.20040909132007:onCreate
#@+node:ekr.20040107092135.3:class SearchBox
class SearchBox:

    """A search box for Leo"""

    #@    @+others
    #@+node:ekr.20040909132007.1:ctor
    def __init__ (self,c):
        
        self.c = c
    #@nonl
    #@-node:ekr.20040909132007.1:ctor
    #@+node:ekr.20040108054555.4:_getSizer
    def _getSizer(self, parent, height, width):
        """Return a sizer object to force a Tk widget to be the right size"""
        if USE_FIXED_SIZES: 
            sizer = Tk.Frame(parent, height=height, width=width)
            sizer.pack_propagate(0) # don't shrink 
            sizer.pack(side="right")
            return sizer
        else:
            return parent
    #@nonl
    #@-node:ekr.20040108054555.4:_getSizer
    #@+node:ekr.20040108054555.3:addWidgets
    def addWidgets(self):
        """Add the widgets to the navigation bar"""
        
        c = self.c ; toolbar = c.frame.iconFrame
        # Button.
        self.go = Tk.Button(self._getSizer(toolbar, 25, 32), text="GO", command=self.doSearch)
        self.go.pack(side="right", fill="both", expand=1)
        # Search options.
        options = [name for name, flags in OPTION_LIST]
        self.option_value = Tk.StringVar() 
        self.options = Tk.OptionMenu(
            self._getSizer(toolbar, 29, 130), self.option_value, *options)
        self.option_value.set(options[0]) 
        self.options.pack(side="right", fill="both", expand=1)
        # Text entry.
        self.search = Tk.Entry(self._getSizer(toolbar, 24, 130))
        self.search.pack(side="right", padx=3, fill="both", expand=1)
        self.search.bind("<Return>", self.onKey)
        # Store a list of the last searches.
        self.search_list = []
    #@-node:ekr.20040108054555.3:addWidgets
    #@+node:ekr.20040107092135.5:doSearch
    def doSearch(self,*args,**keys):
        
        """Do the actual search"""
        # import pdb; pdb.set_trace()
        c = self.c
        text = self.search.get()
        # Remove the old find frame so its options don't compete with ours.
        search_mode = self.option_value.get() 
        new_find = QuickFind(c,text,search_mode)
        
        if 1:
            old_find, c.frame.findPanel = c.frame.findPanel, new_find
        else: # Global find frame.
            old_find, g.app.findFrame = g.app.findFrame, new_find
        # Do the search.
        c.findNext()
        # Restore the find frame.
        if 1:
            c.frame.findPanel = old_find
        else:
            g.app.findFrame = old_find
        # Remember this list 
        self.updateRecentList(text, search_mode) 
        if 0: # This doesn't work yet: the user can't see the match.
            self.search.focus_set()
    #@nonl
    #@-node:ekr.20040107092135.5:doSearch
    #@+node:ekr.20040107111307:onBackSpace
    def onBackSpace (self,event=None):
        g.trace()
    #@-node:ekr.20040107111307:onBackSpace
    #@+node:ekr.20040108054555.5:onKey
    def onKey (self,event=None): 
        """Called when the user presses Return in the text entry box"""
        self.search.after_idle(self.doSearch)
    
    #@-node:ekr.20040108054555.5:onKey
    #@+node:ekr.20040108054555.8:searchRecent
    def searchRecent(self, *args, **kw):
        """Do a search on a recently used item"""
        # Find the item.
        name = self.option_value.get() 
        for item_name, mode in self.search_list:
            if item_name == name: 
                # Ok, so set mode and text and then do the search 
                self.option_value.set(mode)
                self.search.delete(0, "end")
                self.search.insert(0, name)
                self.doSearch() 
                break
        else:
            print name, self.search_list 
            g.es("Recent search item not found! Looks like a bug ...", color="red")
    #@nonl
    #@-node:ekr.20040108054555.8:searchRecent
    #@+node:ekr.20040108054555.7:updateRecentList
    def updateRecentList(self, text, search_mode):
        """Update the list of recently searched items"""
    
        # First update the menu - delete all the options if there are any
        menu = self.options["menu"]
        if self.search_list:
            menu.delete(len(OPTION_LIST),"end")
    
        menu.add_command(label="-------------", command=lambda:0) 
    
        # Update and prune list to remove a previous search for this text 
        self.search_list = [(text, search_mode)] +  [
            (name, mode) for name, mode in self.search_list[:SEARCH_LIST_LENGTH] if name <> text] 
    
        # Now update the menu 
        for name, mode in self.search_list:
            menu.add_command(
                label=name,command=Tk._setit(self.option_value,name,self.searchRecent))
    #@nonl
    #@-node:ekr.20040108054555.7:updateRecentList
    #@-others
#@nonl
#@-node:ekr.20040107092135.3:class SearchBox
#@+node:ekr.20040107092135.6:class QuickFind
class QuickFind(leoFind.leoFind):
    
    """A class for quick searching"""
    
    #@    @+others
    #@+node:ekr.20040107092135.7:__init__
    def __init__(self,c,text,search_option=""):
        
        """Initialize the finder"""
    
        # Init the base class.
        leoFind.leoFind.__init__(self,c)
        
        self.c = c
        self.s_ctrl = Tk.Text() # Used by find.search()
        self.__find_text = text
        self.search_option = search_option
    #@nonl
    #@-node:ekr.20040107092135.7:__init__
    #@+node:ekr.20040107092135.8:update_ivars
    # Modified from leoTkinterFind.update_ivars.
    
    def update_ivars (self):
        
        """Called just before doing a find to update ivars."""
    
        for key in self.intKeys:
            # g.trace('settattr',key,False)
            setattr(self, key,False)
    
        self.change_text = ""
        self.find_text = self.__find_text
    
        # Set options from OPTIONS_DICT.
        for flag_name in OPTION_DICT[self.search_option]: 
            if flag_name.startswith("!"): 
                value = 0 
                name = flag_name[1:] 
            else: 
                value = 1 
                name = flag_name
            # g.trace('settattr',name,value)
            setattr(self, name, value)
    #@nonl
    #@-node:ekr.20040107092135.8:update_ivars
    #@+node:ekr.20040107103252:init_s_ctrl
    def init_s_ctrl (self,s):
        
        t = self.s_ctrl
        t.delete("1.0","end")
        t.insert("end",s)
        t.mark_set("insert",g.choose(self.reverse,"end","1.0"))
        return t
    #@nonl
    #@-node:ekr.20040107103252:init_s_ctrl
    #@+node:ekr.20040107103339:gui_search
    def gui_search (self,t,*args,**keys):
    
        return t.search(*args,**keys)
    #@nonl
    #@-node:ekr.20040107103339:gui_search
    #@-others
#@-node:ekr.20040107092135.6:class QuickFind
#@-others

if Tk: # OK for unit testing.

    if g.app.gui is None:
        g.app.createTkGui(__file__)

    if g.app.gui.guiName() == "tkinter":
        leoPlugins.registerHandler("after-create-leo-frame", onCreate)
        g.plugin_signon(__name__)
#@nonl
#@-node:ekr.20040107092135.2:@thin searchbox.py
#@-leo
