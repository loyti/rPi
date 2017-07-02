spI = ["MJ is GOAT", 8,1,14]
sS = ["Red Sox Rule", "From Michigan, show the point on your right palm"]
bS = ["When I write I remeber", "Teach me and I know", "Involve me and I learn"]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
sum = 0
sumInt = [sum]
sumString = []
bigList = [spI, sS, bS, mL, lL]
for currentTest in bigList:
	if isinstance(currentTest, list):
		for itemTest in currentTest:
			if type(itemTest) is int:
				sum += itemTest
				sumInt.append(itemTest)
				print "you found an int"
				continue
			elif type(itemTest) is str:
				sumString.append(itemTest)
				print "you found a string"
				continue
		
print sumString, sum, sumInt
