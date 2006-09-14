#@+leo-ver=4-thin
#@+node:danr7.20061010105952.1:@thin word_count.py
#@@language python
#@@tabwidth -4

#@<< docstring >>
#@+node:danr7.20061010105952.2:<< docstring >>
'''Word Count 1.0 plugin by Dan Rahmel

This plugin displays a messagebox with information about the body text of the current node 
such as number of: characters, words, lines, and paragraphs. It adds a "Word Count..." option
to the bottom of the Edit menu that will activate the messagebox.

The Word Count... menu has a shortcut key of 'W'.
'''
#@-node:danr7.20061010105952.2:<< docstring >>
#@nl
#@<< version history >>
#@+node:danr7.20061010105952.3:<< version history >>
#@@killcolor
#@+at
# 1.00 - Finalized 1st version of plug-in & added return focus line
# 0.95 - Tested counting routines
# 0.94 - Added shortcut key to menu
# 0.93 - Created para count routine & added char count
# 0.92 - Created line count routine
# 0.91 - Created word count routine
# 0.90 - Created initial plug-in framework
#@-at
#@nonl
#@-node:danr7.20061010105952.3:<< version history >>
#@nl
#@<< imports >>
#@+node:danr7.20061010105952.4:<< imports >>
import leoGlobals as g
import leoPlugins
import tkMessageBox

#@-node:danr7.20061010105952.4:<< imports >>
#@nl

__version__ = "1.0"

#@+others
#@+node:danr7.20061010105952.5:createWordCountMenu
def createWordCountMenu (tag,keywords):

    c = keywords.get("c")

    # Get reference to current File > Export... menu
    exportMenu = c.frame.menu.getMenu('Edit')
    # Use code to find index of menu shortcut
    index_label = '&Word Count...'
    # Find index position of ampersand -- index is how shortcut is defined
    amp_index = index_label.find("&")
    # Eliminate ampersand from menu item text
    index_label = index_label.replace("&","")
    # Add 'Word Count...' to the bottom of the Edit menu.  
    exportMenu.add('command',label=index_label,underline=amp_index,command= lambda c = c : word_count(c))
#@-node:danr7.20061010105952.5:createWordCountMenu
#@+node:danr7.20061010105952.6:word_count
def word_count( c ):
    myBody = c.currentPosition().bodyString()
    charNum = len(myBody)
    wordNum = len(myBody.split(None))
    paraSplit = myBody.split("\n")
    paraNum = len(paraSplit)
    for myItem in paraSplit:
        if myItem == "":
            paraNum -= 1
    lineNum = len(myBody.splitlines())
    myStats = "Words-->" + str(wordNum) + "\nCharacters-->" + str(charNum) + "\nParagraphs-->" + str(paraNum) + "\nLines-->" + str(lineNum)

    answer = tkMessageBox.showinfo("Word Count", myStats)
    # Return focus to Commander window
    c.bringToFront()

#@-node:danr7.20061010105952.6:word_count
#@-others

if 1: # Ok for unit testing: creates menu.
    leoPlugins.registerHandler("create-optional-menus",createWordCountMenu)
    g.plugin_signon(__name__)
#@nonl
#@-node:danr7.20061010105952.1:@thin word_count.py
#@-leo
