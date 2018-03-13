#find the length of the longest common subsequence in two given strings

"""def lcs(a,b,i,j):

	if i>= len(a) or j>= len(b):
		return 0
	elif a[i] == b[j]:
		return 1+ lcs(a,b,i+1,j+1)
	else:
		return max(lcs(a,b,i+1,j),lcs(a,b,i,j+1),lcs(a,b,i+1,j+1))
"""

def lcs(a,b):

	m = len(a)
	n = len(b)

	L = [[None]*(n+1) for i in xrange(m+1)]
	
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				#set the first row and col to 0, for starting point reference
				L[i][j] = 0
			elif a[i-1] == b[j-1]:
				#look at prev diagonal element and add one
				L[i][j] = L[i-1][j-1]+1
			else:
				#consider max value of left element and above element
				L[i][j] = max(L[i-1][j],L[i][j-1])

	#returning the last value in the table which will correspond to the length of a and b
	return L[m][n]


def main():
	str1 = "AFXFXR"
	str2 = "ABCDGH"
	i=0
	j=0
	res = lcs(str1,str2)
	print(res)

main()