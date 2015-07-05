title: "Quadrotor Mini-Rotorcraft, Part 1 : Mathematical Modeling"
date: 2015-03-14
lang: en
description: The complete dynamics of an aircraft, taking into account aero-elastic effects, flexibility of the wings, internal dynamics of the engine and the whole set of changing variables are quite complex and somewhat.
categories: 
- Control

**Table of content**

[TOC]

## Desciption 
The quad-rotor model is obtained by representing the aircraft as a solid body evolving in a three dimensional space and subject to the main thrust and three torques: pitch, roll and yaw.

<center><figure>
<img src="{{ url_for('static', filename='images/quad-rotor.png') }}" alt="FrameWork" style="width:304px;height:228px;" >
  <figcaption>*Figure 1 : The quad-rotor control input.*</figcaption>
</figure> 
</center>

## How it works
The quad-rotor mini-rotorcraft is controlled by the angular speeds of four electric motors as shown in Figure 1. 

Each motor produces a thrust and a torque to generate : 

* the main thrust, 
* the yaw torque, 
* the pitch torque, and 
* the roll torque. 

From Figure 1 it can be observed that the motor \\( M_i \\) (for \\(i=1,...,4\\) produces the force \\( f_i \\) and the torque \\( \tau{M_i} \\), which is proportional to the square of the angular speed, that is, 

$$ f_i = k \omega_i^2 $$

$$ \tau_{M_i} = k_{drag} \omega^2$$

The propellers rotations sens must be arranged to tend to cancel gyroscopic effects and aerodynamic torques in trimmed flight as follow :

* The front (\\(M_1\\)) and the rear (\\(M_3\\)) motors rotate **counter-clockwise**, 

* while the left (\\(M_2\\)) and right (\\(M_4\\)) motors rotate **clockwise**


Since that :

* ***Main thrust*** \\( u \\) is obtained by increasing the sum of individual thrusts of each motor. 


* ***Pitch motion*** is obtained by increasing the speed of the rear motor \\( M_3 \\) while reducing the speed of the front motor \\( M_1 \\).


* ***Roll motion*** is obtained by increasing the speed of the rear motor \\( M_4 \\) while reducing the speed of the front motor \\( M_2 \\).

* ***Yaw motion*** is obtained by increasing the torque of the front and rear motors \\( \tau_{M_1} \\) and \\( \tau_{M_3} \\), respectively) while decreasing the torque of the lateral motors (\\( \tau_{M_2} \\) and \\( \tau_{M_4} \\), respectively). 

Such motions can be accomplished while maintaining the total thrust constant, see Figure 2.



## Euler-Lagrange formulation
In the following we will use the Euler-Lagrange approach to obtain the dynamical model of the system. If your are not familiar with this later you could use the Newton-Euler one.

Let's begin by construct the Lagrangian of our system. It's given as follow : 

$$ L(q, \dot{q}) = T_{rot} + T_{trans} - U $$

Where :

* \\( q=(\zeta, \eta)=(x,y,z,\psi, \theta, \phi) \in R^6 \\) is the generalized coordinates of the rotorcraft.

    * \\(\zeta = (x,y,z) \in R^3 \\) denotes the position vector of the center of mass of the quad-rotor relative to a fixed inertial frame. 

    * \\(\eta=(\psi, \theta, \phi)  \in R^3 \\) the rotorcraft’s Euler angles (the orientation of the rotorcraft). \\(\phi\\) is the yaw angle around the *z-axis*, \\(\theta\\) is the pitch angle around the *x-axis* and \\(\psi\\) is the roll angle around *x-axis*.


### Potential energy

The potential energy of the rotorcraft is given by ,

$$  U = mgz $$ 

Where :

* \\(z\\) is the rotorcraft altitude.
* \\(m\\) denotes the mass of the quad-rotor.
* \\(g\\) is the acceleration due to gravity).


### Tranlational Kinetic energy 

The translational kinetic energy is given as follow :

$$ T_{trans} = \frac{m}{2} \dot{\zeta}^T\dot{\zeta} $$

Where :

* \\( \dot\zeta \\) is the vector of the angular velocity.
* \\(m\\) denotes the mass of the quad-rotor.


