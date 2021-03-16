dict1 = dict(
    name = "Kaustubh",
    age = 13
)

for key, value in dict1.items():
    if key == "age":
        dict1[key] = value + 14

print(dict1)