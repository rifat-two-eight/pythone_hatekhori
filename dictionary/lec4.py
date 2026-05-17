data = {
    "name" : "Rifat",
    "age" : 22,
    "city" : "Dhaka",
    "country" : ["Bangladesh", "India", "Pakistan"],
    "favorite_food" : ("biriyani", "kacchi", "polao"),
    "is_student" : False,
    "number" : {
        "mobile" : "01700000000",
        "home" : "02-00000000"
    }
}

data["name"] = "Atiqur Rahman Rifat"

print(data["number"]["home"])