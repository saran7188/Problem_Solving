n=int(input())
ls=list(map(int,input().split()))
ls1=[]
print(ls[:1],ls[2:])
for i in range(n):
	if (sum(ls[:i])==sum(ls[i:])):
		ls1.append(sum(ls[:i]))


print(max(ls1))