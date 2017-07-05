class mathDojo(object):
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
class add(mathDojo):
	def __init__(self):
		superself.result = self.num1 + self.num2
		print "You just added {} with {} giving you {}".format(self.num1, self.num2, self.result)
		return self
	def subtract(self):
		self.result = self.num1 - self.num2
		print "You just subtracted {} from {} giving you {}".format(self.num1, self.num2, self.result)
		return self

mathDojo().add(2).add(2,5).subtract(3,2).result
