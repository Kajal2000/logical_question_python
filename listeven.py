num = [3,5,6,7,3,3,6,2,1]
i = 0
sum = 0
while i < len(num):
	sum = sum + num[i]
	i = i + 1
print sum
if sum%2==0:
	print "even h",sum
else:
	print "odd hain",sum