class Call(object):
	count = 0
	def __init__(self):
		pass

	def newCall(self,callerName,callerNumber,callTime,callReason):
		self.__class__.count += 1
		self.id = self.__class__.count
        	self.callerName = callerName
        	self.callerNumber = callerNumber
        	self.callTime = callTime
        	self.callReason = callReason
        	return self

	def displayCall(self):
        	print self.id,self.callerName,self.callerNumber,self.callTime,self.callReason
        	return self

randomCall1 = Call()
randomCall1.newCall("Brice",7145555555,1700,"Pizza Delivery")
randomCall1.displayCall()

randomCall2 = Call()
randomCall2.newCall("Niko",6265555555,800,"Breakfast")
randomCall2.displayCall()

randomCall3 = Call()
randomCall3.newCall("Kelvin",2135555555,1200,"Lunch")
randomCall3.displayCall()

randomCall4 = Call()
randomCall4.newCall("Oli",3105555555,1000,"Films")
randomCall4.displayCall()

class CallCenter(object):
	def __init__(self):
		pass
	def callTake(self):
        	pass
	def callQue(self):
        	pass
