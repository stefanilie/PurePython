def get_dividers(n):
	list_div=[]
	for i in range(1,n+1):
		if n%i == 0:
			list_div.append(i)
	return list_div
#print get_dividers(15);

def power(n):
	power=1
	for i in range(n):
		power = power*n
	return power
#print power(4);

# 'primavara' -> 'prra'
def both_ends(s):
	string=''
	if(len(s)>2):
		string = s[0] + s[1]+ s[len(s)-2]  + s[len(s)-1]
		return string
	else:
		return string
#print both_ends('primavara');

def replace_chars(s):
	string = s[0]
	for i in range(len(s)):
		if i != 0:
			if s[i] == s[0]:
				string+='*'
			else:
				string+=s[i]
	return string
#print replace_chars('eleve')

# ['mere', 'banane'], [7, 5, 3] -> {'mere': 7, 'banane': 5}
# ['mere', 'pere', 'prune'], [9, 3] -> {'mere': 9, 'pere': 3, 'prune': 0}
def build_dict(keys, values):
	dictionary = {}
	counter=0
	if(len(keys)>len(values)):
		for i in range(len(values)):
			dictionary[str(keys[i])]=values[i]
			counter +=1
		for i in range(counter, len(keys)):
			dictionary[str(keys[i])] = 0
	else:
		for i in range(len(keys)):
			dictionary[str(keys[i])] = values[i]
	return dictionary

#print build_dict(['mere', 'pere', 'prune'], [9, 3]);
#print build_dict(['mere', 'banane'], [7, 5, 3]);

# 6.
# [1, 2, 3, 4, 5, 6], 2 -> [5, 6, 3, 4, 1, 2]
def swap_k(l, k):
	if not(0 <= k and k <= (len(l)/2)):
		return []
	else:
		print "else"
		for i in range(k):
			aux=l[i];
			l[i]=l[len(l)-k+i]
			l[len(l)+i-k] = aux
		return l

#print swap_k([1, 2, 3, 4, 5, 6], 2)

# 7. 
# ['a', 'b', 'a', 'c'] -> {'a': 2, 'b': 1, 'c': 1}
#Nu are nici o logica. ma bate.
def how_many(l):
	dictionary={}
	for i in range(len(l)):
		counter=1
		print "l[i]="+l[i];
		for j in range(i+1, len(l)):
			print "verific daca "+l[i]+"=="+l[j]
			if(l[i]==l[j]):
				counter += 1
				print "a instrat pe if si va creste contorul "+ str(counter)
		print "am iesit din for cu counter="+ str(counter)
		dictionary[l[i]]=counter
		print "am atribuit lui "+str(dictionary[l[i]])+ "valuarea "+ str(counter)
		print "\n"
	return dictionary

print how_many(['a', 'b', 'a', 'c', 'a']);

#The mind can only absorb what the butt can endure