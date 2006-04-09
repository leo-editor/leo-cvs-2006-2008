#@+leo-ver=4-thin
#@+node:pap.20051010170720:@thin newButtons.py
#@<< docstring >>
#@+node:pap.20051010170720.1:<< docstring >>
"""Allows the use of template nodes for common tasks

Template nodes can be create for any node. The template can then
be inserted at the click of a button. This is a bit like a permanent
clipboard except that templates can have items in them which can 
be overriden. Nodes can contain any number of child nodes.

For instance you might want to have a template for a unit test method.
The unit test method template includes a name and description. When
you create an instance of the template these items can be specified.

To override items in the template you insert strings with the following
form::
            $$expr$$
            
These strings can be anywhere in the headline or body text. The *expr*
is an expression which will be evaluated in a namespace containing two
existing names,

    name = the name entered into the entry box in the toolbar
    node = the leo Vnode that was selected when the *New* button was pressed
    
You can use this in many way, eg to create a custom file from a template::
    
    @thin $$name$$.py   <- in the headline text
    
Or to create a unit test node (using methods of the *name* object)::
    
    @thin test$$name.lower()$$
    < body text >
       class $$name$$:   <- in a child node
       
The following menu items are available:
    
MakeTemplateFrom
    Create a template from the current node. You will be asked to enter the
    name for the template.
    
UpdateTemplateFrom
    Update a specific template from the current node. You will be asked
    to select the template to update.
    
DeleteTemplate
    Delete a specific template. You will be asked to select the template to delete.
    
AddRawTemplate
    Adds the contents of a template to the outline but doesn't convert the
    $$name$$ values. This is useful for updating a template using UpdateTemplateFrom
    at a later stage.

"""
#@nonl
#@-node:pap.20051010170720.1:<< docstring >>
#@nl

__name__ = "New Buttons"
__version__ = "0.8"

USE_FIXED_SIZES = 1

#@<< version history >>
#@+node:pap.20051010170720.2:<< version history >>
#@@killcolor
#@+at
# 
# 0.1 Paul Paterson: First version
# 0.2 EKR: Converted to @file-noref
# 0.3 EKR: Added 6 new plugin templates.  Added init function.
# 0.4 EKR: Added importLeoGlobals function.
# 0.5 Paul Paterson: Rewrite from scratch
# 0.6 EKR: Added support for template_path setting.
# 0.7 EKR: removed g.top and improved the code.
# - Added c args to most classes, but **not** to the Template class.
# - Changed global helper to helpers: now a dict (keys are commanders, values 
# are UIHelpers).
# - Eliminated fromFile static method (now part of TemplateCollection ctor).
# - Made getTemplateFromNode a regular method.
# - Changed helper.commander to helper.c for consistency and clarity.
# - Added templates and templateNames ivars to TemplateCollection class.
# - Added add and remove methods to TemplateCollection class.
# 0.8 EKR:
# - cmd_ functions now get c arg.
# - Added message when deleting template file.
#@-at
#@nonl
#@-node:pap.20051010170720.2:<< version history >>
#@nl
#@<< imports >>
#@+node:pap.20051010170720.3:<< imports >>
import leoGlobals as g
import leoPlugins

import os
import glob
import re

# Whatever other imports your plugins uses.
try:
    Tk = g.importExtension('Tkinter',pluginName=__name__,verbose=True)
    Pmw = g.importExtension("Pmw",    pluginName=__name__,verbose=True)    
except ImportError:
    Tk = None
#@-node:pap.20051010170720.3:<< imports >>
#@nl

helpers = {}

#@+others
#@+node:ekr.20060107123625:Module-level functions
#@+node:pap.20051010170720.4:init
def init ():
    
    ok = True # This might depend on imports, etc.
    
    if ok:
        leoPlugins.registerHandler('after-create-leo-frame',onCreate)
        g.plugin_signon("newButtons")
            
    return ok
#@nonl
#@-node:pap.20051010170720.4:init
#@+node:pap.20051010170720.5:onCreate
def onCreate (tag, keywords):
    
    """
    Showing how to define a global hook that affects all commanders.
    """

    import leoTkinterFrame
    log = leoTkinterFrame.leoTkinterLog
    
    # Ensure that the templates folder is there
    folder = g.os_path_join(g.app.loadDir,"..","plugins", "templates")
    try:
        os.mkdir(folder)
    except OSError, err:
        pass # Ok if it is there already

    global helpers
    c = keywords.get("c")
    helpers[c] = helper = UIHelperClass(c,folder)
    helper.addWidgets()
