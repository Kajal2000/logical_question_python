user = (input("enter a number:"))
sum1 = 0
i = user
while i > 0:
	num = i%10
	var = num ** 3
	sum1 = sum1 + var
	i /= 10
if user == sum1:
	print user,"armstrong h"
else:
	print user,"armstrong nhi h"




