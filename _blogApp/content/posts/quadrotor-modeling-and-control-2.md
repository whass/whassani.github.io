title:  "Quadrotor Mini-Rotorcraft, Part 1 : Numerical model of simulation"
date: 2015-07-01
lang: en
description: After mathematically modeling the quadrotor in the previsous article, we will implement it using python. 
categories: 
- Control

**Table of content**

[TOC] 


## reminder of the mathematical model

The mathematical model is given as follow :

$$ m \ddot{\zeta} + mg E_z = F_{\zeta}$$
$$ J \ddot{\eta} = \tau - C(\eta, \dot{\eta}) \dot{\eta} $$

To simplify the notatio we have take

$$ \tau = \left[ \begin{matrix}
                  \tilde\tau_{\psi} \\\
                  \tilde\tau_{\theta}  \\\
                  \tilde\tau_{\phi}   \\\
           \end{matrix} \right] 
           =
           J^{-1}(\tau - C(\eta, \dot{\eta}) \dot{\eta})
$$ 

Therefor we have obtained the general equation of the quad-rotor aircraft, that are :

$$
\begin{align}
m \ddot{x} & = u(sin \phi sin \psi + cos \phi cos \psi sin \theta ) \\\
m \ddot{y} & = u(cos \phi sin \psi sin \theta - sin \phi cos \psi )\\\
m \ddot{z} & = u cos \theta cos \phi - mg \\\
\ddot{\psi} & = \tilde\tau_{\psi} \\\
\ddot{\theta} & = \tilde\tau_{\theta} \\\
\ddot{\phi} & = \tilde\tau_{\phi}
\end{align}
$$

## Programming considerations

We will suppose that we have a genral class of quadrotor mini aircraft that have 3 methods :

* Translation
* Rotation




##
Install numpy