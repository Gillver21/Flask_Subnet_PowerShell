#!/bin/bash


#POST Text 1
echo -e "\n\n\n\nSend IP: 124.62.23.211  with CIDR /28 to API\n"
sleep 2
#Printing echo of command so user informed
echo -e curl -X POST http://:****/ip_subnet/124.62.23.211/28
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -X POST http://:****/ip_subnet/124.62.23.211/28
#Sleep
sleep 2



#POST Text 2
echo -e "\n\n\n\nSend IP: 214.50.111.120  with Subnet Mask of 255.240.0.0 to API\n"
sleep 2
#Printing echo of command so user informed
echo curl -X POST http://:****/ip_subnet/214.50.111.120/255.240.0.0
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -X POST http://:****/ip_subnet/214.50.111.120/255.240.0.0
#Sleep
sleep 2



#POST Text 3
echo -e "\n\n\n\nSend IP: 20.124.83.1  with CIDR /21 to API\n"
sleep 2
#Printing echo of command so user informed
echo -e curl -O -X POST http://:****/ip_subnet/20.124.83.1/21
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -O -X POST http://:****/ip_subnet/20.124.83.1/21
#Sleep
sleep 2
