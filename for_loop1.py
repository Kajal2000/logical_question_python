# for i in range(5,10):
# 	print i

# user = int(raw_input("enter a number"))
# i = 5
# while i <= user:
# 	print i 
# 	i = i + 1

# output = [[11,19],[12,18],[13,17]] 
def string_1(string):
	i = 0
	new = []
	user = int(raw_input("enter a number"))
	while i < len(string):
		j = i
		while j < len(string):
			if string[i] + string[j] == user:
				new.append([string[i],string[j]])
			j = j + 1
		i = i + 1
	print new

# list1 = [19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
# #output = [19,17,12,18,10,14,13,11]
# i = 0
# new = []
# while i < len(list1):
# 	if list1[i] not in new:
# 		new.append(list1[i]) 
# 	i = i + 1
# print new   

# var = ['a','b','c','d','e']
# val2 = [1,2,3,4,5]
# #output should be  {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# i = 0
# new = []
# while i < len(var):
# 	new.append(var[i])
# 	new.append(val2[i])
# 	i = i + 1
# print new

# num = [3,5,6,2,54,7,2,5,7,4]
# i = 0
# new = []
# while i < len(num):
# 	if i < len(num)/2:
# 		new.append(num[i])
# 	if i > len(num)/2:
# 		new.append(num[i])
# 	i = i + 1
# print new
	

# user = input("enter a number")
# i = 1
# while i <= user:
# 	print "".join(i),
# 	i = i + 1

num = [2,3,6,5,6,5]
i = 0
var = 0
while i < len(num):
	if num>var:
		var = num[i]
	i = i + 1
print var

