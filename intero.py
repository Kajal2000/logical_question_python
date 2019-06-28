import requests
url_1 = "http://saral.navgurukul.org/api/courses"
var_1 = requests.get(url_1)
print (var_1.text)