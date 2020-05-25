# Class & Fonctions

import os
import paramiko
from time import sleep
from datetime import datetime

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
		SSHConnection.cnxssh.connect(self.host, username=self.username, password=self.password)
		print('- Connection ssh au serveur {} :\tOK'.format(self.host))

	def deconnectssh(self):
		"""
			Déconnection SSH du serveur distant
		"""
		SSHConnection.cnxssh.close()
		print('- Déconnection ssh du serveur {} :\tOK\n'.format(self.host))

	def execcommandssh(self,command):
		"""
			Exécution de commande SSH sur le serveur distant
		"""
		print('- Début d\'excécution des commandes...\n')
		print(command)
		print(20*"-")
		stdin, stdout, stderr = SSHConnection.cnxssh.exec_command(command)
		for x in stdout:
			print(x)
		print(20*"-")
		print('- Fin d\'excécution des commandes.')

def temporisation(tempo):
	# Pause de 5 secondes
	print('- Pause de {} secondes'.format(tempo))
	sleep(tempo)

def horodatage():
	return datetime.now().strftime('%Y%m%d_%H%M%S')