<center><figure>
<img src="{{ url_for('static', filename='images/quad-rotor-pitch-yaw-roll.png') }}" alt="FrameWork" style="width:304px;height:228px;" >
  <figcaption>*Figure 2 : Pitch, roll and yaw torques of the quad-rotor.*</figcaption>
</figure> 
</center>

### Rotational Kinetic energy 
The translational kinetic energy is given by :

$$ T_{rot} = \frac{1}{2} \dot{\eta}^T J \dot{\eta} $$ 


* The matrix \\(J = J(\eta)\\) acts as the inertia matrix for the full rotational kinetic energy of the quad-rotor, expressed directly in terms of the generalized coordinates \\( \eta \\) and defined as follow :

$$ J=J(\eta)=W_{\eta}^T I W_{\eta}$$

$$ W_{\eta} = \left[\begin{matrix}
                 -sin \theta & 0 & 1\\\
                 cos \theta sin \phi & cos \phi & 0\\\
                 cos \theta cos \phi  & -sin \phi & 0\\\
           \end{matrix}\right]
$$ 
*Exaplanation :*

Initially we have :

$$ T_{rot} = \frac{1}{2} \dot{\Omega}^T I \dot{\Omega} $$ 

Where :

* \\( I \\) is the inertia matrix (we assume that there exists no relationship between the axes inertia).
    * \\(  
I = \left[\begin{matrix}
                 I_{xx} & 0 & 0\\\
                 0 & I_{yy} & 0\\\
                 0 & 0 & I_{zz} \\\
           \end{matrix}\right]
\\)

* \\( \Omega \\) is the vector of the angular velocity.


    The angular velocity vector \\( \omega \\) resolved in the body-fixed frame is related to the generalized velocities \\( \eta \\) by means of the standard kinematic relationship.

$$ \Omega = W_{\eta} \dot{\eta} = \left[\begin{matrix}
                 \dot{\phi}-\dot{\psi}sin \theta \\\
                 \dot{\theta}cos(\phi)+\dot{\psi}cos \theta sin \phi\\\
                 \dot{\psi}cos \theta cos \phi - \dot{\theta}sin(\phi) \\\
           \end{matrix}\right] $$




## Euler-Lagrange equation 

The model of the full rotorcraft dynamics is obtained from Euler–Lagrange equations with external generalized forces.

$$
\frac{d}{dt} \left(\frac{\partial L}{\partial \dot{q}}\right) - \frac{\partial L}{\partial q} =  \left[\begin{matrix}
                 F_{\dot{\zeta}}\\\
                 \tau \\\
           \end{matrix}\right]
$$

Where 

* \\(F_{\dot{\zeta}} = R \hat{F} \in R^3 \\) is the translational force applied to the rotorcraft due to main thrust.
    * \\( \hat{F} = [0, 0, u]^T \\)
        * \\( u= \sum_{i=1}^{4} f_i\\) is the main thrust directed out of the bottom of the aircraft generated by the force \\(f_i\\) of each motor \\(M_i\\).
        * \\(f_i = k_i \omega_i^2\\) where \\(k_i\\) is a constant and \\(\omega\\) i is the angular speed of the *ith* motor.
    * \\(R(\psi, \theta, \phi) \in SO(3)\\) represents the orientation of the aircraft relative to a fixed inertial frame.
* \\( \tau \in R^3 \\) represents the yaw, pitch and roll moments.

    * \\( \tau = \left[ \begin{matrix}
                  \tau_{\psi} \\\
                  \tau_{\theta}  \\\
                  \tau_{\phi}   \\\
           \end{matrix} \right] 
\\)
            = 
\\(            \left[\begin{matrix}
                                 \sum_i^4 \tau_{M_i} \\\
                                 (f_2-f_4) l \\\
                                 (f_3-f_1) l   \\\
                                 \end{matrix}\right] 
\\)       

    * \\( \tau_{M_i} = k_{drag,i} \omega^2 \\) is the moment produced by motor \\( M_i \\) around the center of gravity of the aircraft and where \\(k_{drag,i}\\) is a constant.
    * \\( l \\) is the distance between the motors and the center of gravity, and \\( \tau_{M_i} \\)   

