from datetime import datetime, date

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
	strFormat = '%Y-%m-%d %H:%M'
	def format(self, objDateTime):
		return str(objDateTime)
	def parse(self, strDateToParse):
		return datetime.strptime(strDateToParse, self.strFormat)
'''
nowDate = date.today()
nowStr = '2013-09-28 20:30'
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
	end = date(2002, 12, 4)
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
