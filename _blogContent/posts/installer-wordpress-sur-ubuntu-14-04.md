title: Installer Wordpress sur Ubuntu 14.04
date: 2015-01-22
categories: 
- Linux
- WebServer


Actuellement, WordPress est le CMS (content management system) le plus populaire et le plus utilisé sur Internet. Il vous permet de configurer et de mettre facilement des blogs et des sites Web flexibles.

Dans ce guide, nous allons nous concentrer sur la mise en place de WordPress avec un serveur web Apache sur Ubuntu 14.04.


## Pré-requis :


Avant de commencer ce guide, il y a quelques étapes importantes doivent être réalisées sur votre serveur, à savoir :



	
  1. Toute les manipulation doivent être faite un utilisateur non root avec les privilèges sudo, vous aurez donc besoin d'avoir un utilisateur ou d'en créer un. Pas de panique, les étape 1-4 illustrent comment créer un utilisateur avec des privilèges sudo sous Ubuntu 14.04.

	
  2. Vous aurez besoin d'avoir un LAMP (Linux, Apache, MySQL et PHP) installé sur votre serveur.


Lorsque vous avez terminé avec ces étapes, vous pouvez continuer avec ce guide.




## Créer une base de données MySQL et un utilisateur MySQL dédié pour WordPress


La base de données permets de stocker les informations que les CMS aura à gérer. Nous installerons une base de données relationnelles MySQL.

Pour commencer, ouvrez une session MySQL en tant que root (compte administrateur MySQL et non celui du système) comme suit :

    
    root -p mysql


Vous serez invité à entrer le mot de passe que vous avez défini pour le compte root MySQL lorsque vous avez installé le logiciel. Vous aurez alors une invite de commande MySQL.

