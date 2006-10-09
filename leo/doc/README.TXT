Leo 4.4.2 beta 2                                  October 9, 2006

Leo 4.4.2 beta 2 is available at:
http://sourceforge.net/project/showfiles.php?group_id=3458&package_id=29106

Leo is a text editor, data organizer, project manager and much more. See:
http://webpages.charter.net/edreamleo/intro.html

The highlights of Leo 4.4.2:
----------------------------
- You can now store settings in myLeoSettings.leo without fear of those settings
  being changed by cvs updates or in future versions of Leo.
- Leo's vnode tnode and position classes are now completely independent of the rest of Leo.
  Some api's have been changed.  This 'big reorg' and may affect scripts and plugins.
- Leo's vnode and tnode classes can optionally be compatible with ZODB databases,
  i.e., they can optionally derive from ZODB.Persistence.Persistent.
  See Chapter 17: Using ZODB with Leo for details.
- The leoOPML plugin defines commands to read and write OPML files.
- The slideshow plugin allows Leo to run slideshows defined by @slideshow and @slide nodes.
- The leo_to_rtf and leo_to_html plugins create rtf and html files from Leo outlines.
- Much faster navigation through the outline.
- When focus is in the outline pane, you can move to headlines by typing the first letter of headlines.
- The find command now optionally closes nodes not needed to show the node containing the present match.
- Numerous changes that make Leo easier to use without using a mouse, including new commands and options.
- Many more minibuffer commands appear in the Cmds menu.
- A sax parser can now optionally read .leo files.
- Dozens of bug fixes.

Quote of the month:
------------------
For the non-leo python project I'm (supposed to be) working on, I'm switching from emacs to leo :-)
-- Terry Brown

Links:
------
Leo:      http://webpages.charter.net/edreamleo/front.html
Home:     http://sourceforge.net/projects/leo/
Download: http://sourceforge.net/project/showfiles.php?group_id=3458
CVS:      http://leo.tigris.org/source/browse/leo/
Quotes:   http://webpages.charter.net/edreamleo/testimonials.html
