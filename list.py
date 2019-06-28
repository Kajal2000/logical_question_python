a = int(raw_input("entar a number"))
if (a%2 == 0):
	b = chr(a)
	print b
#--------------------------------------
a = (raw_input("entar a number"))
if (a%2 == 0):
	b = ord(a)
	print b
#--------------------------------------------------------------------------
num = {"name": "kajal", "age": 19}
print num["age"] = 30
#--------------------------------------------------------------------------

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
#--------------------------------------------------------------------------------------
i = 0
while i < len(num):
	i = i + 1
print i

for i in range(1,10):
	if i % 2 == 0:
		print i,"even h"
# for i in range(15):
	else:
		if i % 2 != 0:
	 		print i,"odd h"


