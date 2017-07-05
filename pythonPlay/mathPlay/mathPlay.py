class MathDojo(object):
	def __init__(self, num*):
		self.num = num
	def add(self):
		self.num =+ self.num
		print "You just added {} with {} giving you {}".format(self.num)
		return self
	def subtract(self):
		self.result = self.num1 - self.num2
		print "You just subtracted {} from {} giving you {}".format(self.num1, self.num2, self.result)
		return self

mathDojo().add(2).add(2,5).subtract(3,2).result
