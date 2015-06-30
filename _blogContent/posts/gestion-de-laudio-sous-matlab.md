title: Gestion de l’audio sous Matlab
date: 2015-02-14
categories: 
- Matlab-Simulink


## Lecture d‘un son





>> y =wavread('Nom.wav'); : Nom.wav Fichier qui se trouve dans le dossier de travail.




>>wavplay(y, F) : F représente la fréquence. % (Poser F=20000, puis changer de valeur pour voir son effet).




>>sound(y, F) : Convertir le signal y en un son.




>>aviread(y) : lire les fichiers AVI (Audio / Video Interleaved).







## Enregistrer un son 




>>wavwrite(y, F, 'nom_fichier') : sauvegarde le signal y dans un fichier au format Wav.
