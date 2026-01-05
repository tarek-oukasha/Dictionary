personal_details={
    "name": "Tarek",
    "last name": "Oukacha",
    "age": "16 years old",
    "health":{
        "BMI":"90",
        "allergies":"none",
        "BPM":"90"
    }

}

personal_details_copy = personal_details.copy()

print(personal_details_copy)

print(personal_details["age"])
print("BMI:", personal_details["health"]["BMI"])

print("All keys in the dictionary:")
for key in personal_details:
    print(key)

personal_details.clear()
print("After clearing:", personal_details)
