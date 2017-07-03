name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favAnimal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
nameFav = []
def listDict (name,favAnimal):
	if len(name) >= len(favAnimal):
		nameFav = zip(name,favAnimal)
		nameDict = dict(nameFav)
		print nameDict
	else:
		nameFav = zip(favAnimal,name)
		nameDict = dict(nameFav)
		print nameDict
listDict(name,favAnimal)
