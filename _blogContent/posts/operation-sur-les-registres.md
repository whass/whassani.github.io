title: "Micro-Contrôleur : Opération sur les registres (accès, écriture et lecture)" 
date: 2015-01-22
description: L'aspect fondamental de la programmation des micri-contrôleur est la confifguration des registres. Quoique vous fassiez, congigurer une entrée, une sortie, vitesse de transmission, .... vous devez passer par les registres associé. Ici je vous montre les méthodes utilisé pour cela. 
categories: 
- Embedded

**Table des matière**

[TOC]

Dans l'embarqué, lorsqu'on manipule les registres, tout est une question de mise à 0 ou 1 des bits de ce dernier. On peut distinguer principalement 2 cas : (1) mettre un seul bit donné du registre à 0 ou 1, (2) mettre un ensemble de bits à 0 ou 1.

Dans ce quit suit je vous montrerai comment faire.


## Accès aux registres

Pour accéder à un registre il faut connaitre son adresse mémoire et savoir manipuler les pointeurs.

Example :

Supposons que notre registre est situé à l'adresse mémoire (0x40025400), pour pouvoir y accéder, il suffit de définir une macro comme ceci :
    
    #define NomDuRegistre (*((volatile unsigned long *)0x40025400))

Bien évidemment ce n'est pas la seule méthode, on s'arrêtera à celle-ci.

## Ecrire sur un registre

Si nous reprenons l'example précédent, pour écrire une valeur sur un registre, faites comme ceci :
    
    #define NomDuRegistre (*((volatile unsigned long *)0x40025400))
    .
    .
    .
    NomDuRegistre = Valeur;

## Lire sur un registre

Si nous reprenons l'example précédent, pour écrire une valeur sur un registre, faites comme ceci :

    
    #define NomDuRegistre (*((volatile unsigned long *)0x40025400))
    .
    .
    .
    Valeur = NomDuRegistre;



## Manipulation des bits des registres


Dans la majorité des situations vous serez amener à ne manipuler qu'un bit sur un registre donné. Nous verrons dans ce qui suit, la manière avec laquelle il est possible de manipuler les registres directement en utilisant certaines fonctionnalités du langage C.

### Mettre un seul bit à 0


Soit un registre REG = 0101 0111. Supposons que l'on veuille mettre le 4 ème bit de ce registre à 0.

    
    REG = 0101 0111
    REG &= ~(1<<4); (variante : REG &= 0xEF);)

Résultat :
    
    REG = 0100 0111


Explication :

1. la valeur 1 est décalé 4 fois, on obtient 0001 0000
2. En complémentant à 1 (0 devient 1 et 1 devient 0) la valeur obtenu, on obtient 1110 1111
3. En utilisant un ET logique (0101 0111 & 1110 1111 = 0100 0111)
 

### Mettre un seul bit à 1

Soit un registre REG = 0100 0111. Supposons que l'on veuille mettre le 4 ème bit de ce registre à 1

    
    REG = 0100 0111
    REG |= (1<<4); (variante : REG |= 0x10;)

Résultat :

    REG = 0101 0111


Explication :
1. la valeur 1 est décalé 4 fois, on obtient 0001 0000
2. En utilisant un OU logique, on a : (0100 0111 | 0001 0000 = 0101 0111)


### Isoler la valeur d'un seul bit


Soit un registre REG = 0100 0111. Supposons que l'on veuille récupérer la valeur du 4 ème bit de ce registre

    
    REG = 0101 0111
    data = REG & (1<<4); 

Résultat :

    REG = 0001 0000

Explication :

1. la valeur 1 est décalé 4 fois, on obtient 0001 0000
2. En utilisant un ET logique, on a : (0101 0111 & 0001 0000 = 0001 0000)


Comme on peut le constater, il est très facile de travailler sur les registres.

**NB** l'article suppose que le CPU travaille dans des coditions idéales. En effet, certains problèmes peuvent survenir (Voir l'article sur "le bit danding") pour plus de détails. 