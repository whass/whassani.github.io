title: Le tutoriel complet pour le développement de LaunchPad Stellaris avec GNU/Linux (I)
date: 2015-01-23
categories: 
- Embedded


Dans cet article, j'explique comment programmer la Stellaris EK-LM4F120XL LaunchPad.

[![LM4F120](http://microlabs.niloo.fr/wp-content/uploads/480px-LM4F120_LaunchPad_perspective.jpg)](http://microlabs.niloo.fr/wp-content/uploads/480px-LM4F120_LaunchPad_perspective.jpg)Les outils officiellement fournis par Texas Instrument  semblent assez volumineux ( 1,3 Go pour CCS v5.3). Il existe une alternative sous Linux qui consiste à utiliser les lignes de commandes Unix avec gedit et gcc.


## 1. Construire la chaîne de compilation ARM


Nous allons maintenant mettre en œuvre la chaîne de compilation (compilateur C, assembleur, linker, etc) lequel vous permettra de compiler vos programmes en C écrit pour les processeurs Cortex-m4f.

Le _summon arm toolchain_ est un script shell qui, lorsqu'il est exécuté, télécharge les paquets sources nécessaires et construit la chaîne de compilation. Il suffit de cloner le dépôt git et exécutez le script (compilation assez longue) :

    
    <span class="pln">sudo apt</span><span class="pun">-</span><span class="kwd">get</span><span class="pln"> install flex bison libgmp3</span><span class="pun">-</span><span class="pln">dev libmpfr</span><span class="pun">-</span><span class="pln">dev libncurses5</span><span class="pun">-</span><span class="pln">dev python</span><span class="pun">-</span><span class="pln">yaml </span><span class="kwd">and</span><span class="pln"> zlib1g</span><span class="pun">-</span><span class="pln">dev libmpc</span><span class="pun">-</span><span class="pln">dev autoconf texinfo build</span><span class="pun">-</span><span class="pln">essential libftdi</span><span class="pun">-</span><span class="pln">dev git
    cd </span><span class="pun">~</span><span class="pln">
    git clone https</span><span class="pun">:</span><span class="com">//github.com/esden/summon-arm-toolchain</span><span class="pln">
    cd summon</span><span class="pun">-</span><span class="pln">arm</span><span class="pun">-</span><span class="pln">toolchain</span><span class="pun">;</span> <span class="pun">./</span><span class="pln">summon</span><span class="pun">-</span><span class="pln">arm</span><span class="pun">-</span><span class="pln">toolchain</span>


Si tout va bien, après _summon-arm-toolchain_ fait son travail, vous verrez un dossier appelé "sat" dans votre home et _~ /sat/bin/_ devrait contenir des exécutables comme "arm-none-eabi-gcc" - Félicitations, votre chaîne de compilation est prête ![:)](http://microlabs.niloo.fr/wp-includes/images/smilies/icon_smile.gif) ! Ne pas oublier d'ajouter à votre PATH :

    
    <span class="pln">cd </span><span class="pun">~</span><span class="pln">
    echo </span><span class="str">"PATH=$PATH:~/sat/bin"</span> <span class="pun">>></span> <span class="pun">.</span><span class="pln">bashrc
    echo </span><span class="str">"PATH=$PATH:~/stellarisware"</span> <span class="pun">>></span> <span class="pun">.</span><span class="pln">bashrc
    echo </span><span class="str">"PATH=$PATH:~/lm4tools/lm4flash"</span> <span class="pun">>></span> <span class="pun">.</span><span class="pln">bashrc</span>


IMPORTANT : redémarrer ou fermer/ré-ouvrer la session sinon vous obtiendrez des erreurs dans les étapes suivantes...


## 2. Flasher la stellaris Launchpad avec lm4flash


Premièrement, télécharger _lm4tools_ depuis [https://github.com/utzig/lm4tools](https://github.com/utzig/lm4tools) et compiler le :

    
    <span class="pln">sudo apt</span><span class="pun">-</span><span class="kwd">get</span><span class="pln"> install libusb</span><span class="pun">-</span><span class="lit">1.0</span><span class="pun">-</span><span class="lit">0</span><span class="pun">-</span><span class="pln">dev 
    cd </span><span class="pun">~</span><span class="pln">
    git clone https</span><span class="pun">:</span><span class="com">//github.com/utzig/lm4tools.git</span><span class="pln">
    cd lm4tools</span><span class="pun">/</span><span class="pln">lm4flash</span><span class="pun">;</span><span class="pln"> make</span>


Vous pourrez ainsi flasher avec la ligne de commande suivante en root :

    
    <span class="pln">sudo lm4flash project0</span><span class="pun">.</span><span class="pln">bin</span>




## 3. Construire Stellarisware avec la chaîne de compilation GNU


TI fournit une librairie appelée "_stellarisware_" pour faciliter l'accès aux périphériques du processeur ARM Cortex. Il y a aussi de nombreux exemples de programmes qui montrent l'utilisation de plusieurs de ces périphériques.

Vous pouvez télécharger Stellarisware (SW-EK-LM4F120XL:StellarisWare for the Stellaris LM4F120 LaunchPad Evaluation Board) sur [http://www.ti.com/tool/sw-ek-lm4f120xl](http://www.ti.com/tool/sw-ek-lm4f120xl). Construire Stellarisware est simple :

    
    <span class="pln">cd </span><span class="pun">~</span><span class="pln">
    mkdir stellarisware</span><span class="pun">;</span><span class="pln"> cd stellarisware
    unzip </span><span class="pun">~</span><span class="str">/Téléchargements/</span><span class="pln">SW</span><span class="pun">-</span><span class="pln">EK</span><span class="pun">-</span><span class="pln">LM4F120XL</span><span class="pun">-</span><span class="lit">9453.exe</span><span class="pln">
    make</span>


"make" construira les librairies permettant d’accéder aux périphériques et quelques exemples.

Vous pouvez tester que tout marche en flashant la stellaris launchpad avec un programme de test :

    
    <span class="pln">cd boards</span><span class="pun">/</span><span class="pln">ek</span><span class="pun">-</span><span class="pln">lm4f120xl</span><span class="pun">/</span><span class="pln">blinky</span><span class="pun">/</span><span class="pln">sourcerygxx</span><span class="pun">/</span><span class="pln">
    lm4flash blinky</span><span class="pun">.</span><span class="pln">bin</span>




## 4. Écrire et tester  vos programmes ![:)](http://microlabs.niloo.fr/wp-includes/images/smilies/icon_smile.gif)


À l'aide des exemples de StellarisWare, nous pouvons maintenant tester nos propres petits programmes.

Tout d'abord, nous avons besoin d'un programme C simple. Nous allons utiliser l'exemple de la LED clignotante qui est un des exemples StellarisWare (appelons-le "blink.c") :

    
    <span class="com">#include</span> <span class="str">"inc/hw_gpio.h"</span>
    <span class="com">#include</span> <span class="str">"inc/hw_memmap.h"</span>
    <span class="com">#include</span> <span class="str">"inc/hw_sysctl.h"</span>
    <span class="com">#include</span> <span class="str">"inc/hw_types.h"</span>
    <span class="com">#include</span> <span class="str">"driverlib/gpio.h"</span>
    <span class="com">#include</span> <span class="str">"driverlib/rom.h"</span>
    <span class="com">#include</span> <span class="str">"driverlib/sysctl.h"</span>
    
    <span class="com">#define</span><span class="pln"> LED_RED GPIO_PIN_1
    </span><span class="com">#define</span><span class="pln"> LED_BLUE GPIO_PIN_2
    </span><span class="com">#define</span><span class="pln"> LED_GREEN GPIO_PIN_3
    
    </span><span class="kwd">int</span><span class="pln"> main</span><span class="pun">()</span>
    <span class="pun">{</span>
       <span class="com">/** Configuration de la clock à 50 MHz avec le Quartz externe (16MHz) et PLL */</span><span class="pln">
       ROM_SysCtlClockSet</span><span class="pun">(</span><span class="pln">SYSCTL_SYSDIV_4</span><span class="pun">|</span><span class="pln">SYSCTL_USE_PLL</span><span class="pun">|</span><span class="pln">SYSCTL_XTAL_16MHZ</span><span class="pun">|</span><span class="pln">SYSCTL_OSC_MAIN</span><span class="pun">);</span>
    
       <span class="com">/** Activer PORT F GPIO */</span><span class="pln">
       ROM_SysCtlPeripheralEnable</span><span class="pun">(</span><span class="pln">SYSCTL_PERIPH_GPIOF</span><span class="pun">);</span>
      
       <span class="com">/** Placer les pins LED pins comme sorties */</span><span class="pln">
       ROM_GPIOPinTypeGPIOOutput</span><span class="pun">(</span><span class="pln">GPIO_PORTF_BASE</span><span class="pun">,</span><span class="pln"> LED_RED</span><span class="pun">|</span><span class="pln">LED_BLUE</span><span class="pun">|</span><span class="pln">LED_GREEN</span><span class="pun">);</span>
    
       <span class="kwd">for</span> <span class="pun">(;;)</span> 
       <span class="pun">{</span>
          <span class="com">// Allume la LED Rouge</span><span class="pln">
          ROM_GPIOPinWrite</span><span class="pun">(</span><span class="pln">GPIO_PORTF_BASE</span><span class="pun">,</span><span class="pln"> LED_RED</span><span class="pun">|</span><span class="pln">LED_GREEN</span><span class="pun">|</span><span class="pln">LED_BLUE</span><span class="pun">,</span><span class="pln"> LED_RED</span><span class="pun">);</span><span class="pln">
          ROM_SysCtlDelay</span><span class="pun">(</span><span class="lit">5000000</span><span class="pun">);</span>
    
          <span class="com">// Eteint la LED Rouge</span><span class="pln">
          ROM_GPIOPinWrite</span><span class="pun">(</span><span class="pln">GPIO_PORTF_BASE</span><span class="pun">,</span><span class="pln"> LED_RED</span><span class="pun">|</span><span class="pln">LED_GREEN</span><span class="pun">|</span><span class="pln">LED_BLUE</span><span class="pun">,</span> <span class="lit">0</span><span class="pun">);</span><span class="pln">
          ROM_SysCtlDelay</span><span class="pun">(</span><span class="lit">5000000</span><span class="pun">);</span>
       <span class="pun">}</span>
    <span class="pun">}</span>


Nous avons besoin de deux fichiers de plus pour faire tourner notre code (un fichier contenant le main et un "script linker"). Le script "linker" est utilisé par la chaîne de compilation pour attribuer des adresses mémoire appropriés à des emplacements dans notre programme. Vous pouvez copier ces deux fichiers à partir de l'un des exemples de programmes StellarisWare :

    
    <span class="pln">cp </span><span class="pun">~</span><span class="str">/stellarisware/</span><span class="pln">boards</span><span class="pun">/</span><span class="pln">ek</span><span class="pun">-</span><span class="pln">lm4f120xl</span><span class="pun">/</span><span class="pln">blinky</span><span class="pun">/</span><span class="pln">blinky</span><span class="pun">.</span><span class="pln">ld blink</span><span class="pun">.</span><span class="pln">ld
    cp </span><span class="pun">~</span><span class="str">/stellarisware/</span><span class="pln">boards</span><span class="pun">/</span><span class="pln">ek</span><span class="pun">-</span><span class="pln">lm4f120xl</span><span class="pun">/</span><span class="pln">blinky</span><span class="pun">/</span><span class="pln">startup_gcc</span><span class="pun">.</span><span class="pln">c </span><span class="pun">.</span>


Compilez votre code avec le code suivant :

    
    <span class="pln">arm</span><span class="pun">-</span><span class="pln">none</span><span class="pun">-</span><span class="pln">eabi</span><span class="pun">-</span><span class="pln">gcc blink</span><span class="pun">.</span><span class="pln">c startup_gcc</span><span class="pun">.</span><span class="pln">c </span><span class="pun">-</span><span class="pln">g </span><span class="pun">-</span><span class="pln">mthumb </span><span class="pun">-</span><span class="pln">mcpu</span><span class="pun">=</span><span class="pln">cortex</span><span class="pun">-</span><span class="pln">m4 </span><span class="pun">-</span><span class="pln">mfpu</span><span class="pun">=</span><span class="pln">fpv4</span><span class="pun">-</span><span class="pln">sp</span><span class="pun">-</span><span class="pln">d16 </span><span class="pun">-</span><span class="pln">mfloat</span><span class="pun">-</span><span class="pln">abi</span><span class="pun">=</span><span class="pln">softfp </span><span class="pun">-</span><span class="typ">Os</span> <span class="pun">-</span><span class="pln">ffunction</span><span class="pun">-</span><span class="pln">sections </span><span class="pun">-</span><span class="pln">fdata</span><span class="pun">-</span><span class="pln">sections </span><span class="pun">-</span><span class="pln">MD </span><span class="pun">-</span><span class="pln">std</span><span class="pun">=</span><span class="pln">c99 </span><span class="pun">-</span><span class="typ">Wall</span> <span class="pun">-</span><span class="pln">pedantic </span><span class="pun">-</span><span class="pln">DPART_LM4F120H5QR </span><span class="pun">-</span><span class="pln">c </span><span class="pun">-</span><span class="pln">I</span><span class="pun">/</span><span class="pln">home</span><span class="pun">/</span><span class="pln">$USER</span><span class="pun">/</span><span class="pln">stellarisware </span><span class="pun">-</span><span class="pln">DTARGET_IS_BLIZZARD_RA1</span>


La prochaine étape  génère deux fichiers : blink.o et startup_gcc.o. et va les lier entre eux :

    
    <span class="pln">arm</span><span class="pun">-</span><span class="pln">none</span><span class="pun">-</span><span class="pln">eabi</span><span class="pun">-</span><span class="pln">ld </span><span class="pun">-</span><span class="pln">T blink</span><span class="pun">.</span><span class="pln">ld </span><span class="pun">--</span><span class="pln">entry </span><span class="typ">ResetISR</span> <span class="pun">-</span><span class="pln">o a</span><span class="pun">.</span><span class="kwd">out</span><span class="pln"> startup_gcc</span><span class="pun">.</span><span class="pln">o blink</span><span class="pun">.</span><span class="pln">o </span><span class="pun">--</span><span class="pln">gc</span><span class="pun">-</span><span class="pln">sections</span>


La dernière étape consiste à générer l'image binaire raw :

    
    <span class="pln">arm</span><span class="pun">-</span><span class="pln">none</span><span class="pun">-</span><span class="pln">eabi</span><span class="pun">-</span><span class="pln">objcopy </span><span class="pun">-</span><span class="pln">O binary a</span><span class="pun">.</span><span class="kwd">out</span><span class="pln"> blink</span><span class="pun">.</span><span class="pln">bin</span>


Le fichier résultant est "blink.bin", qui peut être flasher avec lm4flash:

    
    <span class="pln">lm4flash blink</span><span class="pun">.</span><span class="pln">bin</span>


Vous devriez voir la LED rouge qui clignote ![:)](http://microlabs.niloo.fr/wp-includes/images/smilies/icon_smile.gif) !
