#@+leo-ver=4-thin
#@+node:ekr.20031218072017.4099:@thin leoTkinterKeys.py
"""Tkinter keystroke handling for Leo."""

#@@language python
#@@tabwidth -4
#@@pagewidth 80
import leoGlobals as g
import Tkinter as Tk
import leoKeys

class tkinterKeyHandlerClass (leoKeys.keyHandlerClass):
    '''Tkinter overrides of base keyHandlerClass.'''
    #@    @+others
    #@+node:ekr.20061031170011:tkKeys.ctor
    def __init__(self,c,useGlobalKillbuffer=False,useGlobalRegisters=False):
        
        # Init the base class.
        leoKeys.keyHandlerClass.__init__(self,c,useGlobalKillbuffer,useGlobalRegisters)
        
        # Create
        self.createTkIvars()
    #@-node:ekr.20061031170011:tkKeys.ctor
    #@+node:ekr.20061031170011.1:createTkIvars
    def createTkIvars(self):
    
        if not self.useTextWidget and self.widget:
            self.svar = Tk.StringVar()
            self.widget.configure(textvariable=self.svar)
        else:
            self.svar = None
    #@-node:ekr.20061031170011.1:createTkIvars
    #@+node:ekr.20070123085931: tkKeys.defineSpecialKeys
    def defineSpecialKeys (self):
        
        k = self
        
        # These are defined at http://tcl.activestate.com/man/tcl8.4/TkCmd/keysyms.htm.
        # Important: only the inverse dict is actually used in the new key binding scheme.
        # Tk may return the *values* of this dict in event.keysym fields.
        # Leo will warn if it gets a event whose keysym not in values of this table.
        k.guiBindNamesDict = {
            "&" : "ampersand",
            "^" : "asciicircum",
            "~" : "asciitilde",
            "*" : "asterisk",
            "@" : "at",
            "\\": "backslash",
            "|" : "bar",
            "{" : "braceleft",
            "}" : "braceright",
            "[" : "bracketleft",
            "]" : "bracketright",
            ":" : "colon",      # removed from code.
            "," : "comma",
            "$" : "dollar",
            "=" : "equal",
            "!" : "exclam",     # removed from code.
            ">" : "greater",
            "<" : "less",
            "-" : "minus",
            "#" : "numbersign",
            '"' : "quotedbl",
            "'" : "quoteright",
            "(" : "parenleft",
            ")" : "parenright", # removed from code.
            "%" : "percent",
            "." : "period",     # removed from code.
            "+" : "plus",
            "?" : "question",
            "`" : "quoteleft",
            ";" : "semicolon",
            "/" : "slash",
            " " : "space",      # removed from code.
            "_" : "underscore",
        }
        
        # No translation.
        for s in k.tkNamesList:
            k.guiBindNamesDict[s] = s
            
        # Create the inverse dict.
        k.guiBindNamesInverseDict = {}
        for key in k.guiBindNamesDict.keys():
            k.guiBindNamesInverseDict [k.guiBindNamesDict.get(key)] = key
        
    #@-node:ekr.20070123085931: tkKeys.defineSpecialKeys
    #@-others
#@nonl
#@-node:ekr.20031218072017.4099:@thin leoTkinterKeys.py
#@-leo
