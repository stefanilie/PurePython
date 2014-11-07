import random

def count_lines():
	file_to_read = open('count_lines_input.txt', 'r')
	counter=0
	for line in file_to_read:
		counter+=1
	file_to_write = open('count_lines_output.txt', 'w')
	file_to_write.write("Numarul de linii este:")
	file_to_write.write(str(counter))
	file_to_read.close()
	file_to_write.close()

#count_lines()
 
def write_random_lines_and_numbers():
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

#write_random_lines_and_numbers()
 
def my_age_in_days():
	f = open('input_birth.txt', 'r')
	o = open('output_birth.txt', 'w')
	nastere = date(1992, 12, 4)
	now = date.today()
	diff = now-nastere
	print(diff.days)

#my_age_in_days()

# 4. Scrieți o funcție python care generează o carte random dintr-un pachet
# clasic de cărți de joc. Încercați să dați două soluții diferite.
# Exemple de output:
#
# `'5 romb'`
# `'K trefla'`
# `'A rosie'`
# `'J negru'`
 
def get_card():
	culori=['romb', 'rosie', 'neagra', 'trefla']
	carte = ['a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
	objCarte = str(random.choice(carte)+' '+str(random.choice(culori)))
	print objCarte
	return objCarte

#print get_card()

# 5. Scrieți o funcție care returnează o mână de 5 cărți diferite (ca la macao).
# Observație: Nu puteți apela funcția precedentă de 5 ori deoarece există
# posibilitatea să vă dea aceeași carte de mai multe ori. Exemplu de output:
#
# `['10 romb', '4 romb', 'J negru', '7 rosie', '3 trefla']`
 
def get_hand_of_cards():
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

#get_hand_of_cards()
 
def loto():
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

#loto()

def loto_2(arrSelectate, remaining):
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
#loto_2(arr, 6);
 
def sum_of_odd_squares():
	sum=0
	for i in range(number+1):
		if i%2 != 0:
			sum += i*i
			print "L-am adunat pe " + str(i*i) + " si suma e "+ str(sum) 
	print sum

#sum_of_odd_squares()

def any_valid_number(text):
	validation = re.compile(r'(.{,9})021([0-9]{7})(.{,9})')
	result = validation.search(strPhoneNr)
	if str(result) != 'None':
		print 'True'
	else:
		print 'False'

#any_valid_number('0217687999');
#any_valid_number('Numarul meu de telefon este: 0212428042 ai inteles?');

 
def current_time(time_format):
	today = datetime.now()
	if strZone.lower() == 'usa' or strZone.lower() == 'us' or strZone.lower()=='america':
		print today.strftime('%b %d, %Y -  %H:%M')
	else: 
		print today.strftime('%H:%M/ %d.%m')

#current_time();

