#!/bin/python3

import sys #allow all CLI commands
import socket #

from datetime import datetime

#define my target

if len(sys.argv) == 2:

	target = socket.gethostbyname(sys.argv[1]) #translate a host name to ipv4
else:
	print("invalid amoutn of argument Syntax:python3 scanner.py <ip>")
	sys.exit()

#Add a banner

print("-" *50)
print("Scaning started"+target)
print("Time "+str(datetime.now()))
print("-" *50)


try:

	for port in range(1,8500):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af-inet is ipv4 sock straem  is my port
		socket.setdefaulttimeout(1) #it is a float
		result = s.connect_ex((target,port)) #Error indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is Open".format(port))
			s.close


except KeyboardInterrupt:
	print("\nExiting the program")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("Couldn't connect to server.")
	sys.exit()

