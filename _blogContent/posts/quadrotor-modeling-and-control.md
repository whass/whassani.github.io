title: Quadrotor Mini-Rotorcraft Modeling 
date: 2015-03-14
lang: en
description: The complete dynamics of an aircraft, taking into account aero-elastic effects, flexibility of the wings, internal dynamics of the engine and the whole set of changing variables are quite complex and somewhat unmanageable for the purposes of control. Therefore, it is interesting to consider a simplified model of an aircraft formed by a minimum number of states and inputs, but retaining the main features that must be considered when designing control laws for a real aircraft.
categories: 
- Control

dere

The quad-rotor model is obtained by representing the aircraft as a solid body evolving in a three dimensional space and subject to the main thrust and three torques: pitch, roll and yaw.

The quad-rotor mini-rotorcraft is controlled by the angular speeds of four electric motors as shown in Fig. 2.1. Each motor produces a thrust and a torque, whose combination generates the main thrust, the yaw torque, the pitch torque, and the roll torque acting on the quad-rotor. 