#@nonl
#@-node:pap.20051010170720.5:onCreate
#@+node:pap.20051011221702:Commands exposed as menus
#@+node:pap.20051010172840:cmd_MakeTemplateFrom
def cmd_MakeTemplateFrom(c):
    """Make a template from a node"""
    helper = helpers.get(c)
    if helper:
        helper.makeTemplate()
#@nonl
#@-node:pap.20051010172840:cmd_MakeTemplateFrom
#@+node:pap.20051011153949:cmd_UpdateTemplateFrom
def cmd_UpdateTemplateFrom(c):
    """Update a template from a node"""

    helper = helpers.get(c)
    if helper:
        helper.updateTemplate()
#@nonl
#@-node:pap.20051011153949:cmd_UpdateTemplateFrom
#@+node:pap.20051011155514:cmd_DeleteTemplate
def cmd_DeleteTemplate(c):
    """Delete a template"""
    helper = helpers.get(c)
    if helper:
        helper.deleteTemplate()
#@nonl
#@-node:pap.20051011155514:cmd_DeleteTemplate
#@+node:pap.20051011160100:cmd_AddRawTemplate
def cmd_AddRawTemplate(c):

    """Add a raw template"""
    helper = helpers.get(c)
    if helper:
        helper.addRawTemplate()
#@nonl
#@-node:pap.20051011160100:cmd_AddRawTemplate
#@-node:pap.20051011221702:Commands exposed as menus
#@-node:ekr.20060107123625:Module-level functions
#@+node:pap.20051010171746:UI
#@+node:pap.20051010171746.1:class FlatOptionMenu
class FlatOptionMenu(Tk.OptionMenu):
    """Flat version of OptionMenu which allows the user to select a value from a menu."""

    #@    @+others
    #@+node:ekr.20060107141254:ctor
    def __init__(self, master, variable, value, *values, **kwargs):
        """Construct an optionmenu widget with the parent MASTER, with 
        the resource textvariable set to VARIABLE, the initially selected 
        value VALUE, the other menu values VALUES and an additional 
        keyword argument command.""" 
        kw = {
            "borderwidth": 2, "textvariable": variable,
            "indicatoron": 1, "relief": "flat", "anchor": "c",
            "highlightthickness": 2}
        Tk.Widget.__init__(self, master, "menubutton", kw)
        self.widgetName = 'tk_optionMenu' 
        menu = self.__menu = Tk.Menu(self, name="menu", tearoff=0)
        self.menuname = menu._w
        # 'command' is the only supported keyword 
        callback = kwargs.get('command')
        if kwargs.has_key('command'):
            del kwargs['command']
        if kwargs:
            raise TclError, 'unknown option -'+kwargs.keys()[0]
        self["menu"] = menu
        self.__variable = variable
        self.__callback = callback
        self.addMenuItem(value)
        for v in values:
            self.addMenuItem(v)
    #@nonl
    #@-node:ekr.20060107141254:ctor
    #@+node:ekr.20060107141254.1:addMenuItem
    def addMenuItem(self, name):
        """Add an item to the menu"""
        self.__menu.add_command(label=name,
                command=Tk._setit(self.__variable, name, self.__callback))
    #@-node:ekr.20060107141254.1:addMenuItem
    #@-others
