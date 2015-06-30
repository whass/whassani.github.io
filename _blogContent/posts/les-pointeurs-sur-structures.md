title: les pointeurs sur structures
date: 2015-02-17
categories:
- Embedded
tags:
- C

L'utilisation de pointeurs sur structures est très courante en C. Voici un exemple d'utilisation d'un pointeur sur un complexe :

    
    complexe a = { 3.5, -5.12 };
    complexe * p = &a;
    (*p).reel = 1;
    (*p).imag = -1;
    /* a vaut (1 - i) */


Nous avons été obligé de mettre des parenthèses autour de `*p` car l'opérateur `.` est plus prioritaire que l'opérateur `*` . Cela rend difficile la lecture d'un tel programme. Heureusement, l'utilisation de pointeurs sur structures est si courante que le C définit l'opérateur `->` pour accéder aux champs d'une structure via un pointeur. Les deux expressions suivantes sont donc équivalentes :

    
    (*pointeur).champ
    pointeur->champ


Ainsi l'exemple précédent s'écrit beaucoup plus facilement de la manière suivante :

    
    complexe a = { 3.5, -5.12 };
    complexe * p = &a;
    p->reel = 1;
    p->imag = -1;
    /* a vaut (1 - i) */
