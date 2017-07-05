class Products(object):
	def __init__(self, price, itemName, weight, brand, cost, availableI, conditionI):
		self.price = price
		self.itemName = itemName
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.availableI = availableI
		self.conditionI = conditionI
		if (conditionI == "New"):
			self.status = "For Sale"
		else:
			self.status = "NOT For Sale"
	def sold(self):
		self.available = 0
		print "Your product {} is {}".format(self.itemName, self.status)
		return self
	def addTax(self):
		self.tax = self.price * .13
		print "Your total amount due is ${} + ${}tax".format(int(self.price), float(self.tax))
		return self
	def returnI(self):
		self.conditionI = "Old"
		if (self.conditionI != "New"):
			self.available = 1
			self.price = self.price * 8 / 10
			print "The new sales price on {} is {}".format(self.itemName,self.price)
			return self
		else:
			self.price = 0
			print "The item is defective and worth ${}".format(self.price)
			return self
	def displayInfo(self):
		print "Price {}".format(int(self.price))
		print "Name {}".format(str(self.itemName))
		print "Weight {}".format(int(self.weight))
		print "Brand {}".format(str(self.brand))
		print "Cost {}".format(int(self.cost)) 
		print "Available Inventory {}".format(int(self.availableI))
		print "Condition {}".format(str(self.conditionI))
		print "Status {}".format(str(self.status))
product1 = Products(5, "Oreos", 1, "Nabisco", "2", 1, "New")
product1.displayInfo()
product1.sold()
product1.addTax()
product1.returnI()
