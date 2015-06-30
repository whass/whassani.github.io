title: "Latex : Vérifier si un paramètre est vide ou pas"
date: 2015-02-06
categories: 
- Linux


Supposons qu'on veuille tester si le paramètre #1 est vide ou pas.

Vous pouvez utiliser le code suivant :

    
    \usepackage{ifthen}
    \ifthenelse{\equal{#1}{}}{VIDE.}{NON-VIDE.}


Ou bien :

    
    \ifx{#1}%
      % #1 est vide
    \else
      % #1 n'est pas vide
    \fi



