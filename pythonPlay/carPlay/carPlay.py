class Car(object):
	def __init__ (self, price, speed, fuel, mileage):
		self.price = price
        	self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax = .15
		else: 
			self.tax = .12
	def displayInfo(self):
        	print "About your car: Price: {}".format(int(self.price))
		print "Speed: {} mph".format(int(self.speed))
		print "Fuel: {}".format(str(self.fuel))
		print "Mileage: {}mpg".format(int(self.mileage))
		print "Tax: {}".format(self.tax)
	def carGo(self):
        	self.miles += 10
	        print "You just went on a 10 mile journey" 
car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(2000, 15, 'Kind of Full', 95)
car4 = Car(2000, 25, 'Full', 25)
car5 = Car(2000, 45, 'Empty', 25)
car6 = Car(20000000, 35, 'Empty', 15)
car1.displayInfo()
car2.displayInfo()
car3.displayInfo()
car4.displayInfo()
car5.displayInfo()
car6.displayInfo()
