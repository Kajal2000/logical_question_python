import requests
import json
url = "http://saral.navgurukul.org/api/courses"

def url_1(kajal):
    var_1 = requests.get(url)
    var_2 = var_1.json()
    return (var_2)
print url_1(url)

url1 = url+"/"+"courses"
all_courses = url_1(url1)

new_id = []
def avl_courses(course_1):
    i = 0
    while i < len(all_courses["availableCourses"]):
        course_ex = all_courses["availableCourses"][i]["name"]
        course_id = all_courses["availableCourses"][i]["id"]
        print i, course_ex
        new_id.append(course_id)
        i = i + 1
    #print new_id,

print avl_courses("availableCourses")

user_1 = int(raw_input("enter yr exercises"))
exercise = url+"/"+str(user_1)+"/exercises"
a = requests.get(exercise)
#print (a.text)

convert = a.json()
#print (convert)


def courses_exercise():
    i = 0
    while (i < len(convert["data"])):
        var_3 = (convert["data"][i]["name"])
        print i, var_3
        i = i + 1
courses_exercise()
