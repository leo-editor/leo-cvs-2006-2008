;@+leo-ver=4-thin
;@+node:ekr.20050118092706:@thin leo-4-3.nsi
;@@comment ;
; NSIS Script for Leo
; Version 2.0 of this script by David Szent-Gyorgyi, donated to the public domain. Based on
; Version 1.0 of this script by Joe Orr, donated to public domain.
;
; NOTE: this .NSI script is designed for NSIS v2.03+
;
; How to create an installer for Leo using this script:
;	1. Install NSIS 2.03(from http://www.nullsoft.com)
;	2. Put the leo.nsi file in the directory containing the Leo program files.
;	3. Right-click on the leo.nsi file and choose "Compile"
;

; Script generated by the HM NIS Edit Script Wizard and then hand-customized
;@<< defines >>
;@+node:ekr.20050118092706.1:<< defines >>
;@<< 4.3 nsi installer version >>
;@+node:ekr.20050118124408:<< 4.3 nsi installer version >>
!define PRODUCT_VERSION "4.4.2-beta-3"
;@nonl
;@-node:ekr.20050118124408:<< 4.3 nsi installer version >>
;@nl
;@<< HM NIS Edit Wizard helper defines >>
;@+node:ekr.20050118092706.2:<< HM NIS Edit Wizard helper defines >>
; HM NIS Edit Wizard helper defines
!define PRODUCT_NAME "Leo"
!define PRODUCT_PUBLISHER "Edward K. Ream"
!define PRODUCT_WEB_SITE "http://webpages.charter.net/edreamleo/front.html"
; !define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor bzip2
;@-node:ekr.20050118092706.2:<< HM NIS Edit Wizard helper defines >>
;@nl
;@<< custom defines >>
;@+node:ekr.20050118092706.3:<< custom defines >>
;@@comment ;

; hand-created defines
; used for Windows Registry links to uninstaller

!define PRODUCT_NAME_LOWER_CASE "leo"

!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME_LOWER_CASE}"

; On Windows NT-derived operating systems, Python.org installer for Python 2.4 
; can be installed for all users or current user only.
; define the following symbol to install if Python is installed only for current user. 
; !define INSTALL_IF_PYTHON_FOR_CURRENT_USER

!define STRING_PYTHON_NOT_FOUND "Python is not installed on this system. $\nPlease install Python first. $\n$\nClick OK to cancel installation and remove installation Files."

!define STRING_PYTHON_CURRENT_USER_FOUND "Python is installed for the current user only. $\n$\n${PRODUCT_NAME} does not support use with Python so configured. $\n$\nClick OK to cancel installation and remove installation Files."
;@nonl
;@-node:ekr.20050118092706.3:<< custom defines >>
;@nl
;@nonl
;@-node:ekr.20050118092706.1:<< defines >>
;@nl
;@<< Settings >>
;@+node:ekr.20050118092706.4:<< Settings >>
; settings taken from Version 1.0 of NSIS Script for Leo
Caption "Leo Installer"
AutoCloseWindow false 
SilentInstall normal
CRCCheck on ; FIXME shouldn't this be CRCCheck force ? Why give user option of using corrupted installer?
SetCompress auto ; FIXME this is disabled for solid compression, which comes with BZip2 and LZMA compression
SetDatablockOptimize on
; SetOverwrite ifnewer
WindowIcon off

