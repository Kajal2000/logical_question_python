user_input = int(raw_input("enter a number")) 
def shot_function(new_list):
    index = 0
    shot = sorted(new_list)
    return shot

def func(shot_list): 
    i = 0
    var = 0
    while i < len(shot_list):
        if shot_list[i] > var:
            var = shot_list[i]
        i = i + 1
    print var
# func(shot_list)

    # i = var
    # while i < len(shot_list):
    #     if shot_list[i] > var:
    #         var = shot_list[i]
    #     i = i + 1
    # print var

def shotage(user_input):
    i = 1
    new_list = []
    while i <= user_input:
        user = int(raw_input("how many row you want"))
        new_list.append(user)
        i = i + 1
    shot_list = shot_function(new_list)
    func(shot_list)
shotage(user_input)




# var = [44,3,11,4,1,8]
# i = 0
# new = []
# while i <=len(var):
#     min = var[i]
#     if var[i] < min:
#         num = i
# new.append(min)
# var.remove(min)
# print new



      
    