title: "Bash Shell Scripting I : Niveau débutant"
date: 2015-02-23
description: Une introduction complète des fonctionnalités les plus usuelles de l'incontournable Bash, à savoir, ses fonctionnalités et capacités, sa syntaxe, sa configiuration, utlisation interactive, etc.    
categories: 
- Linux

**Table des matières :**

[TOC]

### Fonctionnalités et capacités

Supposons que vous souhaitez rechercher un nom de fichier, vérifiez si le fichier associé existe, puis réagir en conséquence, l'affichage d'un message de confirmation ou non de l'existence du fichier. Si vous avez seulement besoin de le faire une fois, vous pouvez simplement taper une séquence de commandes sur un terminal. Toutefois, si vous devez le faire plusieurs fois, l'automatisation est la voie à suivre. Afin d'automatiser cela, vous aurez besoin d'apprendre comment écrire des scripts shell, le plus commun est bash.

Par exemple saisissant:

    
    find . -name "*.c" -ls


Cette ligne de commande permet d'accomplir la même chose que l'exécution d'un fichier de script contenant les lignes:

    
    #!/bin/bash
    find . -name "* .c" -ls


La première ligne du script, qui commence par #!, contient le chemin complet de l'interpréteur de commande (dans ce cas /bin/bash) qui doit être utilisé par le fichier.


#### Choix commande Shell

L'interpréteur de commandes est chargé de l'exécution des instructions de script. Les interpréteurs couramment utilisés sont :

  * /usr/bin/perl,
  * /bin/bash,
  * /bin/csh,
  * /usr/bin/python et
  * /bin/sh.


En déployant des scripts shell, en utilisant la ligne de commande devient un moyen efficace et rapide pour lancer des séquences complexes. Le fait que des scripts shell sont enregistrés dans un fichier facilite également la création de nouvelles variations du script avec plusieurs utilisateurs.

Linux offre un large choix; ce qui est disponible sur le système est listé dans /etc/shells. Les choix typiques sont:

	
  * /bin/sh
  * /bin/bash
  * /bin/tcsh
  * /bin/csh
  * /bin/ksh

La plupart des utilisateurs de Linux utilisent le shell bash par défaut.


#### **bash Scripts**


Écrivons un script bash simple qui affiche un message de deux lignes sur l'écran.

    
    $ cat > exscript.sh
       #! /bin/bash
       echo "BONJOUR"
       echo "MONDE"


et appuyez sur ENTER et CTRL-D pour enregistrer le fichier, ou tout simplement créer exscript.sh dans votre éditeur de texte favori.

Ensuite, tapez

    
    chmod +x exscript.sh


pour rendre le fichier exécutable. (La commande chmod + x rend le fichier exécutable pour tous les utilisateurs.) Vous pourrez ensuite lancer en tapant simplement

    
    ./exscript.sh


ou en faisant:

    
    $ bash exscript.sh
       BONJOUR
       MONDE


Notez que si vous utilisez la seconde forme, vous ne avez pas à rendre le fichier exécutable.


#### Utilisation interactive de l'utilisation des scripts bash


Maintenant, nous allons voir comment créer un exemple plus interactif en utilisant un script bash. L'utilisateur sera invité à entrer une valeur, qui est ensuite affichée sur l'écran. La valeur est mémorisée dans une variable temporaire, sname.

Nous pouvons référencer la valeur d'une variable de shell en utilisant un $ devant le nom de la variable, comme $ sname. Pour créer ce script, vous devez créer un fichier nommé ioscript.sh dans votre éditeur de texte favori avec le contenu suivant:

    
       #! /bin/bash
       # Lecture interactive des variables
       echo "ENTRER VOTRE NOM"
       read sname
       # Affichage des valeurs variables
       echo $sname


Une fois encore, le rendre exécutable en faisant chmod + x ioscript.sh.

Dans l'exemple ci-dessus, lorsque le ./ioscript.sh est exécuté, il demandera à l'utilisateur de saisir votre nom. L'utilisateur doit alors entrer une valeur et appuyez sur la touche Entrée. La valeur sera alors affichée.