; settings from HM NIS Edit Wizard
Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "LeoSetup-4-4-2-beta-3.exe"
LoadLanguageFile "${NSISDIR}\Contrib\Language files\English.nlf"
InstallDir "$PROGRAMFILES\Leo"
Icon "..\Icons\leo_inst.ico"
; Version 1.0 of NSIS Script for Leo comes with its own uninstall icon
; UninstallIcon "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"
DirText "Setup will install $(^Name) in the following folder.$\r$\n$\r$\nTo install in a different folder, click Browse and select another folder."
LicenseText "If you accept all the terms of the agreement, choose I Agree to continue. You must accept the agreement to install $(^Name)."
LicenseData "..\doc\License.txt"
ShowInstDetails show
ShowUnInstDetails show
;@nonl
;@-node:ekr.20050118092706.4:<< Settings >>
;@nl
;@<< Variables >>
;@+node:ekr.20050118092706.5:<< Variables >>
; Location where the Installer finds a Pythonw.exe
; set by the .onInit function
var PythonExecutable
var StrNoUsablePythonFound
;@nonl
;@-node:ekr.20050118092706.5:<< Variables >>
;@nl
;@<< Function .onInit >>
;@+node:ekr.20050118092706.6:<< Function .onInit >>
; .onInit -- find Pythonw.exe, set PythonExecutable with string value
; of its fully qualified path.
; code taken from the "Leo" Section of Leo Installer Version 1.0
;
Function .onInit
    ;@    << .onInit documentation >>
    ;@+node:ekr.20050118092706.7:<< .onInit documentation >>
      # I sure hope there is a better way to do this, but other techniques don't seem to work.
    
      # Supposedly the Python installer creates the following registry entry
      # HKEY_LOCAL_MACHINE\Software\Python\PythonCore\CurrentVersion
      # and then we can read find the Python folder location via
      # HKEY_LOCAL_MACHINE\Software\Python\PythonCore\{versionno}.
      # Alas, at the time of this writing, the Python installer is NOT writing the first entry.
      # There is no way to know what the current versionno is.
      # Hence, the following hack.
    
      # Get pythonw.exe path from registry... except it isn't there, nor is it an environment variable... thanks guys!
      # We'll have to get it in a roundabout way
      ReadRegStr $9 HKEY_LOCAL_MACHINE "SOFTWARE\Classes\Python.NoConFile\shell\open\command" ""
    
      # the NSIS installer for Python 2.3 leaves the registry entry in the following format:
      # C:\Python23\pythonw.exe[SP]"%1%"[SP]%*
      # the MSI installer for python.org's Python 2.4 release leaves the registry entry in the following format:
      # "C:\Python24\pythonw.exe"[SP]"%1%"[SP]%*
      # where [SP] represents an ASCII space character.
    ;@nonl
    ;@-node:ekr.20050118092706.7:<< .onInit documentation >>
    ;@nl
    ;@    << Try for format used by the NSIS installer >>
    ;@+node:ekr.20050118092706.8:<< Try for format used by the NSIS installer >>
    # Try for the format used by the NSIS installer
    # cut 8 characters from back of the open command
    StrCpy $8 $9 -8
    
    
    IfFileExists $8 ok tryagain
    
    tryagain:
    # ok, that  didn't work, but since the Python installer doesn't seem to be consistent, we'll try again
    # cut 3 characters from back of the open command
    StrCpy $8 $9 -3
    
    # that didn't work. check for the registry entry left by MSI Python 2.4 installers
    # from www.python.org and www.activestate.com
    
    IfFileExists $8 ok tryMSIformat
    ;@nonl
    ;@-node:ekr.20050118092706.8:<< Try for format used by the NSIS installer >>
    ;@nl
    ;@    << Try for format used by the MSI installer of Python 2.4-release >>
    ;@+node:ekr.20050118092706.9:<< Try for format used by the MSI installer of Python 2.4-release >>
    ;@<< Try for format used for Python available to all users >>
    ;@+node:ekr.20050118092706.10:<< Try for format used for Python available to all users >>
    tryMSIformat:
    # is the first character a "
    StrCpy $8 $9 1
    StrCmp $8 '"' foundQuote tryMSIformatCurrentUser
    
    foundQuote:
    # OK. Strip off the " at the start as well as the 9 characters at the end
    StrCpy $8 $9 -9 1
    
    # MessageBox MB_OK "3: Searching for Pythonw.exe -- is it '$8' ? "
    
    IfFileExists $8 ok tryMSIformatCurrentUser
    ;@nonl
    ;@-node:ekr.20050118092706.10:<< Try for format used for Python available to all users >>
    ;@nl
    ;@<< Try for format used for Python available to current users >>
    ;@+node:ekr.20050118092706.11:<< Try for format used for Python available to current users >>
    tryMSIformatCurrentUser:
    ReadRegStr $9 HKEY_CURRENT_USER "SOFTWARE\Classes\Python.NoConFile\shell\open\command" ""
    
    # repeating the logic of tryMSIformat:
    # is the first character a "
    StrCpy $8 $9 1
    StrCmp $8 '"' foundQuoteCurrentUser oops
    
    # Patch: 10/6/06: Complain if Python not found.
    StrCmp $8 '"' foundQuoteCurrentUser 0
    StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_NOT_FOUND}"
    Goto oops
    
    foundQuoteCurrentUser:
    # OK. Strip off the " at the start as well as the 9 characters at the end
    StrCpy $8 $9 -9 1
    
    !ifdef INSTALL_IF_PYTHON_FOR_CURRENT_USER
      StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_NOT_FOUND}"
      IfFileExists $8 ok oops
    !else
      IfFileExists $8 usePythonCUFoundMessage usePythonNotFoundMessage
      usePythonCUFoundMessage:
      StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_CURRENT_USER_FOUND}"
      goto oops
      usePythonNotFoundMessage:
      StrCpy $StrNoUsablePythonFound "${STRING_PYTHON_NOT_FOUND}"
      goto oops
    !endif
    ;@nonl
    ;@-node:ekr.20050118092706.11:<< Try for format used for Python available to current users >>
    ;@nl
    ;@nonl
    ;@-node:ekr.20050118092706.9:<< Try for format used by the MSI installer of Python 2.4-release >>
    ;@nl
