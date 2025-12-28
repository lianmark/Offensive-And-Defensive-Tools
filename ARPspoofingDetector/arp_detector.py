# Added 12/28/2025 23:27
# NOTE ON CONTRIBUTION & TRANSPARENCY
# ~70% of this code was written and designed by me.
# ~30% was assisted by ChatGPT in the form of small code snippets,
# debugging guidance, and design validation.
# This note is included purely for transparency and honesty and to
# accurately represent my level of understanding and contribution at Python.
# Most comments and documentation were written by ChatGPT
import mysql.connector
import mysql.connector
from scapy.config import conf
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import sniff
from scapy.all import get_working_ifaces
from scapy.all import arping

Database = mysql.connector.connect(
    host="<DB_HOST>",         
    user="<DB_USERNAME>",      
    password="<DB_PASSWORD>",
    database="<DB_NAME>",    
    ssl_disabled=False
)
mycursor = Database.cursor()

Data = {}          # Dictionary: IP -> (MAC, Vendor)
IPlist = set()     # Set to track already discovered IPs (avoid duplicates)

interface = ""
GATEWAY_IP = '192.168.1.1'

# ONLY FOR PHYSICAL MACHINE
def get_lan_interface():
    global interface
    for iface in get_working_ifaces():
        # Checks if the interface starts with "Ethernet" and does not have any numbers in it
        # This is done to avoid virtual adapters like "Ethernet 2"
        if "Ethernet" in iface.name and not any(ch.isdigit() for ch in iface.name):
            return iface.name

def update_devices_to_database():
    # Push all collected LAN devices into the database
    # INSERT IGNORE is used to avoid duplicate IP (PRIMARY KEY)
    for key, (value1, value2) in Data.items():
        mycursor.execute(
            "INSERT IGNORE INTO stats (ip, mac, vendor) VALUES (%s, %s, %s)",
            (key, value1, str(value2))
        )
    Database.commit()  # Save changes to DB



## Do it only to update Database
def arp_discovery(iface):
    global IPlist
    # Active ARP scan (who-has) on the local subnet
    answered, unanswered = arping("192.168.1.0/24", iface=iface, timeout=15, verbose=False)
    for _, recv in answered:
        # Only collect private LAN IPs and avoid duplicates
        if recv.psrc.startswith("192.168") and recv.psrc not in IPlist:
            get_ip = recv.psrc          # Source IP from ARP reply
            get_mac = recv.hwsrc        # Source MAC from ARP reply
            get_vendor = conf.manufdb.lookup(recv.hwsrc)  # Vendor lookup via OUI

            ## CUSTOM SETTINGS
            # Manual labeling for known devices
            if get_mac == "<DESKTOP_MAC_ADDRESS>":
                get_vendor = "Desktop Computer ( MAIN )"
            if get_mac == "<ROUTER_MAC_ADDRESS>":
                get_vendor = "GATEWAY - Router"

            ## Sometimes get_VENDOR returns the MAC itself if vendor is unknown
            ## We force it to 'Unknown' in that case
            if get_mac in get_vendor:
                get_vendor = "Unknown"

            ## ADD IP to a set()
            IPlist.add(get_ip)

            ## From set() ADD mac address and vendor to the ip in dictionary
            Data[recv.psrc] = (get_mac, get_vendor)
###########
## TO DO
###########
def detected_mac_duplication():
    try:
        # Passive ARP sniffing to detect MAC/IP anomalies
        packets = sniff(filter="arp", iface=interface, count=5)
        for pkt in packets:
            # Collect ARP source IPs not seen before
            if pkt[ARP].psrc not in Data:
                Data[pkt[ARP].psrc] = pkt[ARP].hwsrc
    except:
        print("Error occured on detected_arp_protocols() FUNCTION")

interface = get_lan_interface()   # Resolve physical LAN interface
arp_discovery(interface)          # Perform ARP discovery
update_devices_to_database()      # Store results in database
