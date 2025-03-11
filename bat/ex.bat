@echo off

ping vg.no
echo:
pause
cls

echo :3
cls

rem This is powershell commands for scripting with those - showing how to use them here bc i hate ps1 scripting

powershell -command "get-timezone"
powershell -command "get-tpm"
powershell -command "write-host 'set-timezone "utc+13"'"
powershell -command "cmd.exe /S /C pause"

start "C:\Program Files\Git\git-bash.exe"

pause 

