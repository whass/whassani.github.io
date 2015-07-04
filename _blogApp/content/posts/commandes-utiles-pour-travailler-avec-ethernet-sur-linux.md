title: Commandes utiles pour travailler avec Ethernet sous Linux
date: 2015-02-20
description: Quelques commandes utilises pour configurer vos ports ethernet en toute simplicité. Afficher les informations, DHCP, allumer et éteindre, force une nouvelle adresse IP, etc.
categories:
- Linux
tags:
- dhclient
- eth0
- ifconfig


##### Affichage des informations de configuration Ethernet:


    $ ifconfig


##### Exécuter DHCP pour acquérir une adresse IP (uniquement sur certains systèmes):

	
    $ dhclient


##### Éteindre et rallumer une connexion Ethernet :

	
    $ ifconfig eth0 down
    $ Ifconfig eth0 up

NB: le nom de la carte peut varier d'une machine à une autre, dans cet exemple, c'est eht0. Pour trouver la votre, faite un 'ifconfig'  et repérer là.

### Forcer une nouvelle adresse IP:

	
    $ Ifconfig eth0 192.168.0.212





