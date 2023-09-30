# Import necessary libraries from Scapy
from scapy.all import *
from scapy.layers.l2 import Ether, ARP

# Specify the network interface to use (you should replace "Ethernet" with your actual interface name)
interface = "Ethernet"

# Define the target IP range you want to scan for ARP responses (You should Replace X.X with actual IP/range
ip_range = "192.168.x.x/24"

# Define the broadcast MAC address
broadcastMac = "ff:ff:ff:ff:ff:ff"

# Create an ARP request packet within an Ethernet frame
packet = Ether(dst=broadcastMac) / ARP(pdst=ip_range)

# Send the ARP request packet and receive responses
ans, unans = srp(packet, timeout=2, iface=interface, inter=0.1)

# Loop through the ARP responses and print the source MAC address and corresponding IP address
for send, receive in ans:
    print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
