num = [23,2,5,7,3,4]
i = 0
var = num[i]
while i < len(num):
	if num[i] < var:
		var = num[i]
	i = i + 1
num.remove(var)
#print num
j = 0
var = num[j]
while j < len(num):
	if num[j] < var:
		var = num[j]
	j = j + 1
print var

# num = ["n","a","v","g","u","r","u","k","u","l"]
# i = 0
# a = " "
# while i < len(num):
# 	j = str(num[i])
# 	a = a + j
# 	i = i + 1
# print a,

# Input : {'one':5, 'two':1, 'three':6, 'four':10} 
# #Output : Second largest value of the dictionary is 6 

# num = {'one':5, 'two':1, 'three':6, 'four':10} 
# i = 0
# var = num[i]
# while i < num(value):
# 	if num[valuse] < var:
# 		var = num[i]
# 	i = i + 1
# print var


 