<center><figure>
<img src="{{ url_for('static', filename='images/quad-rotor-frame.png') }}" alt="FrameWork" style="width:304px;height:228px;" >
  <figcaption>*Figure 3 : The quad-rotor in an inertial frame. f1 , f2 , f3 , f4 represent the thrust of each motor, \\(\psi \\) , \\(\theta \\) and \\(\phi \\) represent the Euler angles, and u is the main thrust.*</figcaption>
</figure> 
</center>

### Euler-Lagrange of translation motion

Since the Lagrangian contains no cross terms in the kinematic energy combining \\(\dot{\zeta}\\) with \\(\dot{\eta}\\), the EUler-Lagrange equation can be partionned into dynamics for \\(\zeta\\) and \\(\eta\\).

The Euler–Lagrange equation for the translational motion is :

$$ \frac{d}{dt} \left\[\frac{\partial L_{trans}}{\partial \dot{\zeta}}\right] - \frac{\partial L_{trans}}{\partial \zeta} = F_{\zeta}$$

Where :

* \\(
L_{trans} = T_{trans} - U =  \frac{m}{2} \dot{\zeta}^T\dot{\zeta} - mg E_z
\\)

* \\(
E_z = [0, 0, z]^T
\\)

Then 

$$ m \ddot\zeta + mg E_z = F_{\zeta}$$

### Euler-Lagrange of rotational motion

The Euler–Lagrange equation for the rotational motion is :

$$ \frac{d}{dt} \left\[\frac{\partial L_{rot}}{\partial \dot{\eta}}\right] - \frac{\partial L_{rot}}{\partial \eta} = \tau$$

Where 

* \\(
L_{rot} = T_{rot} = \frac{1}{2} \dot{\eta}^T J \dot{\eta}
\\)

Thus one obtains`:

$$J \ddot{\eta} + \dot{J} \dot{\eta} -\frac{1}{2} \frac{\partial}{\partial \eta}(\dot{\eta}^T J \dot{\eta}) $$

Defining the Coriolis-centripetal vector :

$$ \tilde{V} (\eta, \dot{\eta}) = \dot{J} \dot{\eta} - \frac{1}{2} \frac{\partial}{\partial \eta}(\dot{\eta}^T J \dot{\eta}) $$

one writes :

$$ J \ddot{\eta} + \tilde{V} (\eta, \dot{\eta}) = \tau $$

but \\( \tilde{V} (\eta, \dot{\eta}) \\) can be expressed as 

$$ \tilde{V} (\eta, \dot{\eta}) = \left( \dot{J}  - \frac{1}{2} \frac{\partial}{\partial \eta}(\dot{\eta}^T J ) \right) \dot{\eta} = C(\eta, \dot{\eta}) \dot{\eta}$$ 

$$ C(\eta, \dot{\eta}) = \left( \dot{J}  - \frac{1}{2} \frac{\partial}{\partial \eta}(\dot{\eta}^T J )\right)$$
where \\( C(\eta, \dot{\eta}) \\) is referred to as the Coriolis term and contains the gyroscopic and centrifugal terms associated with the \\( \eta \\) depence of \\( J \\). 


## General Equation of motion

Finally one obtains :

$$ m \ddot{\zeta} + mg E_z = F_{\zeta}$$
$$ J \ddot{\eta} = \tau - C(\eta, \dot{\eta}) \dot{\eta} $$

To simplify let us take

$$ \tau = \left[ \begin{matrix}
                  \tilde\tau_{\psi} \\\
                  \tilde\tau_{\theta}  \\\
                  \tilde\tau_{\phi}   \\\
           \end{matrix} \right] 
           =
           J^{-1}(\tau - C(\eta, \dot{\eta}) \dot{\eta})
$$ 

Therefor the general equation of the quad-rotor aircraft are :

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


We have finished, be happy.

This is one of the most important step to design a controller, and must be very rigorous, no mistake is tolerated. I'll show in next articles why I'm saying that.

In the next article of the series "Quadrotor Mini-Rotorcraft"; we will construct a simulation model, I'll do it with python since it's free and like that more people can implement the model easily.