s=input()
count=1
maxcount=0
for i in range(1,len(s)):
	if(s[i]==s[i-1]):
		count+=1
	else:
		if(maxcount<count):
			maxcount=count
		count=1
if(maxcount<count):
	maxcount=count
print(maxcount)
