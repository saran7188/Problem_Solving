n=int(input())
lis1=[]
lis2=[]
if(n<4 and n!=1):
    print("NO SOLUTION")
else:
    for i in range(1,n+1):
        if(i%2==0):
            lis1.append(i)
        else:
            lis2.append(i)
    final=lis1+lis2
    print(*final)