# Clase en vídeo: https://youtu.be/TbcEqkabAWU

### Dates ###

# ------------- Date time -----------------

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

"""
con la clase datetime () contiene año, mes, día, hora, minuto, segundo y microsegundo.
- now (): quiere decir treanos la informacino de fecha actual
"""

now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

# Creamos una fecha ingresando directamente en la clase datetime ()
year_2023 = datetime(2023, 1, 1)

print_date(year_2023)

# --------------- Time --------------------


current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# ---------------- Date -------------------

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)



# ------------------ Timedelta () ------------------------

expira = datetime.now() + timedelta(
    days=1,
    hours=2,
    minutes=30
)

print(expira)

# ejemplo 2

inicio = datetime(2026, 1, 1)
fin = datetime(2026, 1, 16)

diferencia = fin - inicio  # esta operacion da como resultado un timedelta ()

print(diferencia)
print(diferencia.days)          # 15
print(diferencia.total_seconds())

# ------------------------- strftime ()  & strptime () --------------------
# DateTime  --> string

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

# String  --> DateTime

from datetime import datetime

texto = "16/01/2026 09:20:15"
fecha = datetime.strptime(texto, "%d/%m/%Y %H:%M:%S")

print(fecha)

"""
%a	Weekday, short version	                          Fri
%A	Weekday, full version	                          Friday
%w	Weekday as a number 0-6, 0 is Sunday	          5	
%d	Day of month 01-31	                              01	
%b	Month name, short version	                      Jan	
%B	Month name, full version	                      January	
%m	Month as a number 01-12	                          12	
%y	Year, short version, without century	          26	
%Y	Year, full version	                              2026	
%H	Hour 00-23	                                      19	
%I	Hour 00-12	                                      08	
%p	AM/PM	                                          AM	
%M	Minute 00-59	                                  41	
%S	Second 00-59	                                  08	
%f	Microsecond 000000-999999	                      548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	N° de dia del año 001-366	                                         016
%U	N° semana del año, domingo como primer día de la semana, 00-53	     02 	
%W	N° semana del año, lunes como primer día de la semana, 00-53	     02	
%c	Versión local de fecha y hora	                                     Fri Jan 16 09:02:29 2026	
%x	Version local de fecha	                                     12/31/18	
%X	Version local de hora	                                     17:41:00	
"""



# ejemplosss .-------------- ANALIZAR

from datetime import timedelta, datetime
import time

token_creado = datetime.now()
expira = token_creado + timedelta(seconds=40)

print(f"Token expira en {expira}")

while True:
    if datetime.now() > expira:
        print("Token expirado")
        break

    time.sleep(1)  # ⬅️ pausa 1 segundo