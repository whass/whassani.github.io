title: Graphisme sous Matlab
date: 2015-02-14
categories: 
- Matlab-Simulink


## Gestion des graphiques à 2d :




 




>>Plot (y) : représente le graphe de la fonction y.




>>title('expression') : affiche le titre du graphe.




>>Xlabel('expression') : affiche l‘étiquette à l‘axe des abscisses.




>>Ylabel('expression') : affiche l‘étiquette à l‘axe des ordonnées.
















>>grid on: affiche la grille.




>>grid off: masque la grille.




>>hold on: permet l'affiche d'une seconde courbe dans une meme figure.




>>clf : efface le graphe .




>>stem (y) : représente la séquence de données (discrètes) y.







## Application :




 x = 0:pi/100:2*pi;




y = sin(x);




y2 = sin(x-.25);




y3 = sin(x-.5);




plot(x,y,x,y2,x,y3)




legend('sin(x)','sin(x-.25)','sin(x-.5)')







## Le style et Couleurs des lignes :




>>plot(x,y,'style_couleur_marker ')





	
  * Couleur : 'c', 'm' 'y' 'r' 'g' 'b' 'w' 'k' [cyan, magenta, yellow, red, green, blue, white et black].

	
  * Style : '-' '--' ':' '-.', .... 

	
    *  Exemple >>plot (y, 'linestyle ', '-') ;




	
  * Marker :  '+'   'o'   '*'  'x'   's'  'd' '^'  'v'   '>'   '<'   'p'   'h'




## Utilisation du Handle :




Quand Matlab crée des objets, il leurs affecte un identifiant appelé handle. Ce dernier est utilisé pour acceder aux propriétés de l‘objet grace aux instructions :






	
  * set 

	
  * get




Exemple :





>> x = 1:10;




>> y = x.^3;




>> h = plot(x,y);




Pour changer de couleur ,on écrit :




>>set(h,'Color','red');




Pour changer le style de ligne , on ecrit :




set(h,'LineWidth', 6);









