from fractions import gcd
from functools import reduce
n=int(input())
while(n>0):
	n-=1
	k=int(input())
	ls=list(map(int,input().split()))
	ls.sort()
	gcder = reduce(lambda x,y : gcd(x,y),ls)
	if(gcder != 1):
		print('-1')
	else:
		print('0')
	

