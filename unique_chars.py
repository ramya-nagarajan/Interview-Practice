def unique(string):
	if len(string) > 128:
		return False

	#initialize all of them to False
	char_set =[False for _ in range(0,128)]
	#print char_set

	for c in string:
		print c
		val = ord(c)
		if char_set[val]:
			#if that value is already present in the char set then there is a duplicate, so return false
			return False
		#Otherwise, add it to the character set
		char_set[val] = True
	return True

def main():
	result = unique("abcdfghlAAAAAAAAAAA")
	print "Result ",result
main()