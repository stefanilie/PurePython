import random 
from datetime import datetime, date
import re
import this

b=[]
a = [1, 3, 20, 1024, 53, 12, 102, 1, 4, 43, 32]
def pozImp():
	for i in range(len(a)):
		if i%2!=0:
			b.append(a[i])
	print b

def fizzBuzz():
	for i in range(100):
		if i%3==0:
			print "fizz"
		elif  i%5==0:
			print "buzz"
		elif i%15==0:
			print "fizz buzz"
		else: 
			print i

def Lista():
	articole={"tastatura": 70, "mouse": 50, "casti": 100}
	suma = 0
	for i in articole:
		print i, "costa", articole[i]
		articole[i] = articole[i]+ articole[i]*0.24
	for i in articole:
		suma=articole[i]+suma
	print "Dupa aplicarea TVA-ului:", articole, "iar totalul este de", suma


def Factorial(n):
	factorial=1
	toAdd=1
	for i in range(n+1):
		toAdd =1
		for j in range(i):
			if(j!=0):
				toAdd = toAdd*j
		factorial = factorial+toAdd
	print factorial

def Interval():
	result=""
	for i in range(2000, 5001, 1):
		if(i%5==0):
			if(i%7!=0):
				if(i!=5000):
					result += str(i) + ", "	
				elif (i==5000):
					result += str(i)

	print result

def Palindrom(str):
	print str[1]

def interschimb():
	a =5
	b=6
	a, b = b, a

#=============================Laboratorul 2==============================
def NumaraLinii():
	inf = open('input.txt', 'r')
	i = 0
	for line in inf:
		i=i+1
	outf = open('output.txt', 'w')
	outf.write("\nNumarul de linii este:")
	outf.write(str(i))
	inf.close()
	outf.close()

def OneHundred():
	i=random.randint(1,10)
	f = open('output_2.txt', 'w')
	while i%2==0:
		i=random.randint(1, 10)
	for j in range(i):
		toWrite = random.randint(100, 1000)
		while(toWrite%2!=0):
			toWrite = random.randint(100, 1000)
		f.write('\n')
		f.write(str(toWrite))
	f.close()

def BirthDate():
	f = open('input_birth.txt', 'r')
	o = open('output_birth.txt', 'w')
	nastere = date(1992, 12, 4)
	now = date.today()
	diff = now-nastere
	print(diff.days)

def Carti():
	culori=['romb', 'rosie', 'neagra', 'trefla']
	carte = ['a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	objCarte = str(random.choice(carte)+' '+str(random.choice(culori)))
	print objCarte
	return objCarte

def Mana5():
	arrCarti=[]
	objCarte = Carti()
	arrCarti.append(objCarte)
	for i in range(4):
		if objCarte not in arrCarti:
			arrCarti.append(objCarte)
		else: 
			while objCarte in arrCarti:
				objCarte = Carti()
		arrCarti.append(objCarte)
	print arrCarti

def sasedin49():
	arrSelectate=[]
	nSelected = 6
	toAdd = random.randint(1, 49)
	arrSelectate.append(toAdd)
	for i in range(5):
		if toAdd not in arrSelectate:
			arrSelectate.append(toAdd)
		else:
			while toAdd in arrSelectate:
				toAdd = random.randint(1,49)
		arrSelectate.append(toAdd)
	print arrSelectate

def sasedin49_2(arrSelectate, remaining):
	toAdd = random.randint(1,49)
	if remaining > 0:
		if toAdd not in arrSelectate:
			arrSelectate.append(toAdd)
			remaining-=1
		else:
			while toAdd in arrSelectate:
				toAdd = random.randint(1,49)
			arrSelectate.append(toAdd)
			remaining-=1
	print arrSelectate
	sasedin49(arrSelectate, remaining)

arr=[]
#nu inteleg de ce nu merge acest apel de functie
#sasedin49_2(arr, 6);

def sumaPatrate(number):
	sum=0
	for i in range(number+1):
		if i%2 != 0:
			sum += i*i
			print "L-am adunat pe " + str(i*i) + " si suma e "+ str(sum) 
	print sum

def validNumber(strPhoneNr):
	validation = re.compile(r'(.{,9})021([0-9]{7})(.{,9})')
	result = validation.search(strPhoneNr)
	if str(result) != 'None':
		print 'True'
	else:
		print 'False'

#validNumber('0217687999');
#validNumber('Numarul meu de telefon este: 0212428042 ai inteles?');

def timezone(strZone=''):
	today = datetime.now()
	if strZone.lower() == 'usa' or strZone.lower() == 'us' or strZone.lower()=='america':
		print today.strftime('%b %d, %Y -  %H:%M')
	else: 
		print today.strftime('%H:%M/ %d.%m')


#timezone();

#============================================LAB 3===================================================

#============================================LAB 4===================================================
def zaruri():
	return [(x+1, y+1) for x in range(6) for y in range(6)]
#print zaruri();

def dublu(List):
	return list({elem for elem in List})
#print dublu([1,11,1,1,4,5,6])

def companii():
	companies = [
	    ("Pixar", 2),
	    ("Disney", 4),
	    ("Warner Bros.", 9),
	    ("Universal", 5),
	    ("Reception", 0),
	    ("Studio Ghibli", 8),
	    ("DreamWorks", 6),
	]

	dictCompanies = {n:s for n, s in companies}
#	print dictCompanies;
	return dictCompanies
#companii();

def companii_by_etaj():
	dictEtaj = {value: key for (key, value) in companii().items()}

	return [dictEtaj.get(i) for i in range(10)]
#print companii_by_etaj();

def zen_of_python():
	words = str(this).split()
	return [indez for indez, word in enumerate(words) if word=='better']
print zen_of_python();