#@nonl
#@-node:pap.20051010171746.1:class FlatOptionMenu
#@+node:pap.20051010171746.2:class UIHelper
class UIHelperClass:
    """Helper class to collect all UI functions"""
    
    #@    @+others
    #@+node:pap.20051010173622:__init__
    def __init__(self, c, folder):
        """Initialize the helper"""
        self.c = c
        self.folder = folder
        self.templateCollection = TemplateCollection(c,folder)
    #@nonl
    #@-node:pap.20051010173622:__init__
    #@+node:pap.20051010171746.3:addWidgets
    def addWidgets(self):
        """Add the widgets to Leo"""
        toolbar = self.c.frame.iconFrame
        # 
        self.frame = Tk.Frame(toolbar)
        self.frame.pack(side="right", padx=2)
        # 
        self.text = Tk.Entry(self._getSizer(self.frame, 24, 130))
        self.text.pack(side="left", padx=3, fill="both", expand=1)
        self.text.bind("<Return>", self.newItemClicked)
        # 
        self.pseudobutton = Tk.Frame(self._getSizer(self.frame, 24, 142),
            relief="raised", borderwidth=2) 
        self.pseudobutton.pack(side="right")
        # 
        self.doit = Tk.Button(self._getSizer(self.pseudobutton, 25, 32),
            text="New", relief="flat", command=self.newItemClicked)
        self.doit.pack(side="left")
        
        if self.templateCollection.templateNames:
            options = [name for name in self.templateCollection.templateNames]
            options.sort()
        else:
            options = ["Template?"]
        self.option_value = Tk.StringVar()
        self.options = FlatOptionMenu(self._getSizer(self.pseudobutton, 29, 110),
            self.option_value, *options)
        self.option_value.set(options[0])
        self.options.pack(side="right", fill="both", expand=1)
    #@-node:pap.20051010171746.3:addWidgets
    #@+node:pap.20051010171746.4:newItemClicked
    def newItemClicked(self, event=None):
        """Generate a callback to call the specific adder"""
        nodename = self.option_value.get()
        if nodename == "Template?":
            pass
        else:
            self.addTemplate(nodename, self.text.get())
    #@nonl
    #@-node:pap.20051010171746.4:newItemClicked
    #@+node:pap.20051011160416:addTemplate
    def addTemplate (self,name,parameter=None):
        """Add a template node"""
        c = self.c ; p = self.c.currentPosition()
        template = self.templateCollection.find(name)
        if template:
            root = p.copy()
            template.addNodes(c,p,parameter,top=True)
            c.selectPosition(root.next())
    #@-node:pap.20051011160416:addTemplate
    #@+node:pap.20051010175537:makeTemplate
    def makeTemplate(self):
        """Make a template from the current node"""
        c = self.c
        def makeit(result,c=c):
            if result is not None:
                p = self.c.currentPosition()
                template = Template().getTemplateFromNode(p, name=result)
                template.save(c)
                self.templateCollection.add(template)
                self.options.addMenuItem(template.name)
                        
        form = MakeTemplateForm(c,makeit)
        
    #@-node:pap.20051010175537:makeTemplate
    #@+node:pap.20051011155041:updateTemplate
    def updateTemplate(self):
        """Update a template from the current node"""
        c = self.c
        def updateit(result,c=c):
            if result is not None:
                tc = self.templateCollection
                # Remove old one
                tc.remove(tc.find(result))
                # Now create a new one
                p = c.currentPosition()
                newtemplate = Template().getTemplateFromNode(p, name=result)
                newtemplate.save(c)
                tc.add(newtemplate)
                         
        form = SelectTemplateForm(self,updateit, "Update template")
        
    #@-node:pap.20051011155041:updateTemplate
    #@+node:pap.20051011160416.1:addRawTemplate
    def addRawTemplate(self):
        """Add a template but don't convert the text"""
        c = self.c
        def addraw(result):
            if result is not None:
                self.addTemplate(result)
                         
        form = SelectTemplateForm(self,addraw, "Add raw template")
    #@nonl
    #@-node:pap.20051011160416.1:addRawTemplate
    #@+node:pap.20051011155642:deleteTemplate
    def deleteTemplate(self):
        """Delete a template"""
        c = self.c
        def deleteit(result):
            if result is not None:
                # Remove old one
                tc = self.templateCollection
                tc.remove(tc.find(result))
                filename = "%s.tpl" % result
                folder = g.os_path_abspath(self.folder)
                os.remove(g.os_path_join(folder, filename))
                g.es('deleted template %s from %s' % (filename,folder),color='blue')
                         
        form = SelectTemplateForm(self,deleteit, "Delete template")
    #@nonl
    #@-node:pap.20051011155642:deleteTemplate
    #@+node:pap.20051010172432:_getSizer
    def _getSizer(self, parent, height, width, pack="left"):
        """Return a sizer object to force a Tk widget to be the right size"""
        if USE_FIXED_SIZES:
            sizer = Tk.Frame(parent, height=height, width=width)
            sizer.pack_propagate(0) # don't shrink 
            sizer.pack(side=pack)
            return sizer
        else:
            return parent
    #@-node:pap.20051010172432:_getSizer
    #@-others
    
    
