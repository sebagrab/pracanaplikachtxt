line= "this IS a very StANGE text"
line.capitalize()
print (line.capitalize())
'e' in line     #czy jest e w tekscie zwraca true false
import string
line.split(' ') #rozbijanie tekstu na tablice
#' '.join(list)

import time
print (time.localtime(time.time()))
import calendar
print (calendar.month(2019,9,w=5))
print(calendar.calendar(2020))

import datetime

d1= datetime.timedelta(days=1,hours=2,minutes=30)
print (d1)

print ('tuday is',datetime.date.today())
bornDate=datetime.date(1992,12,21)
today= datetime.date.today()
print (today-bornDate)
