
#maxuim number

num = [50, 40, 23, 70, 100, 7]
var = 0
i = 0
while i < len(num): #iske len tk hm loop chalate hain
	if var < num[i]: # yaha par hum var lessthen num[i] kiye hain kyu ki
		var = num[i]
	i = i + 1
print var

#odd me 1 numbet add krna hain or even number me 2 add karna hain

num = [50, 7, 9, 20, 10, 4]
i = 0
while i < len(num):
	if num[i] % 2 == 0:
		print num[i] + 2
	else:
		print num[i] + 1
	i = i + 1


#-------------------------------------------------
var = [2,43,6,7]
var.insert(2,45)
print var
#------------------------------------------------
# i = 0
# while i < 10:
# 	if i == 4:
# 		print i
# 	if i == 5:
# 		print i
# 	i = i + 1

var = [2,3,5,7,22,3]
user = input("enter a number")
i = 0
while i < len(var):
	if user == var[i]:
		print i
	i = i + 1

#var = [2,3,5,-1,22,3]
# user = input("enter a number")
# i = 0
# while i < len(var):
# 	if user == var[i]:
# 		var.remove(-1)
# 	if user == var[i]:
# 		print i,
# 	i = i + 1

