startNum = 0
stopNum = 0
def oddEven(startNum, stopNum):
	#startNum = 1
	#stopNum = 2000
	oddNum = []
	evenNum = []
	for i in range(startNum, stopNum):
		if i % 2 is 1:
			oddNum.append(i)
			print "Number is",i,"This number is odd."
		else:
			evenNum.append(i)
			print "Number is",i,"This number is even."
oddEven(1,2000)

newArr = [2,4,10,16]
arrMult = []
multiplier = 5
def multArr(newArr,multiplier):
	for i in newArr:
		i *= multiplier
		arrMult.append(i)
	print arrMult
multArr(newArr,multiplier)
