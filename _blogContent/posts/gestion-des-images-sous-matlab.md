title: Gestion des Images sous Matlab
date: 2015-02-14
categories: 
- Matlab-Simulink


##  Lecture et affichage d'une Image





 




I = imread('nom_image.ext');




figure,imshow(I)







## Redimensionner une Image :




 




 J = imresize(I,0.6);




figure,imshow(J) % --- Affichage ---*(Le 0.6 est le facteur d‘échelle)







## Rotation d'une Image : 







K =imrotate(I,30);




figure, imshow(K) %(Le 30 est le facteur d‘échelle)






