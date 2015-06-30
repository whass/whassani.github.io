title: Opérations sur les polynômes sous Matlab
date: 2015-02-14
categories: 
- Matlab/Simulink


Nota : un polynôme se déclare comme un vecteur qui contient ses coefficients.




## Exemple 1 :




B(x)=5.X4+3.X3+2.X




Sous Matlab : 




>> B=[5 3 0 2 0] ou bien : >> B=[5,3,0,2,0]







## Quelques commandes importantes:




>> Roots (B) : racines du polynôme B.




>> polyval (B,x) : évaluer le polynôme (exp:avant de représenter son graphe).




>> poly (v) : reconstruit un polynôme à partir de ses racines.
