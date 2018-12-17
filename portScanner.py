import socket
from ipaddress import IPv4Network as IPv4

## Errors sum
ErrorsNum = 0

## Entering Ip address
NetInput = input(r"Enter IP address or IP range (10.0.0.1 or 10.0.0.0/24): ")
try:
    netRange = IPv4(NetInput)
except:
    ErrorsNum += 1
    print('Wrong IP address format')

## If IP is good then entering port number
if ErrorsNum ==0:
    ScanPorts = input(r"Enter ports to scan (485, 2486, 144): ")
    try:
        portsRaw = ScanPorts.split(',')
        ports = []
        for port in portsRaw:
            try:
                ports.append(int(port))
            except:
                ErrorsNum += 1
                print('\nWrong port format, try again')
        ports = set(ports)
    except:
         ErrorsNum += 1
         print('\nWrong port format, try again')

## If ports are good start scanning
if ErrorsNum ==0:
    print('\nYou will scan ports {}'.format(ports))
    print('\nScanning has been started. Please wait\n...\n')
    
    for addr in netRange:
        serverIP = socket.gethostbyname(str(addr))
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            openport = sock.connect_ex((serverIP, int(port)))
            if openport == 0:
                print("{1}::{0}   Open".format(port, str(addr)))
            else:
                print("{1}::{0}  Closed".format(port, str(addr)))
            sock.close()
