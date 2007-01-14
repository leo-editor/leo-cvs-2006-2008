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
    #@+node:ekr.20061031170011:ctor (tkinterKeyHandlerClass)
    def __init__(self,c,useGlobalKillbuffer=False,useGlobalRegisters=False):
        
        # Init the base class.
        leoKeys.keyHandlerClass.__init__(self,c,useGlobalKillbuffer,useGlobalRegisters)
        
        # Create
        self.createTkIvars()
    
    #@-node:ekr.20061031170011:ctor (tkinterKeyHandlerClass)
    #@+node:ekr.20061031170011.1:createTkIvars
    def createTkIvars(self):
    
        if not self.useTextWidget and self.widget:
            self.svar = Tk.StringVar()
            self.widget.configure(textvariable=self.svar)
        else:
            self.svar = None
    #@-node:ekr.20061031170011.1:createTkIvars
    #@+node:ekr.20061031170011.3:Minibuffer(Tk keys)
    #@+at 
    #@nonl
    # There is something dubious about tracking states separately for separate 
    # commands.
    # In fact, there is only one mini-buffer, and it has only one state.
    # OTOH, maintaining separate states makes it impossible for one command to 
    # influence another.
    # 
    # trace = self.trace_minibuffer and not g.app.unitTesting
    #@-at
    #@+node:ekr.20061031170011.5:getLabel
    def getLabel (self,ignorePrompt=False):
        
        k = self ; w = self.widget
        if not w: return ''
        
        if self.useTextWidget:
            w.update_idletasks()
            s = w.getAllText()
        else:
            s = k.svar and k.svar.get()
    
        if ignorePrompt:
            return s[len(k.mb_prefix):]
        else:
            return s or ''
    #@-node:ekr.20061031170011.5:getLabel
    #@+node:ekr.20061031170011.6:protectLabel
    def protectLabel (self):
        
        k = self ; w = self.widget
        if not w: return
    
        if self.useTextWidget:
            w.update_idletasks()
            k.mb_prefix = w.getAllText()
        else:
            if k.svar:
                k.mb_prefix = k.svar.get()
    #@-node:ekr.20061031170011.6:protectLabel
    #@+node:ekr.20061031170011.7:resetLabel
    def resetLabel (self):
        
        k = self
        k.setLabelGrey('')
        k.mb_prefix = ''
    #@-node:ekr.20061031170011.7:resetLabel
    #@+node:ekr.20061031170011.8:setLabel
    def setLabel (self,s,protect=False):
    
        k = self ; c = k.c ; w = self.widget
        if not w: return
        trace = self.trace_minibuffer and not g.app.unitTesting
    
        trace and g.trace(repr(s),g.callers())
    
        if self.useTextWidget:
            w.delete(0,'end')
            w.insert(0,s)
            c.masterFocusHandler() # Restore to the previously requested focus.
        else:
            if k.svar: k.svar.set(s)
    
        if protect:
            k.mb_prefix = s
    #@-node:ekr.20061031170011.8:setLabel
    #@+node:ekr.20061031170011.9:extendLabel
    def extendLabel(self,s,select=False,protect=False):
        
        k = self ; c = k.c ; w = self.widget
        if not w: return
        trace = self.trace_minibuffer and not g.app.unitTesting
        
        trace and g.trace(repr(s))
        if not s: return
    
        if self.useTextWidget:
            c.widgetWantsFocusNow(w)
            w.insert('end',s)
            if select:
                i,j = k.getEditableTextRange()
                w.setSelectionRange(i,j,insert=j)
            if protect:
                k.protectLabel()
    #@-node:ekr.20061031170011.9:extendLabel
    #@+node:ekr.20061031170011.10:setLabelBlue
    def setLabelBlue (self,label=None,protect=False):
        
        k = self ; w = k.widget
        if not w: return
        
        w.configure(background='lightblue')
    
        if label is not None:
            k.setLabel(label,protect)
    #@-node:ekr.20061031170011.10:setLabelBlue
    #@+node:ekr.20061031170011.11:setLabelGrey
    def setLabelGrey (self,label=None):
    
        k = self ; w = self.widget
        if not w: return
        
        w.configure(background='lightgrey')
        if label is not None:
            k.setLabel(label)
    
    setLabelGray = setLabelGrey
    #@-node:ekr.20061031170011.11:setLabelGrey
    #@+node:ekr.20061031170011.12:updateLabel
    def updateLabel (self,event):
    
        '''Mimic what would happen with the keyboard and a Text editor
        instead of plain accumalation.'''
        
        k = self ; c = k.c ; w = self.widget
        ch = (event and event.char) or ''
        keysym = (event and event.keysym) or ''
        trace = self.trace_minibuffer and not g.app.unitTesting
    
        trace and g.trace('ch',ch,'keysym',keysym,'k.stroke',k.stroke)
        
        if ch and ch not in ('\n','\r'):
            if self.useTextWidget:
                c.widgetWantsFocusNow(w)
                i,j = w.getSelectionRange()
                if i != j:
                    w.delete(i,j)
                if ch == '\b':
                    s = w.getAllText()
                    if len(s) > len(k.mb_prefix):
                        w.delete(i-1)
                else:
                    w.insert('insert',ch)
                # g.trace(k.mb_prefix)       
            else:
                # Just add the character.
                k.setLabel(k.getLabel() + ch)
    #@-node:ekr.20061031170011.12:updateLabel
    #@+node:ekr.20061031170011.13:getEditableTextRange (should return Python indices)
    def getEditableTextRange (self):
        
        k = self ; w = self.widget
        s = w.getAllText()
        # g.trace(len(s),repr(s))
    
        i = len(k.mb_prefix)
        ###while s.endswith('\n') or s.endswith('\r'):
        ###    s = s[:-1]
        j = len(s)
        return i,j
    #@nonl
    #@-node:ekr.20061031170011.13:getEditableTextRange (should return Python indices)
    #@-node:ekr.20061031170011.3:Minibuffer(Tk keys)
    #@-others
#@nonl
#@-node:ekr.20031218072017.4099:@thin leoTkinterKeys.py
#@-leo
