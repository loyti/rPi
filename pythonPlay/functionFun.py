def oddEven(startNum, stopNum):
	startNum = 1
	stopNum = 2000
	oddNum = []
	evenNum = []
	for i in range(startNum, stopNum):
		if i % 2 is 1:
			oddNum.append(i)
			print "Number is",i,"This number is odd."
		else:
			evenNum.append(i)
			print "Number is",i,"This number is even."
	print oddNum, evenNum
oddEven(1,2000)
