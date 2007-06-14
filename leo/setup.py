# setup.py to execute a Leo egg

print '='*30,'setup.py','='*30

import setuptools

long_description = \
"""Leo is an IDE, an outliner, a scripting and unit testing framework based on Python,
a literate programming tool, a data organizer and a project manager.

Leo is written in 100% pure Python and works on any platform that supports
Python 2.2.1 or above and the Tk Tk 8.4 or above.

Download Python from http://python.org/
Download tcl/Tk from http://tcl.activestate.com/software/tcltk/
 """

setuptools.setup (
    name='leo',
    version='4-4-3-rc1', # No spaces here!

    author='Edward K. Ream',
    author_email='edreamleo@charter.net',
    url='http://webpages.charter.net/edreamleo/front.html',

    # py_modules=[], # The manifest specifies everything.
    packages = setuptools.find_packages(),
    include_package_data = True, # Required, e.g. for Pmw.def

    description = 'Leo: Literate Editor with Outlines',
    license='Python', # licence [sic] changed to license in Python 2.3
    platforms=['Windows, Linux, Macintosh'],
    long_description = long_description,
    keywords = 'outline, outlinter, ide, editor, literate programming',
)

print ; print '='*30,'setup.py complete','='*30 ; print

