title: "Programmation des ports séries UART - Tiva C"
date: 2015-02-19
categories:
- Embedded
tags:
- ClkDiv
- FIFO
- High Speed enable
- HSE
- JTAG
- Port Control Register
- RCGCUART
- Receive enable
- RXE
- Transmit Enable
- TXE
- UART
- UART enable
- UART fractionnal Baud-Rate Divisor
- UART Inger Baud-Rate Divisor
- UARTEN
- UARTRCR
- UARTRSR
- USB


Dans ce qui suit, nous examinons les registres UART du port série de TI ARM Tiva TM4C123GH6PM et montrons comment les programmer pour transmettre et recevoir des données en série. Beaucoup de puces TI ARM disposent jusqu'à huit ports UART. Ils sont désignés par UART0-UART7. Dans le LaunchPad TI, le port de la UART0 TM4C123GH6PM est reliée au ICDI (In-Circuit d'interface de débogage), qui est relié à un connecteur USB. Le ICDI USB se trouve sur la droite du commutateur et est étiqueté comme Debug. Voir Figure la figure ci-après.

[![00040](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00040.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00040.jpeg)

Cette connexion ICDI USB contient trois fonctions distinctes :



	
  1. la programmation (téléchargement) en utilisant le logiciel de programmation LM Flash

	
  2. le débogage en utilisant JTAG, et

	
  3. l'utilisation en tant que port de communication virtuel.


Lorsque le câble USB relie le Tiva LaunchPad, le pilote du périphérique de l'ordinateur hôte établit une connexion virtuelle entre le PC et l'UART0 de la carte. Sur le LaunchPad, la connexion apparaît comme UART0. Sur le PC hôte, il apparaît comme un port COM. Ce est ce qu'on appelle une connexion virtuelle.

Sur le datasheet du TM4C123GH6PM, nous voyons que le UART0 utilise les broches PA0 et PA1 comme TX0 et RX0 (transmetteur et récepteurs respectivement).

[caption id="attachment_536" align="aligncenter" width="624"][![00041](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00041.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00041.jpeg) ICDI USB Port[/caption]

Notez qu'il ya un second connecteur USB sur la TI ARM LaunchPad juste en dessous du commutateur. Il est étiqueté comme périphériques. Ce connecteur de périphérique USB est dédié à la fonctionnalité USB et utilise PD4 et pD5 broches pour les fils de D- et D+ de l'USB, respectivement.

Comme nous l'avons mentionné plus tôt, la TI TM4C123GH6PM peut avoir jusqu'à huit ports UART. Ils sont désignés comme UART0 à UART7. Le tableau suivant montre leurs adresses de base dans la mémoire:



	
  * UART0 base: 0x4000.C000

	
  * UART1 base: 0x4000.D000

	
  * UART2 base: 0x4000.E000

	
  * UART3 base: 0x4000.F000

	
  * UART4 base: 0x4001.0000

	
  * UART5 base: 0x4001.1000

	
  * UART6 base: 0x4001.2000

	
  * UART7 base: 0x4001.3000


La figure ci-après représente le schéma synoptique simplifié de l'unité UART.

[![00042](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00042.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00042.jpeg)






#### Baud-Rate Generator


Deux registres sont utilisés pour définir la vitesse de transmission: Ils sont UART Inger Baud-Rate Divisor (UARTIBRD) et UART fractionnal Baud-Rate Divisor (UARTFBRD). Leurs adresses de décalage sont présentés ci-dessous:

[![00044](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00044.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00044.jpeg)

[![00043](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00043.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00043.jpeg)





Pour la UART0 utilisé dans TI Tiva LaunchPad, leurs adresses physiques sont situés à 0x4000: C000 + 0x024 et 0x4000: C000 + 0x028, respectivement.

Sur les 32 bits du regsitre UARTIBRD, seulement les 16 bits inférieurs sont utilisés et des 32 bits de la UARTFBRD, seuls les 6 bits inférieurs sont utilisés. Cela nous donne totale de 22 bits (16 bits entiers + 6 bits de fraction).



Pour réduire le taux d'erreur et utiliser les vitesses de transmission standardisées, nous devrions utiliser à la fois les deux registres. Certains des taux de transmission standards sont 4800, 9600, 57600, et  115200. Ils peuvent être calculés selon la formule suivante:


Désiré Baud Rate = SYSCLK / (16 × ClkDiv)


où le SYSCLK est [l'horloge système](http://www.embarquez-vous.fr/?p=507)  et ClkDiv est les valeurs que nous chargeons dans les deux registres. Pour TI Tiva LaunchPad, l'horloge du système par défaut est 16 MHz. Donc, nous pouvons réorganiser la formule ci-dessus:


Désiré Baud Rate = 16MHz / (16 × ClkDiv) = 1MHz / ClkDiv


La valeur ClkDiv nous donne l'entier et les valeurs fractionnaires nécessaires pour les registres UARTIBRD et UARTFBRD. Alors que la partie entière du diviseur est facile à calculer, le calcul de la partie de fraction nécessite une manipulation mathématique. Un moyen serait, de multiplier la fraction par 64 et arrondir en ajoutant 0,5.


#### Exemple :


Supposons SYSCLK = 16MHz. Trouver les valeurs des registres UARTIBRD et UARTFBRD pour les vitesses de transmission standard suivantes:
(a) 4800 (b) 9600 (c) 57 600 (d) 115 200

Par défaut, 16 MHz horloge système est divisé par 16 avant qu'il ne soit introduit dans le UART. Par conséquent, nous avons :


16MHz / 16 = 1MHz et **ClkDiv = 1MHz / vitesse de transmission.**






	
  * (a) 1 MHz / 4800 = 208,3333,

	
    * UARTIBRD = 208 et

	
    * UARTFBRD = (0,3333 x 64) + 0,5 = 21,8312 = 21




	
  * (b) 1 MHz / 9600 = 104,166666,

	
    * UARTIBRD = 104 et

	
    * UARTFBRD = (0,16666 × 64) + 0,5 = 11




	
  * (c) 1MHz / 57600 = 17,361,

	
    * UARTIBRD = 17 et

	
    * UARTFBRD = (0,361 × 64) + 0,5 = 23




	
  * (d) 1 MHz / 115 200 = 8,680,

	
    * UARTIBRD = 8 et

	
    * UARTFBRD = (0,680 × 64) + 0,5 = 44







### UART Control (UARTCTL) register


La prochaine registre important dans UART est le registre de contrôle. Ce est un des registres 32 bits et un grand nombre de bits ne sont pas utilisés. Pour nous, les bits les plus importants sont RXE, TXE, HSE et UARTEN.


#### [![00045](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00045.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00045.jpeg)




#### UARTEN (D0) UART enable


Cela permet d'activer ou désactiver l'UART. Lors de l'initialisation nous devons désactiver tout en modifiant certains des registres UART,. Également au cours de l'exécution de certaines tâches critiques, vous pouvez désactiver l'UART pour l'empêcher d'interrompre les tâches.


#### **HSE (D5) High Speed enable**


Il permet de diviser par 8 la vitesse d'horloge et non 16 pour des vitesse de transmission avec une faible fréquence d'horloge.


#### **RXE (D8) Receive enable**


Nous devons le mettre à 1 pour recevoir des données.


#### **TXE (D9) Transmit Enable**


Nous devons le mettre à 1  pour transmettre des données.


### UART Line Control register


Ce est le registre définit le nombre de bits par caractère (de longueur de données) et le nombre de bits d'arrêt.

[caption id="attachment_550" align="aligncenter" width="624"][![00046](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00046.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00046.jpeg) UART Line Control (UARTLCRH)[/caption]


#### STP2 (D3) stop bit2.


Il peut y avoir 1 ou 2 bits d'arrêt. La valeur par défaut est 1 bit d'arrêt mis à la fin de chaque trame. Si le dispositif de réception est lent, on peut utiliser deux bits d'arrêt en faisant l'STP2 = 1.


#### FEN (D4) FIFO enable.


La pile sert principalement à ne pas bloquer le CPU. Par conséquent, la TI Tiva UART a une pile interne de 16-octet FIFO (First In First Out) pour stocker des données pour la transmission. Il ya aussi un autre tampon FIFO de 16 octets pour enregistrer tous les octets reçus. En permettant FEN, nous pouvons écrire jusqu'à 16 octets de bloc de données la pile de transmission et transférer un octet à la fois. Vous pouvez aussi créer un seuil pour l'UART et de notifier au CPU lorsque le seuil de la FIFO est franchit. Même chose pour la réception.


#### WLEN (D6-D5) Word Lenght


La longueur d'un mot transmis peut être 5, 6, 7 ou 8. En général, nous utilisons 8 bits pour chaque trame de données. Notez que la valeur de 5 est celle prise par défaut, il est nécessaire de changer pour 8 bits, comme indiqué ci-dessous:
<table >
<tbody >
<tr >

<td width="98" >**D6**
</td>

<td width="98" >**D5**
</td>

<td width="98" >** **
</td>
</tr>
<tr >

<td width="98" >0
</td>

<td width="98" >0
</td>

<td width="98" >**5 bits**
</td>
</tr>
<tr >

<td width="98" >0
</td>

<td width="98" >1
</td>

<td width="98" >**6 bits**
</td>
</tr>
<tr >

<td width="98" >1
</td>

<td width="98" >0
</td>

<td width="98" >**7 bits**
</td>
</tr>
<tr >

<td width="98" >1
</td>

<td width="98" >1
</td>

<td width="98" >**8 bits**
</td>
</tr>
</tbody>
</table>


### UART Data Register


Pour transmettre un octet de données, nous devons le placer dans le registre UART Data Register. Même s' il contient 32 bits, seuls les 8 bits inférieurs (D7-D0) sont utilisés. 

N.B : 



	
  * Il doit être noté que «Une écriture sur ce registre lance une transmission de l'UART."

	
  * De la même manière, l'octet reçu est placé dans ce registre et doit être lu avant qu'il ne soit perdue.


Pour l'émission, seuls les 8 bits inférieurs sont utilisés. Pour le reception, les 8 bits inférieurs contiennent  l'octet reçu et 4 bits supplémentaires de D11-D8 sont utilisés pour la détection d'erreur telle que, le framing erreur, erreur de parité, et ainsi de suite.

Il ya un autre registre appelé UARTRSR / UARTRCR (UART Receive Status Error/Error Clear) qui peuvent être utilisés pour vérifier la source de l'erreur.

[caption id="attachment_556" align="aligncenter" width="624"][![00047](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00047.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00047.jpeg) UART Data Register[/caption]




### UART Flag Register (Status)


[![00048](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00048.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00048.jpeg)


#### TXFE (Transmit FIFO empty D7):




#### RXFF (Receive FIFO full D6):




#### TXFF (Transmit FIFO full D5):




#### RXFE (Receive FIFO empty D4):


**Busy(UART occupé D3**)




### Enabling clock to UART


Le registre de RCGCUART est utilisé pour activer l'horloge de l'UART. Dans ce registre, il existe un bit pour chacun des modules de UART0 UART7. Si un UART donnée ne est pas utilisé, il faut désactiver l'horloge pour économiser la batterie. Pour utiliser UART0, nous avons mis à la haute D0 de ce registre.

[![00049](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00049.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00049.jpeg)




### Les broches GPIO utilisées pour UART TxD et RxD


En plus de la configuration des registres UART, nous devons aussi configurer les broches d'E/S utilisés par l'UART pour les signaux TxD et RxD. Dans ce [post](http://www.embarquez-vous.fr/?p=450), nous avons montré la configuration minimale pour chaque port. Lorsque les broches GPIO sont utilisés pour des fonctions périphériques alternatives, tels que, UART, Timer, et ADC, nous devons configurer cinq autres registres. Ils sont ORTx Run Mode Clock Gating Control, PORTx Digital Enable, PORTx ADC Mode Selection, PORTx Alternate Selection and PORTx Port Control registers. Les deux premiers registres sont abordés [ici](http://www.embarquez-vous.fr/?p=450). Nous examinons les trois autres registres ici.

[caption id="attachment_566" align="aligncenter" width="624"][![00050](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00050.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00050.jpeg) GPIOAMSEL (GPIO Analog Mode Select)[/caption]



La TI ARM vient avec un ADC sur puce (convertisseur analogique-numérique). Supposons qu'une broches donnée peut être utilisée à la fois pour l'ADC et l'UART et nous voulons l'utiliser pour UART. Dans ce cas, nous devons isoler la fonction ADC car elle n'est pas utilisée.

Cela se fait avec GPIOAMSEL (GPIO Analog Mode Selection). Bien que chaque port a son propre registre de PORTxAMSEL, toutes les broches de chaque port a une capacité de ADC.

Après la réinitialisation, les broches GPIO sont configurés comme simple E/S. Pour les utiliser pour d'autres fins, telle que, l'UART.

Les fonctions alternatives sont sélectionner via le Port Control Register, ce registre contient 32bits. 4 bits sont utilisés pour sélectionner la fonction de chaque broche.Pour la majorité des broches, le numéro de sélection est 1 exceptions faites pour PC4 et PC5. PC4 et PC4 peuvent être utilisés et pour UART4 et UART1.

[caption id="attachment_571" align="aligncenter" width="624"][![00052](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00052.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00052.jpeg) GPIOPCTL Register[/caption]



[caption id="attachment_572" align="aligncenter" width="624"][![00053](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00053.jpeg)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/00053.jpeg) UART Pins and GPIOPCTL Registers[/caption]




### étape pour transmettre les données


Voici les étapes pour configurer le UART0 et transmettre un octet de données pour TI Tiva TM4C123GH6PM sur le LaunchPad:



	
  1. activer l'horloge pour UART0 en écrivant 1 au registre RCGCUART.

	
  2. activer l'horloge pour pour PORTA en écrivant 1 au registre RCGCGPIO.

	
  3. Désactivez l'UART0 en écrivant 0 au registre UARTCTL de UART0.

	
  4. Trouver les bonnes valeurs pour configurer la vitesse de transmission et les écrire sur les registres UARTIBRD et UARTFBRD de UART0.

	
  5. Sélectionnez l'horloge système comme source d'horloge pour l'UART en écrivant un 0 au registre  UARTCC de UART0.

	
  6. Configurer la paramètres de transmission : 1 bit d'arrêt, pas de FIFO, sans interruption, pas de bit parité, et la taille de données de 8 bits. Cela nous donne 0x60 pour le registre de UARTLCRH de UART0.

	
  7. Mettre TxE et RXE de UARTCTL à 1 pour permettre à l'émetteur et le récepteur des UART0.

	
  8. Mettre à 1 le bit UARTEN du registre UARTCTL pour permettre à la UART0.

	
  9. Configurer PA0 et PA1 pour être utilisés comme E/S numérique.

	
  10. Sélectionnez les fonctions alternatives des PA0 (RxD) et les broches PA1 (TxD) en utilisant le GPIOAFSEL.

	
  11. Configurer PA0 et PA1 broches pour la fonction UART.

	
  12. Attendre pour la sortie TxD d'établir ralenti.

	
  13. Surveiller le bit du flag TXFF de l'UART.




Example

Envoie les caractères "YES" au terminal. Vous devez installer TeraTerminal (ou un autre programme de comme HyperTerminal ou Putty) sur votre PC. Pour télécharger TeraTerminal et voir le tutoriel:



    
    /* UART0 est sur USB/Debug */
    /* Utiliser un terminal pour voir "Bonjour" sur un PC */ 
    #include ;
    #include "tm4c123gh6pm.h"
    void UART0Tx(char c);
    void delayMs(int n);
    int main(void)
    {
        SYSCTL->RCGCUART |= 1;  /* l'horloge pour l'UART0 */
        SYSCTL->RCGCGPIO |= 1;  /* activer l'horloge pour le PORTA */
        /* UART0 initialization */
        UART0->CTL = 0;         /* désactiver l'UART0 */
        UART0->IBRD = 104;      /* 16MHz/16=1MHz, 1MHz/104=9600 baud rate */
        UART0->FBRD = 11;       /* fraction partie */
        UART0->CC = 0;          /* utiliser l'horloge système  */
        UART0->LCRH = 0x60;     /* 8-bit, no parity, 1-stop bit, no FIFO */
        UART0->CTL = 0x301;     /* activer UART0, TXE, RXE */ 
        /* UART0 TX0 and RX0 use PA0 and PA1. Set them up. */
        GPIOA->DEN = 0x03;      /* Mettre PA0 et PA1 comme digital */
        GPIOA->AFSEL = 0x03;    /* Utiliser PA0,PA1 alternate function */
        GPIOA->PCTL = 0x11;     /* configurer PA0 et PA1 pour l'UART */
        delayMs(1);             /* attendre que la ligne se stabilise */   
        for(;;)
        {
            UART0Tx('Y');
            UART0Tx('E');
            UART0Tx('S');
            UART0Tx(' ');   
        }
    }
    /* UART0 Transmit */
    /* Cette fonction attend jusqu'à ce que le buffer de transmission soit disponible */
    /* écrire un caractère sur le buffer de transmission */
    
    void UART0Tx(char c) 
    {
        while((UART0->FR & 0x20) != 0); /* attendre jusqu'à ce que Tx buffer soit vide */
        UART0->DR = c;                  /* avant de mettre un autre byte */
    } 
    /* retard n millisecondes (16 MHz CPU clock) */
    void delayMs(int n)
    {
        int i, j;
        for(i = 0 ; i < n; i++)
            for(j = 0; j < 3180; j++)             {}  /* do nothing for 1 ms */ 
    } 
    
    
