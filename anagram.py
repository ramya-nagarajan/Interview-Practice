#!/usr/bin/python

def anagram_checker(s1,s2):

	word1 = []
	word2 = []
	for i in range(len(s1)):
		word1.append(s1[i])

	for i in range(len(s2)):
		word2.append(s2[i])

	if(len(word1) == len(word2)):
		for c in word1:
			if c in word2:
				word2.remove(c)

	if len(word2) == 0:
		return True
	else:
		return False

def main():
	result = anagram_checker("ramya","aarmy")
	print result
main()
