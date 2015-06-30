title: "Prise en main rapide du langage C pour l'embarqué, débutant c'est votre bible !"
date: 2015-01-22
categories: 
- Embedded




Ci-après vous trouverez l'ensemble des instructions qui vous seront utiles lors de la programmation de vos micro-contrôleur en C.


## Ponctuation


<table > 
<tbody >
<tr >

<td >







Punctuation






</td>

<td >







Signification






</td>
</tr>
<tr >

<td >







;






</td>

<td >







Fin de la déclaration






</td>
</tr>
<tr >

<td >







:






</td>

<td >







Définit une étiquette






</td>
</tr>
<tr >

<td >







,






</td>

<td >







Sépare les éléments d'une liste






</td>
</tr>
<tr >

<td >







()






</td>

<td >







Début et fin d'une liste de paramètres






</td>
</tr>
<tr >

<td >







{}






</td>

<td >







Début et fin d'une instruction composée






</td>
</tr>
<tr >

<td >







[]






</td>

<td >







Début et fin d'un tableau d'index






</td>
</tr>
<tr >

<td >







" "






</td>

<td >







Début et fin  d'un string






</td>
</tr>
<tr >

<td >







' '






</td>

<td >







Début et fin d'un caractère constant (character constant)






</td>
</tr>
</tbody>
</table>



## Type de données


<table > 
<tbody >
<tr >

<td >







Type de données






</td>

<td >







Gamme






</td>

<td >







Précision






</td>
</tr>
<tr >

<td >







unsigned char






</td>

<td >







0 to +255






</td>

<td >







8-bit non signé






</td>
</tr>
<tr >

<td >







signed char






</td>

<td >







-128 to +127






</td>

<td >







8-bit signé






</td>
</tr>
<tr >

<td >







unsigned int






</td>

<td >







32-bit in Keil






</td>

<td >







compiler-dependent






</td>
</tr>
<tr >

<td >







int






</td>

<td >







32-bit in Keil






</td>

<td >







compiler-dependent






</td>
</tr>
<tr >

<td >







unsigned short






</td>

<td >







0 to +65535






</td>

<td >







16-bit non signé






</td>
</tr>
<tr >

<td >







short






</td>

<td >







-32768 to +32767






</td>

<td >







16-bit signé






</td>
</tr>
<tr >

<td >







unsigned long






</td>

<td >







0 to 4294967295L






</td>

<td >







32-bit non signé






</td>
</tr>
<tr >

<td >







long






</td>

<td >







-2147483648L to 2147483647L






</td>

<td >







32-bit non signé






</td>
</tr>
<tr >

<td >







float






</td>

<td >







±10-38 to ±10+38






</td>

<td >







32-bit virgule flottante






</td>
</tr>
<tr >

<td >







double






</td>

<td >







±10-308 to ±10+308






</td>

<td >







64-bit virgule flottante






</td>
</tr>
</tbody>
</table>
<table > 
<tbody >
<tr >

<td >







Hex Digit






</td>

<td >







Décimal






</td>

<td >







Binaire






</td>
</tr>
<tr >

<td >







0






</td>

<td >







0






</td>

<td >







0000






</td>
</tr>
<tr >

<td >







1






</td>

<td >







1






</td>

<td >







0001






</td>
</tr>
<tr >

<td >







2






</td>

<td >







2






</td>

<td >







0010






</td>
</tr>
<tr >

<td >







3






</td>

<td >







3






</td>

<td >







0011






</td>
</tr>
<tr >

<td >







4






</td>

<td >







4






</td>

<td >







0100






</td>
</tr>
<tr >

<td >







5






</td>

<td >







5






</td>

<td >







0101






</td>
</tr>
<tr >

<td >







6






</td>

<td >







6






</td>

<td >







0110






</td>
</tr>
<tr >

<td >







7






</td>

<td >







7






</td>

<td >







0111






</td>
</tr>
<tr >

<td >







8






</td>

<td >







8






</td>

<td >







1000






</td>
</tr>
<tr >

<td >







9






</td>

<td >







9






</td>

<td >







1001






</td>
</tr>
<tr >

<td >







A OU a






</td>

<td >







10






</td>

<td >







1010






</td>
</tr>
<tr >

<td >







B OU b






</td>

<td >







11






</td>

<td >







1011






</td>
</tr>
<tr >

<td >







C OU c






</td>

<td >







12






</td>

<td >







1100






</td>
</tr>
<tr >

<td >







D OU d






</td>

<td >







13






</td>

<td >







1101






</td>
</tr>
<tr >

<td >







E OU e






</td>

<td >







14






</td>

<td >







1110






</td>
</tr>
<tr >

<td >







F or f






</td>

<td >







15






</td>

<td >







1111






</td>
</tr>
</tbody>
</table>



## Opérateurs








<table > 
<tbody >
<tr >

<td >







Opérateur






</td>

<td >







Signification






</td>
</tr>
<tr >

<td >







=






</td>

<td >







Instruction d'affectation






