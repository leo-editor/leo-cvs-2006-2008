print '='*30,'setup.py','='*30

# Boilerplate to automatically download setuptools if it not installed.
#import ez_setup
#ez_setup.use_setuptools()

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
    version='4.4.3b3', # No spaces!
        # pre-release tags: 4.4.3b1 or 4.4.3rc1 or 4.4.3preview1
        # Do not use post-release-tags: 4.4.3-whatever.
        # final release: 4.4.3final or just 4.4.3.
    author='Edward K. Ream',
    author_email='edreamleo@charter.net',
    url='http://webpages.charter.net/edreamleo/front.html',
    download_url='http://sourceforge.net/project/showfiles.php?group_id=3458',
    py_modules=[], # The manifest specifies everything.
    # packages = setuptools.find_packages(),
    include_package_data = True, # Required, e.g. for Pmw.def
    exclude_package_data = { '': ['*.pyc','*.pyo']},
    zip_safe=False, # Never run Leo from a zip file.
    install_requires=[], #'python>=2.2.1',],
    description = 'Leo: Literate Editor with Outlines',
    license='Python', # licence [sic] changed to license in Python 2.3
    platforms=['all',],
    long_description = long_description,
    keywords = 'outline, outliner, ide, editor, literate programming',
)

print ; print '='*30,'setup.py complete','='*30 ; print
