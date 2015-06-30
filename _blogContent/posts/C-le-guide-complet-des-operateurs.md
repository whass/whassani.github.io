title: " C : Le guide complet des opérateurs"
date: 2014-05-14
lang: fr
description: Le C est un outils primordial si vous voulez faire de l'embarqué, un outils incontournable. Cet article propose un guide complet des opérateurs utilisés en C à savoir, les opérateus de calcul, d'assignation, d'incrémentation, de comparaison, logique, etc. Il est à utiliser comme un aide mémoire.
categories: 
- Embedded


**Table des matières :**

[TOC]


## Les opérateurs de calcul

Les opérateurs de calcul permettent de modifier mathématiquement la valeur d'une variable.

| Opérateur | Dénomination | Effet | Exemple | Résultat (avec x valant 7) |
|-----------|--------------|-------|---------|----------------------------|
| + | opérateur d'addition | Ajoute deux valeurs | x+3 | 10 |
| - | opérateur de soustraction | Soustrait deux valeurs | x-3 | 4 |
| * | opérateur de multiplication | Multiplie deux valeurs | x*3 | 21 |
| / | opérateur de division | Divise deux valeurs | x/3 | 2.3333333 |
| = | opérateur d'affectation | Affecte une valeur à une variable | x=3 | Met la valeur 3 dans la variable x |

## Les opérateurs d'assignation

Ces opérateurs permettent de simplifier des opérations telles que _ajouter une valeur dans une variable et stocker le résultat dans la variable_. Une telle opérations s'écrirait habituellement de la façon suivante par exemple : _x=x+2_ 
Avec les opérateurs d'assignation il est possible d'écrire cette opération sous la forme suivante : _x+=2_ 
Ainsi, si la valeur de x était 7 avant opération, elle sera de 9 après...

Les autres opérateurs du même type sont les suivants :

| Opérateur | Effet |
|-----------|-------|
| **+=** | additionne deux valeurs et stocke le résultat dans la variable (à gauche) |
| **-=** | soustrait deux valeurs et stocke le résultat dans la variable |
| ***=** | multiplie deux valeurs et stocke le résultat dans la variable |
| **/=** | divise deux valeurs et stocke le résultat dans la variable |


<a name="incrémentation" class="ancre"></a>

## Les opérateurs d'incrémentation

Ce type d'opérateur permet de facilement augmenter ou diminuer d'une unité une variable. Ces opérateurs sont très utiles pour des structures telles que des boucles, qui ont besoin d'un compteur (variable qui augmente de un en un).

Un opérateur de type _x++_ permet de remplacer des notations lourdes telles que _x=x+1_ ou bien _x+=1_.

| Opérateur | Dénomination | Effet | Syntaxe | Résultat (avec x valant 7) |
|-----------|--------------|-------|---------|----------------------------|
| **++** | Incrémentation | Augmente d'une unité la variable | x++ | 8 |
| **--** | Décrémentation | Diminue d'une unité la variable | x-- | 6 |

<a name="comparaison" class="ancre"></a>

## Les opérateurs de comparaison

| Opérateur | Dénomination | Effet | Exemple | Résultat (avec x valant 7) |
|-----------|--------------|-------|---------|----------------------------|
| == 
**A ne pas confondre avec le signe d'affectation (=) !** | opérateur d'égalité | Compare deux valeurs et vérifie leur égalité | x==3 | Retourne 1 si x est égal à 3, sinon 0 |
| < | opérateur d'infériorité stricte | Vérifie qu'une variable est strictement inférieure à une valeur | x<3 | Retourne 1 si x est inférieur à 3, sinon 0 |
| <= | opérateur d'infériorité | Vérifie qu'une variable est inférieure ou égale à une valeur | x<=3 | Retourne 1 si x est inférieur ou égal à 3, sinon 0 |
| > | opérateur de supériorité stricte | Vérifie qu'une variable est strictement supérieure à une valeur | x>3 | Retourne 1 si x est supérieur à 3, sinon 0 |
| >= | opérateur de supériorité | Vérifie qu'une variable est supérieure ou égale à une valeur | x>=3 | Retourne 1 si x est supérieur ou égal à 3, sinon 0 |
| != | opérateur de différence | Vérifie qu'une variable est différente d'une valeur | x!=3 | Retourne 1 si x est différent de 3, sinon 0 |

<a name="logiques" class="ancre"></a>

## Les opérateurs logiques (booléens)

