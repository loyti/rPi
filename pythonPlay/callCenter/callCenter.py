class Call(object):
	callID = 0
	callQue = []
	activeCall = False
	def __init__(self):
		pass

	def newCall(self,callerName,callerNumber,callTime,callReason):
		self.__class__.callID += 1
		self.id = self.__class__.callID
		self.__class__.callQue.append(callerName)
		self.callQue = self.__class__.callQue
		self.__class__.activeCall = True
		self.activeCall = self.__class__.activeCall
        	self.callerName = callerName
        	self.callerNumber = callerNumber
        	self.callTime = callTime
        	self.callReason = callReason
        	return self

	def displayCall(self):
        	print self.id,self.callerName,self.callerNumber,self.callTime,self.callReason
        	if len(self.callQue) == 1:
			print len(self.callQue),"Caller in the queue",self.callQue
		else:
			print len(self.callQue),"Callers in the queue",self.callQue
		return self

	def openCall(self):
		self.__class__.activeCall != self.__class__.activeCall
		self.activeCall = self.__class__.activeCall
		print "The call with {} is open {}".format(self.callQue,self.activeCall)
		return self

	def closeCall(self):
		self.activeCall != self.activeCall
		print "The call is closed {}".format(self.activeCall)
		temp = self.callQue.pop(0)
		print "{} has been removed from the Queue and {} remain".format(temp,self.callQue)
		return self
	
randomCall1 = Call()
randomCall1.newCall("Brice",7145555555,1700,"Pizza Delivery")
randomCall1.displayCall().openCall()

randomCall2 = Call()
randomCall2.newCall("Niko",6265555555,800,"Breakfast")
randomCall2.displayCall()

randomCall3 = Call()
randomCall3.newCall("Mark",2135555555,1200,"Lunch")
randomCall3.displayCall()

randomCall4 = Call()
randomCall4.newCall("Oli",3105555555,1000,"Films")
randomCall4.displayCall()

randomCall1.closeCall()