oops:
    MessageBox MB_OK "$StrNoUsablePythonFound"
    Quit
ok:
     MessageBox MB_OK "Found Python executable at '$8'"
     StrCpy $PythonExecutable $8
FunctionEnd
;@nonl
;@-node:ekr.20050118092706.6:<< Function .onInit >>
;@nl
;@<< Section "Leo" >>
;@+node:ekr.20050118092706.13:<< Section "Leo" >>
Section "Leo" SEC01

  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  ;@  << install top-level files >>
  ;@+node:ekr.20050118103207.1:<< install top-level files >>
  File "..\__init__.py"
  File "..\install"
  File "..\manifest.in"
  File "..\MANIFEST"
  File "..\uninstall"
  ;@nonl
  ;@-node:ekr.20050118103207.1:<< install top-level files >>
  ;@nl
  SetOutPath "$INSTDIR\config"
  ;@  << install config files >>
  ;@+node:ekr.20050118104149.1:<< install config files >>
  File "..\config\leoSettings.leo"
  ;@nonl
  ;@-node:ekr.20050118104149.1:<< install config files >>
  ;@nl
  SetOutPath "$INSTDIR\dist"
  ;@  << install dist files >>
  ;@+node:ekr.20050118104149.4:<< install dist files >>
  File "createLeoDist.py"
  
  File "leoDist.leo"
  
  File "leo-4-3.nsi"
  
  File ".pycheckrc"
  ;@nonl
  ;@-node:ekr.20050118104149.4:<< install dist files >>
  ;@nl
  SetOutPath "$INSTDIR\doc"
  ;@  << install doc files >>
  ;@+node:ekr.20050118104901.1:<< install doc files >>
  File "..\doc\leoDiary.leo"
  File "..\doc\LeoDocs.leo"
  File "..\doc\LeoPostings.leo"
  File "..\doc\LeoSlideShows.leo"
  
  File "..\doc\leoNotes.txt"
  File "..\doc\leoToDo.txt"
  File "..\doc\leoToDoLater.txt"
  
  File "..\doc\Readme.txt"
  File "..\doc\Pkg-info.txt"
  File "..\doc\Install.txt"
  File "..\doc\License.txt"
  
  File "..\doc\LeoTechReport.pdf"
  
  File "..\doc\default.css"
  File "..\doc\leo_rst.css"
  File "..\doc\silver_city.css"
  
  SetOutPath "$INSTDIR\doc\LeoN"
  
  File "..\doc\LeoN\sun98achieving.pdf"
  File "..\doc\LeoN\sun97generic.pdf"
  File "..\doc\LeoN\sun98operational.pdf"
  File "..\doc\LeoN\sun98reversible.pdf"
  
  SetOutPath "$INSTDIR\doc\html"
  
  File "..\doc\html\*.*"
  ;@-node:ekr.20050118104901.1:<< install doc files >>
  ;@nl
  SetOutPath "$INSTDIR\extensions"
  ;@  << install extensions files >>
  ;@+node:ekr.20050118122404:<< install extensions files >>
  File "..\extensions\aspell23.pyd"
  File "..\extensions\aspell24.pyd"
  
  File "..\extensions\__init__.py"
  File "..\extensions\optparse.py"
  File "..\extensions\path.py"
  File "..\extensions\sets.py"
  File "..\extensions\subprocess.py"
  
  SetOutPath "$INSTDIR\extensions\Pmw"
  File "..\extensions\Pmw\__init__.py"
  
  SetOutPath "$INSTDIR\extensions\Pmw\Pmw_1_2"
  File "..\extensions\Pmw\Pmw_1_2\__init__.py"
  
  SetOutPath "$INSTDIR\extensions\Pmw\Pmw_1_2\bin"
  File "..\extensions\Pmw\Pmw_1_2\bin\*.*"
  
  SetOutPath "$INSTDIR\extensions\Pmw\Pmw_1_2\contrib"
  File "..\extensions\Pmw\Pmw_1_2\contrib\*.*"
  
  SetOutPath "$INSTDIR\extensions\Pmw\Pmw_1_2\demos"
  File "..\extensions\Pmw\Pmw_1_2\demos\*.*"
  
  SetOutPath "$INSTDIR\extensions\Pmw\Pmw_1_2\doc"
  File "..\extensions\Pmw\Pmw_1_2\doc\*.*"
  
  SetOutPath "$INSTDIR\extensions\Pmw\Pmw_1_2\lib"
  File "..\extensions\Pmw\Pmw_1_2\lib\*.*"
  
  SetOutPath "$INSTDIR\extensions\Pmw\Pmw_1_2\tests"
  File "..\extensions\Pmw\Pmw_1_2\tests\*.*"
  ;@nonl
  ;@-node:ekr.20050118122404:<< install extensions files >>
  ;@nl
  SetOutPath "$INSTDIR\icons"
  ;@  << install icons >>
  ;@+node:ekr.20050118104901.4:<< install icons >>
  File "..\Icons\*.*"
  ;@nonl
  ;@-node:ekr.20050118104901.4:<< install icons >>
  ;@nl
  SetOutPath "$INSTDIR\modes"
  ;@  << install modes >>
  ;@+node:ekr.20051208095832:<< install modes >>
  File "..\modes\*.xml"
  ;@nonl
  ;@-node:ekr.20051208095832:<< install modes >>
  ;@nl
  SetOutPath "$INSTDIR\plugins"
  ;@  << install plugins >>
  ;@+node:ekr.20050118104901.7:<< install plugins >>
  File "..\plugins\leoPlugins.leo"
  
  File "..\plugins\*.ini"
  File "..\plugins\*.txt"
  
  File "..\plugins\*.py"
  
  SetOutPath "$INSTDIR\plugins\trees"
  
  File "..\plugins\trees\*.py"
  File "..\plugins\trees\pluginsManager.txt"
  ;@nonl
  ;@-node:ekr.20050118104901.7:<< install plugins >>
  ;@nl
  SetOutPath "$INSTDIR\scripts"
  ;@  << install scripts >>
  ;@+node:ekr.20050118104901.13:<< install scripts >>
  File "..\scripts\scripts.leo"
  File "..\scripts\leoScripts.txt"
  File "..\scripts\*.py"
  File "..\scripts\openLeoScript.sh"
  ;@nonl
  ;@-node:ekr.20050118104901.13:<< install scripts >>
  ;@nl
  SetOutPath "$INSTDIR\src"
  ;@  << install src files >>
  ;@+node:ekr.20050118104901.10:<< install src files >>
  File "..\src\buttons.txt"
  File "..\src\leoProjects.txt"
  File "..\src\LeoPy.leo"
  File "..\src\oldLeoProjects.leo"
  
  File "..\src\__init__.py"
  File "..\src\leo*.py"
  ;@-node:ekr.20050118104901.10:<< install src files >>
  ;@nl
  SetOutPath "$INSTDIR\test"
  ;@  << install test files >>
  ;@+node:ekr.20050118122404.1:<< install test files >>
  File "..\test\__init__.py"
  File "..\test\test.leo"
  File "..\test\unitTest.leo"
  ;@-node:ekr.20050118122404.1:<< install test files >>
  ;@nl
  SetOutPath "$INSTDIR\test\unittest"
  ;@  << install unittest files >>
  ;@+node:ekr.20050830052109:<< install unittest files >>
  File "..\test\unittest\batchTest.py"
  File "..\test\unittest\errorTest.py"
  ;@-node:ekr.20050830052109:<< install unittest files >>
  ;@nl

