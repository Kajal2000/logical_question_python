
# list in minium
num = [3,5,2,7,9] 
i = 0
var = num[i]
while i < len(num):
	if num[i] < var:
		var = num[i]
	i = i + 1
print var
