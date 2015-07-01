title: Bit-banding - une approche élégante pour la mise à 1 ou à 0 des Bits de vos registres
description: Typiquement un noyau CPU ne peut pas écrire des bits d'un registre individuellement. En effet, il doit écrire des octets ou mots entiers à la fois selon la flow (Read-Modify-Write). Mais que ce passera-t-il si durant (Read-Modify-Write) une interruption prioritaire survient ? Pour en savoir plus, lisez la la suite.
date: 2015-02-14
categories: 
- Embedded
- Linux

** Table des matières **

[TOC]

### Le problème de lecture-modification-écriture

Avant d'expliquer ce qu'est le Bit-bading, laissez-moi vous expliquer un peu le contexte : 

Typiquement un noyau CPU ne peut pas écrire des bits d'un registre individuellement. En effet, il doit écrire des octets ou mots entiers à la fois. Si un CPU a besoin de changer la valeur d'un bit mais ne peut pas écrire un octet à la fois, il doit d'abord lire la valeur actuelle dans un registre temporaire, modifier cette valeur avec une opération logique, puis écrire le résultat final. Ce processus en trois étapes est appelée** lecture-modification-écriture** (Read-Modify-Write).

L'usage de "lecture-modification-écriture" ne posent aucun problème lorsque le CPU fait une chose à la fois (ex. exécution séquentielle d'un programme), mais des problèmes peuvent survenir lorsqu'une application fait plusieurs choses en même temps. Par exemple, ce qui se passe si une interruption se produit entre les opérations "lire et modifier" lorsqu'on souhaite modifier la valeur d'un registre?. Comme l'opération écriture ne s'est pas faite, alors cette nouvelle sera valeur écrasée. 

* Ce qui conduit à un **race-condition** comportement indésirable.

### Mode opératoire du bit-banding

Le bit-banding est un terme que ARM utilise pour décrire une caractéristique disponible sur les cœurs des processeurs Cortex M3 et M4. 

Fondamentalement, le dispositif prend :
* une zone (ou bande) mémoire (la région Bit-band) 
* et fait correspondre à chaque bit dans cette région à un mot entier dans une deuxième zone de mémoire (la Bit-band Alias Region).

L'avantage de Bit-banding est qu'une écriture d'un mot dans la région d'alias effectue une écriture d'un bit correspondant dans la région bit-band. Par conséquent, la lecture d'un mot dans la région d'alias retournera la valeur du bit correspondant dans la région de bit-band. 

Ces opérations se font en une seule instruction machine évitant ainsi le ***race-condition***. 

Ceci est particulièrement utile pour interagir avec des registres périphériques où il est souvent nécessaire d'agir sur un seul bit. 

L'image ci-dessous montre le principe du bit-banding, à des fins de démonstration, j'ai choisis d'utiliser des mots de 8 bits. Sur le Cortex M3 et M4 de la région d'alias contient des mots de 32 bits.

![bit-banding](http://d1u2s20mo6at4b.cloudfront.net/wp-content/uploads/Screen-Shot-2013-01-30-at-7.39.59-AM.png)

Pour utiliser cette caractéristique, vous devez avoir l'adresse du mot dans la région Alias (Alias Region) qui correspond au bit que vous voulez manipuler (lecture/écrire). Ceci est fait en C avec une macro.


    
    #define BITBAND_SRAM_REF 0x20000000
    #define BITBAND_SRAM_BASE 0x22000000
    #define BITBAND_SRAM(a,b) ((BITBAND_SRAM_BASE + (a-BITBAND_SRAM_REF)*32 + (b*4))) // Convert SRAM address
    #define BITBAND_PERI_REF 0x40000000
    #define BITBAND_PERI_BASE 0x42000000
    #define BITBAND_PERI(a,b) ((BITBAND_PERI_BASE + (a-BITBAND_PERI_REF)*32 + (b*4))) // Convert PERI address
    #define MAILBOX 0x20004000
    #define TIMER 0x40004000// Mailbox bit 0
    #define MBX_B0 *((volatile unsigned int *)(BITBAND_SRAM(MAILBOX,0)))// Mailbox bit 7
    #define MBX_B7 *((volatile unsigned int *)(BITBAND_SRAM(MAILBOX,7)))// Timer bit 0
    #define TIMER_B0 *((volatile unsigned char *)(BITBAND_PERI(TIMER,0)))// Timer bit 7
    #define TIMER_B7 *((volatile unsigned char *)(BITBAND_PERI(TIMER,7)))
    int main(void){    unsigned int temp = 0;
        MBX_B0 = 1; // Word write    
        temp = MBX_B7; // Word read    
         TIMER_B0 = temp; // Byte write    
         return TIMER_B7; // Byte read
    }


Pour plus de détails veuillez vous référer a cette adresse [the ARM InfoCenter page on bit-banding](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dai0179b/CHDJHIDF.html).

Ce n'est pas la seule solution existante. Pour toute les architectures connues, ils existent des mécanismes pour agir sur un bit individuellement. L'"'approche qu'utilise ARM est élégante et n'utilise que le ANSI C là où les autres utilisent des extensions spéciales ou le langages assembleur.

















