from netmiko import ConnectHandler

# Define the router details
router = {
    "device_type": "cisco_ios",
    "ip": "192.168.0.1",
    "username": "admin",
    "password": "password",
    "secret": "enable_password",
}

# Connect to the router
net_connect = ConnectHandler(**router)
net_connect.enable()

# Enter configuration mode
net_connect.config_mode()

# Configure interface
interface_config_commands = [
    "interface GigabitEthernet0/1",
    "ip address 192.168.1.1 255.255.255.0",
    "no shutdown",
]
output = net_connect.send_config_set(interface_config_commands)
print(output)

# Save configuration
net_connect.exit_config_mode()
net_connect.write_memory()

# Disconnect from the router
net_connect.disconnect()