day = raw_input("enter a number")
team = raw_input("enter a team")
if day == "monday":
    if team == "2":
        print "kajal,puja"
    else:
        print "nothing"
else:
    print "kuch nhi"


i = 1
while i <= 5:
	print (str(i)* i)
	i = i + 1


num = [1,2,4,6,8]
num.insert(2,"3")
print num


string = [20,23,8,25,10,23,25]
new = []
i = 0
while i < len(string):
	if string[i] not in new:
		new.append(string[i])
	i = i + 1
print new
i = 0
new_list = []
while i < len(new):
	if new[i] % 2 == 0:
		new_list.append(new[i]+2),
	else:
		new_list.append(new[i]+2),
	i = i + 1
print new_list