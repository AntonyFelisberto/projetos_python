from datetime import datetime
from pytz import timezone as timez

data = datetime(2023, 4 , 20)
print(data)

data_hora = datetime(2023,4 ,20,7,49,27)
print(data_hora)

data_str = "2023-04-20 07:49:23"
data_diretiva = "%Y-%m-%d %H:%M:%S"
data_convertida = datetime.strptime(data_str,data_diretiva)

data_brasileira = "20/04/2020"
data_convert = "%d/%m/%Y"
data_nova = datetime.strptime(data_brasileira,data_convert)
print(data_nova)

data = datetime.now()
print(data)
#usando pytz - pip install pytz
data = datetime.now(timez("America/Sao_Paulo"))
print(data)
print(data.timestamp()) #numero de segundos de 1970 até hoje
print(datetime.fromtimestamp(1682874055.448715)) #numero de segundos de 1970 até hoje convertidos pra data

data_hora = datetime(2023,4 ,20,7,49,27,tzinfo=timez("America/Sao_Paulo"))
print(data_hora)
