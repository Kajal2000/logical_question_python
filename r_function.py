# list1 = [10,10,11,11]
# list2 = [10,10,11,11]
# i = 0
# while i <= len(list1):
#     if list1 == list2:
#         print "yes"
#         break
#     else:
#         print "no"
#         break
#     i = i + 1

# n = int(raw_input("enter your number"))
# user = int(raw_input("enter your number"))
# print n*user,
#iteration, statements, collections (List, Map, Tuple, Set etc

# num1 = [1,7,9,11]
# num2 = [2,4,8,15]
# new = []
# i = 0
# while i < len(num1)  j < len(num2):
#     if num1[i] < num2[j]:
#     new[k] == num1[i]
#     i = i + 1
#     k = k + 1

 
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def printnumber (a):
#     if a > 0:
#         printnumber (a-1)
#         print a
# printnumber(10)

# i = 10
# while i > 0:
#     print i
#     i = i - 1

# num1 = [1,3,5,7]
# num = [2,4,6,8,]
# list1 = num1+num
# print (list1)


# var = 0
# i = 0
# j = 0
# while i < len(list1):
#     if list1[i]>list1[i]:
#         var = list1[i]
#         print var
#         j = j + 1
#     i = i + 1


# def mergeSort(alist):
#     if len(alist)>1:
#         mid = len(alist)/2
#         lefthalf = alist[:mid]
#         righthalf = alist[mid:]

#         mergeSort(lefthalf)
#         mergeSort(righthalf)

#         i=0
#         j=0
#         k=0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 alist[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 alist[k]=righthalf[j]
#                 j=j+1
#             k=k+1

#         while i < len(lefthalf):
#             alist[k]=lefthalf[i]
#             i=i+1
#             k=k+1

#         while j < len(righthalf):
#             alist[k]=righthalf[j]
#             j=j+1
#             k=k+1
#     print(alist)

# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)

# new1 = []
# new2 = []
# A = [1,2,3,4,5,6]
# B = A[:len(A)/2]
# C = A[len(A)/2:]
# print B 
# print C



# new = []
# var = [8,12,3,4,5,6,7,8,9]
# a = var[:len(var)//2]
# print a 
# b = a[:len(a)//2] 
# new.append(b)
# print new


# string =[[1,2,3],
#         [0,4,5],
#         [2,0,1],
#         [0,4,5]]
# sum1 = 0
# i = 0
# j = 0
# while i < len(string):
#     j = 0
#     while j < len(string):
#         if string[i+1][j] == 0:
#             if string[i+1 and i-1][j] == 0:
#                 if string[i-1][j] == 0:
#                     sum1 = sum1 + string[i][j]
#                 j = j + 1
#             i = i + 1
#     print sum1

i = 1
while i < 5:
    j = 1
    while j < 5:
        print i,
        j = j + 1
    print " "
    i = i + 1
