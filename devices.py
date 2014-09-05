#=======================================
# Author: Francois Laubscher
# Date: 2014-09-04
# Description: Find all devices connected to network
#=======================================

import socket
import re
import sys

# gets local machine IP
def get_ip():    
    return str(socket.gethostbyname_ex(socket.gethostname())[2][1])

# gets subnet of local machine
def get_subnet():
    address = get_ip()
    subnet = ""

    if len(address) > 0:
        address = re.sub("[^\\d.]", "", address)
        address = str(address).replace(".", " ")
        parts = address.split()
        subnet = "{0}.{1}.{2}.".format(parts[0], parts[1], parts[2])

    return subnet

# check if an address is connected to the network  
def connected(addr):
    connected = False

    while not connected:
        for i in range(0, 2000):
            sys.stdout.write('.')
            s = socket.socket()
            if s.connect_ex((addr, i)) == 0:
                s.close()
                connected = True                
                return True
            else:
                s.close()

    
    return false


# get all connected devices on network
def list_devices():
    devices = [];
    network = get_subnet()
    
    # find all ips for this network
    for ip in xrange(1, 256):
        address = network + str(ip)
        print "scanning {0}\n".format(address)

        # check if this address is connected
        if(connected(address)):
            devices.append(address)

    return devices

print "\r"
print list_devices()
raw_input("Done")


