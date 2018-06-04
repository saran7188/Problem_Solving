n,k=map(int,input().split())
ls=list(map(int,input().split()))
ls.sort()
if(ls[k]<=1000000000 and ls[k]>=1):
	if k==0:
		print(ls[k])
	elif ls[k]==ls[k-1]:
		print('-1')
	else:
		print(ls[k-1])