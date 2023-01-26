import socket
from colorama import Fore, Back, Style
input = input("Enter target site or ip:\n")
hostname = f"{input}"

for port in range(1,1024):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((hostname,port)):
        print(Fore.RED + "Port {} is closed".format(port))
    else:
        print(Fore.GREEN + "Port {} is open".format(port))
    sock.close()
    
   
