import random
randomNum = random.random()*100+50
letterGrade = ["A+","A","B","C","D","F"]
print "You scored a ",randomNum,"on your test"
def testGrade(randomNum):
	if randomNum > 100:
		print "Score",randomNum,"Your grade is",letterGrade[0]
	elif randomNum > 90:
		print "Score",randomNum,"Your grade is",letterGrade[1]
	elif randomNum > 80:
		print "Score",randomNum,"Your grade is",letterGrade[2]
	elif randomNum > 70:
		print "Score",randomNum,"Your grade is",letterGrade[3]
	elif randomNum > 60:
		print "Score",randomNum,"Your grade is",letterGrade[4]
	else:
		print "Score",randomNum,"Your grade is",letterGrade[5],"Random Numbers Stink"
testGrade(randomNum)
