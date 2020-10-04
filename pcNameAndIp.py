import socket 
import requests


hostname = socket.gethostname() 

privateIp = socket.gethostbyname(hostname) 
publicIp = requests.get('http://ip.42.pl/raw').text

print("Your Computer Name is : " + hostname) 
print("Your Private IP is : " + privateIp) 
print("Your Public IP is : " + publicIp) 


