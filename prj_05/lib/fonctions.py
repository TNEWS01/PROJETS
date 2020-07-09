# -------------------
# Class & Fonctions
# -------------------

# Import des modules
# -------------------
import os
import paramiko
from time import sleep
from datetime import datetime

# Définition des Class
# -------------------
class SSHConnection:
	"""
		Class pour effectuer une connextion SSH via le module paramiko
	"""
	# Initialisation de la connexion
	cnxssh = paramiko.SSHClient()
	cnxssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
	cnxssh.load_system_host_keys()

	def __init__(self,host,username,password,port):
		paramiko.util.log_to_file('c:\\Temp\\cnx_paramiko.log')
		self.host = host
		self.port = port
		self.username = username
		self.password = password

	def connectssh(self):
		"""
			Connection SSH au serveur distant
		"""
		try:
			msginfo('Connection ssh au serveur {} ...'.format(self.host))
			SSHConnection.cnxssh.connect(self.host, username=self.username, password=self.password)
			msginfo('Connection : OK')
		except paramiko.ssh_exception.AuthenticationException as e:
			msgerreur('Authentification ssh : KO')
			print('Log Erreur : \n', e)

	def deconnectssh(self):
		"""
			Déconnection SSH du serveur distant
		"""
		SSHConnection.cnxssh.close()
		msginfo('Déconnection ssh du serveur {} : OK'.format(self.host))

	def execcommandssh(self,command,numcmd):
		"""
			Exécution de commande SSH sur le serveur distant
		"""
		msginfo('Début d\'excécution de la commande N° {}'.format(numcmd))
		print(command)
		stdin, stdout, stderr = SSHConnection.cnxssh.exec_command(command)
		for x in stdout:
			print(x)
		msginfo('Fin d\'excécution de la commande N° {}'.format(numcmd))

# Définition des fonctions
# -------------------
def temporisation(tempo):
	# Pause de 5 secondes
	sep1(20)
	print('- Pause de {} secondes'.format(tempo))
	sleep(tempo)
	sep1(20)

def hd1():
	return datetime.now().strftime('%Y%m%d_%H%M%S')

def hd2():
	return datetime.now().strftime('%Y/%m/%d à %H:%M:%S')

def hd3():
	return datetime.now().strftime('%H:%M:%S')

def sep1(n):
	print( n * "-")

def sep2(n):
	print( n * "=")

def msginfo(msg):
	print(hd3() + ' -', msg)

def msgerreur(msg):
	print(hd3() + ' -', msg)


