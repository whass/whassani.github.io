title:  "Quadcopter Drone, Part 2 : Mathematical Modeling"
date: 2015-07-01
lang: en
description: After showing the functional principle of the quadcopter (direction control, motion types, ..) in the part I of Quadcopter Drone series, we want to model mathematically the quadcopter from scratch in this part. We will develop the related differential equations of the the quadcopter motions by using the Euler-Lagrange principle.
categories:
- Control
- Modeling
- Quadcopter
- Drone


**Table of content**

[TOC]



## Overview

The quad-rotor structure is presented in Figure 1 including the corresponding angular velocities, torques and forces created by the four rotors (numbered from 1 to 4).

<center><figure>
<img src="{{ url_for('static', filename='images/the-inertial-and-body-frame.png') }}" alt="FrameWork" style="width:70%;" >
  <figcaption>*Figure 1 : The inertial and body frames of a quadcopter.*</figcaption>
</figure>
</center>

## Inertial and body frames
The absolute linear position of the quad-rotor copter is defined in the inertial frame \\( x,y,z\\)-axes with \\( \zeta \\). The attitude, i.e. the angular position, is defined in the inertial frame with three Euler angles η. Pitch angle θ determines the rotation of the quad-rotor around the y-axis. Roll angle φ determines the rotation around the x-axis and yaw angle ψ around the z-axis. Vector q contains the linear and angular position vectors

$$
\zeta = \left[\begin{matrix}
              x   \\\
              y   \\\
              z   \\\
        \end{matrix}\right]
,
\eta = \left[\begin{matrix}
              \phi   \\\
              \theta \\\
              \psi   \\\
        \end{matrix}\right]
,
\mathbb{q} = \left[\begin{matrix}
              \zeta \\\
              \eta  \\\
    \end{matrix}\right]
$$

The origin of the body frame is in the center of mass of the quad-rotor. In the body frame, the linear velocities are determined by \\( V_B\\) and the angular velocities by \\( \Omega \\)

$$
V_B = \left[\begin{matrix}
              v_{x,Q}   \\\
              v_{y,Q}   \\\
              v_{z,Q}   \\\
        \end{matrix}\right]
,
\Omega = \left[\begin{matrix}
              p   \\\
              q \\\
              r   \\\
        \end{matrix}\right]
$$

The rotation matrix from the body frame to the inertial frame is

$$
^{I}R_{B} =  \left[\begin{matrix}
           C\psi C\theta & C\psi S\theta S\phi - S\psi C\phi & C\psi S\theta C\phi + S\psi S\phi \\\
           S\psi C\theta & S\psi S\theta S\phi + C\psi C\phi & S\psi S\theta C\phi - C\psi S\phi \\\
           -S\theta & C\theta S\phi & C\theta C\phi \\\
     \end{matrix}\right]
$$

in which \\( Sx=sin(x) \\) and \\( Cx = cos(x) \\). The rotation matrix \\( ^{I}R_{B} \\) is orthogonal thus \\( (^{I}R_{B})^{-1} = (^{I}R_{B})^T \\) which is the rotation matrix from the inertial frame to the body frame.

The transformation matrix for angular velocities from the inertial frame to the body frame is \\( W_{\eta}\\), and from the body frame to the inertial frame is \\( W_{\eta}^{-1} \\), as shown in,

$$
\dot \eta = W_{\eta}^{-1} \Omega,  
           \left[\begin{matrix}
                 \dot \phi   \\\
                 \dot \theta \\\
                 \dot \psi   \\\
           \end{matrix}\right]
           =
           \left[\begin{matrix}
                 1 & S\phi T\theta & C\phi T\theta \\\
                 0 & C\phi         & -S\phi        \\\
                 0 & S\phi/C\theta & C\phi/C\theta \\\
           \end{matrix}\right]
           \left[\begin{matrix}
                 p \\\
                 q \\\
                 r \\\
           \end{matrix}\right]
$$

