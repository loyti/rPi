listOne = [1,2,5,6,2]
listTwo = [1,2,5,6,2]

listThree = [1,2,5,6,5]
listFour = [1,2,5,6,5,3]

listFive = [1,2,5,6,5,16]
listSix = [1,2,5,6,5]

testList = []
testCompare = 0

for i in range(len(listThree)):
	print listThree[i]
	testList.append(listThree[i])
	print testList
for j in range(len(listFour)):
	print listFour[j]
if (listThree[i] is listFour[j]):
	testList.append(listThree[i])
	print "The lists are the same"
else: 
	testCompare += 1
	print "The lists are not the same"
if testCompare is 0:
	print "The lists are the same"
else: 
	print "The lists are not the same"
