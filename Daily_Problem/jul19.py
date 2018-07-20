#Sum of first n fib numbers
n=int(input())
temp1=1
temp2=1
if(n==1):
	print(1)
elif(n==2):
	print(2)
else:
	sum1=2
	for i in range(3,n+1,1):
		temp=temp1+temp2
		temp1=temp2
		temp2=temp
		sum1+=temp
		#print(i,temp)
	print(sum1)

