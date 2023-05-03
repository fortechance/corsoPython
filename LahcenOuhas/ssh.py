# SSH to Multiple Devices from devices file
from files import ConnectHandler

with open('devices.txt') as routers:
    HOST = "192.168.1.205"
    for IP in routers:
        Router = {
            'device_type': 'cisco_ios',
            'ip': IP,
            'username': 'roger',
            'password': 'cisco'
        }
  
        net_connect = ConnectHandler(**Router)

        print ('Connecting to ' + IP)
        print('-'*79)
        output = net_connect.send_command('sh ip int brief')
        output = net_connect.send_command('sh ip route 93.62.232.0')
        output = net_connect.send_command('sh ip prefix-list RedStaticBGP-prefer-CAR')
    
     
        print(output)
        print()
        print('-'*79)

# Finally close the connection
net_connect.disconnect()


