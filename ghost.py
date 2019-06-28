# string =[[1,2,3],
#         [0,4,1],
#         [2,0,1]]
# count = 0
# i = 0
# j = 0
# sum = 0
# while i <= len(string)-1:
#     j = 0
#     while j <= len(string):
# 		if string[i+1] != 0:
# 			count = count + 1
# 		elif string[i+1][j] and [i-1][j] == 0:
# 			count = count + 1
# 			sum = sum + count
# 			j = j + 1
# 		i = i + 1
# print sum

string =[[1,2,3],
        [0,4,1],
        [2,0,1]]
count = 0
i = 0
a = 0
new = []
while i < len(string):
	j = 0
	while j < len(string[i]):
		if string[i][j] != 0 and [i-1][j] != 0:
			count = count + 1
			new.append(count[i][j])
			while a < len(new):
				count = count + new[a]
				a = a + 1
			j = j + 1
		i = i + 1
print count 