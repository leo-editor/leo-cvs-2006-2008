echo off
rem ekr pylint-leo.bat
rem WW0212Access to a protected member of a client class
rem W0401 Wildcard import (pychecker)
rem W0402 Uses of a deprecated module (string in leoAtFile)
rem W0613 Unused argument (sometimes used for debugging)
rem W0621 Redefining <name> from outer scope: especially __pychecker__

rem passed...
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoAtFile.py --disable-msg=W0212,W0401,W0402,W0613,W0621 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt

echo on

cd c:\prog\pylint-0.13.2\bin

call pylint.bat c:\prog\tigris-cvs\leo\src\leoFileCommands.py --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt

pause