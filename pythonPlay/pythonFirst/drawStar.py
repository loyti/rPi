x = [4, 6, 1, 3, 5, 7, 25]
def drawStar (x):
	for i in x:
		print "*" * i
drawStar(x)

def stars2(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars2(x)

