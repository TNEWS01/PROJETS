# -------------------
# Programme Test de connexion ssh au serveur Linux
# TF
# v 1.0
# -------------------

# Import des Modules
# -------------------
import os
from lib.config import *
from lib.fonctions import *

# Initialisation des Variables
if os.environ['USERNAME'] == 'ADMIN':
	jobnum = 'XX'
	jobname = 'PyCharm'
	vmname = 'vmlinux01'
	writelogcnx = 'Oui'
else:
	jobnum = os.environ['BUILD_NUMBER']
	jobname = os.environ['JOB_NAME']
	vmname = os.environ['PARAM_VMNAME']
	logcnx = os.environ['PARAM_LOGCNX']

	if logcnx == 'true':
		writelogcnx = 'Oui'
	else:
		writelogcnx = 'Non'

# Variables d'environnement
# print(os.environ)

# Programme principal
# -------------------
if __name__ == '__main__':

	sep2(20)
	print('Début du Programme :', hd2())
	sep2(20)



	print('N° du Job Jenkins : {}'.format(jobnum))
	print('Nom du Job Jenkins : {}'.format(jobname))
	print('Nom de la VM Linux : {}'.format(vmname))
	print('Ecriture des Log cnx : {}'.format(writelogcnx))

	sep2(20)

	# Déclaration de la Class pour la VM
	cnx1 = SSHConnection(vmcfg[vmname]['hostssh'],vmcfg[vmname]['userssh'],vmcfg[vmname]['pwdssh'],vmcfg[vmname]['portssh'])

	# Connection au serveur distant
	cnx1.connectssh()

	# Pause de x secondes
	temporisation(2)

	# Commandes à exécuter
	rep = "/home/" + vmcfg[vmname]['userssh'] + "/tests"
	msglog = hd1() + ' - ' + jobnum + ' - ' + jobname + ' : Connection ssh OK'
	logfile = rep + "/tests_cnxssh.log"

	if writelogcnx == 'Oui':
		listcommandes = ['hostname', 'pwd', 'echo "' + msglog + '" >> ' + logfile, 'ls ' + rep,'cat ' + logfile + ' | tail -3']
	else:
		listcommandes = ['hostname', 'pwd', 'ls','cat ' + logfile + ' | tail -5']

	# Option pour exécuter toutes les commandes à la fois
	# command = str('')
	# for x in listcommandes:
	# 	command += x + '\n'

	numcmd = int(1)
	for command in listcommandes:
		cnx1.execcommandssh(command,numcmd)
		numcmd += 1
		sep1(20)

	# Déconnection au serveur distant
	cnx1.deconnectssh()

	sep2(20)
	print('Fin du Programme :', hd2())
	sep2(20)
