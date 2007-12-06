echo off
rem ekr pylint-leo.bat

rem E0602 Undefined variable
rem E1101 Instance of <class> has no x member

rem W0104 Statement seems to have no effect
rem W0122 Use of the exec statement
rem W0141 Used builtin function 'map'
rem W0201 Attribute defined outside __init__
rem W0212 Access to a protected member of a client class
rem W0231 __init__ method from base class is not called
rem W0232 Class has no __init__ method
rem W0401 Wildcard import (pychecker)
rem W0402 Uses of a deprecated module (like string)
rem W0406 Module import itself
rem W0602 Using global for x but no assigment is done (leoEditCommands defines classList after all classes).
rem W0603 Using the global statement
rem W0612 Unused variable
rem W0613 Unused argument (sometimes used for debugging)
rem W0621 Redefining <name> from outer scope: especially __pychecker__
rem W0622 Redefining built-in
rem W0631 Using possibly undefined loop variable

rem R0903 Too few public methods (0/1)


REM passed...
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoAtFile.py --disable-msg=W0212,W0401,W0402,W0613 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoFileCommands.py --disable-msg=W0401,W0402 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoImport.py --disable-msg=W0402 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
REM *** leoEditCommands.py: Dangerous: E1101. W0631 is ok. many W0612 and W0201 warnings
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoEditCommands.py --disable-msg=E1101,W0141,W0201,W0402,W0602,W0612,W0613,W0621,W0631 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
REM *** leoGlobals.py: Dangerous: E0602,E1101.
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoGlobals.py --disable-msg=E0602,E1101,W0104,W0122,W0212,W0402,W0406,W0602,W0603,W0612,W0613,W0621,W0631,R0903 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoNodes.py --disable-msg=W0212,W0231,W0232,W0401,W0402,W0612,W0613,W0622,R0903 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem *** Template: disable warnings for unused args & variables.
rem call pylint.bat c:\prog\tigris-cvs\leo\src\xxx.py --disable-msg=W0612,W0613 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\xxx.py --disable-msg=W0612,W0613 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt

rem not passed...

rem to do leoCommands, leoTangle, leoUndo, leoPlugins
rem to do leoFind, leoFrame, leoGui, leoMenu
rem to do leoTkinterDialog, leoTkinterFind, leoTkinterGui, leoTkinterFrame, leoTkinterKeys, leoTkinterMenu, leoTkinterTree.

echo on

cd c:\prog\pylint-0.13.2\bin

call pylint.bat c:\prog\tigris-cvs\leo\src\leoChapters.py --disable-msg=W0212,W0231,W0232,W0401,W0402,W0612,W0613,W0622,R0903 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt

echo "*****done*****"

pause