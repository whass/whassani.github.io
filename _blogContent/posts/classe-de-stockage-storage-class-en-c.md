title: Classe de stockage (storage class) en C
date: 2015-02-18
categories: 
- Embedded
tags:
- auto
- extern
- register
- static
- storage class


Chaque variable en C a deux propriétés : type et classe de stockage. Le type fait référence aux types de données des variables (entier, virgule flottante, caractère, etc.). La classe de stockage determine la durée de vie d'une variable.

Il existent 4 types de classe de stockage :



	
  1. automatic : pour les variables locales ;

	
  2. external : déclare une variable sans la définir ;

	
  3. static : rend une définition de variable persistante.

	
  4. register : demande au compilateur de faire tout son possible pour utiliser un registre processeur pour cette variable ;


Les classes static et extern sont, de loin, les plus utilisées. register est d'une utilité limitée, et auto est maintenant obsolète.


## auto


Les variable déclarées à l'intérieur d'une fonction est automatic par défaut. Ces variables sont aussi connues sous le nom de local du fait qu'elle n'ont aucun effet à l'extérieur de la fonction dans lesquelles elles sont définies.

Comme les variables qui se trouve à l'intérieur d'une fonction sont par défaut automatique, le mot clé automatic est rarement utilisé.


## extern


Les variables externes peuvent être utilisées par n'importe quelle fonction. Elles sont connues sous le nom de variable globale. Les variables déclarées en-dehors de toutes les fonctions sont considérées comment externes.

N.B : Dans le cas où on a un programme qui contient plusieurs fichiers, si une variable globale est déclarée dans le fichier 1 et utilisée dans le fichier 2, le compilateur va afficher une erreur. Pour résoudre ce problème, le mot-clé _extern_ est utilisé dans le fichier 2 pour spécifier que cette dernière est globale et et déclarée dans un autre fichier.




## register


Les variables registres sont similaires aux variables automatiques et n'existent que dans certaines fonctions seulement.

Si le compilateur trouve une variable _register_, il va essayer de la stocker dans un registre du microprocesseur plutôt que dans la mémoire. Les variables stockées dans un registre sans plus rapide d'accès qu'une mémoire.

Dans la cas des programmes très grand, les variables utilisées dans les boucles et les paramètres des fonctions sont déclarées comme variables registres.

Comme le nombre de registre est limitées si le nombre de variable registered dépasse le nombre de resigners disponible, la variable va être automatiquement stockée dans une case mémoire.




## static


La valeur de la variable statique persiste jusqu'à la fin du programme. Une variable peut être déclarée statique utilisant le mot clé: static.

L'effet de la classe 'static' dépend de l'endroit où l'objet est déclaré :



	
  * _Objet local à une fonction_ : la valeur de la variable sera persistante entre les différents appels de la fonction. La variable ne sera visible que dans la fonction, mais ne sera pas réinitialisée à chaque appel de la fonction. L'intérêt est de garantir une certaine encapsulation, afin d'éviter des usages multiples d'une variable globale. Qui plus est, cela permet d'avoir plusieurs fois le même nom, dans des fonctions différentes.


example :

    
    #include 
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
    


Résultat d'exécution du code ci dessus :

    
    i vaut 1 et j vaut 1.
    i vaut 2 et j vaut 1.
    i vaut 3 et j vaut 1.
    





	
  * _Objet global et fonction_ : comme une variable globale est déjà persistante, le mot-clé `static` aura pour effet de limiter la portée de la variable ou de la fonction au seul fichier où elle est déclarée, toujours dans le but de garantir un certain niveau d'encapsulation.


N.B : Une variable de classe statique est initialisée au moment de la compilation à zéro par défaut (contrairement aux variables dynamiques qui ont une valeur initiale indéterminée). Elle peut être initialisée explicitement à n'importe quelle valeur _constante_.
