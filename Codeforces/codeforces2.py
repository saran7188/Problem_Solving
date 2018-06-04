n=int(input())
k=input()
count=[0]*n
for i in range(n):
	for j in range(n):
		if(k[i:i+2]==k[j:j+2]):
			count[i]+=1
key=0
for l in range(n):
	if count[key]<=count[i]:
		key=i
print(k[key:key+2])