Note complémentaire: Le hash-tag/dièse/nombre-signe (#) est utilisé pour démarrer commentaires dans le script et peut être placé n'importe où dans la ligne (le reste de la ligne est considéré comme un commentaire).


#### valeurs de retour


Tous les scripts shell génèrent une valeur de retour lors de la fin de l'exécution (la valeur peut être définie). Les valeurs de retour permettent de savoir si le script a été correctement exécuté ou pas. En outre, cela aide à déterminer comment ce processus se est arrêté et prendre les mesures appropriées à prendre, dans le succès ou l'échec.


#### Analyse des Valeurs de retour

Lorsqu'un script s'exécute, on peut vérifier s'il a échoué ou pas.

Par convention,
	
  * succès : 0,
  * échec : valuer non nulle.

Pour récupérer la variable de retour, il faut utiliser $? comme ceci :
    
    $ ls /etc/passwd
    /etc/passwd    
    $ echo $?
    0


Dans cet exemple, le système est capable de localiser le fichier /etc/passwd et renvoie une valeur de 0 pour indiquer le succès de l'opération;
	
  * la valeur de retour est toujours stockée dans la variable d'environnement $?.


### Syntaxe
#### Syntaxe de base et des caractères spéciaux

Scripts vous obliger à suivre une syntaxe de langage standard. Règles définissent comment définir des variables, construire, format, etc.

Ci-après certains usages de caractères spéciaux dans les scripts bash :
	
  * `#`  Utilisé pour ajouter un commentaire, sauf lorsqu'il est utilisé comme `\#`, ou `#!` lors du démarrage d'un script
	
  * `\`  Utilisés à la fin d'une ligne pour indiquer que la commande se poursuit à la ligne suivante
	
  * ;  Utilisé pour interpréter que ce qui suit comme une nouvelle commande

  * $ : Indique que ce qui suit est une variable
	
Notez que lorsque # est inséré au début d'une ligne de commentaire, toute la ligne est ignoré.


#### Commandes longues fractionnement sur des lignes multiples

Les utilisateurs ont parfois besoin de combiner plusieurs commandes et instructions et exécuter même les  exécuter conditionnellement. Cette méthode est appelée chaînage de commandes.

L'opérateur de concaténation (\) est utilisé pour concaténer des commandes sur plusieurs lignes.

Par exemple, vous souhaitez copier le fichier /var/ftp/pub/userdata/custdata/read server1.linux.com dans le répertoire /opt/oradba/master/abc sur server3.linux.co.in.

Pour effectuer cette action, vous pouvez écrire la commande en utilisant l'opérateur \ :
    
    scp abc@server1.linux.com: \
     /var/ftp/pub/userdata/custdata/read \
     abc@server3.linux.co.in: \
     /opt/oradba/master/abc/

La commande est divisé en plusieurs lignes pour qu'elle soit lisible et plus facile à comprendre.


#### Mettre plusieurs commandes sur une seule ligne

Parfois, vous pouvez regrouper plusieurs commandes sur une seule ligne. le ; (point-virgule) est utilisé pour séparer ces commandes et de les exécuter séquentiellement comme se ils avaient été tapé sur des lignes séparées.

Les trois commandes dans l'exemple suivant seront tous exécuter, même si ceux qui les précédentes échouent:
    
    $ make; make install; make clean

Cependant, vous pouvez vouloir annuler les commandes suivantes si l'on échoue. Vous pouvez le faire en utilisant l'opérateur && (et) comme dans:
    
    $ Make && make install && make clean

Si la première commande échoue la seconde ne sera jamais exécutée.

Un raffinement final est d'utiliser l'opérateur || (ou) comme dans:
    
    $ cat fichier1 || cat fichier2  || cat fichier3

Dans ce cas, vous continuez jusqu'à ce que quelque chose arrive et puis vous arrêtez l'exécution.

#### fonctions

Une fonction est un bloc de code qui implémente une série d'opérations. Les fonctions sont utiles pour exécuter des procédures plusieurs fois et peut-être avec des variables d'entrée variables.  L'utilisation des fonctions se fait  en deux étapes:

* Déclarer une fonction
* Appel d'une fonction

La déclaration de la fonction nécessite un nom pour l'invoquer. La syntaxe correcte est:
    
         nom_fonction () {
            commande ...
         }


Par exemple, la fonction suivante est nommé affichage:
    
         affichage () {
            echo "Ceci est un exemple de fonction"
         }


On peut ajouter des arguments comme ceci :
    
         affichage () {
            echo "Ceci est un exemple de paramètre" $1
         }


example :
    
    #!/bin/bash 
    # Lecture interactive des variables 
    echo "ENTRER VOTRE NOM" 
    read sname 
    # Affichage des valeurs variables 
    echo $sname 
    affichage(){ 
         echo "Ceci est le nom" $1 
    } 
    affichage $sname


#### Built-in Commandes Shell

Les scripts shell sont utilisés pour exécuter des séquences de commandes et d'autres types de déclarations. Les commandes peuvent être répartis dans les catégories suivantes :
	
* applications compilées
* Built-in commandes bash
* autres scripts

Applications compilées sont des fichiers exécutables binaires que vous pouvez trouver sur le système de fichiers. 

Le script shell a toujours accès à des applications compilées tels que rm, ls, df, vi, et gzip. bash a beaucoup de Built-in commands qui peuvent être utilisés pour afficher la sortie d'un script shell ou de terminal. 

Parfois, ces commandes ont le même nom que des programmes exécutables sur le système, tels que echo qui peut conduire à des problèmes. les commandes Built-in comprennent cd, pwd, echo, read, logout, printf, let, et ulimit. Une liste complète des commandes de bash intégrés peut être trouvée dans bash man, ou en tapant simplement help.  



#### Substitution de commandes Built-in 

À certains moments, vous devrez peut-être remplacer le résultat d'une commande comme une partie d'une autre commande. Il peut être fait de deux façons:
	
* En enfermant la commande intérieure avec backticks (`)
* En enfermant la commande intérieure en $()

