# DwarvenGenerator

## Index 

- [Introduction](#intro)

- [Project Brief](#brief)

- [My Solution](#solution)

- [Risk Assessment](#risk)

- [Deployment](#deploy)

- [User Journey](#journey)

- [Technologies Used](#tech)

- [The Future](#future)



<a name="intro"></a>
## Introduction 

This will discuss the steps i took to produce my application for the second project i undertook at QA Academy.


if you would like to give my application a go please follow these steps:

- create a new VM 

- copy the below piece of code and enter it into the terminal of the new vm

```curl https://raw.githubusercontent.com/TomLLew/DwarvenGenerator/master/install-dwarvengenerator.sh | sudo bash```

- to stop the application use docker-compose down


<a name="brief"></a>
## Project Brief

Tasked with creating a application, that has a service-orientated architecture at its core. This architecture must include atleast 4 services, these services must work together to make a fully functioning application. The application must be fully integrated with a version control system which will be built through a CI server and then fully deployed to a cloud-based virtual machine. The application must be deployed using containerisation, as part of the project a andible playbook needs to be created to provision the environment that the application needs to run.


<a name="solution"></a>
## My Solution

As my solution to this brief i have decided to build a dwarven generator, this application will generate a random dwarven character which will include:  

- service 1 = a service that generates a random first and last name for the dwarf from a list based on user input supplied by service 3.

- service 2 = a service that generates a random job and clan for the dwarf based on user input supplied by service 3.

- service 3 = a service that send user data to services 1 and 2, then brings the information from services 1 and 2 and compiles them together, this service will also generate a skill and random stat points based on the input from service 2 and then returns them to service 4.

- service 4 = a service that acts as the frontend of the application and send user data to service 3, it will recieve the data back from service 3 and display this on the webpage for the user to see.

[Trello](https://trello.com/b/EwPR7BCu/dwarvengenerator) 


<a name="risk"></a>
## Risk Assessment


![Risk Assessment](https://github.com/TomLLew/DwarvenGenerator/blob/master/Documentation/risk-assessment%20.png)


This is the risk assessment i created detailing a number of risks that could appear and cause me problems. I have rated them by likelihood and impact, i have also added what i plan to do to prevent these risks with a reassessment at the end to look back on these risks.



<a name="deploy"></a>
## Deployment


![CI pipeline](https://github.com/TomLLew/DwarvenGenerator/blob/master/Documentation/service-architecture.jpg)



This is the Architecture used for this project. The environments where made using Ansible, as you can see i have a vm with 4 containers enclosed within a container using NGINX, the other vm has jenkins installed on it with a docker registry. jenkins is set up with a ssh connection to the vm running the application containers, this allows jenkins to update the services currently running. When the source code is changed a webhook from github will trigger a pipeline build of the new docker images and push them to the registry, the jenkins will ssh across the the other vm and update the services with the appropriate images. 



<a name="journey"></a>
## User Journey



![User journey](https://github.com/TomLLew/DwarvenGenerator/blob/master/Documentation/usecase.png)



This is a general user journey for the applicatiion, as you can see the user first connects to the NGINX container which will route the connection to the frontend container which will bring up the homepage.



![homepage](https://github.com/TomLLew/DwarvenGenerator/blob/master/Documentation/frontend-homepage.png)



as you can see the user is given an option to select the gender of the dwarf, upon selecting a gender and clicking generate the gender data is passed to service 3 which sends it to service 1 and gets a respone of firstname and lastname. service 3 will also send the data to service 2 where it will recieve a job and clan, service 3 will then compile this data and using the data recieved from service 2 about the clan will trigger, some logic to determine the stats and skill for that dwarf based on the clan generated. service 3 will then send it back to the frontend service, where it will be displayed to the user.



![character page](https://github.com/TomLLew/DwarvenGenerator/blob/master/Documentation/frontend-characterpage.png)


<a name="tech"></a>
## Technologies used


- Python
- Flask
- Git
- Github
- [Ansible](https://github.com/TomLLew/DwarvenGenerator/tree/master/Ansible)
- [Trello](https://trello.com/b/30LbMCdG/individual-project) 
- Jenkins
- Docker


<a name="future"></a>
## The future
Many things can be added, for the future. 
I would like to add more races to the application, this will appeal to a wider audience. I also would like to have a service that allows for the user to create their own accounts and save the characters that are generated for them where they can delete them if they wanted.
