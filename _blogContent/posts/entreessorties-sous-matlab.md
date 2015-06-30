title: Entrées/Sorties sous Matlab
date: 2015-02-14
categories: 
- Matlab-Simulink

## input(entrée)
La commande **input** permet de demander à l’utilisateur Matlab d’entrer les valeurs de variables à




utiliser.







## Pause




La commande pause permet de stopper l’exécution Matlab.




Vous pouvez préciser le nombre de secondes de pose ou revenir à Matlab en appuyant sur n’importe quelle touche.







## save et load (sauvegarder et charger)







La commande save permet de sauvegarder dans un fichier, dont le nom par défaut est matlab.mat




, le contenu de certaines variables dont vous souhaitez garder une trace. Ce fichier peut être appelé par la commande




load qui restaure toutes les variables que vous avez sauvegard ́ees.





## Example



    
    >> n=input('Entrez la valeur de n :’) ; % Affectez une valeur à n.
    >> a=input('Precisez la valeur de a :') ; % Affectez une valeur à a.
    >> v=a . ˆ [ 0 : n ] ;
    >> A=toeplitz(v ) ;
    >> d=det(A) ; %Création de la matrice de Toeplitz A
    >> save restoep n a A d ; % Sauvegarde de n, a, A, d dans restoep.mat 
    >> clear % Efface toutes les variables de la session.
    >> load restoep % Restaure les variables de restoep.mat.
    >> who % Vérification.