SectionEnd
;@nonl
;@-node:ekr.20050118092706.13:<< Section "Leo" >>
;@nl
;@<< Section "Start Menu Shortcuts"  >>
;@+node:ekr.20050118092706.14:<< Section "Start Menu Shortcuts"  >>
; FIXME $SMPROGRAMS depends on the value of SetShellVarContext. Since that defaults to 'current'
; that means that this installer will make Leo available for the current user only.
; Unless I am grossly mistaken this is a needless hindrance, and a Bad Thing since
; security concerns are such that it would be best to not run Leo with the Administrator privileges
; of the account used to install the software.
;
; Sure enough, the Start Menu Shortcuts and Desktop Shortcut work for the installer account only. 
;
; Question is -- do we want Leo always available for any log-in on this computer?
;
; My guesses:
; Ideally, Uninstall.lnk should appear only for the current user, and the uninstaller should refuse to run
; if run by a user who lacks Admin privileges on Windows NT and its descendants
;
; How will Windows XP Home deal with that? 

Section "Start Menu Shortcuts" SEC02
  CreateDirectory "$SMPROGRAMS\Leo"
  CreateShortCut "$SMPROGRAMS\Leo\Uninstall.lnk" "$INSTDIR\uninst.exe" "" "$INSTDIR\uninst.exe" 0
