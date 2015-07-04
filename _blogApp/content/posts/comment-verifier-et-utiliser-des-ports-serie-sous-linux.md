title: Comment vérifier et utiliser les ports séries sous Linux
date: 2015-02-21
description: Comment vérifier et configurer les ports série sous Linux à des fins diverses telles que modem, connexion null modems ou connecter un terminal ?
categories:
- Linux

Comment vérifier et configurer les ports série sous Linux à des fins diverses telles que modem, connexion null modems ou connecter un terminal ?

Linux offre divers outils. Linux utilise ttySx pour nommer un port série. Par exemple, COM1 (DOS nom / Windows) est ttyS0, ttyS1 COM2 est et ainsi de suite.


## Afficher les port série connectés


Il suffit d'utiliser la commande _dmesg _(messages système)

    
    $ dmesg | grep tty


Example de sortie :

    
    [ 1.870774] console [tty0] enabled
    [11510.094075] cdc_acm 1-3:1.2: ttyACM0: USB ACM device




### La commande _setserial_


setserial est un programme conçu pour établir et/ou afficher les informations de configuration associé à un port série. Ces informations sont les I/O (entrées/sorties) ainsi que les IRQ (interruptions matérielles) qu'un port série utilise.

Il suffit de taper la commande suivante:

    
    $ setserial -g /dev/ttyS[0123]


Sortie:

    
    /Dev/ttyS0, UART: 16550A, Port: 0x03f8, IRQ: 4
     /Dev/ttyS1, UART: 16550A, Port: 0x1020, IRQ: 18
     /Dev/ttyS2, UART: inconnu, Port: 0x03e8, IRQ: 4
     /Dev/ttyS3, UART: inconnu, Port: 0x02e8, IRQ: 3


setserial avec l'option -g renseigne sur les ports séries connectés physiquement à votre machine.




## Programmes de console série Linux


Une fois identifiés les ports série, vous pouvez configurer les configurer en utilisant divers utilitaires, tels que :



	
  * [**minicom**](http://www.cyberciti.biz/tips/connect-soekris-single-board-computer-using-minicom.html) :Le meilleur programme de communication série convivial pour contrôler les modems et la connexion à vider dispositifs

	
  * [**wvidial ou autre GUI en réseau**](http://www.cyberciti.biz/tips/linux-configure-modem-to-connect-to-the-internet-using-a-ppp-dialup-account.html) - un composeur PPP avec intelligence intégrée.

	
  * **getty / agetty** - agetty ouvre un port tty, demande un nom d'utilisateur et appelle la commande /bin/login.

	
  * **configuration du grub / lilo** - Pour configurer le port série comme console système


