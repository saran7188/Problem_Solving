n=int(input())

lis=list(map(int,input().split()))
maxi=0
lastmax=lis[0]
for i in range(1,len(lis)):
    if(lis[i]<lastmax):
        maxi+=abs(lastmax-lis[i])
    else:
        lastmax=lis[i]
print(maxi)
