from socket import * 
from struct import unpack 
import sys 

INTERFACE = "eth0"
TARGET = "8.8.8.8" 

if __name__ == "__main__": 
  sock = socket(AF_PACKET, SOCK_DGRAM, 0x0800) 
  sock.bind((INTERFACE, 0x0800)) 
  while True: 
    data = sock.recvfrom(1500, 0)[0] 
    ip = inet_ntop(AF_INET, data[12:16]) 
    if ip == TARGET: 
      print "GOT TARGET" 
      sys.exit(1)
