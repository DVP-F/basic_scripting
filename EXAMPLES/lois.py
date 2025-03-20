from scapy.all import IP, TCP, send # pip install scapy --python C:\path\to\python

# Define the target IP address and list of port numbers
target_ip = "192.168.1.2"
target_ports = [22, 80, 420, 443, 5560, 6969]

# Create a TCP SYN packet
packet = IP(dst=target_ip) / TCP(dport=target_ports, flags="S")

# Send packets and display feedback
sent_count = 0
for port in target_ports:
    for i in range(10):
        send(packet)
        sent_count += 1
        print(f"Sent packet {sent_count} to port {port}")
print("All packets sent!")
