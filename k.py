var = [2,3,54,-1,5]
var.remove(-1)
print var


places = ["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
i = len(places)
while i > 1:
	i = i - 1
	print places[i]


# list in minium

num = [3,5,2,7,9] 
i = 0
var = num[i]
while i < len(num):
	if num[i] < var:
		var = num[i]
	i = i + 1
print var
