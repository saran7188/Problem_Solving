n=int(input())
ls=list(map(int,input().split())
print(ls)
ls.sort()
count=0
flag=0
while(True):
	temp=ls[0]
	while temp in ls:
		ls.remove(temp)
		count+=1
	if(flag==0):
		poi=count
	else:
		if(poi+count<=n):
			poi=poi+count
		elif(poi+count>n):
			poi=poi+count-((poi+count)-n)
			count=count-((poi+count)-n)
			print(count)
			exit()

