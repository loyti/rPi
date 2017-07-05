class Bike(object):
    def __init__ (price,maxSpeed,miles):
        Bike.price = "$Really Expen$ive"
        Bike.maxSpeed = maxSpeed
        Bike.miles = 0
    def displayInfo(Bike):
        print "A little about your Bike: Price: {}, {} max kph & {} miles traveled".format(str(Bike.price), int(Bike.maxSpeed), str(Bike.miles))
        return Bike
    def ride(Bike):
        Bike.miles += 10
        print "You just went on a 10 mile journey" 
        return Bike
    def reverse(Bike):
        Bike.miles -= 5
        print "Backing up 5 miles in reverse is quite interesting You have gone {} miles ".format(Bike.miles)
        return Bike
    def noNeg(Bike):
        if (Bike.miles < 0):
            Bike.miles = 0
        print "You backed up off a cliff and were saved just in time but the bike is gone :( Here is a new one :)"
        return Bike

bike1 = Bike(99.99, 12)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(139.99, 20)
bike2.ride()
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.displayInfo()
