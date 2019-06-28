string = [[1,2,3],[4,5,6],[7,8,9]]
i = 0
sum = 0
while i < len(string):
		sum = sum + string[i][i]
		i = i + 1
print sum

# both are different 

num = [[1,2,3],[4,5,6],[7,8,10]]
i = 0
j = 0
sum2 = 0
sum1 = 0
while i < len(num):
	sum1 = sum1 + num[i][i]
	j=j+1
	sum2 = sum2 + num[i][-j]
	i = i + 1
print sum1
print sum2
var = sum1-sum2
print var

# [10,20,10,30,10,40,20,30,40]

num = [10,20,30,40]
i = 0
new = []
while i < len(num):
	j = 1
	j = j + 1
	while j < len(num):
		new.append([num[i],num[j]])
		j = j + 1
	i = i + 1
print new
