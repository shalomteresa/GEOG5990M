# GEOG5990M

PROJECT TITLE: Spatial Agent Based Model

In this model, agents are the independent elements that have simple charachteristics. These agents interact with each other and the environment in which they are placed in. As the iterations of the model run, the actions of the agents change with each iteration. These actions that were altered effect the 
charachteristics of the individual agent along with other agents, and the environment in which they are present. In order to initialize the model, the 
data is read from the files or url provided and the model output is saved to files. The model output consists of written files, images and an animation file that visualized the results. This model will also generate a simple Graphic User Interface (GUI). 

This model could be framed as an ecological model used to observe the changes and effects of individual entities on the environment around them in various incidences of the natural world. For example, the agents could be represented by a flock of sheep moving around the field which could be considered as the environment they are in and as the time passes by, the interactions of the sheep among themselves and with the field in the form of grazing alters both their characteristics and the characteristics of the environment. In this example, the model outputs represent these changes in the form of images and animation. 

DEVELOPMENT PROCESS: The Model was built in several stages 

ABM1 
In the intial stage, the location of two agents is represented by their cartisean coordinates. The coordinates are initialised at a location and move randomly one step  and code was written to calculate the euclidean distance between the coordinates. 

ABM2
Secondly, the code was changed so the coordinates for each agent were stored in lists with length 2 in which the x-coordinate is the first item and the y-coordinate is the second item of the list. The agents were also stored in lists at this stage. The for loops are used to create and move the agents. 
The agents are plotted in a 2-dimentional space. 

ABM3
At this stage, the code was changed for calculating the distance by turning it into a function and other functions for calculating the maximum distance and minimum distance between agents were also introduced. The movement of the agents in the 2-Dimensional space are restricted to limited x and y coordinates to define a boundary.

Timing:
In order to explore the efficiency of the code, the time taken to create the number of distances and to calculate distances between them were plotted.
The functions were further modified to reduce the time taken to get the outputs and efficiency of the code was improved. 

ABM4
The complexity of the code is simplified by defining an agent class in a separate file called agentframework where agent characteristics are named and can be referred to by their name instead of their index in the model file. From this stage the code was split into multiple files. 

ABM5
Following that, environment element is initialized from a file. The interactions of the agents with the environment are recorded as the output and saved as a file. As the agents move they alter the environment which could be visualised by the eat function of the model. The agents that are processed first tend to have more resource to eat from the environment which creates a bias if they are generated in the same order. Therefore, the resources are further shared in the next stage.

ABM6
In order to share the resources among the agents equally and to create interactiong between agents, the code is modified to calculate the number of neighbours within a certain proximity of the current agent and divides the current agent's store equally among them. The order of the agents doesn't play a role in sharing of resouces at this stage and the output file is generated in the form of a gif displaying the interactions between the agents and the environment. 

ABM7
The code was developed to animate the model in a separate window and stopping conditions were defined to exit the model upon fulfilling that condition.

ABM8
A GUI was developed in the code at this stage.

ABM9
In the final stage data was initialized from a HTML file table to execute part of the model.

INSTALLATION and USAGE of the model are mentioned in the user manual.

CREDITS:

Tutorial followed from the course material 
https://agdturner.github.io/GEOG5990/home/index.html

Andy Turner
https://www.geog.leeds.ac.uk/people/a.turner/index.html

LICENSE:
Apache License 2.0



