title: Sauvegardez vos données dans le Cloud avec OwnCloud
date: 2014-10-22
description: OwnCloud est une application web qui vous permettra de stocker vos données dans le Cloud un peu comme DropBox, à la seule différence que vous êtes seul maître de vos données. Il ne se limite qu'au stockage de données, mais aussi, comme agenda, lecteur de musique, etc.
categories: 
- Linux
- Web-Server

** Table des matières **

[TOC]

OwnCloud est une application web qui vous permettra de stocker vos données dans le Cloud un peu comme DropBox, à la seule différence que vous êtes seul maître de vos données.

Il ne se limite qu'au stockage de données, mais aussi, comme agenda, lecteur de musique, etc.

Dans ce guide, nous allons installer et configurer ownCloud sur une Ubuntu 14.04.


## Installez OwnCloud

La version de ownCloud disponibles dans les dépôts officiel d'Ubuntu 14.04 par défaut est obsolète maintenant. La dernière version est compilé pour Ubuntu par l'outil fourni par par openSUSE.

Pour cela, nous téléchargeons d'abord la clé de ownCloud associé à ce fichier :

    
    CD
    wget http://download.opensuse.org/repositories/isv:/ownCloud:/community/xUbuntu_14.04//Release.key


Maintenant, ajoutez la clé à apt d'ubuntu afin qu'il puisse valider les fichiers:

    
    sudo apt-key add - <Release.key


Ajoutez les dépôts Owncloud dans le Build Service openSUSE à des listes de sources d'Apt en tapant:

    
    echo 'deb http://download.opensuse.org/repositories/isv:ownCloud:community/xUbuntu_12.04/ /' | sudo tee -a /etc/apt/sources.list.d/owncloud.list


Enfin, mettre à jour la base de données de package et installer ownCloud et MySQL (il es possible d'utiliser d'autres bases de données (SQLite, MariaDB), mais SQL est la plus performante parmis celles supportées par owncloud):

    
    sudo apt-get update
    sudo apt-get install owncloud mysql-server


Vous serez invité à définir un mot de passe root pour l'administrateur de votre base de données MySQL pendant l'installation.


## Configurer MySQL


La base de donnée par défaut utilisé par OwnCloud est SQLite, pour des raisons de performances, nous préférerons l'usage de MySQL. Pour ce faire, nous devons configurer MySQL en premier.

Tapez les commandes suivantes pour initialiser la base de données et sécuriser le système:

    
    sudo mysql_install_db
    sudo mysql_secure_installation


Le mot de passe du root vous sear demandé dans un premier temps, ensuite, le système vous demandera si vous voulez le changer ou pas, à vous de voir. Pour les autres questions, appuyer sur "entree" pour sélectionner oui pour tous les réglages.

Maintenant, vous connecter à MySQL en tant que l'utilisateur root en tapant:
    
    mysql -u root -p


Encore une fois, vous serez invité à entrer le mot de passe d'administration MySQL.

Créer une base de données avec cette commande:
    
    CREATE DATABASE owncloud;


Créer et attribuer des privilèges à un nouvel utilisateur de MySQL pour gérer les opérations de base de données pour ownCloud:

    
    GRANT ALL ON owncloud.* to 'owncloud'@'localhost' IDENTIFIED BY '<span class="highlight">select_database_password</span>';
    


Quitter MySQL en tapant:

exit;

On a presque terminé.


## Configuration finale


Maintenant, si sur votre navigateur WEB tapez :

http://votre_nom_de_domaine_ou_IP/owncloud

Si tout est OK, vous verrez cela :

[![Capture d’écran 2015-01-22 à 12.37.45](http://ec2-54-175-20-183.compute-1.amazonaws.com/wp-content/uploads/2015/01/Capture-d’écran-2015-01-22-à-12.37.45.png)](http://ec2-54-175-20-183.compute-1.amazonaws.com/wp-content/uploads/2015/01/Capture-d’écran-2015-01-22-à-12.37.45.png)

Choisissez le nom ainsi qu'un mot de passe administrateur que vous souhaitez (j'ai choisi blender pour moi !), saisissiez-les. Avant de terminer l'installation, cliquez sur "support de stockage & base de données". Vous verrez apparaître cela :

[![Capture d’écran 2015-01-22 à 12.36.57](http://ec2-54-175-20-183.compute-1.amazonaws.com/wp-content/uploads/2015/01/Capture-d’écran-2015-01-22-à-12.36.57.png)](http://ec2-54-175-20-183.compute-1.amazonaws.com/wp-content/uploads/2015/01/Capture-d’écran-2015-01-22-à-12.36.57.png)



Cliquez sur "MySQL/MariaDB" et saisissez  les informations relatives à cette dernière (celles vous avez configuré dans la dernière étape)

Cliquez sur "Terminer l'installation", encore une fois, si tout s'est bien passé, vous accéderez à votre OwnCloud. Un message de bienvenu vous invitera à télécharger les clients webs de OwnCloud pour votre machine (PC, Mac, Smartphone, etc.) sur les système mac os, android et linux. Libre à vous de les télécharger ou pas.

[![Capture d’écran 2015-01-22 à 12.48.59](http://ec2-54-175-20-183.compute-1.amazonaws.com/wp-content/uploads/2015/01/Capture-d’écran-2015-01-22-à-12.48.59.png)](http://ec2-54-175-20-183.compute-1.amazonaws.com/wp-content/uploads/2015/01/Capture-d’écran-2015-01-22-à-12.48.59.png)

Bravo, votre serveur est prêt pour stocker vos données.
