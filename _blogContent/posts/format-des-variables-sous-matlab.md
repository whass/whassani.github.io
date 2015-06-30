author: blender
date: 2013-03-14
title: Format des variables sous Matlab
categories: 
- Matlab-Simulink

Soit x = [4/3 1.2345e-6]








	
  * format short       1.3333 0.0000

	
  * format short e    1.3333e+000 1.2345e-006

	
  * format short g    1.3333 1.2345e-006

	
  * format long         1.33333333333333 0.00000123450000

	
  * format long e      1.333333333333333e+000 1.234500000000000e-006

	
  * format long g      1.33333333333333 1.2345e-006

	
  * format bank       1.33 0.00

	
  * format rat          4/3 1/810045

	
  * format hex         3ff5555555555555 3eb4b6231abfd271







**Nota** :




on commence d‘abord par définir le format, puis l‘opération à effectuer ou le nombre à affiché.
