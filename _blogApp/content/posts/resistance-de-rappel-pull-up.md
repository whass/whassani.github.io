title: Résistance de rappel (Pull-Up)
date: 2015-02-19
description: Admettons que vous ayez une des broches de votre processeur est configurée comme entrée. Supposons que cette dernière est en l'air (rien n'est relié à la broche) et que votre programme lit l'état de la broche, quelle est la valeur qui sera lue ?. 0 me diriez-vous, y a rien, détrompez vous ce n'est pas forcémment le cas. Petite indice (tension flottante).
categories: 
- Embedded
tags:
- électronique
- Pull-Up
- résistance de rappel

** Table des matières **

[TOC]

[![Pull_Up_Resistor_Circuit](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/Pull_Up_Resistor_Circuit.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/Pull_Up_Resistor_Circuit.png)

Les Résistances de rappels  (Pull-Up en anglais) sont très fréquentes lors de l'utilisation des microcontrôleurs (MCU) ou ne importe quel appareil utilisant les circuits logiques.

Ce tutoriel vous expliquera quand et où utiliser des résistances pull-up, puis nous ferons un calcul simple pour montrer pourquoi pull-ups sont importantes.


## Qu'est-ce qu'une résistance de pull-up

Admettons que vous ayez une des broches de votre processeur est configurée comme entrée. Supposons que cette dernière est en l'air (rien n'est relié à la broche) et que votre programme lit l'état de la broche, quelle est la valeur qui sera lue ?

1. état haut (tiré à VCC)
2. ou état bas (tiré à la terre)?

C'est difficile à dire. Ce phénomène est appelé ***tension flottante***. Pour éviter cet état inconnu, on utilise soit un ***pull-up*** (résistance de rappel) ou un ***pull-down*** (résistance d'excursion) qui feront en sorte que la broche est en soit un état haut ou bas, tout en utilisant une faible quantité de courant.

Pour simplifier, nous nous concentrerons sur les pull-ups, car ils sont plus fréquents. Ils opèrent en utilisant les mêmes concepts, en effet, la résistance de pull-up est connectée à l'état haut (ce qui est généralement de 3,3 V ou 5V et est souvent arbitré comme VCC) et la résistance d'excursion basse est connecté à la masse.

***N.B :*** Pull-ups sont souvent utilisés avec les boutons et commutateurs.

[![Switch_Pull_Up_Circuit](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/Switch_Pull_Up_Circuit.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/Switch_Pull_Up_Circuit.png)

Avec un pull-up :

* la broche d'entrée lira un état haut lorsque le bouton n'est pas enfoncé. En d'autres termes, une petite quantité de courant circule entre +Vcc et la broche d'entrée (non à la masse), la lecture d'un état haut (proche de +V). 

* Lorsque le bouton est pressé, la broche d'entrée est directement connectée à la masse. Le courant circule à travers la résistance à la masse, donc la broche d'entrée indique un état bas.


## Alors, que résistance valeur devriez-vous choisir?

La réponse est courte et facile, elle est de l'ordre de 10k et doit être choisie pour satisfaire à deux conditions :

1. Lorsque le bouton est enfoncé, la broche d'entrée est tirée vers le bas. La valeur de la résistance de tirage (Rtirage) contrôle la quantité de courant.

2. Lorsque le bouton n'est pas enfoncé, la broche d'entrée est tirée vers le haut. La valeur de la résistance de pull-up commande la tension sur la broche d'entrée.

***En règle générale***, pour lire la valeur correcte à l'état 2 (Bouton n'est pas enfoncé), il suffit d'utiliser une résistance de rappel (Rtirage) d'environ (1 / 10ème) inférieure à l'impédance d'entrée (R2) de la broche d'entrée.

* ***N.B 1:*** Si vous utilisez une résistance 1MΩ pour la R1 de pull-up et que l'impédance de la broche d'entrée R2 est de l'ordre de 1MΩ (formant un diviseur de tension), la tension sur la broche d'entrée va être environ la moitié de VCC, et le microcontrôleur pourrait ne pas lire l'état bas, comme attendu mais l'état haut (voir normes TTL et CMOS).

* ***N.B 1:*** Une autre chose à souligner, dans certains cas le Pull-Up peut ralentir les variation des niveaux des broche dans le cas des des variations très rapide. 
En effet, le système qui alimente la broche d'entrée est essentiellement un condensateur couplé à la résistance de pull-up, formant ainsi un filtre RC, et les filtres RC prennent un certain temps pour charger et décharger. Si vous avez un signal qui change très rapidement (comme les clés USB), une résistance de pull-up de haute valeur peut limiter la vitesse à laquelle la broche peut changer d'état de façon fiable. C'est pourquoi vous verrez souvent des résistance faibles (de l'ordre de 1k à 4.7KΩ) dans les lignes de signaux USB.


## Le calcul d'une valeur de résistance Pull-up

[![pull](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/pull.jpg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/pull.jpg)

Disons que vous voulez limiter le courant à environ 1 mA lorsque le bouton est enfoncé dans le circuit ci-dessus, où Vcc = 5V. Quelle valeur résistance devriez-vous utiliser?

Il est facile de montrer comment calculer la résistance pull-up en utilisant la loi d'Ohm:

`V=R.I`


Se référant au schéma ci-dessus, la loi d'Ohm est maintenant:


`Vcc = (courant qui traverse R1) . R1`


Ainsi :


`R1 = Vcc/(courant qui traverse R1)`


Sachant que la valeur souhaitée de (courant qui traverse R1) est 0.001 alors :


` R1 = 5 / 0.001 = 5kOhms `


N'oubliez pas de convertir toutes vos unités en volts, ampères et ohms avant de calculer (par exemple 1mA = 0,001 ampères). La solution consiste à utiliser une résistance 5kΩ.