#pip install socket
#pip install publicip

import socket
import publicip

print(publicip.get()) # returns public ip

print(socket.gethostname()) # returns computer name
