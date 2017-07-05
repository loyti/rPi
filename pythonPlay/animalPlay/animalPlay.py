class Animals(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		print "Walking takes energy. Lose 1 health for {} total health".format(int(self.health))
		return self

	def run(self):
		self.health -= 5 
		print "Running is hard lose 5 health for {} total health remaining".format(int(self.health))
		return self

	def displayHealth(self):
		print "My name is {} and my current Health is: {}".format(str(self.name),int(self.health))
		return self

animal = Animals("Rev")
animal.walk().run().walk().run().displayHealth()

class Dog(Animals):
	def __init__(self,name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		print "Dogs love getting a massage. Gain 5 for {} total health".format(int(self.health))
		return self

class Dragon(Animals):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		print "My name is {} and I fly because I'm a Dragon. Flying is tiring, lose 10 for {} total health".format(str(self.name),int(self.health))
		return self

f = Dog("fido")
f.run().walk().displayHealth()

d = Dragon("Malificent")
d.walk().run().fly().displayHealth()

