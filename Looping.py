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

k = int(input("Enter a number: "))
while k > 0:
    print(k)
    k -= 5
    if k == 5:
        print("Found 5, breaking the loop")
        break
    elif k < 5:
        print("k values becomes less than 5, breaking the loop")
        break
    else:
        print("k is not 5, continuing the loop")
print("Loop ended")

for i in range(12):
    if i ==6:
        print("Skipping 6, continuing the loop")
        continue    
    print("5 X", i, "=", 5*i)

    if i % 2 == 0:
        print(i, "is even")