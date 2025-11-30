# first_name = "tarek"
# last_name = "oukacha"
# school = "english academy"
# date_of_birth = "6/11/2009"
# email = "ttssjjaa@gmail.com"
# age = 16
# address = "UAE"

# personal_info = ["tarek","oukacha","english academy",'6/11/2009',"ttssjjaa@gmail.com",16,"UAE"]

# print("first name =",personal_info[0])
# print("last name =",personal_info[1])
# print("date of birth =",personal_info[2])
# print("email =",personal_info[3])
# print("age =",personal_info[4])
# print("address =",personal_info[5])

personal_info1 = {
    "first_name" : "tarek",
    "last_name" : "oukacha",
    "school" : "english academy",
    "date_of_birth" : "6/11/2009",
    "email" : "ttssjjaa@gmail.com",
    "age" : 16,
    "address" : "UAE",
    "friends" : ["ram","mohammad","abdullah"]
}
personal_info2 = {
    "first_name" : "ram",
    "last_name" : "oukacha",
    "school" : "aaess",
    "date_of_birth" : "5/12/2023",
    "email" : "ajjsdp@gmail.com",
    "age" : 5,
    "address" : "alain",
    "friends" : ["mohammad","ahmed","isa"]

}
personal_info3 = {
    "first_name" : "mohammad",
    "last_name" : "oukacha",
    "school" : "repton",
    "date_of_birth" : "2/6/2013",
    "email" : "ytfjj@gmail.com",
    "age" : 12,
    "address" : "dubai",
    "friends" : ["jj","yusuf","jhon"]
}
# print(personal_info1.get("first_name"))
# print(personal_info1.get("last_name"))
# print(personal_info1.get("school"))
# print(personal_info1.get("date_of_birth"))
# print(personal_info1.get("email"))
# print(personal_info1.get("address"))
# print(personal_info1.get("friends")[0])

personal_infos = [personal_info1,personal_info2,personal_info3]

print(personal_infos[0])

#print all the keys or values from personal_info1
print(personal_info1.keys())
print(personal_info1.values())

#print the number of key value pair (item) in the dictionary
print(len(personal_info1))

#check the data type of the variable personal_info1
print(type(personal_info1))

#print the value of first name from the personal_info1
print(personal_info1.get("first_name"))
print(personal_info1['first_name'])

print(personal_info1.get("last_name"))
print(personal_info1.get("school"))
print(personal_info1.get("date_of_birth"))
print(personal_info1.get("email"))
print(personal_info1.get("age"))
print(personal_info1.get("address"))
print(personal_info1.get("friends"))
#try to print from a key that does not exist in the dictionary
print(personal_info1.get("grades"))
#print(personal_info1['grades'])


print(personal_info1.get("friends")[2])

friends = ["ram","mohammad","abdullah"]

print(friends[2])

#check if the key grades exists inside the personal_info1
if "grade" in personal_info1:
    print("it is there")
else :
    print("it is not there")