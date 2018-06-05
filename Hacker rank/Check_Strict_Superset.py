s=set(map(int,input().split()))
n=int(input())
k=n
count=0
while(n>0):
    arr=set(map(int,input().split()))
    if len(s)<=len(arr) :
        print("False")
    else:
        if(len(arr.difference(s))==0):
            count+=1
    n-=1
if(count == k):
    print("True")
else:
    print("False")
