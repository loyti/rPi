word_list = ['hello','world','my','name','is','Anna']
char = 'o'
listWords = []
for i in range(len(word_list)):
	print word_list[i]
	for j in word_list[i]:
		if j is 'o':
			listWords.append(word_list[i])
print listWords
