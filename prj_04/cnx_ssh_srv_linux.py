# Programme Test pour Jenkins

from lib.config import *
from lib.fonctions import *

# Programme principal
if __name__ == '__main__':

	print(20*'='+'\nDébut du Programme\n' + 20*'=')

	# Déclaration de la Class pour VM01
	cnx1 = SSHConnection(vmcfg['vm01']['hostssh'],vmcfg['vm01']['userssh'],vmcfg['vm01']['pwdssh'],vmcfg['vm01']['portssh'])

	# Connection au serveur distant
	cnx1.connectssh()

	# Pause de 5 secondes
	temporisation(5)

	# Commandes à exécuter
	rep = "/home/" + vmcfg['vm01']['userssh'] + "/tests"
	msglog = horodatage() + ' - Connection ssh OK'
	logfile = "tests_cnxssh.log"

	listcommandes = ['cd '+rep, 'pwd', 'echo "'+msglog+'" >> '+logfile, 'ls', 'cat '+logfile+' | tail -5' , 'sleep 5']

	command = str('')
	for x in listcommandes:
		command += x + '\n'

	cnx1.execcommandssh(command)

	# Déconnection au serveur distant
	cnx1.deconnectssh()

	print(20*'='+'\nFin du Programme\n' + 20*'=')
