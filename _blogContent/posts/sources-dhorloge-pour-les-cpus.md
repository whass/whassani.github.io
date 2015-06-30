title: Sources d'horloges pour les CPUs
date: 2015-02-19
categories:
- Embedded
tags:
- PLL
- RC
- XTAL

De nombreux microcontrôleurs possèdent au moins trois sources d'horloge.



	
  1. L'oscillateur RC (résistance et capacité). Ce est la source d'horloge la moins précise pour la CPU. Mais il ne nécessite pas d'oscillateur externe.

	
  2. L'oscillateur externe en cristal (XTAL). Il est plus précis mais à des fréquences élevées (100 MHz par exemple), les cristaux sont chers.

	
  3. PLL (boucle à verrouillage de phase). Un compromis entre précision et économie , il utilise un quartz basse fréquence peu couteux et un circuit PLL pour générer une source d'horloge à haute fréquence pour le CPU. Cette option est largement utilisée pour les systèmes à la fréquence du processeur de plus de 20 MHz. Un autre avantage de l'utilisation de la boucle PLL est que la fréquence d'horloge est programmable. Ainsi, vous pouvez la possibilité d'élever la fréquence pour des tâches intensives et de ralentir l'horloge pour économiser l'énergie.


example

TI Tiva LaunchPad est relié à un oscillateur 16MHz XTAL et une PLL pour programmer sa fréquence d'horloge. La puce TM4C123GH6PM sur TI Tiva LaunchPad dispose également d'un circuit RC à 16MHz sur puce (horloge par défaut).
