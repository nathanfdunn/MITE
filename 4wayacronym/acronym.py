words = [x.strip() for x in open('/usr/share/dict/words').readlines()]

words = [x for x in words if len(x)==4]

# Makes no difference in the end
# Exclude proper nouns, etc.
# words = [x for x in words if x.lower() == x]

def calcKey(string):
	return ''.join(sorted({c for c in string}))

mymap = {}
for x in words:
	key = calcKey(x)
	if len(key) == 4:
		if key not in mymap:
			mymap[key] = []
		mymap[key].append(x)

def uniquestart(strList):
	return len({x[0] for x in strList})

mymap = {x:mymap[x] for x in mymap if len(mymap[x]) >= 4 and uniquestart(mymap[x]) >= 4}

sizemap = [(len(mymap[key]), key) for key in mymap]
sizemap.sort(reverse=True)

for size, key in sizemap:
	print key
	for word in mymap[key]:
		print '\t\t', word
