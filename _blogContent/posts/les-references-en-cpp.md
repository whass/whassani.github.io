title: Les références en C++. Plusieurs noms, mais une seule variable !
date: 2015-03-05
description: Soit une variable utilisée dans deux parties très différentes du programme ou des parties créées par différents programmeurs. Sachant que cette variable n'a qu'une seule case mémoire, alors, comment faire pour que le nom donné par le programmeur A et celui donné par le programmeur B pointe vers vers la même variable !
categories:
- C-C++

Soit une variable utilisée dans deux parties très différentes du programme des parties ou créées par différents programmeurs. Dans une des parties, un des programmeurs va s'occuper de la déclaration de la variable alors que l'autre programmeur va juste l'afficher. Ce deuxième programmeur aura juste besoin d'un accès à la variable et un alias sera donc suffisant.

Pour cela, il faut savoir qu'une variable n'a qu'une seule case mémoire mais peut avoir plusieurs références (étiquettes), donc plusieurs noms.

Au niveau du code, on utilise une esperluette (&) pour déclarer une référence sur une variable.

    int ageUtilisateur(16); //Déclaration d'une variable.
    int& maVariable(ageUtilisateur); //Déclaration d'une référence nommée maVariable qui est accrochée à la variable ageUtilisateur



