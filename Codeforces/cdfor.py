s=input()
vowels=['a','e','i','o','u']
flag=0
if not (((s[len(s)-1:] in vowels) or (s[len(s)-1:] == 'n'))):
	print("NO")
else:
	for i in range(len(s)):
		if s[i] in vowels:
			True
		elif (s[i]=='n'):
			True
		else:
			if s[i+1] in vowels:
				True
			else:
				flag+=1
				print("NO")
	if(flag==0):
		print("YES")