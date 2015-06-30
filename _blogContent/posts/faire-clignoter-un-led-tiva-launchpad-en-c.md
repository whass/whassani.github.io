date: 2015-02-17
title: Faire Clignoter un LED - TIVA Launchpad en "C"
categories: 
- Embedded


## Pré-requis


Je vous conseil de revoir ces articles pour bien démarrer

[ GPIO (General Purpose I/O) Programmation et interface](http://www.embarquez-vous.fr/?p=424)

[Autours des GPIO, manipulation des I/O numériques](http://www.embarquez-vous.fr/?p=199)


## Méthode


Pour fair clignoter les LED RVB de la TI Tiva LaunchPad, les étapes suivantes doivent être suivies.



	
  1. Activer l'horloge pour le PORTF,

	
  2. définir les directions en mettant les bits de registre de direction de 1, 2 et 3 du PORTF en sortie,

	
  3. activer la fonction E/S numériques de PORTF,

	
  4. Mettre les sorties à l'état HAUT,

	
  5. appeler un retard,

	
  6. Mettre les sorties à l'état LOW,

	
  7. appeler un retard,

	
  8. Répétez les étapes 4-7.




##  Code



    
    /* Faire Clignoter les LED en C par accès aux registre via leurs adresses */
    /* Ce programme permet de faire clignoter les trois LED chaque 0,5 .*/
    /*PF1 - LED rouge
      PF2 - LED bleu
      PF3 - LED verte
      Elles sont active à l'état haut ('1' allume la LED).*/
    /* PORTF data register */
    #define PORTFDAT (*((volatile unsigned int*)0x400253FC))
    /* PORTF data direction register */
    #define PORTFDIR (*((volatile unsigned int*)0x40025400))
    /* PORTF digital enable register */
    #define PORTFDEN (*((volatile unsigned int*)0x4002551C))
    /* run mode clock gating register */
    #define RCGCGPIO (*((volatile unsigned int*)0x400FE608))
    /* coprocessor access control register */
    #define SCB_CPAC (*((volatile unsigned int*)0xE000ED88))
    void delayMs(int n);     /* function prototype pour le retard */
    int main(void)
    {
        /* activer l'horloge pour GPIOF au clock gating register */
        RCGCGPIO |= 0x20;
        /* mettre les pins 3-1 du PORTF en sortie */
        PORTFDIR = 0x0E;
        /* mettre les pins 3-1 du PORTF en numérique */
        PORTFDEN = 0x0E;
        while(1)
        {
            /* écrire sur le PORTF pour allumer toute les LEDs */
            PORTFDAT = 0x0E;
            delayMs(500);
            /* écrire sur le PORTF pour éteindre toute les LEDs */
            PORTFDAT = 0;
            delayMs(500);
        }
    }
    /* retard de n millisecondes (16 MHz CPU clock) */
    void delayMs(int n)
    {
        int i, j;
        for(i = 0 ; i < n; i++)
            for(j = 0; j < 3180; j++)
                {}  /* do nothing for 1 ms */
    }
    /* Cette fonction est appelée par le code assembleur de démarrage pour effectuer des tâches spécifiques d'initialisation du système. */
    void SystemInit(void)
    {
        /* Accorder l'accès du coprocesseur*/
        /* Ceci est requis car TM4C123G a un coprocessor à point flottant */
        SCB_CPAC |= 0x00F00000;
    }
