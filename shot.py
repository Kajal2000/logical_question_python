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
