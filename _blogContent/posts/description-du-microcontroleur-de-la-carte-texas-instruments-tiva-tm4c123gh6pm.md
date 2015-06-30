title: ARM Cortex M4, Description du microcontroleur de la carte Texas Instruments Tiva TM4C123GH6PM
date: 2015-02-14
categories: 
- Embedded

La TI LaunchPad utilise le microcontrôleur TM4C123GH6PM, sa version étant la puce. La TM4C123GH6PM est une version améliorée de la LM4F120, pas de panique, tous vos programme écris pour LM4F120 reste valable sur TM4C123GH6PM sans aucune modification, mais pas dans l'autre sens. 




La puce TM4C123GH6PM a :





	
  * 256K octets (256KB) pour le code sur sa mémoire Flash,

	
  * 32 Ko de SRAM sur puce pour les données, 

	
  * et un grand nombre de périphériques sur puce comme indiqué dans les figures ci-après 


[![](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/TI-Tiva-TM4C123GH6PM-Microcontroller-High-Level-Block-Diagram1.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/TI-Tiva-TM4C123GH6PM-Microcontroller-High-Level-Block-Diagram1.png)





[![](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/TI-Tiva-Peripherals.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/TI-Tiva-Peripherals.png)

Il utilise également une **memory mapped I/O** qui signifie que les I/O ports périphériques sont mappés dans l'espace mémoire de 4 Go. Voir le tableau 2-1 et la figure 2-3 pour carte mémoire de la puce TM4C123GH6PM.


<table border="1" class="alignleft" >_Map Mémoire du TM4C123GH6PM_
<tbody >
<tr >
Mémoire
Espace Alloué
Adresse Allouée
</tr>
<tr >
Flash

<td style="text-align: center;" >256KB
</td>

<td style="text-align: center;" >0x00000000 à 0x0003FFFF
</td>
</tr>
<tr >
SRAM

<td style="text-align: center;" >32KB
</td>

<td style="text-align: center;" >0x20000000 à 0x20007FFF
</td>
</tr>
<tr >
I/O

<td style="text-align: center;" >4Go
</td>

<td style="text-align: center;" >0x40000000 à 0x400FFFFF
</td>
</tr>
</tbody>
</table>










[![](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/memory-map.png)](http://www.embarquez-vous.fr/wp-content/uploads/2015/02/memory-map.png)

Au regard de ces figures,  les points suivants doivent être notés:



	
  1. 256 Ko de mémoire flash est utilisée pour le code du programme. On peut également enregistrer le code dans la mémoire Flash ROM des données fixes, telles que les look-up table (table de correspondances). La mémoire flash est organisé en 1-KB bloc. Chaque bloc peut être effacé ou écrit de façon indépendante.


	
  2. 


 La mémoire  SRAM de 32KB est utilisée pour stocker les variables, et pile. Elle commence à l'adresse 0x20000000. Les alias d'adresses ( **address** **aliases**) peuvent être utilisées pour une partie de la SRAM pour permettre un accès à des bits individuellement (un bit à al fois). Ceci est appelé **_bit-banding_**.


	
  3. Les périphériques tels que I / O, Timer, ADC sont mappés à des adresses mémoires à partir de 0x40000000. Dans TM4C123GH6PM la limite supérieure est 0x400FFFFF. Pour plus de détails voir le tableau précédent. L'adresse mémoire limite supérieure peut varier entre en fonction de la famille des puces ARM en fonction du nombre de périphériques.





## GPIO


Les entrées/sorties du TM4C123GH6PM ARM I sont désignés du port A au port F. Le tableau suivant montre la plage d'adresses (se trouvant dans la plage **SFR (Special function register)**)affectée à chaque ports GPIO:



	
  * **GPIO Port A :** 0x4000.4000 to 0x4000.4FFF

	
  * **GPIO Port B :** 0x4000.5000 to 0x4000.5FFF

	
  * **GPIO Port C :** 0x4000.6000 to 0x4000.6FFF

	
  * **GPIO Port D :** 0x4000.7000 to 0x4000.7FFF

	
  * **GPIO Port E :** 0x4002.4000 to 0x4002.4FFF

	
  * **GPIO Port F :** 0x4002.5000 to 0x4002.5FFF







