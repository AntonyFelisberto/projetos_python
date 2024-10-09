from netmiko import ConnectHandler

R1 = {
    "device_type":"cisco_ios",
    "host":"SEU HOST",
    "username":"andre",
    "password":"cisco"
}
R2 = {
    "device_type":"cisco_ios",
    "host":"SEU HOST",
    "username":"andre",
    "password":"cisco"
}
R3 = {
    "device_type":"cisco_ios",
    "host":"SEU HOST",
    "username":"andre",
    "password":"cisco"
}
with open("config-router-file") as file:
    config_line = file.read().splitlines()

lista_routers = [R1,R2,R3]

for routers in (R1, R2, R3):  
    connect = ConnectHandler(**routers)
    configure = connect.send_config_set(config_line)
    print(configure)
    connect.disconnect()