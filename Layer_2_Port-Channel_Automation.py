#===============Importing_Of_All_Required_Library====================#
import time 
import getpass
from netmiko import ConnectHandler 
#===============Taking_the_user_Input====================#
user = input("Enter the Username: ")
passwd = getpass.getpass("Enter the Password: ") 
#=================Creating_the_IP_List_Of_All_Devices_which_need_to_be_configure==================#
host_list=['192.168.6.143','192.168.6.144','192.168.6.145','192.168.6.146']  
#=========Running_a_for_loop_for_each_IP's_on_the_above_List=================#
for ips in host_list: 
#==========Defining_all_the_required_field_for_taking_devices_access==========#
    cisco_switch = {
        'device_type': 'cisco_ios',
        'host': ips,
        'username': user,
        'password': passwd,
        'port': 22,          # optional, defaults to 22
        'secret': 'secret',     # optional, defaults to ''
        'use_keys': 'diffie-hellman-group1-sha1'
    }
    net_connect = ConnectHandler(**cisco_switch) #sending the conncetion request to devices with above mentioned Parameters
    #===============Taking_the_user_Input_for_Port-Channel_Interface====================#
    interface_number=input("Enter the interface range Gig0/0-? Note: value should only be number eg.; 1,2,3 etc")
    #=============Performing_the_Configuration=====================#
    commands=[f'interface range gig 0/0-{interface_number}',
            'shutdown',
            'switchport trunk encapsulation dot1q',
            'switchport mode trunk',
            'switchport trunk allowed vlan all',
            'channel-group 6 mode active',
            'no shut',
            'write',]
    net_connect.send_config_set(commands)
    commands=[f'interface po6',
            'switchport trunk encapsulation dot1q',
            'switchport mode trunk',
            'switchport trunk allowed vlan all',
            'no shut',
            'write,']
    net_connect.send_config_set(commands)
    time.sleep(30) # making the program wait for 30 sec before executing the next line
    output=net_connect.send_command('show etherchannel summary')
    print(output)
    net_connect.disconnect() # Disconnect and close the program
    

