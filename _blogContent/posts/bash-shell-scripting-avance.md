title: "Bash Shell Scripting II - Niveau avancé"
date: 2015-02-23
description: Cet article est la suite du Bash Shell Scripting I destiné à ceux ceux qui souhaitent aller plus loin. Il est déidié à la création de script bash pour la manipulation de chaînes, la logique booléenne, les boucle, débogage, etc.
categories: 
- Linux

**Tables des matières**

[TOC]

## manipulation de chaînes
Une variable de type chaîne contient une séquence de caractères de texte. Elle peut inclure des lettres, chiffres, symboles et signes de ponctuation. Quelques exemples: ABCDE, 123, 123, ABCDE ABCDE-123, et 123% = acbde

Les opérateurs de chaînes comprennent ceux qui font la comparaison, le tri, et de trouver la longueur. l'utilisation de certains opérateurs de base sont illustrés ci-après :
	
* [String1 > string2] Compare l'ordre de tri des string1 et string2.
* [String1 = string2] Compare les caractères dans chaîne1 avec les caractères string2.
* myLen1 = $ {#string1} Enregistre la longueur de string1 dans la variable myLen1.


Pour extraire le premier caractère d'une chaîne, nous pouvons préciser:

$ {chaine:0: 1} Ici 0 est le décalage dans la chaîne, où, l'extraction doit commencer et 1 est le nombre de caractères à extraire.

(.) Pour extraire tous les caractères d'une chaîne après un point, utiliser l'expression suivante:

    
	${string#*.}


## expressions booléennes

Les expressions booléennes ont pour résultat  TRUE ou FALSE, et les résultats sont obtenus en utilisant les différents opérateurs booléens énumérés dans le tableau.
	
* && **ET** L'action sera effectuée uniquement si les deux conditions sont satisfaites.
* ||   **OU** L'action sera effectuée que si l'une des conditions est satisfaite.
* !     **PAS** L'action sera effectuée uniquement si la condition n'est pas satisfaite.


**N.B** :	

* si vous avez plusieurs conditions qui s'enchaînent avec l'opérateur &&,   le traitement s'arrête dès que la condition est évaluée à False. Par exemple, si vous avez un && B && C et A est vrai, mais B est faux, C ne sera jamais exécutée.

* De même, si vous utilisez l'opérateur ||, le traitement s'arrête dès que quelque chose est vrai. Par exemple, si vous avez A || B || C et A est faux et B est vrai, C ne sera jamais exécutée.




### Tests dans les expressions booléennes


Nous pouvons utiliser ces expressions lorsque vous travaillez avec plusieurs types de données y compris les chaînes ou des nombres ainsi que les fichiers. Par exemple, pour vérifier si un fichier existe, utiliser le test conditionnelle suivante:


	[-e <Nom du fichier>]


De même, pour vérifier si la valeur de nombre1 est supérieur à la valeur de nombre2, utiliser le test conditionnelle suivante:

    
	[$nombre1 -gt $nombre2]


l'opérateur -gt retourne TRUE si nombre1 est supérieur à nombre2.


### La déclaration de cas (case)


La déclaration de cas est utilisée dans les scénarios où la valeur réelle d'une variable peut conduire à différents chemins d'exécution. La déclarations de cas sont souvent utilisés pour traiter les options de ligne de commande.

Voici quelques-uns des avantages de l'utilisation de la déclaration de cas:

* Il est plus facile à lire et à écrire.
* C'est une bonne alternative à multi niveau imbriquée if-then-else-fi.
* Il vous permet de comparer une variable contre plusieurs valeurs à la fois.
* Cela réduit la complexité d'un programme.


**Structure de la déclaration de cas (case)**


Voici la structure de base de la déclaration de cas:

    
	case expression in
	    pattern1) "exécuter des commandes";;
	    pattern2) "exécuter des commandes";;
	    pattern3) "exécuter des commandes";;
	    pattern4) "exécuter des commandes";;
	    *) "Exécuter des commandes par défaut ou rien";;
	esac




## Les boucles


En utilisant les boucles, vous pouvez exécuter une ou plusieurs lignes de code de façon répétitive. Habituellement, vous faites cela jusqu'à ce qu'à qu'une condition d'arrêt soit satisfaite.

Trois types de boucles sont souvent utilisés dans la plupart des langages de programmation:

* for
* while
* until

### La boucle "for"


La boucle **for** opère sur chaque élément d'une liste d'éléments. La syntaxe de la boucle est:

    
	for variable in list
		do "exécuter une itération pour chaque élément dans la liste jusqu'à ce que la liste est terminée"
	done
	

exemple :
    
	#!/bin/bash 
	sum=0
	for i in 1 2 3 4
		sum = $(($sum+$i))
	done
	echo "la somme des $i est $sum"
	


