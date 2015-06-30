title: Interruptions et exceptions dans les ARM Cortex-M
date: 2015-01-29
categories: 
- Embedded

Un système embarqué utilise les entrées/sorties pour communiquer avec le monde extérieur. La particularité d'un système embarqué par rapport aux système est sont couplage étroit avec monde extérieu.

L'un des problème majeur est le fait que un bout de code s'exécute nettement plus vide que le Hardware (exemple  de l'écran LCD, envoyer un ordre d'extinction peut se fair en 1us alors que son extinction effective peut durer 1ms, voyez bien un rapport de 1000 !). Durant ce temps, le processeur peut exécuter des milliers d'instructions. Par conséquent, la synchronisation entre l'exécution du logiciel et de son environnement externe est critique pour le succès d'un système embarqué.



Dans ce post je vous présenterai  les concepts généraux d'interruptions et des détails spécifiques pour le microcontrôleur Cortex ™ -M. Nous utiliserons ensuite interruptions périodiques pour provoquer une tâche logicielle à exécuter périodiquement. Si une broche GPIO est configuré comme une entrée, comment elle peut être utilisée comme source d'interruption sur front montant, déscendant ou les deux.

L'utilisation des interruptions permet au logiciel de répondre rapidement aux changements dans l'environnement externe.



Initialiser l'interruption

Associer l'interruption à une routine

un moyen pour faire communiquer la routine avec le programme principal


## Définition


une **interruption** est transfert automatique de l'exécution d'un logiciel en réponse à un évènement matériel qui asynchrone avec le logiciel qui est en cours d'exécution. Une interruption peur être interne (timer, défaillance mémoire, ...) ou externe (switch, ...).