; In Version 1.0 installer, was
; CreateShortCut "$SMPROGRAMS\Leo\Leo.lnk" "$PythonExecutable" '"$INSTDIR\src\leo.py"' "$INSTDIR\Icons\LeoApp.ico" 0
  CreateShortCut "$SMPROGRAMS\Leo\Leo.lnk" '"$PythonExecutable"' '"$INSTDIR\src\leo.py"' "$INSTDIR\Icons\LeoApp.ico" 0
SectionEnd
;@nonl
;@-node:ekr.20050118092706.14:<< Section "Start Menu Shortcuts"  >>
;@nl
;@<< Section "Desktop Shortcut" >>
;@+node:ekr.20050118092706.15:<< Section "Desktop Shortcut" >>
Section "Desktop Shortcut" SEC03
  CreateShortCut "$DESKTOP\Leo.lnk" '"$PythonExecutable"' '"$INSTDIR\src\leo.py"' "$INSTDIR\Icons\LeoApp.ico" 0
SectionEnd
;@nonl
;@-node:ekr.20050118092706.15:<< Section "Desktop Shortcut" >>
;@nl
;@<< Section ".leo File Association" >>
;@+node:ekr.20050118092706.16:<< Section ".leo File Association" >>
Section ".leo File Association"
  SectionIn 1
  SectionIn 2
  SectionIn 3

  # back up old value of .leo in case some other program was using it
  ReadRegStr $1 HKCR ".leo" ""
  StrCmp $1 "" Label1
  StrCmp $1 "LeoFile" Label1
  WriteRegStr HKCR ".leo" "backup_val" $1

Label1:
  WriteRegStr HKCR ".leo" "" "LeoFile"
  WriteRegStr HKCR "LeoFile" "" "Leo File"
  WriteRegStr HKCR "LeoFile\shell" "" "open"
; In Version 1.0 installer, the .ico reference was
;  WriteRegStr HKCR "LeoFile\DefaultIcon" "" $INSTDIR\Icons\LeoDoc.ico,0
; which does not work under Windows XP Professional SP2.
  WriteRegStr HKCR "LeoFile\DefaultIcon" "" $INSTDIR\Icons\LeoDoc.ico
  WriteRegStr HKCR "LeoFile\shell\open\command" "" '"$PythonExecutable" "$INSTDIR\src\leo.py" %1'

SectionEnd
;@nonl
;@-node:ekr.20050118092706.16:<< Section ".leo File Association" >>
;@nl
;@<< Section -AdditionalIcons >>
;@+node:ekr.20050118092706.17:<< Section -AdditionalIcons >>
Section -AdditionalIcons
  SetOutPath $INSTDIR
  CreateDirectory "$SMPROGRAMS\Leo"
  CreateShortCut "$SMPROGRAMS\Leo\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd
