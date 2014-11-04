def qsort(l):
	if not l:
		return []
	p=l[0]
	print l
	return qsort([x for x in l if x< p])+ [p] + qsort([x for x in l if x>p])

#qsort([1,3,4,2,7]);

#def dict():
#	list_with_dup = [1,2,2,3,3,3,4]
#	set([1,2,3])
#	print {x:0 for x in list_with_dup}

def map_in_dict(fn , d):
	return {key: fn(value) for key, value in d.items()}


my_dict = {"ana": 0, "gigi": 2}
map_in_dict(f, my_dict);