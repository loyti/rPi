class MathDojo(object):
	def __init__(self):
		self.result = 0
	def add(self, *nums):
		for i in nums:
			if isinstance(i, list) or isinstance(i, tuple):
				for j in i: 
					self.result += i
			else:
				self.result += i
		print "You've done addition... Your new total is {}".format(self.result)
		return self
	def subtract(self, *nums):
		for i in nums:
			if isinstance(i, list) or isinstance(i, tuple):
				for j in i:
					self.result -= i
			else:
				self.result -=  i
		print "You just subtracted, your new total is {}".format(self.result)
		return self

MathDojo().add(2).add(20,5).subtract(3,20).result