Tout d'abord, il faut créer une base de données pour WordPress, nous l'appellerons wordpress (libre à vous d'utiliser un autre nom). Entrez cette commande pour créer la base de données:

CREATE DATABASE wordpress;

*Ne pas oublier le point-virgule (;) en fin de ligne afin de signifier à MySQL que la ligne de commande est terminée.

Ensuite, pour des raisons de sécurité, nous allons créer un compte utilisateur MySQL dédié exclusivement à la base de données wordpress. Nous l'appellerons wordpressuser à qui on attribuera un mot de passe de mot de passe aussi (même remarque, vous pouvons utiliser les nom et mot de passe que vous souhaitez).

    
    CREATE USER wordpressuser@localhost identified by 'mot-de-passe';


À ce stade, vous avez une base de données et un compte d'utilisateur dédié pour WordPress. Toutefois, ces deux éléments n'ont aucun lien pour le moment. A ce stade, l'utilisateur n'a pas accès à la base de données wordpress. Pour ce faire, rien de plus simple, exécutez :

    
    GRANT ALL PRIVILEGES ON <span class="highlight">wordpress</span>.* TO <span class="highlight">wordpressuser</span>@localhost;
    


Pour lier l'utilisateur wordpressuser à la base de données wordpress; et a tous les privilèges sur cette dernière. n'oubliez pas de “flusher” les privilèges, comme ceci :

    
    FLUSH PRIVILEGES;


C'est fini, nous pouvons sortir de l'invite MySQL en tapant:

    
    exit;


Vous devriez maintenant être de retour à votre invite de commande régulière.


## Télécharger WordPress


Il est temps de télécharger wordpress. Heureusement, le lien de téléchargement de la dernière version est toujours le même.

    
    cd ~
    wget http://wordpress.org/latest.tar.gz


Ceci va télécharger un fichier compressé qui contient le contenu du répertoire des fichiers archivés de WordPress à notre répertoire.

Nous pouvons extraire les fichiers à reconstruire le répertoire WordPress nous avons besoin en tapant:

    
    tar xzvf latest.tar.gz


Cela va créer un répertoire appelé wordpress dans votre répertoire home.



Avant de passer à la troisième étapes, quelques paquets sont recommandés. Ces paquets vous permettrons en outres, de travailler avec des images, d'installer des plugins et les mises à jour de votre site à l'aide de vos identifiants de connexion SSH.

    
    sudo apt-get update
    



    
    sudo apt-get install php5-gd libssh2-php
    
    




## Configurer WordPress


Nous y arriverons, mais vous devez savoir que Wordpress se configure en quelques minutes via votre navigateur web (Firefox, Chrome, Safari, etc.). Avant d'y arriver nous devons juste spécifier à wordpress la base de données qu'il devra utiliser (noms de la base, utilisateur et mot de passe). Cela, ce fait via le fichier de configuration de wordpress.

Mettez vous sur le dossier dans lequel vous avez mis les fichier de wordpress, dans notre cas :

    
    cd ~ / wordpress


Wordpress fournit un échantillon du fichier de configuration que vous des renommer en tapant :

    
    cp wp-config-sample.php wp-config.php


Maintenant que nous avons un fichier de configuration sur lequel nous pouvons travailler, nous allons l'ouvrir dans un éditeur de texte :

    
    sudo nano config.php


Ce fichier est presque entièrement adapté à nos besoins déjà. Les seules modifications que nous devons faire sont les paramètres qui gèrent nos informations de base de données.

Nous aurons besoin de trouver les réglages pour DB_NAME, DB_USER et DB_PASSWORD pour que WordPress puisse se connecter correctement et s'authentifier sur la base de données que nous avons créé.

Remplissez les valeurs de ces paramètres avec les informations de la base de données que vous avez créé. Il devrait ressembler à ceci :

    
    // ** Paramètres MySQL - Vous pouvez obtenir cette information auprès de votre hébergeur ** //
    / ** Le nom de la base de données pour WordPress * /
    define ('DB_NAME', 'wordpress');



    
    / ** * Nom d'utilisateur MySQL base de données /
    define ('DB_USER »,« wordpressuser');



    
    / ** MySQL mot de passe de base de données * /
    define ('DB_PASSWORD', 'mot de passe');


Ce sont les seules valeurs que vous devez changer.

Lorsque vous avez terminé, enregistrez et fermez le fichier.


## Copier les fichiers à la racine du serveur Web


Maintenant que nous avons notre application configurée, nous devons copier le dossier wordpress à la racine d'Apache.

Une des façons les plus faciles et les plus fiables de transférer des fichiers d'un répertoire à un autre tout en préservant les permissions et d'utiliser la commande rsync.

L'emplacement de la racine d'Apache dans le guide Ubuntu 14.04 LAMP est /var/www/html/. Nous pouvons transférer nos fichiers WordPress en tapant:

    
    sudo rsync -AVP ~/wordpress/ /var/www/html/


Cela va copier en toute sécurité la totalité du contenu du répertoire que vous avez décompressé à la racine d'Apache.

Mettez vous maintenant dans la racine afin de faire quelques modifications d'autorisations finales

    
    cd /var/www/html


Vous aurez à changer la propriétaire de nos fichiers pour une sécurité accrue.

Nous donnerons la propriété à un utilisateur régulier (non root) avec les privilèges sudo. Cela peut être votre utilisateur régulier si vous le souhaitez, mais vous pouvez en créer un autre exclusivement dédié à wordpress, à vous que de choisir.

Dans ce guide, nous avez crée un utilisateur régulier avec les privilèges sudo appelé demo.

Afin de permettre aux fichier de l'utilisateur demo d'interagir avec Apache, il est nécessaire que ce dernier fasse partie du groupe de fichier du serveur web (www-data). Comprenez par www, données web. Nous pouvons rapidement affecter demo à ce groupe en tapant:

    
    sudo chown -R démo: www-data *


Les ajouts (Image, document, etc.) que vous apporterez à votre site web sont contenus dans le dossier "uploads". Nous allons en créer un manuellement en tapant :

    
    mkdir /var/www/html/wp-content/uploads


Nous devons permettre au serveur Web lui-même à écrire dans ce répertoire. Nous pouvons attribuer ce dossier à celui de notre serveur web, comme ceci:

    
    sudo chown -R :www-data/var/www/html/wp-content/uploads


Cela permettra au serveur web de créer des fichiers et des répertoires dans ce répertoire, ce qui nous permettra de télécharger du contenu sur le serveur.


## Installation complète via l'interface Web


Maintenant que vous avez vos fichiers en place et votre CMS configuré, vous pouvez compléter l'installation via l'interface web.

Dans votre navigateur Web, accédez au nom de domaine de votre serveur ou l'adresse IP publique:

http://domaine_serveur_ou_IP
Vous verrez la page de configuration initiale WordPress, où vous pourrez créer un compte administrateur initial :

![Wordpress initial config](https://assets.digitalocean.com/articles/wordpress_1404/initial_config.png)

Remplissez les informations pour le site et le compte administratif que vous souhaitez faire. Lorsque vous avez terminé, cliquez sur le bouton Installer qui se trouve en bas de la page.

WordPress confirme l'installation, puis vous demande de vous connecter avec le compte que vous venez de créer:

![WordPress confirm install](https://assets.digitalocean.com/articles/wordpress_1404/confirm_install.png)

Cliquez sur le bouton en bas, puis de remplir vos identifiant et mot de passe de votre compte:

![WordPress login](https://assets.digitalocean.com/articles/wordpress_1404/login.png)

Voilà, c'est terminé ! vous avez accès désormais à l'interface administrateur de wordpress.

![WordPress admin interface](https://assets.digitalocean.com/articles/wordpress_1404/admin_interface.png)



Amusez vous bien, et partagez avec nous vos histoires, réalisations et .... tout ce que vous voulez.

Merci d'avoir suivit ce tuto, laissez moi un commentaire dans la cas où .... ça ne marche pas pour vous, ou que ça marche et que vous êtes content !

