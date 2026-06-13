name = "sagiruddin"

for n in name:
    print(n,end=" ")
print("\n")
print("************************************\n")


list1 = [1, 2, 3, 4, 5]

for i in list1:
    print(i)
    if i == 3:
        print("Found 3, breaking the loop")
print("************************************\n")
string1 = ["sagir", "sag", "sagi", "sagiru", "sagirudd", "sagiruddin"]
for s in string1:
    print(s)
    if s == "sagiru":
        print("Found sagiru, breaking the loop")
        break

print("************************************\n")
for i in range(1, 11, 2):
    print(i)    

print("************************************\n")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")\
        

i =3

while i > 0:
    print(i)
    i -= 1  