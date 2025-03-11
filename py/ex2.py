import subprocess as run

run.call("wt")

run.call('powershell -command "ping ::1 -n 2"')
run.call("cmd /S /C pause")

run.run("powershell -command 'get-timezone'")

