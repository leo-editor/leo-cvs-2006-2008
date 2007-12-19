echo off
rem ekr pylint-leo.bat

rem *** Most warnings are disabled in the .rc file.

rem E0602 Undefined variable
rem E1101 Instance of <class> has no x member

REM templates
rem call pylint.bat c:\prog\tigris-cvs\leo\src\xxx.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\xxx.py --disable-msg=W0612,W0613 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt

REM passed...
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoAtFile.py --disable-msg=W0212,W0401,W0402,W0613 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoAtFile.py --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoChapters.py --disable-msg=W0212,W0231,W0232,W0401,W0402,W0612,W0613,W0621,W0622,R0903 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoCommands.py --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoFileCommands.py --disable-msg=W0401,W0402 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
REM *** leoEditCommands.py: Dangerous: E1101. W0631 is ok. many W0612 and W0201 warnings
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoEditCommands.py --disable-msg=E1101,W0141,W0201,W0402,W0602,W0612,W0613,W0621,W0631 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
REM *** leoGlobals.py: Dangerous: E0602,E1101.
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoGlobals.py --disable-msg=E0602,E1101,W0104,W0122,W0212,W0402,W0406,W0602,W0603,W0612,W0613,W0621,W0631,R0903 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoImport.py --disable-msg=W0402 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoNodes.py --disable-msg=W0212,W0231,W0232,W0401,W0402,W0612,W0613,W0622,R0903 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt

REM not passed...

rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoFind.py     --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoFrame.py   --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoGui.py       --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoMenu.py    --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoPlugins.py  --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTangle.py  --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkiinterGui.py    --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterDialog.py --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterFind.py    --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterFrame.py  --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterKeys.py    --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterMenu.py   --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterTree.py   --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoUndo.py             --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt'

REM All:
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoAtFile.py --disable-msg=W0212,W0401,W0402,W0613 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoChapters.py --disable-msg=W0212,W0231,W0232,W0401,W0402,W0612,W0613,W0621,W0622,R0903 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoCommands.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoEditCommands.py --disable-msg=E1101,W0141,W0201,W0402,W0602,W0612,W0613,W0621,W0631 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoFileCommands.py --disable-msg=W0401,W0402 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoFind.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoFrame.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoGlobals.py --disable-msg=E0602,E1101,W0104,W0122,W0212,W0402,W0406,W0602,W0603,W0612,W0613,W0621,W0631,R0903 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoGui.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoImport.py --disable-msg=W0402 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoMenu.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoNodes.py --disable-msg=W0212,W0231,W0232,W0401,W0402,W0612,W0613,W0622,R0903 --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoPlugins.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTangle.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkiinterGui.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterDialog.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterFind.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterFrame.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterKeys.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterMenu.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoTkinterTree.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt
rem call pylint.bat c:\prog\tigris-cvs\leo\src\leoUndo.py --disable-msg= --rcfile=c:\prog\tigris-cvs\leo\test\pylint-leo-rc.txt'

echo on

cd c:\prog\pylint-0.13.2\bin



echo "*****done*****"

pause