Ce type d'opérateur permet de vérifier si plusieurs conditions sont vraies :

| Opérateur | Dénomination | Effet | Syntaxe |
|-----------|--------------|-------|---------|
| **||** | OU logique | Vérifie qu'une des conditions est réalisée | ((condition1)||(condition2)) |
| **&&** | ET logique | Vérifie que toutes les conditions sont réalisées | ((condition1)&&(condition2)) |
| **!** | NON logique | Inverse l'état d'une variable booléenne (retourne la valeur 1 si la variable vaut 0, 0 si elle vaut 1) | (!condition) |

<a name="bitabit" class="ancre"></a>

## (Les opérateurs bit-à-bit)

Si vous ne comprenez pas ces opérateurs cela n'est pas important, vous n'en aurez probablement pas l'utilité. Pour ceux qui voudraient comprendre, rendez-vous aux chapitres suivants :

*   [Compréhension du binaire](/contents/95-le-codage-binaire)
*   [Représentation des données](/contents/100-representation-des-nombres-entiers-et-reels)
*   [Instructions arithmétiques et logiques en assembleur](/contents/18-instructions-arithmetiques-et-logiques-en-assembleur)

Ce type d'opérateur traite ses opérandes comme des données binaires, plutôt que des données décimales, hexadécimales ou octales. Ces opérateurs traitent ces données selon leur représentation binaire mais retournent des valeurs numériques standard dans leur format d'origine.

Les opérateurs suivants effectuent des opérations bit-à-bit, c'est-à-dire avec des bits de même poids.

| Opérateur | Dénomination | Effet | Syntaxe | Résultat |
|-----------|--------------|-------|---------|----------|
| **&** | ET bit-à-bit | Retourne 1 si les deux bits de même poids sont à 1 | 9 & 12 (1001 & 1100) | 8 (1000) |
| **|** | OU bit-à-bit | Retourne 1 si l'un ou l'autre des deux bits de même poids est à 1 (ou les deux) | 9 | 12 (1001 | 1100) | 13 (1101) |
| **^** | OU exclusif bit-à-bit | Retourne 1 si l'un des deux bits de même poids est à 1 (mais pas les deux) | 9 ^ 12 (1001 ^ 1100) | 5 (0101) |

<a name="rotbit" class="ancre"></a>

## (Les opérateurs de rotation de bit)

Si vous ne comprenez pas ces opérateurs cela n'est pas important, vous n'en aurez probablement pas l'utilité. Pour ceux qui voudraient comprendre, rendez-vous aux chapitres suivants :

*   [Compréhension du binaire](/contents/95-le-codage-binaire)
*   [Représentation des données](/contents/100-representation-des-nombres-entiers-et-reels)
*   [Instructions arithmétiques et logiques en assembleur](/contents/18-instructions-arithmetiques-et-logiques-en-assembleur)

Ce type d'opérateur traite ses opérandes comme des données binaires d'une longueur de 32 bits, plutôt que des données décimales, hexadécimales ou octales. Ces opérateurs traitent ces données selon leur représentation binaire mais retournent des valeurs numériques standard dans leur format d'origine.

Les opérateurs suivants effectuent des rotations sur les bits, c'est-à-dire qu'ils décalent chacun des bits d'un nombre de bits vers la gauche ou vers la droite. La première opérande désigne la donnée sur laquelle on va faire le décalage, la seconde désigne le nombre de bits duquel elle va être décalée.

| Opérateur | Dénomination | Effet | Syntaxe | Résultat |
|-----------|--------------|-------|---------|----------|
| **<<** | Rotation à gauche | Décale les bits vers la gauche (multiplie par 2 à chaque décalage). Les zéros qui sortent à gauche sont perdus, tandis que des zéros sont insérés à droite | 6 << 1 (110 << 1) | 12 (1100) |
| **>>** | Rotation à droite avec conservation du signe | Décale les bits vers la droite (divise par 2 à chaque décalage). Les zéros qui sortent à droite sont perdus, tandis que le bit non nul de poids plus fort est recopié à gauche | 6 >> 1 (0110 >> 1) | 3 (0011) |
| **>>>** | Rotation à droite avec remplissage de zéros | Décale les bits vers la droite (divise par 2 à chaque décalage). Les zéros qui sortent à droite sont perdus, tandis que des zéros sont insérés à gauche | 6 >>> 1 (0110 >>> 1) | 3 (0011) |


