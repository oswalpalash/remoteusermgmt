import platform
import time
import paramiko

def createUser(serverIp,serverPass,username,password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(serverIp, username='root', password=serverPass)
	stdin, stdout, stderr = client.exec_command('useradd -p ' +password +' '+ username)
	client.close()

def deleteUser(serverIp,serverPass,username):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(serverIp, username='root', password=serverPass)
	stdin, stdout, stderr = client.exec_command('deluser --remove-home '+ username+'; userdel -r '+username)	
	client.close()

def listUsers(serverIp,serverPass):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(serverIp, username='root', password=serverPass)
	stdin, stdout, stderr = client.exec_command('cut -d: -f1 /etc/passwd')
	result = []
	for line in stdout:
		result.append(line.strip('/n'))		
		client.close()
	return result

