import socket
hostname = socket.gethostname()
IPaddr = socket.gethostbyname(hostname)
print("Your Computer name is: "+hostname)
print("Your IP address is :"+ IPaddr)