</td>
</tr>
<tr >

<td >







?






</td>

<td >







Sélection






</td>
</tr>
<tr >

<td >







<






</td>

<td >







Inférieur à






</td>
</tr>
<tr >

<td >







>






</td>

<td >







Supérieur à






</td>
</tr>
<tr >

<td >







!






</td>

<td >







Non Logique






</td>
</tr>
<tr >

<td >







~






</td>

<td >







Le complément à 1






</td>
</tr>
<tr >

<td >







+






</td>

<td >







Addition






</td>
</tr>
<tr >

<td >







-






</td>

<td >







Soustraction






</td>
</tr>
<tr >

<td >







*






</td>

<td >







Multiplicateur ou référence à un poiteur






</td>
</tr>
<tr >

<td >







/






</td>

<td >







Division






</td>
</tr>
<tr >

<td >







%






</td>

<td >







Modulo, reste de la division






</td>
</tr>
<tr >

<td >







|






</td>

<td >







OU logique






</td>
</tr>
<tr >

<td >







&






</td>

<td >







ET logique, ou Adresse de






</td>
</tr>
<tr >

<td >







^






</td>

<td >







OU EXCLUSIF Logique






</td>
</tr>
<tr >

<td >







.






</td>

<td >







Utilisé pour accéder à une partie d'une structure






</td>
</tr>
</tbody>
</table>



## Logique booléenne


<table > 
<tbody >
<tr >

<td colspan="2" rowspan="1" >







Lois fondamentale de bool






</td>
</tr>
<tr >

<td >







A& B = B & A






</td>

<td >







Loi commutative






</td>
</tr>
<tr >

<td >







A |B = B | A






</td>

<td >







Loi commutative






</td>
</tr>
<tr >

<td >







(A & B) & C = A & (B & C)






</td>

<td >







Loi associative






</td>
</tr>
<tr >

<td >







(A | B) | C = A | (B | C)






</td>

<td >







Loi associative






</td>
</tr>
<tr >

<td >







(A | B) & C = (A & C) | (B & C)






</td>

<td >







Loi distributive






</td>
</tr>
<tr >

<td >







(A & B) | C = (A | C) & (B | C)






</td>

<td >







Loi distributive






</td>
</tr>
<tr >

<td >







A& 0 = 0






</td>

<td >







Identité de 0






</td>
</tr>
<tr >

<td >







A |0 = A






</td>

<td >







Identité de 0






</td>
</tr>
<tr >

<td >







A& 1 = A






</td>

<td >







Identité de 1






</td>
</tr>
<tr >

<td >







A |1 = 1






</td>

<td >







Identité de 1






</td>
</tr>
<tr >

<td >







A |A = A






</td>

<td >







Propriété de OU






</td>
</tr>
<tr >

<td >







A | (~A) = 1






</td>

<td >







Propriété de OU






</td>
</tr>
<tr >

<td >







A& A= A






</td>

<td >







Propriété de ET






</td>
</tr>
<tr >

<td >







A & (~A) = 0






</td>

<td >







Propriété de ET






</td>
</tr>
<tr >

<td >







~(~A) = A






</td>

<td >







Inverse






</td>
</tr>
<tr >

<td >







~(A | B) = (~A) & (~B)






</td>

<td >







Théorème De Morgan






</td>
</tr>
<tr >

<td >







~(A & B) = (~A) | (~B)






</td>

<td >







Théorème De Morgan






</td>
</tr>
</tbody>
</table>



## Opérations


<table > 
<tbody >
<tr >

<td >







Opération






</td>

<td >







Signification






</td>
</tr>
<tr >

<td >







==






</td>

<td >







Comparaison






</td>
</tr>
<tr >

<td >







<=






</td>

<td >







Inférieur ou égale à






</td>
</tr>
<tr >

<td >







>=






</td>

<td >







Supérieur ou égale à






</td>
</tr>
<tr >

<td >







!=






</td>

<td >







Pas égale à






</td>
</tr>
<tr >

<td >







<<






</td>

<td >







Décalage à gauche






</td>
</tr>
<tr >

<td >







>>






</td>

<td >







Décalage à droite






</td>
</tr>
<tr >

<td >







++






</td>

<td >







Incrémenter






</td>
</tr>
<tr >

<td >







--






</td>

<td >







Décroitre






</td>
</tr>
<tr >

<td >







&&






</td>

<td >







ET booléen






</td>
</tr>
<tr >

<td >







||






</td>

<td >







OU booléen






</td>
</tr>
<tr >

<td >







+=






</td>

<td >







Ajouter une valeur à






</td>
</tr>
<tr >

<td >







-=






</td>

<td >







Soustraire une valeur à






</td>
</tr>
<tr >

<td >







*=






</td>

<td >







Multiplier une valeur à






</td>
</tr>
<tr >

<td >







/=






</td>

<td >







Diviser une valeur à






</td>
</tr>
<tr >

<td >







|=






</td>

<td >







OU une valeur à






</td>
</tr>
<tr >

