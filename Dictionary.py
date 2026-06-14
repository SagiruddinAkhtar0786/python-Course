dic = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "designation": "Software Engineer"
}

""" printquote = f"{dic['name']} is a {dic['age']} year old {dic['designation']} living in {dic['city']}."
print(printquote) """

""" for key, value in dic.items():
    print(f"{key}: {value}")     """

for key in dic.keys():
    print(key)

for value in dic.values():
    print(value)

print(type(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])))