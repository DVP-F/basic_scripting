import subprocess

while True:
	subprocess.call('powershell -command "cmd.exe /S /C cls"')
	inn = input(
"""Input 1 to ping vg.no
Input 2 for Terminal
Input 3 for Command Prompt
Input 4 for local ping
^C to exit
 > """
	)
	if (inn == "1"):
		subprocess.run("ping vg.no")
		input("Exit: ")
	elif (inn == "2"):
		subprocess.run("wt.exe")
	elif (inn == "3"):
		subprocess.call("cmd /S /K cls")
	elif (inn == "4"):
		temp = subprocess.check_output("ping localhost -n 2").decode()
		input((temp + "\nExit: ")) 

