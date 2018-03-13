def nums(a,b):
	x =a
	y=b

	while x!=y :
		if x ==y:
			return x
		elif x>y:
			x = x-y
		elif x<y:
			y = y-x

res = nums(2437,875)
print res