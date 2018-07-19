n=int(input())
a=[]
for i in range(n):
	a.append(int(input()))

#print(a)
temp=1
if(a[0]==3):
	print("NO")
	exit()

if(n==2):
	#print("adfasfas")
	if((a[0]==1 and a[1]==2) or (a[0]==2 and a[1]==1)):
		print("NO")
		exit()
else:
	for i in range(1,n,2):
		if(a[i-1]==a[i+1] and a[i]!=a[i-1]):
			print("NO")
			exit()		

print("YES")