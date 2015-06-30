title: GPIO (General Purpose I/O) Programmation et interface
date: 2015-02-17
description: GPIO pour General Purpose Input Output désigne tout simplement les entrées-sorties d'un micro-contrôleur, micro-processeur, etc. C'est ce qui permet de passer du monde extérieur au monde binaire. A travers la puce ARM tiva-c de ti, je vous exposerai les élements les plus imortants des GPIO à savoir, les bus (APB (Advanced Bus périphérique) et AHB (Advanced High-Performance Bus)), l'adresse, les pins, les registes (Direction et Data Registers), l'horloge, pin multiplexing, etc.    
categories:
- Embedded
tags:
- Advanced Bus périphérique
- Advanced High-Performance
- Direction et Data Registers
- GPIO
- GPIO Clock enable for all the I/O
- IO
- offset
- pin multiplexing
- special function register
- Special Purpose IO

** Table des matières **

[TOC]

## Aperçu

Comment leurs noms l'indiquent, les GPIO servent d'entrées/sortie pour les microprocesseur, il existe deux type :

1. **General Purpose I/O (GPIO):** ils sont utiliser pour interfacer les périphériques, tels que, les LEDs, les switches, le LCD, et bien plus.

2. **Special purpose I/O:** ils sont conçus pour des fonctions spécifiques, tels que, ADC (Analog-to-Digital), Timer, UART (universal asynchronous receiver transmitter), etc,.




## Example : I/O Pins in TI Tiva LaunchPad

La puce ARM utilisé dans TI Tiva LaunchPad est Tiva série C TM4C123GH6PM dispose des ports A, B, C, D, E et F. Les broches sont désignés comme ceci : PA0-PA7, PB0-PB7, PC0-PC7, PD0-PD7, PE0-PE5 et PF0-PF4. Voir Figure suivante :

