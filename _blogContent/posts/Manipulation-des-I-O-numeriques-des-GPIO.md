title: Manipulation des I/O numériques des GPIO
date: 2015-01-24
description: Cet article vous montre à travers un exemple pratique consistant à allumer une des LED de la carte ARM tiva-c. Quoique simple, cet exemple  regroupe tout les concepts fondamentaux pour manipuler les GPIO, ç savoir, la configuration, l'accès aux registres, lecture et écriture, etc. 
categories: 
- Embedded


Dans ce qui suit, j'aborderai avec vous, à travers un exemple très simple, un concept fondamental dans les systèmes embarqués, à savoir la manipulation des GPIO !

Les GPIO pour General Purpose Input Output, sont l'ensemble des entrées/sorties numériques permettant de communiquer avec le monde extérieur.

Dans ce qui suit, je vous apprendrez à :

* Manipuler les registres
* Configurer les registres
* Accéder aux GPIO
* Lire et écrire les GPIO
* Identifier les pins sur une carte et leurs registres sur le micro-contrôleur.


### Pré-requis

Dans ce qui suit, je supposerai que :
	
  * vous avez déjà installé et configuré
	
    * CCS V6 (Code Composer Studio) sur votre machine Ubuntu ou Windows
	
    * TivaWare
	
  * Possédez une carte Tiva C Séries TM4C123G LaunchPad Evaluation Kit EK-TM4C123GXL.
	
  * Vous savez comment écrire sur un registre.



### Méthodologie


La méthode est relativement simple, pour manipuler les GPIO il suffit de :

1. Activer le port sur le lequel le GPIO est relié	

2. Configurer ce port

3. écrire et lire sur ce port.

## Example pratique : Faire clignoter une LED

Nous souhaitons allumer et éteindre la LED rouge de notre carte.

La figure ci-après illustre l'ensemble des entrées/sorties dont dispose le micro-contrôleur de notre carte de développement.

[![port-cortex-m4](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/port-cortex-m4.gif)](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/port-cortex-m4.gif)

Nous devons chercher parmi toutes ces entrées/sorties, laquelle correspondant à la LED rouge. Un seul moyen de le savoir, le schéma de la carte. J'ai fait un screenshot de la partie qui nous intéresse

[![Capture d’écran 2015-01-28 à 07.42.31](http://www.embarquez-vous.fr/wp-content/uploads/2015/01/Capture-d’écran-2015-01-28-à-07.42.31.png)](http://ec2-54-175-20-183.compute-1.amazonaws.com/wp-content/uploads/2015/01/Capture-d’écran-2015-01-28-à-07.42.31.png)

L'ensemble du schéma est disponible en téléchargement libre à l'adresse suivante :

http://www.ti.com/lit/ug/spmu296/spmu296.pdf


Conclusion, la LED rouge est connectée à PF1, qui correspond au deuxième bit du port F.
	
1. Identifier le pin sur la carte : LED_R

2. Identifier le port sur le lequel le pin est relié (port F), ainsi que :

  * l'adresse mémoire du registre de contrôle des ports (0x400FE608).

  * Activer le port (mettre le bit numéro 5 du registre de contrôle à l'état haut)

3. Identifier les registres de contrôles du port

  1. Les adresse mémoires des registres de contrôle (0x40025400, 0x4002551C)
     
    * définir la direction (registre : 0x40025400, mettre le bit numéro 2 à l'état haut)

	
    * activer la sortie numérique (registre : 0x4002551C, mettre le bit numéro 2 à l'état haut)

	
    * D'autres registres peuvent être configuré, mais ces deux sont largement suffisant pour lire et écrire un GPIO

4. Identifier le registre de données du port
	
  * l'adresse mémoire du registre de données (0x400253FC)
	
  * le bit du registre de données qui agit sur le pin (le deuxième bit)

5. écrire sur la sortie en agissante sur le registre de donnée (mettre le bit numéro 2 à l'état haut ou bas)





### Code source


```    
  #define RegistreDonnees (*((volatile unsigned long *)0x400253FC))
  #define RegistreDirection (*((volatile unsigned long *)0x40025400))
  #define RegistreActivationSortieNumerique (*((volatile unsigned long *)0x4002551C))
  #define RegistreControleGPIO (*((volatile unsigned long *)0x400FE608))
    
  int main(void)
  {
    RegistreControleGPIO = 0x00000020; // activer le PORT F GPIO
    RegistreDirection |= (1<<1); // mettre la sortie 2 du port F en sortie
    RegistreActivationSortieNumerique |= (1<<1); // mettre la sortie 2 du port F en numérique
    
    while(1)
    {
      RegistreDonnees |= (1<<1); // mettre la sortie 2 du port F à l'état haut - allumer la LED-
      RegistreDonnees &= ~(1<<1); // mettre la sortie 2 du port F à l'état bas - éteindre la LED 
    }
  }
    
```

Félicitations vous avez configurer votre premier I/O from scratch
