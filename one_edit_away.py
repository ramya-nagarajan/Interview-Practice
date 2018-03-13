def insert_to_str(s1,s2):
	i=0
	j=0
	flag =False
	while i<len(s1) and j<len(s2):
		if s1[i] != s2[j]:
			if flag == True:
				# already added one element, adding one more would make it two away and not one away
				return False
			#first occurence of the new letter, so can add it to the string, set flag
			flag = True
			#how much ever is remaining in the shorter string should be present as such in the rest of the longer string, so we increment only the shorter one
			j = j+1
		else:
			j = j+1
			i = i+1
	return True

def one_edit_away(s1,s2):
	if len(s1)+1 == len(s2):
		#s1 is the longer string
		return insert_to_str(s1,s2)
	elif len(s1)-1 == len(s2):
		#since s2 is the longer string
		return insert_to_str(s2,s1)
	return False


def main():
	s1 = "pala"
	s2 = "xal"
	res = one_edit_away(s1,s2)
	print res

main()