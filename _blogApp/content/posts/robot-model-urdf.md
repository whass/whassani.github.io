title:  "Create an urdf (Universal Robot Description File) file"
date: 2015-07-09
lang: en
description: The Unified Robot Description Format (URDF) is the standard ROS XML representation of the robot model (kinematics, dynamics, sensors) describing a robot. 
categories: 
- Simulation

**Table of content**

[TOC]


## Create the tree structure

In this tutorial we'll create the URDF description of the "robot" shown in the image below. 

<center><figure>
<img src="{{ url_for('static', filename='images/link.png') }}" alt="FrameWork" style="width:50%;" >
</figure> 
</center>

The robot in the image is a tree structure. Let's start very simple, and create a description of that tree structure, without worrying about the dimensions etc. 

Fire up your favorite text editor, and create a file called ***my_robot.urdf***: 


    <robot name="test_robot">
            <link name="link1" /> <!-- create a link named link 1-->
            <link name="link2" />
            <link name="link3" />
            <link name="link4" />

        <joint name="joint1" type="continuous"> <!--  meaning that it can take on any angle from negative infinity to positive infinity -->
            <parent link="link1"/>
            <child link="link2"/> 
        </joint>

        <joint name="joint2" type="continuous">
            <parent link="link1"/>
            <child link="link3"/>
        </joint>

        <joint name="joint3" type="continuous">
            <parent link="link3"/>
            <child link="link4"/>
        </joint>
    </robot>


Let describe each part of the program

#### balise ***robot*** :

    <robot name="test_robot">
    </robot>

This balise tell to the parser that this is a robot and its name is test_robot.


#### balise ***link*** :

    <link name="link1" />


Each link in your model must have a link balise and its name.

#### balise ***joint*** :

        <joint name="joint3" type="continuous">
            <parent link="link3"/>
            <child link="link4"/>
        </joint>


Each joint must connect at least two joints, therefore, we have to define its parents and childs, in this example, the parent if the 3rd link and the child is the 4th link :   

    <parent link="link3"/>
    <child link="link4"/>


## Dimension : Origins of the joints

So now that we have the basic tree structure, let's add the appropriate dimensions. As you notice in the robot image, the reference frame of each link (in green) is located at the bottom of the link, and is identical to the reference frame of the joint. 

#### balise ***origin*** :
To add dimensions to our tree, all we have to specify is the offset from a link to the joint(s) of its ***children***. To accomplish this, we will add the field ***origin**** to each of the joints.

Let's look at the second joint. Joint2 is offset in the Y-direction from link1, a little offset in the negative X-direction from link1, and it is rotated 90 degrees around the Z-axis. 

So, we need to add the following ***origin*** element:

    <origin xyz="-2 5 0" rpy="0 0 1.57" />

where 

    <robot name="test_robot">
        <link name="link1" />
        <link name="link2" />
        <link name="link3" />
        <link name="link4" />

      <joint name="joint1" type="continuous">
        <parent link="link1"/>
        <child link="link2"/>
        <origin xyz="5 3 0" rpy="0 0 0" />
      </joint>

      <joint name="joint2" type="continuous">
        <parent link="link1"/>
        <child link="link3"/>
        <origin xyz="-2 5 0" rpy="0 0 1.57" />
      </joint>

      <joint name="joint3" type="continuous">
        <parent link="link3"/>
        <child link="link4"/>
        <origin xyz="5 0 0" rpy="0 0 -1.57" />
      </joint>
    </robot> 


## Kinematics : links axes of rotation

What we didn't specify yet is around which axis the joints rotate. Once we add that, we actually have a full kinematic model of this robot! All we need to do is add the ***axis*** element to each joint. The axis specifies the rotational axis in the local frame.

#### balise ***axis*** :

So, if you look at joint2, you see it rotates around the positive Y-axis. So, simple add the following xml to the joint element: 

    <axis xyz="0 1 0" /> 

Similarly, joint1 is rotating around the following axis: 

    <axis xyz="-0.707 0.707 0" />


Note that it is a good idea to normalize the axis.

If we add this to all the joints of the robot, our URDF looks like this: 

    <robot name="test_robot">
        <link name="link1" />
        <link name="link2" />
        <link name="link3" />
        <link name="link4" />

      <joint name="joint1" type="continuous">
        <parent link="link1"/>
        <child link="link2"/>
        <origin xyz="5 3 0" rpy="0 0 0" />
        <axis xyz="-0.9 0.15 0" />
      </joint>

      <joint name="joint2" type="continuous">
        <parent link="link1"/>
        <child link="link3"/>
        <origin xyz="-2 5 0" rpy="0 0 1.57" />
        <axis xyz="-0.707 0.707 0" />
      </joint>

      <joint name="joint3" type="continuous">
        <parent link="link3"/>
        <child link="link4"/>
        <origin xyz="5 0 0" rpy="0 0 -1.57" />
        <axis xyz="0.707 -0.707 0" />
      </joint>
    </robot> 