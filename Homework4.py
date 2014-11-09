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
return