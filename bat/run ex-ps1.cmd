@echo off 
g: 
cd "resources\code\course in scripting\bat" 
powershell -command "./ex.ps1" 

rem This is needed for the file locations i have for this setup and this project - however something similar is necessary to run powershell scripts. the needed command is line 4. 
rem Windows doesnt let you run PS scripts by default - the best if not only practical way is to force powershell with a cmd - that is, kernel call - command, and to- 
rem - minimize jank, a small script like this is way easier to use, maintain and set up 

rem Additionally, the 'g:' command does what 'cd g:' cant - changes the drive the terminal runs at. 
