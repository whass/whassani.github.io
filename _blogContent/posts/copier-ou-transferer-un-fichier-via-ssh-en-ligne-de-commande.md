title: Copier ou transférer un fichier ou un dossier via SSH en ligne de commande
date: 2015-01-22
categories: 
- Linux
- WebServer


La commande **scp** permet de copier un fichier ou un répertoire (-r) du client vers le serveur ou du serveur vers le client. Le chemin du serveur peut être indiqué en absolu (_/home/dupont/Repertoire_ par exemple) ou relatif à partir du répertoire de base _Repertoire_. Pour utiliser **scp**, vous devez connaître l’arborescence exacte des répertoires de la machine distante. Il est impératif que **SSH** soit installé sur les deux machines devant communiquer pour effectuer votre transfert.


## Forme générale


scp [-pqrvBC1246] [-F ssh_config] [-S program] [-P port] [-c cipher] [-i identity_file] [-l limit] [-o ssh_option] [[user@]host1:]file1 [...] [[user@]host2:]file2

C'est du charabia pour vous !, voyons la syntaxe selon le cas de figure :


## Syntaxe





	
  * Copie d'un fichier d'une machine _serveur1_ vers une autre machine _serveur2_:

    
    > scp Login1@Serveur1:Chemin1/NomFichier1 Login2@Serveur2:Chemin2/NomFichier2




	
  * Copie d'un fichier depuis le répertoire courant vers un répertoire du serveur:

    
    > scp Fichier login@serveur:Chemin




	
  * Copie d'un répertoire, avec éventuellement ses sous-répertoires, vers un répertoire du serveur:

    
    > scp -r Repertoire login@serveur:Chemin




	
  * Copie d'un fichier du serveur vers le répertoire courant:

    
    > scp login@serveur:Chemin/Fichier .




	
  * Copie d'un répertoire du serveur vers le répertoire courant:

    
    > scp -r login@serveur:Chemin/Repertoire.





Vous ne comprenez toujours rien !, regardez ces exemples :


## Exemples



    
    > scp blender@ccali.in2p3.fr:/afs/in2p3.fr/home/c/calvat/Readme.txt .


copie le fichier _Readme.txt_ de _/afs/in2p3.fr/home/c/calvat_ sur ccali.in2p3.fr vers le répertoire local courant.

    
    > scp -r blender@ccali.in2p3.fr:/afs/in2p3.fr/home/c/calvat/toto .


copie le répertoire _toto_ et les sous-répertoires attachés de _/afs/in2p3.fr/home/c/calvat_ sur ccali.in2p3.fr vers le répertoire local courant.

Attention : il y a un point (.) en fin de ligne !, si vous n'être pas encore familier avec linux, le point signifie le dossier sur le lequel vous êtes (pwd pour le connaitre).

Si vous ne comprenez toujours rien, laissez moi un commentaire pour m'expliquez ce qui
