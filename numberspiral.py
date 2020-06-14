n=int(input())
for i in range(n):
	a,b=map(int,input().split())
	maxi=max(a,b)
	ans=0
	pivot=1+((maxi*(maxi-1)))
	if(maxi%2==0):
		if(maxi==a):
			ans=pivot+maxi-b
		else:
			ans=pivot-maxi+a
	else:
		if(maxi==a):
			ans=pivot-maxi+b
		else:
			ans=pivot+maxi-a
	print(ans)