[![00006](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00006.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00006.jpeg)

Remarquez que les ports PE et PF ne dispose de 8 broches et les PC0-PC3 sont utilisés pour les connexions JTAG au débogeur sur le LaunchPad.


## Les bus APB et AHB

Les puces ARM ont deux bus: APB (Advanced Bus périphérique) et AHB (Advanced High-Performance Bus). Le bus AHB est beaucoup plus rapide que l'APB. Le AHB permet d'accéder d'un seul cycle d'horloge au  périphériques. L'APB est plus lent et son temps d'accès minimum est de deux cycles d'horloge.

Les adresses des ports d'E/S affectés à l'AP-PF pour APB sont les suivantes:

* GPIO Port A (APB): 0x4000.4000	
* GPIO Port B (APB): 0x4000.5000
* GPIO Port C (APB): 0x4000.6000
* GPIO Port D (APB): 0x4000.7000
* GPIO Port E (APB): 0x4002.4000
* GPIO Port F (APB): 0x4002.5000 (ce port est connecté à la LED et SW sur TI Tiva LaunchPad)


Les adresses des ports d'E/S affectés à l'AP-PF pour AHB sont les suivantes:

* GPIO Port A (AHB): 0x4005.8000
* GPIO Port B (AHB): 0x4005.9000
* GPIO Port C (AHB): 0x4005.A000
* GPIO Port D (AHB): 0x4005.B000
* GPIO Port E (AHB): 0x4005.C000
* GPIO Port F (AHB): 0x4005.D000




### Direction et Data Registers (registres de données)


En général, chaque microcontrôleur dispose d'au moins deux registres associés à chacun des ports d'E/S. Ils sont les registres de données et de direction.

Le registre de direction est utilisé pour faire en sorte que la broche soit une entrée ou une sortie. Le registre de données permet soit de lire (lorsque la broche est configuré en entrée) ou d'écrire (lorsque la broche est configuré en entrée). Voir Figure suivante :

[![00007](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00007.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00007.jpeg)




#### Data Register (GPIODATA) dans TI ARM

Le registre de données GPIO (GPIODATA) est situé à l'offset 0x0000 à l'adresse de base de ce port. Ceci est illustré ci-dessous.

[![00008](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00008.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00008.jpeg)


#### Bit-Banding


_Rappel : le bit-banding permet l'écrire sur un registre en un seul cycle d'horloge._

Parce le registre GPIODATA supporte le bit-banding, il occupe 256 mots (offset 0x000 - 0x3FC). Pour être capable d'écrire tous les 8 bits du registre de données GPIO à la fois, il faut utiliser l'offset 0x3FC.


##### Bit-banding de cas d'étude (Pour les experts seulement)

Pourquoi faudrait-il  256 mots (1024 octets) pour le GPIODATA ?

Comme le montre la figure ci-dessous, afin de rendre le mot adresses alignées, les bits 1 et 0 sont toujours à 0.

En utilisant les bits 2-9 de l'adresse, montre les bits qui doivent être changés lors de l'écriture dans le registre de GPIODATA.

Par exemple, pour écrire à l'adresse la valeur 0x34 (0000110100 en binaire) signifiant que les broches 0, 2 et 4 du port doivent être changés tandis que les autres broches restent inchangés.

Pour changer toutes les broches du port, tous les masques de bits (bits 2-9) doit être réglée. Cela rend l'adresse de décalage de 0x3FC (001 111 111 100 en binaire).

[![00009](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00009.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00009.jpeg)



### Direction registrer dans le TI ARM

Dans le cas des puces TI ARM, chaque bit du registre de direction doit être mis à 0 pour configurer la broche en entrée et à 1 pour configurer la broche en sortie. L'adresse du registre de Direction GPIO est situé à l'adresse de décalage de 0x400 à l'adresse de base de ce port. Ceci est illustré ci-dessous.

[![00011](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00011.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00011.jpeg)


#### Example pratique
Trouver l'adresse physique de la GPIODATA et GPIODIR enregistre pour PORTF si l'adresse de base de la PORTF est 0x40025000.

solution :

L'emplacement de l'adresse physique de l'GPIODATA pour PORTF commence à 0x40025000 :

0x40025000 + 000 = 0x40025000

Pour être capable d'écrire à tous les 8 bits du registre de données à la fois, vous devez utiliser :

0x40025000 + 0x3FC = 0x400253FC.

L'emplacement de l'adresse physique de GPIODIR pour la PORTF est

0x40025000+0x400=0x40025400

Pour accéder aux I/Ode la puce ARM TM4C123GH6PM utilisés dans LaunchPad, nous devons examiner deux autres registres. Ils sont les GPIODEN et RCGCGPIO.


### le GPIO Digital Enable Register
Chaque broche de la puce ARM TI peut avoir plusieurs fonctions. Nous choisissons la fonction en programmant un registre de fonction spéciale (SFR).

L'utilisant d'une seule broche pour de multiples fonctions est appelé multiplexage de broches (***pin multiplexing***) et est largement utilisé par les microcontrôleurs.

En l'absence du multiplexage de broches, un microcontrôleur aura besoin de plusieurs centaines de broches pour soutenir toutes ses fonctions. Par exemple, une broche peut être utilisé comme entrée analogique, numérique, etc. Bien sûr, pas tous en même temps.

Le GPIODEN (Activer numérique) _special function register_ permet d'activer la broche pour être utilisé comme I/O numérique à la place de la fonction analogique. Chaque port (de A-F) a son propre registre de GPIODEN. Ceci est illustré ci-dessous.

[![00012](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00012.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00012.jpeg)

Comme on peut le voir l'offset de ce registre est 0x51C

L'horloge


### Le GPIO Clock enable for all the I/O ports

Le RCGCGPIO est utilisé pour activer la source d'horloge pour les entrées/sorties. Si un port I/O n'est pas utilisé, la source d'horloge pour elle peut être désactivée pour **économiser de l'énergie**.

Il ya seulement une special function register RCGCGPIO pour tous les ports et chaque bit de ce registre est utilisé pour activer la source d'horloge à l'un des ports.

Dans le cas des TI TM4C123GH6PM puisque nous avons seulement ports A à F, les inférieurs 6 bits de ce registre sont utilisés. Les bits de registre sont présentés ci-dessous.

[![00013](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00013.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00013.jpeg)

L'adresse de base du registre spécial RCGCGPIO est 0x400F.E000 et son offset est 0x608; par conséquent, l'adresse physique est 0x400FE000 + 0x608 = 0x400FE608.


#### Exemple :


Montrer comment activer l'horloge du PORTF et  activer la fonction Digital des broches des port PORTF1, PORTF2 et PORTF3.

solution:

a) Pour activer la source d'horloge pour PORTF nous devons fixer à 1 la bit 5 du registre RCGCGPIO (écrire la valuer 0x20).
b) Nous devons écrire la valeur 0b00001110 = 0x0E à PORTFDEN registre situé à l'adresse 0x4002551C