<td >







&=






</td>

<td >







ET une valeur à






</td>
</tr>
<tr >

<td >







^=






</td>

<td >







OU EXCLUSIF une valeur à






</td>
</tr>
<tr >

<td >







<<=






</td>

<td >







Décaler une valeur à gauche






</td>
</tr>
<tr >

<td >







>>=






</td>

<td >







Décaler une valeur à droite






</td>
</tr>
<tr >

<td >







%=






</td>

<td >







Modulo une valeur à






</td>
</tr>
<tr >

<td >







->






</td>

<td >







Pointer à une structure






</td>
</tr>
</tbody>
</table>



## Opération sur les registres


<table >
<tbody >
<tr >

<td >









Opération sur les registres






</td>
</tr>
<tr >

<td >







register |= (1<<x); // mettra le x_ème bit à 1 (x=0 à 31)

Explication : "1" décalé "x" fois avec l'instruction "<<", quelque soit la valeur du x_ème bit du registre (0 ou 1) on a (1 OU 0 = 1) et (1 OU 1 = 1)






</td>
</tr>
<tr >

<td >







register &= ~(1<<x); // mettra le x_ème bit à 0 (x=0 à 31)






</td>
</tr>
<tr >

<td >







data = register & (1<<x); // isoler le x_ème bit (x=0 à 31)






</td>
</tr>
<tr >

<td >







register ^= (1<<x); // complémenter le x_ème bit (x=0 à 31)






</td>
</tr>
</tbody>
</table>



## Général








<table > 
<tbody >
<tr >

<td >







Keyword






</td>

<td >







Meaning






</td>
</tr>
<tr >

<td >







__asm






</td>

<td >







Specify a function is written in assembly code (specific to ARM KeilTMuVision®)






</td>
</tr>
<tr >

<td >







auto






</td>

<td >







Specifies a variable as automatic (created on the stack)






</td>
</tr>
<tr >

<td >







break






</td>

<td >







Causes the program control structure to finish






</td>
</tr>
<tr >

<td >







case






</td>

<td >







One possibility within a switch statement






</td>
</tr>
<tr >

<td >







char






</td>

<td >







Defines a number with a precision of 8 bits






</td>
</tr>
<tr >

<td >







const






</td>

<td >







Defines parameter as constant in ROM, and defines a local parameter as fixed value






</td>
</tr>
<tr >

<td >







continue






</td>

<td >







Causes the program to go to beginning of loop






</td>
</tr>
<tr >

<td >







default






</td>

<td >







Used in switch statement for all other cases






</td>
</tr>
<tr >

<td >







do






</td>

<td >







Used for creating program loops






</td>
</tr>
<tr >

<td >







double






</td>

<td >







Specifies variable as double precision floating point






</td>
</tr>
<tr >

<td >







else






</td>

<td >







Alternative part of a conditional






</td>
</tr>
<tr >

<td >







extern






</td>

<td >







Defined in another module






</td>
</tr>
<tr >

<td >







float






</td>

<td >







Specifies variable as single precision floating point






</td>
</tr>
<tr >

<td >







for






</td>

<td >







Utilisé pour créer un boucle






</td>
</tr>
<tr >

<td >







goto






</td>

<td >







Passer à emplacement spécifique (label)






</td>
</tr>
<tr >

<td >







if






</td>

<td >







Structure de contrôle conditionnelle






</td>
</tr>
<tr >

<td >







int






</td>

<td >







Defines a number with a precision that will vary from compiler to compiler






</td>
</tr>
<tr >

<td >







long






</td>

<td >







Defines a number with a precision of 32 bits






</td>
</tr>
<tr >

<td >







register






</td>

<td >







Specifies how to implement a local






</td>
</tr>
<tr >

<td >







return






</td>

<td >







Leave function






</td>
</tr>
<tr >

<td >







short






</td>

<td >







Defines a number with a precision of 16 bits






</td>
</tr>
<tr >

<td >







signed






</td>

<td >







Specifies variable as signed (default)






</td>
</tr>
<tr >

<td >







sizeof






</td>

<td >







Built-in function returns the size of an object






</td>
</tr>
<tr >

<td >







static






</td>

<td >







Stored permanently in memory, accessed locally






</td>
</tr>
<tr >

<td >







struct






</td>

<td >







Used for creating data structures






</td>
</tr>
<tr >

<td >







switch






</td>

<td >







Complex conditional control structure






</td>
</tr>
<tr >

<td >







typedef






</td>

<td >







Used to create new data types






</td>
</tr>
<tr >

<td >







unsigned






</td>

<td >







Always greater than or equal to zero






</td>
</tr>
<tr >

<td >







void






</td>

<td >







Used in parameter list to mean no parameter






</td>
</tr>
<tr >

<td >







volatile






</td>

<td >







Can change implicitly outside the direct action of the software.






</td>
</tr>
<tr >

<td >







while






</td>

<td >







Utilisé pour créer un boucle






</td>
</tr>
</tbody>
</table>

