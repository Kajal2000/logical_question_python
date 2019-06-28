num1 = int(raw_input("enter your number"))
num2 = int(raw_input("enter your number"))
if num1 > num2:
	var = num2
else:
	var = num1
i = 1
while i < var:
	if num1 % i == 0 and num2 % i == 0:
		a = i
	i = i + 1
print a

