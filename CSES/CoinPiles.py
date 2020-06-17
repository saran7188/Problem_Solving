n=int(input())
for i in range(n):
	a,b=map(int,input().split())
	if((2*a-b)>=0 and (2*b-a)>=0 and (2*a-b)%3==0 and (2*b-a)%3==0):
		print("YES")
	else:
		print("NO")