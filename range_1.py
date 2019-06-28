# num = [10, 20, 30, 40, 50, 40, 40, 60, 70] #range: 40-80
# i = 0
# count = 0
# while i < len(num):
# 	if num[i] >= 40 and num[i] < 80:
# 		count = count + 1
# 	i = i + 1
# print count
#===========================================================================
# Input : [10, 20, 30, 40, 50, 40, 40, 60, 70] range: 10-40
# Output : 4

num = [10, 20, 30, 40, 50, 40, 40, 60, 70] #range: 10-40
i = 0
count = 1
while i < len(num):
	if num[i] > 10 and num[i] > 40:
		count = count + 1
	i = i + 1
print count 

#=====================================================================
# def add(num):
# 	i = 0
# 	count = 0
# 	while i < len(num):
# 		if num[i] >= 40 and num[i] < 80:
# 			count = count + 1
# 		i = i + 1
# 	print count
# add([10, 20, 30, 40, 50, 40, 40, 60, 70] )

