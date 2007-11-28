echo off
rem ekr pylint-leo.bat

rem E1101 Instance of <class> has no x member
rem W0141 Used builtin function 'map'
rem W0201 Attribute defined outside __init__
rem W0212 Access to a protected member of a client class
rem W0401 Wildcard import (pychecker)
rem W0402 Uses of a deprecated module (like string)
rem W0602 Using global for x but no assigment is done (leoEditCommands defines classList after all classes).
rem W0612 Unused variable
rem W0613 Unused argument (sometimes used for debugging)
rem W0621 Redefining <name> from outer scope: especially __pychecker__
rem W0622 Redefining built-in
rem W0631 Using possibly undefined loop variable

rem passed...
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoAtFile.py --disable-msg=W0212,W0401,W0402,W0613 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoFileCommands.py --disable-msg=W0401,W0402 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoImport.py --disable-msg=W0402 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt

rem leoEditCommands: disabling E1101 is dangerous, disabling W0631 is ok.
rem leoEditCommands: many W0612 and W0201 warnings
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoEditCommands.py --disable-msg=E1101,W0141,W0201,W0402,W0602,W0612,W0631 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt

echo on

cd c:\prog\pylint-0.13.2\bin

call pylint.bat c:\prog\tigris-cvs\leo\src\leoGlobals.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt

pause