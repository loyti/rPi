students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def studentNames (students):
	for i in students:
		print i["first_name"],i["last_name"]
studentNames(students)

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def allNames(users):
	countS = 0
	countI = 0
	for i in users:
		if i is "Students":
			print "Students"
			for x in users[i]:
				countS += 1
				print countS,"-",x["first_name"],x["last_name"],"-",len(x["first_name"])+len(x["last_name"])
		else: 
			print "Instructors"
			for x in users[i]:
				countI += 1
				print countI,"-",x["first_name"],x["last_name"],"-",len(x["first_name"])+len(x["last_name"])

allNames(users)
