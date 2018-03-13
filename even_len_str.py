def even_length(sentence):

	list1 = [word for word in sentence.split() if len(word) % 2 == 0 ]
	return max(list1,key=len)

res = even_length("Today is a sunday. Tomorrow is a monday")
print res