#@nonl
#@-node:pap.20051010171746.2:class UIHelper
#@+node:pap.20051011154233:class HelperForm
class HelperForm:
    """Base class for all forms"""
    
    #@    @+others
    #@+node:pap.20051011154400:__init__
    def __init__(self, c, callback, title):
        """Initialise the form"""
        self.c = c
        self.root = root = g.app.root
        self.callback = callback
        
        self.dialog = dialog = Pmw.Dialog(root,
                buttons = ('OK', 'Cancel'),
                defaultbutton = 'OK',
                title = title,
                command = self.formCommit,
        )
        
    #@-node:pap.20051011154400:__init__
    #@+node:pap.20051011154642:formCommit
    def formCommit(self, name):
        """The user closed the form"""
        if name == "OK":
            result = self.getResult()
        else:
            result = None
        self.dialog.destroy() 
        self.callback(result)
           
    #@nonl
    #@-node:pap.20051011154642:formCommit
    #@-others
#@nonl
#@-node:pap.20051011154233:class HelperForm
#@+node:pap.20051010195044:class MakeTemplateForm
class MakeTemplateForm(HelperForm):
    """A form to initialize a template"""
    
    #@    @+others
    #@+node:pap.20051010195044.1:__init__
    def __init__(self, c, callback):
        """Initialise the form"""
        
        self.c = c
        HelperForm.__init__(self, c, callback, "Add new template")
        
        parent = self.dialog.interior()
        
        def isvalid(x):
            if len(x) > 1:
                return 1
            else:
                return -1
                
        self.name = Pmw.EntryField(parent,
                labelpos = 'w',
                label_text = 'Template name:',
                validate = isvalid,
        )
        
        self.getResult = self.name.getvalue
        
        entries = (self.name, )
        
        for entry in entries:
            entry.pack(fill='x', expand=1, padx=10, pady=5)
        
        Pmw.alignlabels(entries)
    
    #@-node:pap.20051010195044.1:__init__
    #@-others
#@nonl
#@-node:pap.20051010195044:class MakeTemplateForm
#@+node:pap.20051011153949.1:class SelectTemplateForm
class SelectTemplateForm(HelperForm):
    """A form to select a template"""
    
    #@    @+others
    #@+node:pap.20051011154233.1:__init__
    def __init__(self, helper, callback, title):
        """Initialise the form"""
        
        self.helper = helper
        self.c = c = helper.c
        HelperForm.__init__(self, c, callback, title)
        
        # items = [template.name for template in helper.templates] or ["Template?"],
        if helper.templateCollection.templateNames:
            items = [name for name in helper.templateCollection.templateNames]
            items.sort()
        else:
            items = ["Template?"]
                
        self.name = Pmw.OptionMenu(self.dialog.interior(),
                labelpos = 'w',
                label_text = 'Template name:',
                items = items,
                menubutton_width = 10,
        )
        
        self.getResult = self.name.getvalue
        entries = (self.name, )
        
        for entry in entries:
            entry.pack(fill='x', expand=1, padx=10, pady=5)
        
        Pmw.alignlabels(entries)
    #@nonl
    #@-node:pap.20051011154233.1:__init__
    #@-others
#@nonl
#@-node:pap.20051011153949.1:class SelectTemplateForm
#@-node:pap.20051010171746:UI
#@+node:pap.20051010173800:Implementation
#@+node:pap.20051010173800.1:class TemplateCollection
class TemplateCollection(list):
    """Represents a collection of templates"""
    
    #@    @+others
    #@+node:pap.20051010173800.2:__init__
    def __init__(self, c, folder):
        """Initialize the collection"""
        
        self.c = c
        self.folder = folder
        self.templateNames = []
        self.templates = {}
        for filename in glob.glob(g.os_path_join(folder, "*.tpl")):
            try:
                # Create a new template by evaluating the file.
                text = file(filename, "r").read()
                template = eval(text)
                self.add(template)
                # g.trace(repr(template))
            except Exception:
                g.es('Exception reading template file %s' % filename)
                g.es_exception()
    #@nonl
    #@-node:pap.20051010173800.2:__init__
    #@+node:ekr.20060107134001:add & remove
    def add (self,template):
    
        name = template.name
        self.templateNames.append(name)
        self.templates [name] = template
    
    def remove (self,template):
    
        name = template.name
        if name in self.templateNames:
            self.templateNames.remove(name)
            del self.templates [name]
    #@nonl
    #@-node:ekr.20060107134001:add & remove
    #@+node:pap.20051010183939:find
    def find(self, name):
        """Return the named template"""
        return self.templates.get(name)
    #@nonl
    #@-node:pap.20051010183939:find
    #@-others
