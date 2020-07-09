# -------------------
# Programme Test de connexion ssh au serveur Linux
# TF
# v 1.0
# -------------------

# Note 1 : origin/master
# Note 2 : origin/master
# Note 3 : TESTS
# Note 4 : TESTS
# Note 5 : TESTS
# Note 6 : TESTS
# Note 7 : TESTS
# Note 8 : TESTS
# Note 9 : TESTS

# Import des Modules
# -------------------
from lib.config import *
from lib.fonctions import *

# Programme principal
# -------------------
if __name__ == '__main__':

	sep2(20)
	print('Début du Programme :', hd2())
	sep2(20)

	vmname = "vmlinux01"

	print('Nom de la VM Linux : {}'.format(vmcfg[vmname]['hostssh']))

	sep2(20)

	# Déclaration de la Class pour la VM
	hostssh = vmcfg[vmname]['hostssh']
	userssh = vmcfg[vmname]['userssh']
	pwdssh = vmcfg[vmname]['pwdssh']
	portssh = vmcfg[vmname]['portssh']

	cnx1 = SSHConnection(hostssh, userssh, pwdssh, portssh)

	# Connection au serveur distant
	cnx1.connectssh()

	# Pause de x secondes
	temporisation(2)

	# Commandes à exécuter
	# listcommandes = ['cd /home/admin/tests ; pwd ; fic=$(ls -rt1 Test*.log | tail -1); echo $fic; > $fic; ls -rtl']
	listcommandes = ['cd /home/admin/tests ; > $(ls Test*.log)']

	# Option pour exécuter toutes les commandes à la fois
	# command = str('')
	# for x in listcommandes:
	# 	command += x + '\n'

	numcmd = int(1)
	for command in listcommandes:
		cnx1.execcommandssh(command, numcmd)
		numcmd += 1
		sep1(20)

	# Déconnection au serveur distant
	cnx1.deconnectssh()

	sep2(20)
	print('Fin du Programme :', hd2())
	sep2(20)
