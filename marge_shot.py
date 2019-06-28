num1 = [0,1,]
num2 = [2,4,3,7]
new = []
i = 0
j = 0
k = 0
while (i < len(num1)) and (i < len(num2)):
    if num1[i] < num2[j]:
        new[k] = num1[i]
        k = k + 1
        i = i + 1
    else:
        new[k] = num2[j]
        k = k + 1
        j = j + 1
    