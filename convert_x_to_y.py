
def convert_x_to_y(m,n):

	if m==n:
		return 0
	
	if m>n:
		return m-n

	if m<=0 and n >0:
		return -1

	if n%2 == 1:
		return 1+convert_x_to_y(m,n+1)
	else:
		return 1+convert_x_to_y(m,n/2)

res = convert_x_to_y(11,3)
print res