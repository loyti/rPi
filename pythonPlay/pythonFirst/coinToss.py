import random
tossTimes = 5000
#x = random.random()
def coinToss(tossTimes):
	heads = 0
	tails = 0
	while tossTimes > 0:
		x = random.random()
		if x > .5:
			heads += 1
			print "Flipping a coin... It's heads and there are",heads,"so far and",tails,"tails so far"
			tossTimes -= 1
		else:
			tails += 1
			print "Flipping a coin... It's tails and there are",heads,"so far and",tails,"tails so far"
			tossTimes -= 1
coinToss(tossTimes)
