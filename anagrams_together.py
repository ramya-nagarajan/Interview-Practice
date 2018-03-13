# print anagrams together

class Word(object):
	def __init__(self,string,index):
		self.string = string
		self.index = index

def createDupArray(string,size):
	dupArray = []

	for i in xrange(size):
		dupArray.append(Word(string[i],i))
	return dupArray

def sortedAnagrams(words,size):
	
	dupArray = createDupArray(words,size)

	for i in xrange(size):
		dupArray[i].string = ''.join(sorted(dupArray[i].string))

	dupArray = sorted(dupArray,key=lambda k: k.string)

	for word in dupArray:
		print words[word.index]

def main():
	
	words = ["rope","pore","aorr","roar","make","kame","cake"]
	size = len(words)
	sortedAnagrams(words,size)
main()