#merge two sorted arrays

def mergetwosorted(a,b,n,m):
	
	k= n+m-1
	i = m-1
	j = n-1

	while i>=0 and j>=0:
		if a[i] > b[j]:
			a[k] = a[i]
			k=k-1
			i=i-1
		else:
			a[k] = b[j]
			k = k-1
			j = j-1
	
	while j>=0:
		a[k] = b[j]
		k= k-1
		j=j-1
	return a

def main():
	a = [1,2,3,4,5,6,7,0,0,0,0,0,0,0,0]
	b = [3,4,5]
	#print a
	#print b
	n = len(a)
	m = len(b)
	#print n,m
	a = mergetwosorted(a,b,3,7)
	print a

main()
