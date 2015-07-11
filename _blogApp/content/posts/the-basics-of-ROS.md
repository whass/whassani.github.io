title:  "The basics of ROS"
date: 2015-07-11
lang: en
description: As its name suggests, ROS (Robot Operating System) is an operating system for robots. In this article we will describe ROS in brief and its basics. How ROS resources are organized on disk ?. The concepts of node which describe the instance of an executable.  How messages are formatde and exchanged via ROS ?.
categories:
- Robotics
- Control
- Modeling

**Table of content**

[TOC]


The basic principle of a robotic OS is to run in parallel a large number of executables that need to exchange information synchronously or asynchronously. For example, a robotic OS must poll at a frequency defined the robot's sensors (ultrasound or infrared distance sensor, pressure sensor, temperature sensor, gyroscope, accelerometer, cameras, microphones ...) to retrieve this information, process (do what is called data fusion), to pass the processing algorithms (speech processing, computer vision, simultaneous localization and mapping, ...) and finally back to control the motors. This whole process is carried out continuously and in parallel. Moreover, the robotic OS will manage the processes concurrences in order to ensure effective access to robot resources.

After a brief description of ROS, We will describe the ROS concepts grouped under the name "ROS Computation Graph". These are the concepts used by the system during operation, before, we will describe the "ROS FileSystem" which corresponds to static concepts.

## ROS in brief ...

As its name suggests, ROS (Robot Operating System) is an operating system for robots. As operating systems for PCs, servers or stand-alone devices, ROS is a complete operating system for service robotics.

ROS is a meta operating system, something between the operating system and middleware.

It provides services close to an operating system (hardware abstraction, competition management, processes ...) but also high-level features (asynchronous calls, synchronous calls, centralized database data, system settings robot ...).

## The ROS file system

ROS Resources are organized in a hierarchical structure on disk. Two important concepts stand out:

* ***The package:*** This is the primary unit of ROS software organization. A package is a directory that contains the nodes (we will see below what a node), external libraries, data, configuration files and an XML configuration file named manifest.xml.

* ***The stack:*** A stack is a collection of packages. It provides aggregation capabilities such as navigation, location ... A stack is a directory that contains directories of packages and a configuration file named stack.xml.

## ROS Computation Graph

### Nodes

In ROS, a node is an instance of an executable. A node may be a sensor, a motor, a treatment algorithm, monitoring ... Each launched node is declared to the Master. Here we find the microkernel architecture where each node is an independent resource.

*** The Master node***

The Master is a service declaration and registration of nodes and allows nodes to know each other and exchange information. The Master is implemented via XML-RPC.

The Master has a ***subpart*** highly used that is the ***Server***. It also implemented as a XML-RPC, as the name suggests is a sort of central database in which the nodes can store and share information and global parameters.

### Informations exchange

The exchange of information is done using messages and is carried out either :
* asynchronously via a topic or
* synchronously via a service.

<center><figure>
<img src="{{ url_for('static', filename='images/ROS-services-and-topic.jpg') }}" alt="FrameWork" style="width:70%;" >
  <figcaption>*ROS topic and service concepts.*</figcaption>
</figure>
</center>

*** Messages ***

A message is a composite data structure. A message consists of a combination of primitive types (strings, boolean, integer, float ...) and message (the message is a recursive structure).

For example, a node representing a servo robot, certainly release its state on a topic (depending on what you have programmed) with a message containing such an integer representing the motor position, a float of its temperature, another float of its speed ...

The description of messages is stored in package_name/msg/monMessageType.msg. This file describes the structure of messages.

#### The topics

A topic is an information transport system based on the system of the *** subscription / publication *** (subscribe / publish). One or more nodes can publish information on a topic and one or more nodes can read information on this topic. The topic is somehow an asynchronous bus information much like an RSS feed. This notion of asynchronous bus many-to-many is essential in the case of a distributed system.

The topic is typed, that is to say, the type of information that is published (the message) is always structured in the same way. The nodes send or receive messages on topics.

#### services

The topic is an asynchronous communication mode allowing many-to-many communication. However the service responds to another need, that of a synchronous communication between two nodes. This concept is similar to the concept of remote procedure call (remote procedure call).

The description of services is stored in package_name /srv/monServiceType.srv. This file describes the data structures of requests and responses.
