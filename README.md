devices.py
==========

Find all devices connected to a local network

# You might need to update this function yourself if you're connected to 2 or more networks.
def get_ip():    
    return str([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])
    

# If you want to retrieve your IP on the second network device try the following:
def get_ip(): 
    return str(socket.gethostbyname_ex(socket.gethostname())[2][1])
    
