n=int(input())
res=n//5
finalres=res
while(res>5):
	res=res//5
	finalres+=res
print(finalres)