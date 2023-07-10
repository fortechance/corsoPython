from netmiko import ConnectHandler
# Define the router details
router = {
    "device_type": "cisco_ios",
    "ip": "131.226.217.149",
    "username": "developer",
    "password": "lastorangerestoreball8876",
    #"secret": "enable_password",
}

# Connect to the router
net_connect = ConnectHandler(**router)
#net_connect.enable()

# Send commands and receive output
#output1 = net_connect.send_command('sh startup-config')
#output2 = net_connect.send_command('sh int descr')
print("sono lahcen")
output3 = net_connect.send_command('show ip bgp all')
#print(output1) 
#print(output2) 
print(output3) 
#output = net_connect.send_command('show ip bgp all | in ip pubblico')
# Enter configuration mode
net_connect.config_mode()

# Configure interface
interface_config_commands = [
    "interface GigabitEthernet3",
    "ip address 192.168.40.1 255.255.255.252",
    "no shutdown",
]
output = net_connect.send_config_set(interface_config_commands)
print(output)

# Save configuration
#net_connect.exit_config_mode()
net_connect.save_config()
print(dir(net_connect))