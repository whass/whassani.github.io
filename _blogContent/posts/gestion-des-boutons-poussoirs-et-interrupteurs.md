title: Travailler avec des boutons poussoirs et interrupteurs
date: 2015-02-19
description: Les bouttons poussoirs et les interrupteurs sont des éléments avec lesquels vous travaillerai en permancen si vous travaillez dans l'embarqué. Dans cet article, à travers la ARM tiva-c de TI, je vous expose la procédure complète pour travailler avec ces éléments. La procédure reste valable pour la majorité des micro-contrôleurs.
categories: 
- Embedded
tags:
- GPIOPUR
- Pull-Up Resistor

Un bouton poussoir peut être soit enfoncé soit relâché? Son usage normal, fait que lorsqu'on l'enfonce c'est pour déclencher une action !

La carte Tiva C Launchpad contient 3 boutons poussoirs.

	
  1. Un utilisé pour le reset du microcontrôleur

	
  2. Un désigné par SW1 et connecté au pin port PF0 (Port F pin 0)

	
  3. Un désigné par SW2 et connecté au pin port PF4 (Port F pin 4)


[![00015](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00015.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00015.jpeg)



Indication de la schématique, il n'y a pas de résistance de résistance de rappel [(Pull-Up)](http://www.embarquez-vous.fr/?p=511) à SW1 ou SW2. Les broches PF0 PF4 et sont reliés à bouton-poussoir SW1 et SW2 directement (En fait, ils sont reliés par des résistances de zéro ohm de sorte qu'ils peuvent être enlevés si d'autres fonctions de ces deux broches sont souhaitées).

Pour utiliser le SW1 et SW2 nous devons permettre à la résistance de pull-up interne à PF0 et PF4 d'être utilisée.

Le tableau suivant montre le registre pour la PUR (Pull-Up Resistor).

[![00016](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00016.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00016.jpeg)

L'offset du registre GPIOPUR est l'adresse 0x510, ainsi sont adresse physique par rapport au port F est :


    0x40025000+0x510=0x40025510


## Procédure


Pour lire SW1 et l'afficher dans la LED verte, les étapes suivantes sont nécessaire.

	
  1. activer l'horloge du PORTF

	
  2. Mettre dans le registre de direction PF4 comme entrée et PF3 comme sortie

	
  3. mettre le PORTF en sortie numériques

	
  4. activer l'option PUR pour ces sorties

	
  5. lire sw1 sur le PORTF

	
  6. inverser sa valeur (pour mettre à 1)

	
  7. activer la LED verte

	
  8. répéter les opérations 5 à 7


```    
/*  p2_7.c: Read a switch and write it to the LED */

/*  This program reads SW1 of Tiva LaunchPad and writes the inverse of the value to the green LED. SW1 is low when pressed (Normally High). LED is on when high. */

#include "TM4C123GH6PM.h"

int main(void)
{
    unsigned int value;
    SYSCTL->RCGCGPIO |= 0x20;   /* activer l'horloge GPIOF */
    GPIOF->DIR = 0x08;          /* mettre PORTF3 pin comme sortie (LED) pin */
                                /* et PORTF4 comme entrée, SW1 sur le PORTF4 */
    GPIOF->DEN = 0x18;          /* mettre PORTF pins 4-3 comme des pin numériques */
    GPIOF->PUR = 0x10;          /* activer la résistance Pull-Up pour le pin 4 */
    while(1)
    {
        value = GPIOF->DATA;    /* lire les données du PORTF */
        value = ~value;         /* switch is low active; LED is high active */
        value = value >> 1;     /* shift it right to display on green LED */
        GPIOF->DATA = value;     /* put it on the green LED */
    }
}
/* This function is called by the startup assembly code to perform system specific initialization tasks. */
void SystemInit(void)
{
    /* Grant coprocessor access */
    /* This is required since TM4C123G has a floating point coprocessor */
    SCB->CPACR |= 0x00F00000;
}
```