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
for routers in (R1, R2, R3):
    connect = ConnectHandler(**routers)
    print(connect.find_prompt())
    connect.disconnect()