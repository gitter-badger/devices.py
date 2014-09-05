#=======================================
# Author: Francois Laubscher
# Date: 2014-09-05
# Description: Find all Windows devices connected to network
#=======================================

import socket
import re
import sys

# gets local machine IP
def get_ip():
    return str([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])
    # use this line if you're connected to more than one LAN
    # return str(socket.gethostbyname_ex(socket.gethostname())[2][1]) 

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
    s = socket.socket()       
    if s.connect_ex((addr, 135)) == 0: # this port is usually open on a Windows device
        s.close()             
        return True
    else:            
        s.close()
        return False


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
            print "{0} connected as {1}".format(address, socket.getfqdn(address))
            #devices.append(address)

    return devices

print "\r"
list_devices()
raw_input("Done")


