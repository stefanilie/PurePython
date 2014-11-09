"""
Ex1:
Implementati o functie echivalenta cu functia built-in ``map`` din Python,
care primeste 2 parametri: o functie si un iterabil.
Iterabilul poate fi o lista sau un string.
"""
 
def my_map(func, iterable):
	if(type(iterable)==str):
		return func(iterable)
	else:
		if(type(iterable)==list):
			return [func(x) for x in iterable]

"""
Ex2:
Implementati o functie echivalenta cu functia built-in ``filter`` din Python,
care primeste 2 parametri: o functie si un iterabil.
Iterabilul poate fi o lista sau un string.
"""
 
def my_filter(func, iterable):
	if(type(iterable) == str):
		if(func(iterable) == True):
			return iterable
		else:
			if(not func(iterable)):
				return ""
	else:
		if(type(iterable)==list):
			return[func(x) for x in iterable if func(x)==True]

"""
Ex3:
Simulați o mică bază de date de persoane folosind un dicționar:
 
a) Vom avea o bază de date key -> value, key este un id, value este un dicționar
cu 2 chei: nume și vârstă. Inițializați o bază de date goală.
"""
 
db = {}

"""
b) Scrieti o clasa Person care primeste la initializare nume, varsta si sex.
Pentru a fi mai usor la gender folositi 'F' pt feminin si 'M' pt masculin.
"""
 
class Person(object):
	def __init__(self, name='', age=0, sex=''):
		strName=name
		nAge=age
		bSex=sex;
"""
c) Scrieti o functie ``person_factory`` care primeste o lista de tupluri.
Fiecare tuplu este o pereche de forma (name, age, gender). Functia intoarce o
lista de obiecte de tip Persone initializate cu valorile primite. Lista va
creea obiecte de tip Person doar daca varsta este mai mare sau egala cu 18 si
va fi ordonata dupa acest atribut.
"""
 
def person_factory(persons_data):
	return [Person(x[0], x[1], x[2]) for x in persons_data if x[1]>18]

"""
d) Creați o metodă ``add_persons`` care primește o bază de date și o listă de
persoane pe care le introduce în această bază de date. Apelați-o și introduceți
câteva persoane.
Atentie la felul in care alageti indexul, sa nu suprascrieti intrari care
exista deja in baza de date. Functia poate fi apelata de mai multe ori pt
a introduce persoane in baza de date
"""
 
def add_persons(db, persons):
	

