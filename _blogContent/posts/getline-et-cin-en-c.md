title: "Affichage en C++ : getline() et cin en C++"
date: 2015-03-05
categories:
- C-C++












Quand on mélange l'utilisation des chevrons et de **getline()**, il faut toujours placer l'instruction **cin.ignore()** après la ligne **cin>>a**.

C'est une règle à apprendre.

Exemple













    
    #include <iostream> 
    #include <string> 
    using namespace std;
    int main()
    {



    
     cout << "Combien vaut pi ?" << endl;
     double piUtilisateur(-1.); //On crée une case mémoire pour stocker un nombre réel
     cin >> piUtilisateur; //Et on remplit cette case avec ce qu'écritl'utilisateur
     cin.ignore();
     cout << "Quel est votre nom ?" << endl;
     string nomUtilisateur("Sans nom"); //On crée une case mémoire pour contenir une chaine de caractères
     getline(cin, nomUtilisateur); //On remplit cette case avec toute la ligne que l'utilisateur a écrit
     cout << "Vous vous appelez " << nomUtilisateur << " et vous pensez que pivaut " << piUtilisateur << "." << endl;
    return 0; 
    }
























