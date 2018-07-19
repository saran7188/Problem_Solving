n,k=map(int,input().split())
ls=list(map(int,input().split()))

if(sum(ls)+n-1==k):
	print("YES")
else:
	print("NO")