### La boucle while

La boucle while répète un ensemble de déclarations tant que la commande de contrôle renvoie true. La syntaxe est:
    
	while "condition est vraie"
		do "commandes à executer"
		----
	done


exemple :

    
	#!/bin/bash 
	echo "entrer un nombre"
	read nm
	fact=1
	i=0
	while [$i -le $nm]
	do
	    fact = $(($fact*$i))
	    i = $(($i+1))
	done
	echo "le factoriel de $nm est $fact"
	



### La boucle until


La boucle **until** répète un ensemble de déclarations tant que la commande de contrôle est fausse. Ainsi, il est essentiellement à l'opposé de la boucle while. La syntaxe est:

    
    until "la condition est fausse"
    do
         "Commandes d'exécution"
         ----
    done


exemple :

    
    #!/bin/bash 
    echo "entrer un nombre"
    read nm
    mx=10
    until [$nm -gt $mx]
    do
        nm = $(($nm+2))
    done    




## Introduction au débogage de script


Tout en travaillant avec des scripts et des commandes, vous pouvez rencontrer des erreurs. Ceux-ci peuvent être due à une erreur dans le script, comme une syntaxe incorrecte, ou d'autres sources comme un fichier manquant ou la permission insuffisante pour effectuer une opération. Ces erreurs peuvent être signalées avec un code d'erreur spécifique. 

Alors, comment allez-vous identifier et fixer une erreur?

Débogage vous aide à détecter et de résoudre de telles erreurs, et est l'une des tâches les plus importantes d'un administrateur système.


### En savoir plus sur le débogage de script
Avant de corriger une erreur (ou bug), il est essentiel de connaître sa source.
En bash shell script, vous pouvez exécuter un script en mode débogage en faisant
    
    bash -x ./script_file.sh


Le mode de débogage permet d'identifier l'erreur parce que:

* Il retrace et préfixes chaque commande avec le caractère +.
* Il affiche chaque commande avant de l'exécuter.
* Il peut déboguer que certaines parties d'un script (si désiré) avec:
* set -x # active le débogage
...
* set +x # désactive le débogage

exemple :

*Sans débogage

    #! /bin/bash
    echo "entrer votre nom avec votre titre"
    read nom
    echo "votre titre est ${nom:0:3}"
    echo "votre nom est ${nom#*.}"
	
	

sortie :
    
    entrer votre nom avec votre titre 
    Mr Blender 
    votre titre est Mr 
    votre nom est Mr Blender


*Avec débogage

    #!/bin/bash 
    echo "entrer votre nom avec votre titre"
    set -x
    read nom
    echo "votre titre est ${nom:0:3}"
    echo "votre nom est ${nom#*.}"
    set +x

sortie :
    
    entrer votre nom avec votre titre 
    + read nom 
    Mr Blender 
    + echo 'votre titre est Mr ' 
    votre titre est Mr 
    + echo 'votre nom est Mr Blender' 
    votre nom est Mr Blender 
    + set +x




### Redirection erreurs vers un fichier ou un écran

Dans UNIX / Linux, tous les programmes qui s'exécutent donnent lieu à trois flux de fichiers qui sont:
	
  1. **stdin** (0) entrée standard, par défaut le clavier / terminal pour exécuter des programmes depuis la ligne de commande.

	
  2. **stdout** (1) sortie standard , par défaut, l'écran pour les programmes exécuté depuis la ligne de commande

	
  3. **stderr** (2) Erreur standard, où les messages d'erreur de sortie sont affichés ou sauvegardés


Utilisation de la redirection nous permet de sauvegarder les flux de sortie stdout et stderr dans un fichier ou deux fichiers séparés pour une analyse ultérieure après l'exécution d'un programme ou une commande.

exemple :

Enregistrer le script ci-après dans un fichier nom "ioscript.sh"

    
    #!/bin/bash 
    echo "entrer votre nom avec votre titre"
    read nom
    echo "votre titre est ${nom:0:3}
    echo "votre nom est ${nom#*.}"
    


sortie :

    entrer votre nom avec votre titre
    Mr Blender


Remarquez que l'exécution s'arrête au premier echo, car, une erreur a été introduite volontairement à la 4ème ligne (manque le " à la fin de la ligne).

***Pour rediriger*** le message d'erreur vers un fichier error.txt exécuter :

    
    $ bash ioscript.sh 2> error.txt


En lisant le ficher error.txt
    
    $ cat error.txt
    ioscript.sh: ligne 5: Caractère de fin de fichier (EOF) prématuré lors de la recherche du « " » correspondant ioscript.sh: ligne 6: Erreur de syntaxe : fin de fichier prématurée


Il nous signale bien que (") est manquant.