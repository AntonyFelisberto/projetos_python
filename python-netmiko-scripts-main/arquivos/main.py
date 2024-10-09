from netmiko import ConnectHandler

R1 = {
    "device_type":"cisco_ios",
    "host":"SEU HOST",
    "username":"andre",
    "password":"cisco"
}

connect = ConnectHandler(**R1)

loopback = ["interface loopback 13"]

configure = connect.send_config_set()
output = connect.send_command("show ip int brief")
print(output)