$$
\Omega = W_{\eta} \dot \eta,  
           \left[\begin{matrix}
                 p \\\
                 q \\\
                 r \\\
           \end{matrix}\right]
           =
           \left[\begin{matrix}
                 1 & 0      & -S\theta      \\\
                 0 & C\phi  & C\theta S\phi \\\
                 0 & -S\phi & C\theta C\phi \\\
           \end{matrix}\right]
           \left[\begin{matrix}
                 \dot \phi   \\\
                 \dot \theta \\\
                 \dot \psi   \\\
           \end{matrix}\right]  
$$

in which \\(Tx=tan(x)\\). The matrix W_{\eta} is invertible if \\(\theta \neq (2k-1) \phi/2, (K \in \mathbf{Z} ) \\).

The quad-rotor is assumed to have symmetric structure with the four arms aligned with the body x- and y-axes. Thus, the inertia matrix is diagonal matrix \\(I\\) in which \\(I_{xx} = I_{yy}\\)
$$
I = \left[\begin{matrix}
          I_{xx} & 0      & 0      \\\
          0      & I_{yy} & 0      \\\
          0      & 0      & I_{zz} \\\
    \end{matrix}\right]
$$

The angular velocity of rotor \\( i \\) i, denoted with \\(\omega_i\\), creates force \\(f_i\\) in the direction of the rotor axis. The angular velocity and acceleration of the rotor also create torque \\(\tau_{M_i}\\) around the rotor axis

$$ f_i = k \omega_i^2 $$

$$ \tau_{M_i} = b \omega_i^2 + I_M \dot \omega_i $$

in which the lift constant is \\( k \\), the drag constant is \\( b \\) and the inertia moment of the rotor is \\( I_M \\) . Usually the effect of \\( \dot \omega_i \\) is considered small and thus it is omitted.

The combined forces of rotors create thrust T in the direction of the body z-axis. Torque \\( \tau \\) consists of the torques \\( \tau_\phi \\),\\( \tau_\theta \\) and \\( \tau_\psi \\) in the direction of the corresponding
body frame angles
$$
  T=\sum_{i=1}^{4} f_i = k \sum_{i=1}^{4} \omega_i^2
$$

$$
 \tau_B =   \left[ \begin{matrix}
                  \tau_{\phi}   \\\
                  \tau_{\theta} \\\
                  \tau_{\psi}   \\\
          \end{matrix} \right]
            =
          \left[\begin{matrix}
                  l (f_2-f_4)         \\\
                  l (f_3-f_1)         \\\
                  \sum_i^4 \tau_{M_i} \\\
          \end{matrix}\right]
            =
          \left[\begin{matrix}
                  (\omega_2^2 - \omega_4^2) l         \\\
                  (\omega_3^2 - \omega_1^2) l         \\\
                  \sum_i^4 \tau_{M_i} \\\
          \end{matrix}\right]
$$

in which \\(l\\) is the distance between the rotor and the center of mass of the quad-rotor. Thus, the roll movement is acquired by decreasing the 2nd rotor velocity and increasing the 4th rotor velocity. Similarly, the pitch movement is acquired by decreasing the 1st rotor velocity and increasing the 3th rotor velocity. Yaw movement is acquired by increasing the the angular velocities of two opposite rotors and decreasing the velocities of the other two.

## Euler-Lagrange formulation
In the following we will use the Euler-Lagrange approach to obtain the dynamical model of the system. If your are not familiar with this later you could use the Newton-Euler one.

Let's begin by construct the Lagrangian of our system. It's given as follow :

$$ \mathcal{L}(q, \dot{q}) = E_{r} + E_{t} - E_{p} $$
$$ \mathcal{L}(\mathbb{q}, \dot{\mathbb{q}}) = (m/2) \dot{\zeta}^T\dot{\zeta} + (m/2) \Omega^T I \Omega - mgz $$

The model of the full quadrotor dynamics is obtained from Euler–Lagrange equations with external generalized forces.

