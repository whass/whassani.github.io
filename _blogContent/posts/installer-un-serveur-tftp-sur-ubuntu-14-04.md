title: Installer un serveur TFTP sur Ubuntu 14.04
date: 2015-02-24
categories:
- Linux
- Embedded
tags:
- client tftp
- serveur tftp
- TFTP

### Aperçu


**TFTP** (pour _**Trivial File Transfer Protocol**_ ou **Protocole simplifié de transfert de fichiers**) est un protocole simplifié de transfert de fichiers.

Il fonctionne en UDP sur le port 69, au contraire du FTP qui utilise lui TCP. L'utilisation d'UDP, protocole « non fiable », implique que le client et le serveur doivent gérer eux-mêmes une éventuelle perte de paquets. En termes de rapidité, l'absence de fenêtrage nuit à l'efficacité du protocole sur les liens à forte latence. On réserve généralement l'usage du TFTP à un réseau local.

Les principales simplifications visibles du TFTP par rapport au FTP est qu'il ne gère pas le listage de fichiers, et ne dispose pas de mécanismes d'authentification, ni de chiffrement. Il faut connaître à l'avance le nom du fichier que l'on veut récupérer. De même, aucune notion de droits de lecture/écriture n'est disponible en standard.

À cause de ces fonctionnalités absentes, FTP lui est généralement préféré. TFTP reste très utilisé pour la mise à jour des logiciels embarqués sur les équipements réseaux (routeurs, pare-feu, etc.) ou pour démarrer un PC à partir d'une carte réseau. (source wikipedia)


### [![Diagramme_des_Flux_de_TFTP](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/Diagramme_des_Flux_de_TFTP.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/Diagramme_des_Flux_de_TFTP.png)




### Installation


Le serveur TFTP existe dans les dépôts officiel d'ubuntu, pour l'installer tapez :

    
    $ sudo apt-get install tftpd-hpa


Configurez le dossier que vous souhaitez partager via le serveur TFTP (ici : /home/user_name/test-ftp/public/) :

    
    $ sudo nano /etc/default/tftpd-hpa
    TFTP_USERNAME="tftp"
    TFTP_ADDRESS="0.0.0.0:69"
    TFTP_OPTIONS="--create --listen --verbose /home/user_name/test-ftp/public<span style="color: #ff0000;">/</span>"
    RUN_DAEMON="yes"




Redémarrez le serveur pour que les changements soient bien pris en charge :



    
    $ sudo service tftpd-hpa restart




Vérifiez que tout est bien installé :



    
    $ netstat -a | grep tftp




Vous devez obtenir cela :



    
    udp 0 0 *:tftp *:*




### Tester le serveur


Installer un client TFTP

    
    $ sudo apt-get install tftp




Créez un fichier de test et sauvegardez le dans le dossier public de votre serveur TFTP :










$ echo "Coming via TFTP" > ~/test/public/test_tftp.txt







Maintenant, téléchargerons le fichier test_tftp.txt via TFTP :




Mettez-vous dans le dossier dans lequel vous souhaitez télécharger le fichier, admettons que ce soit votre bureau :



    
    $ cd ~/Desktop
    $ tftp
    tftp> connect 127.0.0.1
    tftp> get /home/user_name/test-ftp/public/test_tftp.txt
    Received 17 bytes in 0.0 seconds
    tftp> quit
    $ cat test_tftp.txt
    Coming via TFTP




### 









