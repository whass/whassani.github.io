title: Les matrices sous Matlab
date: 2015-02-14
categories: 
- Matlab/Simulink

## Création de matrices





>> A = [a11 …. a1m; …. ; an1 …. anm]







## Exemple





>> A=[ 1 2 3 4 ; 2 3 4 1 ; 3 4 1 2 ; 4 1 2 3]







## Quelques matrices usuelles prédéfinies





Soient i, j deux entiers strictement positif alors :




>>zeros(i,j)  %renvoi une matrice de zéros.




>>ones(i,j) : donne une matrice de uns .




>>eye(i,j) : donne une matrice identité.




>>rand(i,j);  donne une matrice d‘éléments aléatoires




>>randn(i,j) : donne une matrice d‘éléments aléatoires.distribués normalement






##  Quelques commandes importantes:




>> A(i, :) : désigne la ième ligne de la matrice A.




>> A(:, j) : désigne la jème colonne de la matrice A.




>> A(i:j , :) : désigne la sous matrice formées des ième et jème lignes de la matrice A.




>> A(:, i:2:j) : désigne la sous matrice formée des colonnes impaires de la matrice A.




Nota : le 2 est le pas considéré.




>>size(A) : permet d'obtenir la taille de la matrice A.




>>max(A) : désigne l‘élément maximal de la matrice A.




>>min(A) : désigne l‘élément minimal de la matrice A.




>>mean(A) : désigne la moyenne des éléments de matrice A.




>>median(A) : désigne la valeur médiane des éléments de matrice A.










>>sort(A ) : tri par ordre croissant des éléments de matrice A.




>>prod(A) : produit des éléments de matrice A.




>>sum(A) : somme des éléments de matrice A.




>>expm(A) : exponentielle de matrice A. (important :A doit être carrée).




>>sqrtm(A) : racine carrée de la matrice A. (important :A doit être carrée)










>>inv (A) : la matrice inverse de A. (important :A doit être carrée)





>>det(A) : déterminant de la matrice A. (important :A doit être carrée)




>>eig (A) : valeurs propres et vecteurs propres de la matrice A.




>>null(A) : noyau de la matrice A.




>>rank(A) : rang de matrice A






