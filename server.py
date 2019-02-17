#only user registration partially implemented
import sqlite3
import socket
import threading

registrationFormat = "uniqueUserName password" #password in encrypted format

class DataBase:
	def __init__(self,constraints):
		self.conn = sqlite3.connect('users.db')
		self.cursor = conn.cursor()
		self.constraints = constraints

	def createTable(self,tableName,fields):
		query = "CREATE TABLE "+tableName
		details = "("
		for i in range(len(fields)):
			if(i == 0):
				details += (fields[i] + ',')
			elif(i != len(fields) - 1):
				details += (' '+fields[i]+',')
			else:
				details += (' '+fields[i]+')')
		query += details
		self.cursor.execute(query)

	def checkConstraints(self,info):
		if(len(userInfo.strip().split()) != len(self.constraints.strip().split())):
			return (False,"Arguments not given properly")
		elif(self.inDataBase(userInfo.strip().split()[0])):
			return (False,"Username already registered")
		else:
			return (True,"Registration successful")

	def insert(self,record,tableName):
		if(tableName == 'voters'):
			uname = record.strip().split()[0]
			password = record.strip().split()[1]
			self.cursor.execute("INSERT INTO voters (username, password) VALUES (?, ?)",(uname, password))
			self.conn.commit()


	def inDataBase(self,record,tableName):
		if(tableName == 'voters'):
			record_ = record_.strip().splpit()
			self.cursor.execute("SELECT * FROM voters WHERE username="+"'"+record_[0]+"'")
			if len(self.cursor.fetchall()) == 0:
				return True
			else:
				return False




def Register(name, sock, addr):
	voters = DataBase(registrationFormat)
	
	fields = ['username TEXT','password TEXT'] 
	voters.createTable('voters',fields)
	
	sock.send(str.encode("registration format :"+registrationFormat))
	userInfo = sock.recv().decode("utf-8")

	registered = 0

	while(not registered):
		registrationConstraintsInfo = voters.checkConstraints(userInfo,'voters')
		if(registrationConstraintsInfo[0] == False):
			sock.send(registrationConstraintsInfo[1] + " send agein : ".encode('utf-8'))
		else:
			voters.insert(userInfo,'voters')
			sock.send(registrationConstraintsInfo[1].encode('utf-8'))
			registered = 1

def startHosting():
	host = socket.gethostbyname('0.0.0.0')
	port = 63
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((host,port))
	sock.listen(5)

	print("Server is hosting registration...")

	userRegisterFlag = 1

	while(userRegisterFlag):
		userRegisterFlag = input("Continue registration (0/1) : ")
		c,addr = sock.accept()

		print("Registering user "+"("+str(addr[0])+":"+str(addr[1])+")")
		t = threading.Thread(target = Register, args = ('registration',c,addr))
		t.start()

	sock.close()


def Main():
	count = 0
	while(True):
		hostPoll = input('Host '+str(count)+'th poll ? (y/n): ')
		if(hostPoll == 'y'):
			startHosting()#user registration
			count += 1
		else:
			quit = input('Quit ?(y/n) :')
			if(quit == 'y'):
				break



if __name__ == "__main__":
	Main()