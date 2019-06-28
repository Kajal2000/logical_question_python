i = 1
q = 0
sum = 0
while i <= 10:
	user = input("enter your number")
	if user == q:
		break
	sum = sum + int(user)
	ava = sum / i
	i = i + 1
print ava

