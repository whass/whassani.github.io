title: Applications en Bare-Metal (sans OS) sur la Beagle Bone Board
date: 2015-02-22
description: Mise en place d'applications embarqués sans os sur la BeagleBone Black équipé d'un processeur ARM-A7. Utilisation de StarterWare de TI et de la chaine de compilation croisée pour ARM (linaro-gcc)
categories: 
- Linux
- Embedded
tags:
- arm
- beaglebone
- compilation croisée
- cross-compile
- GCC
- linaro
- linux
- Patch
- sitara
- TFTP

** Table des matières **

[TOC]

Dans ce qui suit, je vais vous montrer comment mettre en place des applications en Bare-Metal (i.e., sans OS) sur la BeagleBone Black équipé d'un processeur ARM-A7.


## Installer StarterWare


Téléchargez StarterWare du site de Texas Instrument directement via le lien ci-après :
    
[http://software-dl-1.ti.com/dsps/forms/self_cert_export.html?prod_no=AM335X_StarterWare_02_00_01_01_Setup.bin&ref_url=http://software-dl.ti.com/dsps/dsps_public_sw/am_bu/starterware/latest/](http://software-dl-1.ti.com/dsps/forms/self_cert_export.html?prod_no=AM335X_StarterWare_02_00_01_01_Setup.bin&ref_url=http://software-dl.ti.com/dsps/dsps_public_sw/am_bu/starterware/latest/) 


Rendez le binaire téléchargé exécutable comme ceci :

    
    $ chmod +x AM335X_StarterWare_02_00_01_01_Setup.bin


Exécutez-le, ensuite il vous sera demandé de choisir l'emplacement de l'installation. Choisissons _ti-env_, ainsi StarterWare sera dans cet emplacement :

    
    $ ~/ti-env/AM335X_StarterWare_02_00_01_01/


Télécharger le Patch pour la BeagleBone Black via le même lien que celui de StarterWare via le lien ci-après :


[href="http://software-dl.ti.com/dsps/dsps_public_sw/am_bu/starterware/latest/exports/StarterWare_BBB_support.tar.gz">http://software-dl.ti.com/dsps/dsps_public_sw/am_bu/starterware/latest/exports/StarterWare_BBB_support.tar.gz](href="http://software-dl.ti.com/dsps/dsps_public_sw/am_bu/starterware/latest/exports/StarterWare_BBB_support.tar.gz">http://software-dl.ti.com/dsps/dsps_public_sw/am_bu/starterware/latest/exports/StarterWare_BBB_support.tar.gz) 

Pour le patcher, rien de plus simple :

* 1-Décompressez l'archive

    
    StarterWare_BBB_support.tar.gz


2- Et copiez le contenu dans le dossier

    
    ~/ti-env/AM335X_StarterWare_02_00_01_01


3- Cliquez sur merge pour ne remplacer que les fichiers du patch BBB dans StarterWare




## Installer la chaîne de compilation croisée pour ARM


Télécharger l'archive de linaro-gcc pour linux via :

[https://launchpad.net/gcc-arm-embedded/4.7/4.7-2012-q4-major](https://launchpad.net/gcc-arm-embedded/4.7/4.7-2012-q4-major)



Créez un dossier dans lequel l'archive sera enregistrée

$ mkdir ~/ti-env/linaro-gcc

Décompressez l'archive et sauvegardez-là dans le dossier linaro-gcc (libre de vous de choisir un autre).

Créez un variable d'environnement dans laquelle vous sauvegarderez le chemin vers le compilateur linaro-gcc comme ceci :

    $ export LIB_PATH=${HOME}/ti-env/linaro-gcc/gcc-arm-none-eabi-4_7-2012q4


## Configuration de StarterWare pour Linaro-gcc


Pour cela, vous devez d'abord indiquer l'emplacement du compilateur pour ARM à StarterWare, pour cela éditez le fichier _makedefs_ comme ceci :

    $ nano ~/ti-env/AM335X_StarterWare_02_00_01_01/build/armv7a/gcc/makedefs

Modifier :

    
    ifndef PREFIX
       PREFIX=arm-none-eabi-
    endif


Par :

    
    ifndef PREFIX
       PREFIX=${LIB_PATH}/bin/arm-none-eabi-
    endif





## Compilez les applications (exemple de l'UART)


Mettez-vous sur le dossier de BeagleBone Black comme ceci :

    
    $ cd ~/ti-env/AM335X_StarterWare_02_00_01_01/armv7a/gcc/am335x/beaglebone


ensuite compilez les projets déjà existants dans StarterWare (gpio, uart, ....) comme ceci :

    
    $ make


Vérifiez que la compilation s'est bien passée dans le dossier suivant :

    
    $ cd ~/ti-env/AM335X_StarterWare_02_00_01_01/binary</span>/armv7a/gcc/am335x/beaglebone


Les dossiers que vous devrez voir dans le cas de l'UART sont :

    
    $ cd uart/Release
    $ ls -Al
     total 100
    -rwxrwxr-x 1 parallels parallels 8488 févr. 24 20:54 uartEcho.bin
    -rwxrwxr-x 1 parallels parallels 105879 févr. 24 20:54 uartEcho.out
    -rw-rw-r-- 1 parallels parallels 8496 févr. 24 20:54 uartEcho_ti.bin


Précautions : 

1- Vérifier que la variable d'environnement existe et qu'elle correspond bien à l'emplacement du compilateur

    
    $ printenv LIB_PATH


Dans notre cas on devra avoir le dossier :
    
    $ ~/tiv-env/ti-env/linaro-gcc/gcc-arm-none-eabi-4_7-2012q4

2- Que vous avez bien modifier le fichier makedefs comme illustré dans (Configuration de StarterWare pour Linaro-gcc)




## Charger les applications via U-Boot

Dans cette partie, nous verrons configurer U-Boot pour charger soit, votre noyau Linux avec son système de fichiers, ou le chargement d'une application en metal bar via TFTP.