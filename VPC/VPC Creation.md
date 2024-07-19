# Creation of VPC #  
Region: Mumbai  
CIDR = 10.0.0.0/16 (65,536 IP Address)  

![image](https://github.com/user-attachments/assets/24dea360-b8fe-4398-a21a-7b62c9ff80aa)
 
## Cretion of Subnets for Demo-VPC ##  
VPC – Demo-VPC  
CIDR – 10.0.0.0/24 -> Public subnet (256 IP Address)  
10.0.1.0/24 -> Private subnet (256 IP Address)  

![image](https://github.com/user-attachments/assets/5c280fcb-222b-4fcb-afff-becee0ce962c)

## Creation of Internet Gateway ##  
State : Detached  
attach Demo-VPC to it.  
![image](https://github.com/user-attachments/assets/0b945ef3-d250-4110-8e91-f6c8678f4e55)  

## Creation of additional Route table for public subnet ##  
Private subnet should be associated with private route table(under subnet associations)  
By default, routes destination is 10.0.0.0/16 i.e., entire VPC which we can’t remove/delete as it should be accessible.  

![image](https://github.com/user-attachments/assets/1096fdc0-4bb1-4c49-a96a-912828f98f3b)


For Public route table, I am adding Internet gateway (in routes)  
Associating Public subnet to it.  

![image](https://github.com/user-attachments/assets/dc46b96b-d7bb-416a-a4bd-fb94897f1931)


## Create Public Instance and Private Instance ##
Public Instance  
Name = Public-EC2  
Attached to Demo-VPC, Public-subnet, created a security group of   
	> SSH, port 22, anywhere  
	>Custom, port 80, anywhere  
Public IP address = No  

Enabled Public DNS in Demo-VPC  

Private Instance  
Name = Private-EC2  
Attached to Demo-VPC, Private-subnet, created a security group of   
	> SSH, port 22, anywhere  
Public IP address = Yes  

![image](https://github.com/user-attachments/assets/91a33539-a7d1-4017-8b97-eed1e4234c98)

## Resource MAP ##

![image](https://github.com/user-attachments/assets/a57d0421-1384-4a10-ba6c-c39e781fe369)

 









 
 

