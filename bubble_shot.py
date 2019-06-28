
num = [3,5,0,1,9,2,-1]
j = 0
while j<len(num):
	i=0
	while i < len(num)-1:
		if num[i]>num[i+1]:
			num[i],num[i+1] = num[i+1],num[i]
		i+=1
	j = j + 1
print num