$$
\frac{d}{dt} \left(\frac{\partial \mathcal{L}}{\partial \dot{\mathbb{q}}}\right) - \frac{\partial \mathcal{L}}{\partial \mathbb{q}} =  \left[\begin{matrix}
                 F_{\zeta}\\\
                 \tau \\\
           \end{matrix}\right]
$$


The linear and angular components do not depend on each other thus they can be
studied separately.

### Translational motion

The linear external force is the total thrust of the rotors. The linear Euler-Lagrange equations are

$$
F_{\zeta} = ^{I}R_B
          \left[\begin{matrix}
            0         \\\
            0         \\\
            T         \\\
          \end{matrix}\right]
= m \ddot \zeta + m g
           \left[\begin{matrix}
            0         \\\
            0         \\\
            1         \\\
          \end{matrix}\right]
$$


### Rotational motion

The matrix \\( J(\eta) \\) from \\( \Omega \\) to \\( \eta \\)  is

$$ J=J(\eta)=W_{\eta}^T I W_{\eta}$$

$$
J = \left[\begin{matrix}
          I_{xx} & 0      & -I_{xx} S \theta      \\\
          0      & I_{yy} (C \phi)^2 + I_{zz} (S \phi)^2 & (I_{yy}-I_{zz}) C\phi S \phi C \theta      \\\
          - I_{xx} S \theta   & (I_{yy}-I_{zz}) C\phi S \phi C \theta & I_{xx} (S \theta)^2 + I_{yy} (S \phi)^2 (C \theta)^2 +  I_{zz} (C \phi)^2 (C \theta)^2 \\\
    \end{matrix}\right]
$$

Thus, the rotational energy \\(E_r \\) can be expressed in the inertial frame as

$$ E_{rot} = (1/2) \dot{\Omega}^T J \dot{\Omega} = (1/2) \dot{\eta}^T J \dot{\eta} $$

The external angular force is the torques of the rotors. The angular Euler-Lagrange equations are

$$
\tau = \tau_B = J \ddot{\eta} + \dot{J} \dot{\eta} -\frac{1}{2} \frac{\partial}{\partial \eta}(\dot{\eta}^T J \dot{\eta})
$$

Defining the Coriolis-centripetal vector :

$$ \tilde{V} (\eta, \dot{\eta}) = \dot{J} \dot{\eta} - \frac{1}{2} \frac{\partial}{\partial \eta}(\dot{\eta}^T J \dot{\eta}) $$

one writes :

$$ J \ddot{\eta} + \tilde{V} (\eta, \dot{\eta}) = \tau $$

but \\( \tilde{V} (\eta, \dot{\eta}) \\) can be expressed as

$$ \tilde{V} (\eta, \dot{\eta}) = \left( \dot{J}  - \frac{1}{2} \frac{\partial}{\partial \eta}(\dot{\eta}^T J ) \right) \dot{\eta} = C(\eta, \dot{\eta}) \dot{\eta}$$

$$ C(\eta, \dot{\eta}) = \left( \dot{J}  - \frac{1}{2} \frac{\partial}{\partial \eta}(\dot{\eta}^T J )\right)$$
where \\( C(\eta, \dot{\eta}) \\) is referred to as the Coriolis term and contains the gyroscopic and centrifugal terms associated with the \\( \eta \\) depence of \\( J \\).

Therefore :

$$ J \ddot{\eta} = \tau - C(\eta, \dot{\eta}) \dot{\eta} $$

The matrix \\( C(\eta, \dot{\eta}) \\) is a \\( 3X3 \\) matrix and has the form :

$$
C(\eta, \dot{\eta})= \left[\begin{matrix}
           C_{1,1} & C_{1,2} & C_{1,3} \\\
           C_{2,1} & C_{2,2} & C_{2,3} \\\
           C_{3,1} & C_{3,2} & C_{3,3} \\\
\end{matrix}\right]
$$

Where :

