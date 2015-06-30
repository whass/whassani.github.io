title: Les fonctions et scripts sous Matlab
date: 2014-02-14
categories: 
- Matlab-Simulink


## Les fonctions élémentaires





Un certain nombre de fonctions élémentaires sont prédéfinies : sin, cos, abs,...



    
    <span class="a">>> x=[0:0.5:pi]
    >> sin(x)
    >> x=[0:0.2:10]
    >> exp(x)</span>










## Fonctions et scripts





### Exemple de fonction




écrire ce programme et l‘enregistrer sous nom : trinome.m









    
    <span class="a">%--- calcul des solutions de l'équation a*x^2+b*x+c=0 ---*
    </span><span class="a">function r =trinome(a,b,c)
    </span><span class="a">delta=b^2-4*a*c;
    </span><span class="a">if delta==0 
    </span><span class="a">    r(1)=-b/2;
    </span><span class="a">else
    </span><span class="a">   delta > 0
    </span><span class="a">   r(1)=(-b-sqrt(delta))/2*a;
    </span><span class="a">   r(2)=(-b+sqrt(delta))/2*a;
    </span><span class="a">end
    </span><span class="a">disp(['delta == ', num2str(delta)]);
    </span><span class="a">disp(['la solution est ', num2str(r)]);</span>










### Utilisation de la fonction dans un script:




écrire ce programme et l‘enregistrer sous nom : trinome3.m









    
    <span class="a">%--- calcul des solutions de l'équation a*x^2+b*x+c=0 ---*
    disp('Ceci est un script qui calcul des solutions de l''équation a*x^2+b*x+c=0');
    disp('Donner la valeur de a')
    a=input('a = ');
    disp('Donner la valeur de b')
    b=input('b = ');
    disp('Donner la valeur de c')
    c=input('c = ');
    trinome(a,b,c); % <span class="l">appel <span class="l">de <span class="l">la <span class="l">fonction <span class="l">aux <span class="l">paramèters <span class="l">a,b,c</span></span></span></span></span></span></span></span>


