;@nonl
;@-node:ekr.20050118092706.17:<< Section -AdditionalIcons >>
;@nl
;@<< Section -Post >>
;@+node:ekr.20050118092706.19:<< Section -Post >>
Section -Post
  WriteRegStr HKEY_LOCAL_MACHINE "SOFTWARE\EKR\leo" "" "$INSTDIR"
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name) (remove only)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd
;@nonl
;@-node:ekr.20050118092706.19:<< Section -Post >>
;@nl
;@<< Uninstall-related Settings >>
;@+node:ekr.20050118092706.18:<< Uninstall-related Settings >>
; from Leo installer Version 1.0
;
; UninstallText "This will uninstall Leo from your system"
; UninstallCaption "Uninstall Leo"
; UninstallIcon c:\prog\tigris-cvs\leo\Icons\uninst.ico

; UninstallText "This will uninstall Leo from your system"
UninstallCaption "Uninstall Leo"
UninstallIcon c:\prog\tigris-cvs\leo\Icons\uninst.ico
;@nonl
;@-node:ekr.20050118092706.18:<< Uninstall-related Settings >>
;@nl
;@<< Function un.onUninstSuccess >>
;@+node:ekr.20050118092706.20:<< Function un.onUninstSuccess >>
Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) was successfully removed from your computer."
FunctionEnd
;@nonl
;@-node:ekr.20050118092706.20:<< Function un.onUninstSuccess >>
;@nl
;@<< Function un.onInit >>
;@+node:ekr.20050118092706.21:<< Function un.onInit >>
Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove $(^Name) and all of its components?" IDYES +2
  Abort
FunctionEnd
;@nonl
;@-node:ekr.20050118092706.21:<< Function un.onInit >>
;@nl
;@<< Section Uninstall >>
;@+node:ekr.20050118092706.22:<< Section Uninstall >>
; Uninstall section as generated by HM NE, with hand-edits