#@nonl
#@-node:pap.20051010173800.1:class TemplateCollection
#@+node:pap.20051010174103:class Template
class Template:
    """Represents a template, with no association with any commander.
    
    Warning: Templates are created by doing an eval of tpl files,
    so changes in the ctor and the file format affect each other.
    """
    
    #@    @+others
    #@+node:pap.20051010180444:__init__
    def __init__(self, headline="", body="", children=None, name=None):
        """Initialize the template"""
        self.name = name
        self.headline = headline
        self.body = body
        if children is None:
            self.children = []
        else:
            self.children = children
    #@nonl
    #@-node:pap.20051010180444:__init__
    #@+node:pap.20051010184315:addNodes
    def addNodes (self,c,parent,parameter="",top=False):
        """Add this template to the current"""
        
        c.beginUpdate()
        try:
            # Add this new node
            c.insertHeadline()
            c.endEditing()
            p = c.currentPosition()
            p.setHeadString(self.convert(self.headline,parameter,parent))
            p.setBodyString(self.convert(self.body,parameter,parent))
        
            # Move it to the proper place.
            if top and not parent.isExpanded():
                p.moveAfter(parent)
            else:
                p.moveToNthChildOf(parent,0)
            
            # Now add the children - go in reverse so we can add them as child 0 (above)
            children = self.children [:]
            children.reverse()
            for child in children:
                child.addNodes(c,p,parameter)
        finally:
            c.endUpdate()
    #@nonl
    #@-node:pap.20051010184315:addNodes
    #@+node:ekr.20060107131019:getTemplateFromNode
    def getTemplateFromNode (self,p,name):
    
        self.name = name
        self.headline = p.headString()
        self.body = p.bodyString()
    
        # Find children
        self.children = children = []
        child = p.getFirstChild()
        while child:
            children.append(Template().getTemplateFromNode(child,child.headString()))
            child = child.getNext()
        return self
    #@nonl
    #@-node:ekr.20060107131019:getTemplateFromNode
    #@+node:pap.20051010182048:save
    def save(self,c):
        
        """Save this template"""
        
        template_path = g.app.config.getString(c,'template_path')
        if template_path:
            filename = g.os_path_join(template_path, "%s.tpl" % self.name)
        else:
            filename = g.os_path_join(
                g.app.loadDir,"..","plugins", "templates", "%s.tpl" % self.name)
            
        f = file(filename, "w")
        
        g.es('writing template %s to %s' % (self.name,g.os_path_abspath(filename)),color='blue')
    
        try:
            f.write(repr(self))
        finally:
            f.close()
    #@nonl
    #@-node:pap.20051010182048:save
    #@+node:pap.20051010181808:repr
    def __repr__(self):
        """Return representation of this node"""
        return "Template(%s, %s, %s, %s)" % (
                repr(self.headline), 
                repr(self.body), 
                repr(self.children),
                repr(self.name))            
    #@nonl
    #@-node:pap.20051010181808:repr
    #@+node:pap.20051010205823:convert
    def convert(self, text, parameter, p):
        """Return the converted text"""
        
        # g.trace('text',text,'param',parameter)
        if parameter is None:
            return text
            
        matcher = re.compile("(.*)\$\$(.+?)\$\$(.*)", re.DOTALL+re.MULTILINE)
        namespace = {
            "name" : parameter,
            "node" : p,
        }
    
        def replacer(match):
            try:
                result = eval(match.groups()[1], namespace)
            except Exception, err:
                g.es("Unable to replace '%s': %s" % (match.groups()[1], err), color="red")
                result = "*ERROR*"
            return "%s%s%s" % (match.groups()[0], result, match.groups()[2])
    
        oldtext = text    
        while True:
            text = matcher.sub(replacer, text)
            if text == oldtext: break
            oldtext = text
    
        return text
    #@nonl
    #@-node:pap.20051010205823:convert
    #@-others
#@nonl
#@-node:pap.20051010174103:class Template
#@-node:pap.20051010173800:Implementation
#@-others
#@nonl
#@-node:pap.20051010170720:@thin newButtons.py
#@-leo
