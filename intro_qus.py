i = 0
while True:
	user = raw_input("enter a number")
	if user == "exit":
		break 
	i = i + 1

a = {"a":100,"b":200,"c":300}
i = 0
while i < len(a):
	i = i + 1
print (sum(a.values()))
i = 0
var = " "
while i < len(string):
	j = str(string[i])
	var = var + j
	i = i + 1
print var,


num = [[1,2,4],[4,2,6],[5,3,7]]
i = 0
sum = 0
while i < len(num):
	j = 0
	while j < len(num):
		sum = sum + num[i][j]
		j = j + 1
	i = i + 1
print sum


num = [3,4,6,4,2,2]
#output = [3,4,6,2]
#output = [4,6,8,4]
i = 0
new = []
while i < len(num):
	if num[i] not in new:
		new.append(num[i])
	i = i + 1
print new

i = 0
new_list = []
while i < len(new):
	if num[i]%2 == 0:
		new_list.append(num[i]+2)
	else:
		new_list.append(num[i]+1)
	i = i + 1
print new_list

