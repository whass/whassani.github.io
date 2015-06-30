date: 2014-02-14
title: 'C pour l''embarqué : Opération sur les registres'
categories: 
- Embedded


[TOC]

## Opérations de comparaisons

| Opération | Signification                |
|-----------|------------------------------|
| ==        | Egale à                   | 
| <=        | Inférieur ou égale à         |
| >=        | Supérieur ou égale à         | 
| !=        | Différent de                 | 
| >        | Supérieur à          | 
| <        |  Diviser une valeur à        | 


## Opérations de tests logiques

| &&        | ET logique                   | 
| ||        | OU logique                   | 
| ^=        |  OU EXCLUSIF une valeur à    | 


| <<        | Décalage à gauche            | 
| >>        | Décalage à droite            | 
| ++        | Incrémenter                  | 
| --        | Decrémenter                  | 

| +=        | Ajouter une valeur à         | 
| -=        | Soustraire une valeur à      | 
| *=        |  Multiplier une valeur à     | 
| /=        |  Diviser une valeur à        | 
| |=        |  OU une valeur à             | 
| &=        |  ET une valeur à             | 

| <<=       |  Décaler une valeur à gauche | 
| >>=       |  Décaler une valeur à droite | 
| %=        |  Modulo une valeur à         | 
| ->        |  Pointer sur une structure   | 

| Opération | Signification                |
|-----------|------------------------------|
| =        | affectation                  |
| ?        | Sélection         |
| !        |   Non Logique                  | 
| ~        |   Le complément à 1             | 
| +        |   Addition             | 
| -        | Soustraction                  | 
| *        |  Multiplicateur ou référence à un poiteur                   | 
| /        | Division                   | 
| %        |   Modulo, reste de la division              | 
| |       |   OU logique                    | 
| &        | ET logique, ou Adresse de          | 
| ^         |  OU EXCLUSIF Logique      | 
| .        |   Utilisé pour accéder à une partie d'une structure    | 


## Lois fondamentale de bool


| Loi                             | Propriété          |
|---------------------------------|--------------------|
| `A & B = B & A`                   | Loi commutative    |
| `A | B = B | A`                   | Loi commutative    |
| (A & B) & C = A & (B & C)       | Loi associative    | 
| (A | B) | C = A | (B | C)       | Loi associative    | 
| (A | B) & C = (A & C) | (B & C) | Loi distributive   | 
| (A & B) | C = (A | C) & (B | C) | Loi distributive   | 
| A & 0 = 0                       | Identité de 0      | 
| A | 0 = A                       | Identité de 0      | 
| A & 1 = A                       | Identité de 1      | 
| A | 1 = 1                       | Identité de 1      | 
| A | A = A                       | Propriété de OU    | 
| A | (~A) = 1                    | Propriété de OU    | 
| A & A= A                        | Propriété de ET    | 
| A & (~A) = 0                    | Propriété de ET    | 
| ~(~A) = A                       | Inverse            | 
| ~(A | B) = (~A) & (~B)          | Théorème De Morgan | 
| ~(A & B) = (~A) | (~B)          | Théorème De Morgan | 


## Opération sur les registres

Soit REG un registre quelconque, pour :

1. **Mise à 1 du *x_ème* bit**

        `REG |=(1<<x);`

     *Explication* : « 1 » décalé « x » fois avec l’instruction « <<« , quelque soit la valeur du x_ème bit du registre (0 ou 1) on a (1 OU 0 = 1) et (1 OU 1 = 1)

2. **Mise à 0 du *x_ème* bit** 

         `register &= ~(1<<x);` 

3. **Valeur du *x_ème* bit**

         `data = register & (1<<x);`

4. **Complément à 1 du *x_ème* bit** 

         `register ^= (1<<x);`

  

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

