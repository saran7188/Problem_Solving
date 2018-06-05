n=int(input())
while n>0:
    k=int(input())
    arr1=list(map(int,input().split()))
    l=int(input())
    arr2=list(map(int,input().split()))
    if len(set(arr1).difference(set(arr2)))==0:
        print ("True")
    else:
        print("False")
    n=n-1

