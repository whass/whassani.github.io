title: Copiez vos fichiers et dossiers en toute sécurité avec le serveur SSH avec la commande SCP
date: 2015-01-23
categories: 
- Linux
- WebServer

La commande **scp** permet de copier un fichier ou un répertoire (-r) du client vers le serveur ou du serveur vers le client. Le chemin du serveur peut être indiqué en absolu (_/home/dupont/Repertoire_ par exemple) ou relatif à partir du répertoire de base _Repertoire_. Pour utiliser **scp**, vous devez connaître l’arborescence exacte des répertoires de la machine distante. Il est impératif que **SSH** soit installé sur les deux machines devant communiquer pour effectuer votre transfert.

Forme générale

scp [-pqrvBC1246] [-F ssh_config] [-S program] [-P port] [-c cipher]

    
        [-i identity_file] [-l limit] [-o ssh_option] [[user@]host1:]file1
        [...] [[user@]host2:]file2


Si vous êtes novice, vous vous dites surement, MAIS C'EST QUOI CE CHARABIA !!!

Pas de panique, dans ce qui suit, je vous montrerai la manière de copier via ssh avec des examples simples et en abordant différents scénarios.

Let's go ...


## Copie sur le port standard SSH : 22


Si vous utilisz le port standard à savoir le port 22

Pour un fichier

    
    scp /chemin-vers-votre-fichier/ utilisateur@votre-dimaine-ou-IP:/emplacement-de-copie-sur-votre-serveur/


Pour un dossier

    
    scp -r /chemin-vers-votre-dossier/ utilisateur@votre-dimaine-ou-IP:/emplacement-de-copie-sur-votre-serveur/
    




## Copie sur le port non standard SSH : (autre que le 22)



    
    Comme c'est une très mauvaise idée de communiquer via le port 22 (cible facile pour les gens malintentionné !), si vous utilisé un autre port, dans ce cas, utilisez les commandes suivantes :
    
    


Pour un fichier

    
    scp <span style="color: #ff0000;">-P numero-de-port</span> /chemin-vers-votre-fichier/ utilisateur@votre-dimaine-ou-IP:/emplacement-de-copie-sur-votre-serveur/


Pour un dossier

    
    scp <span style="color: #ff0000;">-P numero-de-port</span> -r /chemin-vers-votre-dossier/ utilisateur@votre-dimaine-ou-IP:/emplacement-de-copie-sur-votre-serveur/
    




## Copie en utilisant une clé SSH public


Pour un fichier

    
    scp -P numero-de-port /chemin-vers-votre-fichier/ <span style="color: #ff0000;">-i /emplacement-de-la-cle/</span> utilisateur@votre-dimaine-ou-IP:/emplacement-de-copie-sur-votre-serveur/


Pour un dossier

    
    scp -P numero-de-port -r /chemin-vers-votre-dossier/ <span style="color: #ff0000;">-i /emplacement-de-la-cle/</span> utilisateur@votre-dimaine-ou-IP:/emplacement-de-copie-sur-votre-serveur/
    
    


Si vous avez des questions n'hésitez pas à me laisser un commentaire.
