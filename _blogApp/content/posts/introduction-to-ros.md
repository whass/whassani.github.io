title: "Install ROS (Robotics Operating System)"
date: 2015-07-09
lang: en
description: Robot Operating System (ROS) is a collection of software frameworks for robot software development, providing operating system-like functionality on a heterogeneous computer cluster.
categories: 
- Simulation
- Robotics

**Table of content**

[TOC]

<center><figure>
<img src="{{ url_for('static', filename='images/rosNetworkingCrop.png') }}" alt="FrameWork" style="width:60%;" >
</figure>
</center>



## Description

Robot Operating System (ROS) is a collection of software frameworks for robot software development, providing operating system-like functionality on a heterogeneous computer cluster. 

ROS provides standard operating system services such as hardware abstraction, low-level device control, implementation of commonly used functionality, message-passing between processes, and package management. 

Running sets of ROS-based processes are represented in a graph architecture where processing takes place in nodes that may receive, post and multiplex sensor, control, state, planning, actuator and other messages. 

Software in the ROS Ecosystem can be separated into three groups:

* language and platform-independent tools used for building and distributing ROS-based software;

* ROS client library implementations such as roscpp, rospy, and roslisp;

* packages containing application-related code which uses one or more ROS client libraries.


## Install ROS on Ubuntu

There exist dfifferents version of ROS, currently the latest one is JADE.

In the following we will install ROS from repository.

First, add the following repository to ubuntu sources.list

    $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list'

After that set up your keys

    $ wget http://packages.ros.org/ros.key -O - | sudo apt-key add –

Finally, update repository list 

    $ sudo apt-get update

According to your needs, there exists several ways to install ROS To install, but the easiest (and recommended if you have enough hard disk space)
installation is known as desktop-full. It comes with ROS, the Rx tools, the rviz visualizer (for 3D), many generic robot libraries, the simulator in 2D (such as stage) and 3D (usually Gazebo), the navigation stack (to move, localize, do mapping, and control arms), and also perception libraries using vision, lasers or RGB-D cameras

    $ sudo apt-get install ros-jade-desktop-full


## Setup the environment

To start using it, the system must know where the executable or binary files as well as other commands are. To do that execute the following script :
    
    $ source /opt/ros/jade/setup.bash 

To chack your setup execute :

    $ roscore

You must obtain something like that :

    ... logging to /home/walid/.ros/log/f014ab8a-264e-11e5-92e1-109addb06a19/roslaunch-walid-MacBookPro-4548.log
    Checking log directory for disk usage. This may take awhile.
    Press Ctrl-C to interrupt
    Done checking log file disk usage. Usage is <1GB.

    started roslaunch server http://walid-MacBookPro:35186/
    ros_comm version 1.11.13


    SUMMARY
    ========

    PARAMETERS
     * /rosdistro: jade
     * /rosversion: 1.11.13

    NODES

    auto-starting new master
    process[master]: started with pid [4559]
    ROS_MASTER_URI=http://walid-MacBookPro:11311/

    setting /run_id to f014ab8a-264e-11e5-92e1-109addb06a19
    process[rosout-1]: started with pid [4572]
    started core service [/rosout]


## Install standalone tools

ROS has some tools that need to be installed. These tools will help us install dependencies between programs to compile, download, and install packages from ROS. These tools are ***rosinstall*** and ***rosdep***.

    $ sudo apt-get install python-rosinstall python-rosdep


With these steps, you have all the necessary software installed
on your system to start working with ROS