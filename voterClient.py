#client user reg partial

import socket
import threading
import sys
from passlib.apps import custom_app_context

functionsList = ['Register']

def functionalities():
	print("For registration :python voterClient.py Register username password")


def register(sock, username, password):
	print(username)
	password = custom_app_context.encrypt(password)
	send_ = username+" "+password
	sock.send(send_.encode('utf-8'))
	"""
	info = sock.recv().decode('utf-8')
	print(info)
	repeatFlag = 1
	while(repeatFlag):
		userInfo = input()
		password = userInfo.strip().split()[1].encode('base64','strict')
		sock.send(userInfo.strip().split()[0]+" "+password.encode('utf-8'))
		userInfo = sock.recv.decode('utf-8')
		if(userInfo.strip().split()[1] == "successful"):
			repeatFlag = 0
			print(userInfo)
		else:
			repeatFlag = input("Wish to try again (1/0): ")
	"""
	status = sock.recv(1024).decode('utf-8')
	print(status)


def Main():

	if(len(sys.argv) == 1 or sys.argv[1] not in functionsList):
		functionalities()

	elif(sys.argv[1] == 'Register'):
		host = "127.0.0.1"
		port = 63

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.connect((host,port))
			print("Connected to ("+host+":"+str(port)+")...")
			print(sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3])
			register(sock,sys.argv[2],sys.argv[3])
		except:
			print("Server down...")

if __name__ == '__main__':
	Main()


