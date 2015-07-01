title: Programmation des processeurs ARM avec Code Composer Studio 6 de chez TI et Ubuntu 14.04 64bits
date: 2015-01-23
description: Le logiciel Code Composer Studio est un environnement de développement intégré qui permet de programmer les processeurs embarqués de chez Texas Instrument comme les processeurs spécialisé dans le traitement de signal (DSP) de la famille TMS320, les appareils basé sur l'architecture ARM ou les microcontrôleurs de la famille MSP430.
categories: 
- Embedded

** Table des matières **

[TOC]

[![CCSv6-embeddedprocessor](http://embarquez-vous.fr/wp-content/uploads/2015/01/CCSv6-embeddedprocessor.png)](embarquez-vous.fr/wp-content/uploads/2015/01/CCSv6-embeddedprocessor.png)

Le logiciel **Code Composer Studio** est un environnement de développement intégré qui permet de programmer les processeurs embarqués de chez Texas Instrument comme les processeurs de signal numérique (DSP) de la famille TMS320, les appareils basé sur l'architecture ARM ou les microcontrôleurs de la famille MSP430.

Cet IDE est basé sur Eclipse, un Framework open source.

Let's begin .....


## Résoudre les dépendances

Nous commençons par résoudre les dépendances.
    
    $ sudo apt-get update

    $ sudo apt-get install libc6:i386 libx11-6:i386 libasound2:i386 libatk1.0-0:i386 libcairo2:i386 libcups2:i386 libdbus-glib-1-2:i386 libgconf-2-4:i386 libgdk-pixbuf2.0-0:i386 libgtk-3-0:i386 libice6:i386 libncurses5:i386 libsm6:i386 liborbit2:i386 libudev1:i386 libusb-0.1-4:i386 libstdc++6:i386 libxt6:i386 libxtst6:i386 libgnomeui-0:i386 libusb-1.0-0-dev:i386 libcanberra-gtk-module:i386 gtk2-engines-murrine:i386



## Télécharger Code Composer Studio

Ensuite téléchargez gratuitement CCS, il est disponible sur le wiki de Texas Instrument suivant :

    
[http://processors.wiki.ti.com/index.php/Download_CCS](http://processors.wiki.ti.com/index.php/Download_CCS) 


Choisissez linux, vous serez invité à vous identifié sur la plateforme de Texas Instrument (vous devez disposer d'un compte TI, vous pouvez en créer un).


## Installer Code Composer Studio

Après avoir téléchargé l'exécutable, tapez :
    
    $ cd dossier-de-telechargement
    
    $ ./ccs_setup_6.x.x.xxxxx.bin (remplacer le xxxxxxx avec le numéro de version de votre exécutable)


Si vous avez un message d'erreur vous spécifiant qu'il manque libudev.so.0 dans votre système. Il suffit de lui créer un lien symbolique comme ceci :

    $ sudo ln -s /lib/i386-linux-gnu/libudev.so.1 /lib/libudev.so.0

L'installation est relativement aisée, et se déroule comme suit :

1. Accepter les termes du contrat

[![Capture d’écran 2015-01-23 à 02.15.15](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-02.15.15.png)](http://embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-02.15.15.png)

2. Cocher les outils de développement nécessaire à la Tiva-C launchpad comme sur la figure suivante.

[![Capture d’écran 2015-01-23 à 02.24.09](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-02.24.09.png)](http://embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-02.24.09.png)

3. Sélectionner les émulateurs qui vous intéresse

[![Capture d’écran 2015-01-23 à 02.25.30](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-02.25.30.png)](http://embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-02.25.30.png)


4. Pour l'app centre, libre à vous de les cocher ou pas.

[![Capture d’écran 2015-01-23 à 02.25.55](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-02.25.55.png)](http://embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-02.25.55.png)


Juste avant que l'installation se termine, l'installateur vous demande si vous souhaiter un raccourci ou pas.
	
* Si vous choisissez oui alors, il y'a de forte chance qui si vous cliquez sur le raccourci que ça ne marche pas. Dans ce cas, modifier le fichier du raccourci qui se trouve dans le d'installation de CCS choisi au début comme ceci :

```
    $ cd /votre-dossier-d-installation/
    $ sudo nano nom-du-raccourci
```

Modifier la ligne qui commence par EXEC, elle devrait ressembler à ceci :
    
    EXEC : /votre-dossier-d-installation/ccsvx/eclipse/ccstudio


(x la version installé, la mienne c'est 6, donc ccv6)

* Si vous n'avez pas choisi de créer le raccourci, dans ce cas, exécutez la commande suivante :
 
```
  ./votre-dossier-d-installation/ccsvx/eclipse/ccstudio
```

(n'obliez pas le pointu début de la ligne, car c'est un script)

A l'issu de cela, CCS se lance. Un fenêtre de démarrage vous demandera de choisir le répertoire de travail (comme il est basée sur Ecplise vu qu'il est construit à partir de ce dernier) comme ceci :

[![Capture d’écran 2015-01-23 à 03.13.32](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-03.13.32.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-03.13.32.png)



Choisissez le dossier que vous souhaitez, il n y'a de restrictions.

Cochez "Use this as ..... ask again" si vous ne voulez pas que cette boite de dialogue s'affiche à chaque démarrage de CCS.

S'il vous demande de faire les mise-à-jour, en vous affichant ce message :

[![Capture d’écran 2015-01-23 à 03.30.53](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-03.30.53.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-23-à-03.30.53.png)

Ces dernières concernent l'app center, comme nous l'avons coché précédemment. Je vous conseille de les faire, mais elles ne sont pas obligatoire.

Maintenant CCS et prêt à être utilisé.

Il reste une dernière étape elle concerne les drivers de la carte, ils s'installent facilement comme ceci :

    
    cd /votre-dossier-d-installation/ccsvx/install_scripts
    sudo ./install_drivers.sh



## Installer TivaWare

A titre d'information, TivaWare, contient un ensemble de script, tels que les pilotes ... nous aurons l'occasion de revoir cela plus en détails une autre fois.

Télécharger Tivaware directement (après authentification) du site de Texas Instruments via ce lien :

    
[http://www.ti.com/tool/sw-tm4c](http://www.ti.com/tool/sw-tm4c) 


Une fois sur le site de TI, vous avez la possibilité de télécharger séparément les pilotes ou autre, je vous recommande de les télécharger tous en choisissant :

    
    SW-TM4C: TivaWare for C Series Software (Complete)


Vous serait redirigé vers la page de téléchargement, choisissez la "full release" qui correspond à ce fichier :

    
    SW-TM4C-2.1.0.12573.exe


(le fichier peut varier)

Téléchargez ce fichier et enregistrez-le dans votre dossier d'installation de CCS

    
    cd /votre-dossier-d-installation/
    mkdir tivaware
    cd tivaware 
    unzip ~/Downloads/SW-TM4C-2.1.0.12573.exe


Il y a plusieurs façons d'inclure TivawWre dans vos projets. Afin de minimiser les paramètres requis sur chaque projet, créez un fichier dans votre espace de travail qu'on appellera "vars.ini".

`cd /votre-espace-de-travail/
nano vars.ini`

Une seule ligne est nécessaire :

    
    TIVAWARE_INSTALL=/votre-dossier-d-installation-tivaware/



## Configurez votre projet pour TivaWare


Le fichier vars.ini crée une variable d'environnement pour votre espace de travail (où le fichier est enregistré). Pour configurer votre projet pour utiliser tivaware, faites ceci :

* Importez le fichier vars.ini comme source pour construire des variables CCS
* Ajouter un chemin "inclure des fichiers" pour le compilateur en utilisant la variable TIVAWARE_INSTALL
* Ajoutez le fichier driverlib.lib au projet.


Allez-y et créez un nouveau projet (File => New => CCS Project). Utilisez le screenshot suivant comme guide:

[![Capture d’écran 2015-01-24 à 07.23.44](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-07.23.441.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-07.23.441.png)

Une fenêtre de configuration apprêtera :

[![Capture d’écran 2015-01-24 à 08.49.53](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-08.49.53.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-08.49.53.png)

Choisissez Tiva C series ainsi que le processeur correspondant à votre carte.

Lorsque vous avez terminé, sélectionnez File => Import => Code Composer Studio => Build Variables :

[![Capture d’écran 2015-01-24 à 08.53.36](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-08.53.36.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-08.53.36.png)


Sélectionner vars.ini qu'on crée précédemment.


[![Capture d’écran 2015-01-24 à 08.56.41](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-08.56.41.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-08.56.41.png)

Ensuite, un clic droit sur le nom de votre projet dans l'explorateur de projet. Sélectionnez "Properties" -> ARM Compiler, include options, et ajouter le chemin tel qu'il est illustré sur le screenshot suivant :
    
    ${TIVAWARE_INSTALL}

[![Capture d’écran 2015-01-24 à 09.06.24](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-09.06.24.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-09.06.24.png)

Enfin, ajoutez driverlib.lib à votre projet. Un clic droit sur le nom de votre projet dans l'explorateur de projet et sélectionnez Add files :


[![Capture d’écran 2015-01-24 à 09.09.16](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-09.09.161.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-09.09.161.png)


Le chemin d'accès complet driverlib.lib comme indiqué: /votre-dossier-d-installation/tivaware/driverlib/CCS/Debug.


Sur la fenêtre suivante, sélectionnez lien vers le fichier ( link to file):

[![Capture d’écran 2015-01-24 à 09.12.15](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-09.12.15.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-24-à-09.12.15.png)

Désormais, votre espace de travail est fin prêt.


Nous en avons fini! Vous êtes prêt à devenir expert dans les systèmes embarqué !