Section Uninstall
  DeleteRegKey HKEY_LOCAL_MACHINE "SOFTWARE\EKR\leo"
  ;@  << remove file association >>
  ;@+node:ekr.20050119082907:<< remove file association >>
  ; From v1.0 Installer.
  ReadRegStr $1 HKCR ".leo" ""
  StrCmp $1 "LeoFile" 0 NoOwn ; only do this if we own it.
  
  ReadRegStr $1 HKCR ".leo" "backup_val"
  StrCmp $1 "" 0 RestoreBackup ; if backup == "" then delete the whole key
    DeleteRegKey HKCR ".leo"
  Goto NoOwn
  
  RestoreBackup:
    WriteRegStr HKCR ".leo" "" $1
    DeleteRegValue HKCR ".leo" "backup_val"
    
  NoOwn:
  MessageBox MB_YESNO|MB_ICONQUESTION \
  		 "Delete all files in Leo Program folder?" \
  		 IDNO NoDelete
  ;@nonl
  ;@-node:ekr.20050119082907:<< remove file association >>
  ;@nl
  ;@  << uninstall config files >>
  ;@+node:ekr.20050118104149.2:<< uninstall config files >>
  Delete "$INSTDIR\config\leoSettings.leo"
  Delete "$INSTDIR\config\.leoID.txt"
  ;@nonl
  ;@-node:ekr.20050118104149.2:<< uninstall config files >>
  ;@nl
  ;@  << uninstall dist files >>
  ;@+node:ekr.20050118104149.5:<< uninstall dist files >>
  Delete "$INSTDIR\dist\createLeoDist.p*"
  
  Delete "$INSTDIR\dist\leoDist.leo"
  
  Delete "$INSTDIR\dist\leo-4-3.nsi"
  
  Delete "$INSTDIR\dist\.pycheckrc"
  ;@nonl
  ;@-node:ekr.20050118104149.5:<< uninstall dist files >>
  ;@nl
  ;@  << uninstall doc files >>
  ;@+node:ekr.20050118104901.2:<< uninstall doc files >>
  Delete "$INSTDIR\doc\LeoDocs.leo"
  Delete "$INSTDIR\doc\leoDiary.leo"
  Delete "$INSTDIR\doc\LeoPostings.leo"
  Delete "$INSTDIR\doc\LeoSlideShows.leo"
  
  Delete "$INSTDIR\doc\leoNotes.txt"
  Delete "$INSTDIR\doc\leoToDo.txt"
  Delete "$INSTDIR\doc\leoToDoLater.txt"
  
  Delete "$INSTDIR\doc\License.txt"
  Delete "$INSTDIR\doc\Install.txt"
  Delete "$INSTDIR\doc\Pkg-info.txt"
  Delete "$INSTDIR\doc\Readme.txt"
  
  Delete "$INSTDIR\doc\LeoTechReport.pdf"
  
  Delete "$INSTDIR\doc\silver_city.css"
  Delete "$INSTDIR\doc\leo_rst.css"
  Delete "$INSTDIR\doc\default.css"
  
  Delete "$INSTDIR\doc\LeoN\sun98achieving.pdf"
  Delete "$INSTDIR\doc\LeoN\sun97generic.pdf"
  Delete "$INSTDIR\doc\LeoN\sun98operational.pdf"
  Delete "$INSTDIR\doc\LeoN\sun98reversible.pdf"
  
  Delete "$INSTDIR\doc\html\*.*"
  ;@nonl
  ;@-node:ekr.20050118104901.2:<< uninstall doc files >>
  ;@nl
  ;@  << uninstall extensions files >>
  ;@+node:ekr.20050118122740.1:<< uninstall extensions files >>
  Delete "$INSTDIR\extensions\aspell23.pyd"
  Delete "$INSTDIR\extensions\aspell24.pyd"
  
  Delete "$INSTDIR\extensions\__init__.p*"
  
  Delete "$INSTDIR\extensions\optparse.py"
  Delete "$INSTDIR\extensions\path.p*"
  Delete "$INSTDIR\extensions\sets.p*"
  Delete "$INSTDIR\extensions\subprocess.p*"
  
  Delete "$INSTDIR\extensions\Pmw\__init__.p*"
  
  Delete "$INSTDIR\extensions\Pmw\Pmw_1_2\__init__.p*"
  
  Delete "$INSTDIR\extensions\Pmw\Pmw_1_2\bin\*.*"
  Delete "$INSTDIR\extensions\Pmw\Pmw_1_2\contrib\*.*"
  Delete "$INSTDIR\extensions\Pmw\Pmw_1_2\demos\*.*"
  Delete "$INSTDIR\extensions\Pmw\Pmw_1_2\doc\*.*"
  Delete "$INSTDIR\extensions\Pmw\Pmw_1_2\lib\*.*"
  Delete "$INSTDIR\extensions\Pmw\Pmw_1_2\tests\*.*"
  ;@nonl
  ;@-node:ekr.20050118122740.1:<< uninstall extensions files >>
  ;@nl
  ;@  << uninstall icons >>
  ;@+node:ekr.20050118104901.5:<< uninstall icons >>
  Delete "$INSTDIR\icons\*.*"
  ;@nonl
  ;@-node:ekr.20050118104901.5:<< uninstall icons >>
  ;@nl
  ;@  << uninstall modes >>
  ;@+node:ekr.20051208100413.1:<< uninstall modes >>
  Delete "$INSTDIR\modes\*.xml"
  ;@nonl
  ;@-node:ekr.20051208100413.1:<< uninstall modes >>
  ;@nl
  ;@  << uninstall plugins >>
  ;@+node:ekr.20050118104901.8:<< uninstall plugins >>
  Delete "$INSTDIR\plugins\leoPlugins.leo"
  
  Delete "$INSTDIR\plugins\*.txt"
  Delete "$INSTDIR\plugins\*.ini"
  
  Delete "$INSTDIR\plugins\*.p*"
  
  Delete "$INSTDIR\plugins\trees\*.p*"
  Delete "$INSTDIR\plugins\trees\pluginsManager.txt"
  ;@nonl
  ;@-node:ekr.20050118104901.8:<< uninstall plugins >>
  ;@nl
  ;@  << uninstall scripts >>
  ;@+node:ekr.20050118104901.14:<< uninstall scripts >>
  Delete "$INSTDIR\scripts\scripts.leo"
  Delete "$INSTDIR\scripts\leoScripts.txt"
  Delete "$INSTDIR\scripts\*.p*"
  Delete "$INSTDIR\scripts\openLeoScript.sh"
  ;@nonl
  ;@-node:ekr.20050118104901.14:<< uninstall scripts >>
  ;@nl
  ;@  << uninstall src files >>
  ;@+node:ekr.20050118104901.11:<< uninstall src files >>
  Delete "$INSTDIR\src\buttons.txt"
  Delete "$INSTDIR\src\leoProjects.txt"
  Delete "$INSTDIR\src\LeoPy.leo"
  Delete "$INSTDIR\src\oldLeoProjects.leo"
  
  Delete "$INSTDIR\src\__init__.p*"
  
  Delete "$INSTDIR\src\leo*.p*"
  ;@nonl
  ;@-node:ekr.20050118104901.11:<< uninstall src files >>
  ;@nl
  ;@  << uninstall test files >>
  ;@+node:ekr.20050118122740.3:<< uninstall test files >>
  Delete "$INSTDIR\test\__init__.py"
  Delete "$INSTDIR\test\test.leo"
  Delete "$INSTDIR\test\unitTest.leo"
  ;@-node:ekr.20050118122740.3:<< uninstall test files >>
  ;@nl
  ;@  << uninstall unittest files >>
  ;@+node:ekr.20050830052109.1:<< uninstall unittest files >>
  Delete "$INSTDIR\test\unittest\batchTest.py"
  Delete "$INSTDIR\test\unittest\errorTest.py"
  ;@-node:ekr.20050830052109.1:<< uninstall unittest files >>
  ;@nl
  ;@  << uninstall top-level files >>
  ;@+node:ekr.20050118103447.1:<< uninstall top-level files >>
  ; Gets created automatically by installer.
  Delete "$INSTDIR\uninst.exe"
  
  ; Should match installed files.
  Delete "$INSTDIR\__init__.py"
  Delete "$INSTDIR\install"
  Delete "$INSTDIR\manifest.in"
  Delete "$INSTDIR\MANIFEST"
  Delete "$INSTDIR\uninstall"
  
  
  ;@-node:ekr.20050118103447.1:<< uninstall top-level files >>
  ;@nl
  ;@  << delete folders >>
  ;@+node:ekr.20050119082907.1:<< delete folders >>
  ; First, delete sub-folders...
  RMDir "$INSTDIR\config"
  RMDir "$INSTDIR\dist"
  RmDir "$INSTDIR\doc\html"
  RmDir "$INSTDIR\doc\LeoN"
  RMDir "$INSTDIR\doc"
  
  RMDir "$INSTDIR\extensions\Pmw\Pmw_1_2\bin"
  RMDir "$INSTDIR\extensions\Pmw\Pmw_1_2\contrib"
  RMDir "$INSTDIR\extensions\Pmw\Pmw_1_2\demos"
  RMDir "$INSTDIR\extensions\Pmw\Pmw_1_2\doc"
  RMDir "$INSTDIR\extensions\Pmw\Pmw_1_2\lib"
  RMDir "$INSTDIR\extensions\Pmw\Pmw_1_2\tests"
  RMDir "$INSTDIR\extensions\Pmw\Pmw_1_2"
  RMDir "$INSTDIR\extensions\Pmw"
  RMDir "$INSTDIR\extensions"
  
  RMDir "$INSTDIR\icons"
  RMDir "$INSTDIR\modes"
  
  RMDir "$INSTDIR\plugins\trees"
  RMDir "$INSTDIR\plugins"
  
  RMDir "$INSTDIR\scripts"
  RMDir "$INSTDIR\src"
  
  RMDir "$INSTDIR\test\unittest"
  RMDir "$INSTDIR\test"
  
  ; Delete top-level folder.
  RMDir "$INSTDIR"
  ;@nonl
  ;@-node:ekr.20050119082907.1:<< delete folders >>
  ;@nl

NoDelete:
  Delete "$SMPROGRAMS\Leo\Uninstall.lnk"
  RMDir "$SMPROGRAMS\Leo"
  Delete "$DESKTOP\Leo.lnk"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  SetAutoClose false
SectionEnd
;@nonl
;@-node:ekr.20050118092706.22:<< Section Uninstall >>
;@nl
;@nonl
;@-node:ekr.20050118092706:@thin leo-4-3.nsi
;@-leo
