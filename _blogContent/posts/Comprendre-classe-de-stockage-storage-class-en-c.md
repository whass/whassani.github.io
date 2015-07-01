title: Comprendre les Classes de stockages (storage class) en C
date: 2015-02-18
description: Chaque variable en C a deux propriétés, type et classe de stockage. Le type fait référence aux types de données des variables (entier, virgule flottante, caractère, etc.). La classe de stockage détermine la durée de vie d'une variable.
lang: fr
categories: 
- C-C++

tags:
- auto
- extern
- register
- static
- storage class


Chaque variable en C a deux propriétés : 

* type 
* classe de stockage

Le type fait référence aux types de données des variables (entier, virgule flottante, caractère, etc.). La classe de stockage détermine la durée de vie d'une variable.

Il existent 4 types de classe de stockage :

  1. *automatic* : pour les variables locales;

	
  2. *external* : déclare une variable sans la définir;

	
  3. *static* : rend une définition de variable persistante.

	
  4. *register* : demande au compilateur de faire tout son possible pour utiliser un registre processeur pour cette variable;


Les classes *static* et *extern* sont, de loin, les plus utilisées. *register* est d'une utilité limitée, et *auto* est maintenant obsolète.


## auto


Les variables déclarées à l'intérieur d'une fonction sont *automatic* par défaut. Ces variables sont aussi connues sous le nom de local du fait qu'elles n'ont aucun effet à l'extérieur de la fonction dans lesquelles elles sont définies.

Comme les variables qui se trouve à l'intérieur d'une fonction sont par défaut automatique, le mot clé *automatic* est rarement utilisé.


## extern


Les variables externes peuvent être utilisées par n'importe quelle fonction. Elles sont connues sous le nom de variable globale. 

Les variables déclarées en-dehors de toutes les fonctions sont considérées comment externes.

Cela dit, soyez prudent, si vous mettez le mot-clé *extern* le compilateur va automatiquement essayer de chercher la variable dans un autre fichier !!!

Donc, si vous souhaitez définir une variable globale, définissez-là en-dehors de toutes fonctions. Et si, en plus de cela, vous souhaitez l'utiliser dans un autre fichier, à ce moment là, mettez le nom de variable précéder par le mot-clé *extern*   

**N.B**

Exemple :
  
    extern int var;
    int main(void)
    {
      var = 10;
      return 0;
    }

Affichera une erreur de compilation, par contre :

    #include "unFichier.h"    
    extern int var;
    int main(void)
    {
      var = 10;
      return 0;
    }

compilera correctement.

## register


Les variables registres sont similaires aux variables automatiques et n'existent que dans certaines fonctions seulement.

Si le compilateur trouve une variable *register*, il va essayer de la stocker dans un registre du microprocesseur plutôt que dans la mémoire. Les variables stockées dans un registre sans plus rapide d'accès qu'une mémoire.

Dans la cas des programmes très grand, les variables utilisées dans les boucles et les paramètres des fonctions sont déclarées comme variables registres.

Comme le nombre de registre est limitées si le nombre de variable *register* dépasse le nombre de *registres* disponible, la variable va être automatiquement stockée dans une case mémoire.




## static


La valeur de la variable statique persiste jusqu'à la fin du programme. Une variable peut être déclarée statique utilisant le mot clé: *static*.

L'effet de la classe *static* dépend de l'endroit où l'objet est déclaré :

	
  * _Objet local à une fonction_: la valeur de la variable sera persistante entre les différents appels de la fonction. La variable ne sera visible que dans la fonction, mais ne sera pas réinitialisée à chaque appel de la fonction. L'intérêt est de garantir une certaine encapsulation, afin d'éviter des usages multiples d'une variable globale. Qui plus est, cela permet d'avoir plusieurs fois le même nom, dans des fonctions différentes.


exemple :

    
    #include <stdio.h>
    void f(void)
    {
        static int i = 0; /* i sera initialisée à 0 à la compilation seulement */
        int j = 0; /* j sera initialisée à chaque appel de f */;
        i++;
        j++;
        printf("i vaut %d et j vaut %d.\n", i, j);
    }
     
    int main(void)
    {
        f();
        f();
        f();
        return 0;
    }
    


Résultat d'exécution du code ci dessus :

    
    i vaut 1 et j vaut 1.
    i vaut 2 et j vaut 1.
    i vaut 3 et j vaut 1.
    


	
  * _Objet global et fonction_: comme une variable globale est déjà persistante, le mot-clé *static* aura pour effet de limiter la portée de la variable ou de la fonction au seul fichier où elle est déclarée, toujours dans le but de garantir un certain niveau d'encapsulation.


**N.B** : Une variable de classe statique est initialisée au moment de la compilation à zéro par défaut (contrairement aux variables dynamiques qui ont une valeur initiale indéterminée). Elle peut être initialisée explicitement à n'importe quelle valeur _constante_.
