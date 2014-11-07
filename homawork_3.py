from datetime import datetime, date
import random

"""
Ex. 1
Definiti clasa DateFormat care primeste la initializare, si retine pe self,
un format[1] de data. Adaugati doua metode:
1. format - care transforma un obiect datetime primit ca paramentru in
string folosind formatul setat.
2. parse - care transforma un string primit ca paramentru intr-un obiect
datetime. Folositi formatul specificat.
1)https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
"""
 
 
class DateFormat(object):
	strFormat = '%Y-%m-%d'
	def format(self, objDateTime):
		return str(objDateTime)
	def parse(self, strDateToParse):
		return datetime.strptime(strDateToParse, self.strFormat)
'''
nowDate = date.today()
nowStr = '2013-09-28'
obj = DateFormat()
print obj.format(nowDate);
print obj.parse(nowStr)
'''

"""
Ex. 2
Definiti clasa DateRange care primeste la initializare o valoare start si o
valoare end, ambele sunt obiecte datetime. Adaugati metoda:
1. contains - primeste un obiect datetime si returneaza True daca data se
afla in intervalul [start, end).
"""
 
 
class DateRange(object):
	start=date(1992, 12, 4)
	end = date(1992, 12, 8)
	def __init__(self, objDatetimeStart, objDatetimeEnd):
		self.start = objDatetimeStart.date()
		self.end = objDatetimeEnd.date()
	def contains(self, objDateTime):
		if(self.start < objDateTime.date() and objDateTime.date() < self.end):
			return True
		else:
			return False
"""
now=datetime.now()
obj = DateRange()
print obj.contains(now)
"""


"""
Ex. 3
Definiti clasa Hotel care primeste la initializare un pret pe noapte si un
pret de curatenie. Adaugati metoda:
1. price - primeste o valoare de tip DateRange si returneaza pretul de
cazare pentru acel interval (numarul de nopti inmultit cu pretul
pe noapte la care se adauga o singura data taxa de curatenie).
Ex. 4
Sa presupunem ca Hotel are o singura camera. Modificati clasa sa memoreze o
lista de rezervari. Implementati metodele:
1. book - primeste ca paramentru un DateRange si adauga o rezervare.
2. available - primeste un DateRange si returneaza True daca hotelul este
disponibil in acel interval si False daca este indisponibil.
"""
 
 
class Hotel(object):
	nNightPrice = 0
	nCleaningPrice = 0
	listReservations = []
	def __init__(self):
		self.nNightPrice = random.randint(50,150)
		self.nCleaningPrice = random.randint(0, 50)
	def price(self, objDateRange):
		#nu reusesc sa convertesc rezultatul scaderii dintre date in int
		return self.nNightPrice*(objDateRange.end - objDateRange.start)+self.nCleaningPrice
	def book(self, objDateRange):
		self.listReservations.append(objDateRange)
	def available(self, objDateRange):
		for i in self.listReservations:
			if(i.start < objDateRange.start 
				or i.end > objDateRange.end):
				return False
			else:
				if(i.start > objDateRange.start and i.end < objDateRange.end):
					return True
'''
objHotel = Hotel()
objDateFormat = DateFormat()
datetimeStart = objDateFormat.parse('1992-12-3')
datetimeEnd = objDateFormat.parse('1992-12-4')
objDateRange = DateRange(datetimeStart, datetimeEnd)
print 'Pret: '
print objHotel.price(objDateRange)

print 'book:' 
print objHotel.book(objDateRange)

print 'available'
print objHotel.available(objDateRange)
'''


"""
Ex. 5
Definiti clasa BiggerHotel care extinde clasa Hotel. BiggerHotel pe langa
parametrii primiti de Hotel va primi si un numar care va indica capacitatea
hotelului(nr de camere). Modificati metodele available si book astfel incat
sa tina cont si de numarul de camere.
"""
 
 
class BiggerHotel(Hotel):
	nCapacity = 0
	listReservations={}
	def __init__(self):
		self.nNightPrice = random.randint(50,150)
		self.nCleaningPrice = random.randint(0, 50)
		self.nCapacity = random.randint(0,20)
	def book(self, objDateRange, nRoomNumber):
		self.listReservations[nRoomNumber] = objDateRange
		nCapacity -= 1
	def available(self, objDateRange):
		for i in self.listReservations:
			if(i.start < objDateRange.start 
				or i.end > objDateRange.end and nCapacity < 0):
				return False
			else:
				if(i.start > objDateRange.start and i.end < objDateRange.end nCapacity>0):
					return True



"""
Ex. 6
Definiti clasa Point ce primeste doua coordonate (x, y) are metode interne
pentru operatii aritmetice, definiti aceste metode astfel incat sa putem
aduna/scadea doua puncte. Sugestie __add__, __sub__.
Exemplu:
p1 = Point(1, 2)
p2 = Point(2, 3)
p3 = p1 + p2
p4 = p1 - p2
"""
 
 
class Point(object):
	x=0
	y=0
	def __init__(self, nX, nY):
		self.x = nX
		self.y = nY
	def __add__(PointX, PointY):
		self.x = PointX.X + PointY.x
		self.y = PointX.y + PointY.y
	def __sub__(PointX, PointY):
		self.x = PointX.X - PointY.x
		self.y = PointX.y - PointY.y