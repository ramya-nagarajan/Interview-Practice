#find an element in a sorted rotated array

#Given a sorted array of n integers that has been rotated an unknown number of times, give an O(log n) algorithm that finds an element in the array. 
#You may assume that the array was originally sorted in increasing order

def search(a,e,u,l):
	
	#compute the mid of the array
	m = (u+l)/2

	while(u<=l):
		if(e == a[m]):
			return m
		
		elif(e<a[u]):
			u = m-1

		elif(e>a[u]):
			l = m+1

		

def main():
	arr = [15,16,17,18,1,2,3,5,9]
	search(3,0,len(arr)-1)
