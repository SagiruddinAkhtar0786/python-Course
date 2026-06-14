letter = "hey my name is  {} and I am from {}"

name = "Sagriuddin Akhtar"
country = "India"

print(letter.format(name, country))

fString = f"hey my name is {name} and I am from {country}"
print(fString)
print(fString.upper())

print(fString.lower())
print(fString.title())

print(fString.replace("hey", "Hello"))

print(f"{2*6}")  # Output: 12