Peu importe la méthode, la commande la plus interne sera exécuté dans un environnement shell en premier lieu. 

Pratiquement n'importe quelle commande peut être exécutée de cette façon. Ces deux méthodes permettent la substitution de commande. Par exemple:
    
    $ cd /lib/modules/$(uname -r)/

Dans l'exemple ci-dessus, la sortie de la commande "uname -r" devient l'argument de la commande cd.




#### Variables d'environnement

Presque tous les scripts utilisent des variables contenant une valeur, qui peut être utilisé n'importe où dans le script. Ces variables peuvent être soit de l'utilisateur ou du système.

Quelques exemples de variables d'environnement standard sont HOME, PATH, et HOST. Pour appeler une variables d'environnement elle doivent être précédés du symbole $ ($ HOME par exemple). Vous pouvez afficher et définir la valeur de variables d'environnement.

Par exemple, la commande suivante affiche la valeur stockée dans la variable PATH:
    
    $ echo $PATH

Cependant, aucun préfixe n'est nécessaire lors de l'établissement ou la modification de la valeur de la variable. Par exemple, la commande suivante définit la valeur de la variable de MyColor au bleu:
    
    $ MyColor = bleu

Vous pouvez obtenir une liste des variables d'environnement avec les commande env, set ou printenv.


#### Exporter les variables

Par défaut, les variables créées dans un script ne sont valide que dans ce dernier. Pour les rendre disponibles, ils doivent être promus à des variables d'environnement en utilisant la déclaration d'exportation comme dans:
    
    export VAR = valeur

ou
    
    VAR = valeur; export VAR

les variables exportées ne sont pas partagés, mais seulement copiés, i.e, si vous faites un changement dans un autre script, il n'aura aucun effet dans le script initial.


#### Paramètres des scripts

Les utilisateurs ont souvent besoin de passer des valeurs de paramètres à un script, comme un nom de fichier, date, etc. Scripts auront des chemins différents où arriver à des valeurs différentes selon les paramètres (arguments de commande) passées. Ces valeurs peuvent être du texte ou des chiffres, comme dans :

    
    $ ./script.sh /tmp
    $ ./script.sh 100 200


Dans un script, le paramètre ou un argument est représenté avec un $ et un numéro. Le tableau répertorie certains de ces paramètres.

Signification paramètre

* $0 Nom du script
* $1 Le premier paramètre
* $2, $3, etc. Deuxièmement, troisième paramètre, etc.
* $* Tous les paramètres
* $# Nombre d'arguments


#### Utilisation des paramètres de script

example :
    
    #!/bin/bash

    echo "Le nom du fichier est " $0
    echo "Le 1er paramètre est " $1 
    echo "Le 2ème paramètre est " $2 
    echo "Le 3ème paramètre est " $3 
    echo "La liste de tout les paramètres" $*

Enregister le dans le fichier script-param.sh

    $ ./script-param.sh 1 2 3
    ./script-param.sh
    1
    2
    3
    1 2 3



#### Redirection de sortie

La plupart des systèmes d'exploitation acceptent l'entrée à partir du clavier et d'afficher la sortie sur le terminal. Cependant, dans les scripts shell, vous pouvez envoyer la sortie vers un fichier. Le processus de détourner la sortie vers un fichier est appelé redirection de sortie.

Le caractère > est utilisé pour écrire la sortie dans un fichier. Par exemple, la commande suivante envoie la sortie de libre pour le fichier /tmp/free.out :
    
    $ free > /tmp/free.out

Pour vérifier le contenu du fichier _/tmp/free.out_, à l'invite de commande tapez _cat /tmp/free.out_

Deux caractères (>>) seront ajoutés la sortie à un fichier s'il existe, et d'agir comme > si le fichier n'existe pas déjà.

#### Redirection d'entrée

