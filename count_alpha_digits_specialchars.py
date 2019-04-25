a=open("name.txt",'r')
b=a.read()
print("string formed after reading file a:",b)
alpha,digit,spclchar=0,0,0
for i in b:
	if i.isalpha():
		alpha+=1
	elif i.isdigit():
		digit+=1
	else:
		spclchar+=1
print("no.of alphabets:",alpha)
print("no.of digits:",digit)
print("no.of  special characters:",spclchar)
a.close()
