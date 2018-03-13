
#!/usr/bin/python
import random
import math
import time


def spilt_list():

	l = [200,300,400,555,233,769,900,1234,11268,1,2,3]

	listeven =[]
	listodd =[]

	for i in l:
		if(i%2 ==0):
			listeven.append(i);
		else:
			listodd.append(i);

	print(sorted(listodd))
	print(sorted(listeven))
	


def main():
	spilt_list()

main()