De même que la sortie, l'entrée peut être lue depuis un fichier. Le processus de lecture en entrée d'un fichier est appelé redirection d'entrée et utilise le caractère <. Si vous créez un fichier appelé script8.sh avec le contenu suivant:
    
    #! /bin/bash
    echo "Nombre de traits"
    wc -l </temp/free.out

puis exécuter avec chmod + x script8.sh; ./script8.sh, il comptera le nombre de lignes du fichier de /temp/free.out et affichera le résultat.


### Constructions

#### L'instruction if

La prise de décision conditionnelle en utilisant une instruction if, est un concept de base que toute la programmation utile ou langage de script doivent avoir.

Lorsque une instruction if est utilisé, les actions qui en découlent dépendent de l'évaluation des conditions spécifiques telles que:

* Comparaisons numériques ou chaîne
* Valeur de retour d'une commande (0 pour le succès)
* L'existence de fichiers ou autorisations

Sous forme compacte, la syntaxe d'une instruction if est:
    
    if test-COMMANDES; then consequence COMMANDES; fi

Une définition plus générale est:
    
    if condition
    then
            declarations
    else
            déclarations
    fi


#### Utilisation de l'instruction if

Ce qui suit if vérifie le fichier /etc/passwd, et si le fichier est trouvé, il affiche le message
/etc/passwd existe.:
    
    if [-f /etc/passwd]
    then
         echo "/etc/passwd existe."
    fi

Notez l'utilisation des crochets ([]) pour délimiter la condition de test. Il existe de nombreux autres types de tests que vous pouvez effectuer, comme vérifier si deux nombres sont égaux, supérieur ou inférieur à l'autre et prendre une décision en conséquence; nous allons discuter de ces autres tests.

Dans les scripts modernes vous pouvez trouver dans les supports doublé comme dans [[-f /etc/passwd]]. Ce ne est pas une erreur. Il ne est jamais mauvais de le faire et il évite certains problèmes subtils comme faisant référence à une variable d'environnement vide sans l'entourer de guillemets; nous ne allons pas en parler ici.

#### Tests pour les fichiers

Vous pouvez utiliser l'instruction if pour tester attributs de fichier tels que :

* l'existence d'un fichier ou d'un répertoire
* Permission de lecture ou d'écrire
* Permission d'exécution

Par exemple, dans l'exemple suivant:
    
    if [-f /etc/passwd]; then
        ACTION
    fi

l'instruction if vérifie si le fichier /etc/passwd est un fichier régulier.
Notez la pratique très courante de mettre ; then sur la même ligne que l'instruction if.

bash fournit un ensemble de conditionnels de fichiers, qui peut être utilisé avec l'instruction if, y compris:

* **-e** si le fichier existe.
* **-d** si le fichier est un répertoire.
* **-f** si le fichier est un fichier régulier (c'est à dire, pas un lien symbolique, noeud de périphérique, répertoire, etc.)
* **-s** si le fichier est de taille non nulle.
* **-g** si le fichier a un ensemble _Sgid_ .
* **-u** si le fichier a un ensemble _suid_.
* **-r** si le fichier est lisible.
* **-w** si le fichier est accessible en écriture.
* **-x** si le fichier est exécutable.

Vous pouvez consulter la liste complète des conditions de fichiers en utilisant **man 1 test**.


#### Comparaison de string
Vous pouvez utiliser l'instruction if pour comparer des chaînes à l'aide de l'opérateur == (deux signes égal). La syntaxe est la suivante:
    
    if [string1 == string2]; then
        ACTION
    fi

#### Tests numériques
Vous pouvez utiliser des opérateurs spécialement définies avec l'instruction if pour comparer des chiffres. Les différents opérateurs qui sont disponibles sont listés ci-dessous :

* **-eq** égal à
* **-ne** n'est pas égal à
* **-gt** Supérieur à
* **-lt** Inférieur à
* **-ge** Supérieur ou égal à
* **-le** Inférieur ou égal à


La syntaxe de numéros de comparaison est la suivante:
    
    exp1 -op exp2


#### expressions arithmétiques

Les expressions arithmétiques peuvent être évalués selon les trois modes suivants (espaces sont importants!):

* Utilisation de l'utilitaire de expr: expr est un programme standard, mais quelque peu obsolète. La syntaxe est la suivante:

`exp1 -op exp2`
`expr 8 + 8`
`echo $ (expr 8 + 8)`
	
* Utilisation de $ ((...)): C'est le format de l'enveloppe intégré. La syntaxe est la suivante:
    
`echo $((x + 1))`

* Utilisation de la commande shell let. La syntaxe est la suivante:

`let x = (1 + 2); echo $x`


Dans les scripts Shell modernes l'utilisation de expr est remplacé par
    
`var = $ ((...))`



