string = "aaaaaaabbbbbccccddd"
i = 0
a = 0
b = 0
c = 0
d = 0
while i < len(string):
	if "a" in string[i]:
		a = a + 1
	if "b" in string[i]:
		b = b + 1
	if "c" in string[i]:
		c = c + 1
	if "d" in string[i]:
		d = d + 1
	i = i + 1
print a,b,c,d 

user = input("enter a number")
i=1
while i<=3:
	print user+i
	i=i+1
i=1
while i <= 3:
	print user-i
	i=i+1

