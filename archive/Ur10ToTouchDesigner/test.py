# Echo client program

import socket
import time
import struct

HOST = "192.168.1.156" # The remote host
PORT_30003 = 30003

print("Starting Program")

count = 0
home_status = 0
program_run = 0
s = None
while (True):
	if program_run == 0:
		try:	
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(10)
				s.connect((HOST, PORT_30003))
			except socket.error as socketerror:
				print("ERROR: ", socketerror)		
			packet_1 = s.recv(4)
			size = struct.unpack("!i", packet_1);
			
			packet_2 = s.recv(8)
			packet_3 = s.recv(48)
			packet_4 = s.recv(48)
			packet_5 = s.recv(48)
			packet_6 = s.recv(48)
			packet_7 = s.recv(48) 
			packet_8 = s.recv(48)
			packet_9 = s.recv(48)
			packet_10 = s.recv(48)
			packet_11 = s.recv(48)
			
			packet_12 = s.recv(8)
			x = struct.unpack('!d', packet_12)[0]
			print("X = ", x * 1000)
			
			packet_13 = s.recv(8)
			y = struct.unpack('!d', packet_13)[0]
			print("Y = ", y * 1000)
			
			packet_14 = s.recv(8)
			z = struct.unpack('!d', packet_14)[0]
			print("Z = ", z * 1000)
			
			packet_15 = s.recv(8)
			Rx = struct.unpack('!d', packet_15)[0]
			print("Rx = ", Rx)
			
			packet_16 = s.recv(8)
			Ry = struct.unpack('!d', packet_16)[0]
			print("Ry = ", Ry)
			
			packet_17 = s.recv(8)
			Rz = struct.unpack('!d', packet_17)[0]
			print("Rz = ", Rz)
			
			packet_18 = s.recv(size - 488);
			
			program_run = 0
			s.close()
		except socket.error as socketerror:
			print("Error: ", socketerror)
print("Program finish")