\\(
C_{1,1} = 0 \\\
C_{1,2} = (I_{yy}-I_{zz})(\dot\theta C \phi S \phi + \dot \psi (S \phi)^2 C \theta)+(I_{zz}-I_{yy}) \dot \psi (C \phi)^2 C \theta -I_{xx} \dot \psi C \theta) \\\
C_{1,3} = (I_{zz}-I_{yy})\dot \psi C \phi S \phi (C \theta)^2 \\\
C_{2,1} = (I_{zz}-I_{yy})(\dot \theta C \phi S \phi + \dot \psi (S \phi )^2 C \theta )+(I_{yy}-I_{zz}) \dot \psi (C \phi )^2 C \theta -I_{xx} \dot \psi C \theta \\\
C_{2,2} = (I_{zz}-I_{yy}) \dot \phi C \phi S \phi \\\
C_{2,3} = -I_{xx} \dot \psi S \theta C \theta + I_{yy} \dot \psi (S \phi)^2 S \theta C \theta + I_{zz} \dot \psi (C \phi )^2 S \theta C \theta \\\
C_{3,1} = (I_{yy}-I_{zz}) \dot \psi (C \phi )^2 S \phi C \phi -I_{xx} \dot \theta C \theta \\\
C_{3,2} = (I_{zz}-I_{yy}) (\dot \theta C \phi S \phi S\ theta + \dot \phi (S \phi)^2 C \theta)+(I_{yy}-I_{zz}) \dot \phi (C \phi )^2 C \theta + I_{xx} \dot \psi S \theta C \theta - I_{yy} \dot \psi (S \phi )^2 S \theta C \theta -I_{zz} \dot \psi (C \phi )^2 S \theta C \theta \\\
C_{3,3} = (I_{yy}-I_{zz})(\dot \phi C \phi S \phi (C \theta)^2)-I_{yy} \dot \theta (S \phi)^2 C \theta S \theta - I_{zz} \dot \theta (C \phi)^2 C \theta S \theta +I_{xx} \dot \theta C \theta S \theta \\\
\\)


## General Equation of motion

We some arrangements we obtain :

$$ \left[\begin{matrix}
        \ddot x         \\\
        \ddot y         \\\
        \ddot z         \\\
      \end{matrix}\right]
       =  \left[\begin{matrix}
           C\psi C\theta & C\psi S\theta S\phi - S\psi C\phi & C\psi S\theta C\phi + S\psi S\phi \\\
           S\psi C\theta & S\psi S\theta S\phi + C\psi C\phi & S\psi S\theta C\phi - C\psi S\phi \\\
           -S\theta & C\theta S\phi & C\theta C\phi \\\
     \end{matrix}\right]
      \left[\begin{matrix}
            0         \\\
            0         \\\
            T/m       \\\
          \end{matrix}\right]
-     \left[\begin{matrix}
        0         \\\
        0         \\\
        g         \\\
      \end{matrix}\right]
$$

$$  \ddot{\eta} = J^{-1} (\tau - C(\eta, \dot{\eta}) \dot{\eta}) $$

To simplify let us take

$$ \tilde\tau = \left[ \begin{matrix}
                  \tilde\tau_{\psi} \\\
                  \tilde\tau_{\theta}  \\\
                  \tilde\tau_{\phi}   \\\
           \end{matrix} \right]
           =
           J^{-1}(\tau - C(\eta, \dot{\eta}) \dot{\eta})
$$

Therefor the general equation of the quad-rotor quadrotor are :

$$
\begin{align}
m \ddot{x} & = T(S \phi S \psi + C \phi C \psi S \theta ) \\\
m \ddot{y} & = T(C \phi S \psi S \theta - S \phi C \psi )\\\
m \ddot{z} & = T C \theta C \phi - mg \\\
\ddot{\psi} & = \tilde\tau_{\psi} \\\
\ddot{\theta} & = \tilde\tau_{\theta} \\\
\ddot{\phi} & = \tilde\tau_{\phi}
\end{align}
$$


We have finished, be happy.

This is one of the most important step to design a controller, and must be very rigorous, no mistake is tolerated. I'll show in next articles why I'm saying that.

In the next article of the series "Quadrotor Drone"; we will construct a simulation model, I'll do it with python since it's free and like that more people can implement the model easily.
