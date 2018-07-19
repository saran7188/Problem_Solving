n,k=map(int,input().split())
ls=list(map(int,input().split()))
temp_ls=sorted(ls)

temp1=[]

for i in range(k):
	temp1.append(temp_ls[n-i-1])

print(sum(temp1))
temp2=0
j=0
for i in range(k):
	if(i!=k-1):
		while(True):
			if(ls[j] in temp1):
				temp1.remove(ls[j])
				print(j+1-temp2,end=' ')
				temp2=j+1
				break
			j+=1
	else:
		print(n-temp2,end=' ')



