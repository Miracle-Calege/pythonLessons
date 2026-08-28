import datetime

#faremos o import do modulo datetime nos permitindo usar o relogio do nosso computador


#criamos um objecto do tipo date e inicializamos com o ano,mes e dia
date= datetime.date(2025,1,2)
print(date)

#retorna o dia de hoje

today = datetime.date.today()
print(today)

#criamos um objecto do tipo time colocando as horas, minutos e segundos

time=datetime.time(23,59,59)
print(time)

#retornando a data e hora actual
now=datetime.datetime.now()

#formatando o output usando format specifiers

now=now.strftime("%H:%M:%S %m-%d-%Y")

print(now)

#criamos um objecto de data e hora

target=datetime.datetime(2030,1,2,12,30,1)

current=datetime.datetime.now()


#para verificar se um determinado dia/hora já passou

if target < current:
    print(f"target já passou")
else:
    print("target nao passou")