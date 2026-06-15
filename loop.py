for i in range(5):
    print("Hello, World!")

else:
    print("Loop has completed.")


for i in range(5):
    print("Hello, World! break testing")
    if i == 2:
        break

else:
    print("Loop has completed.")


#indexing in loop  enumurate


fruits = ["sagir","rahu","amit","ravi"]
for index , fruit in enumerate(fruits):
    print(index,fruit)
print("\n88888888888888888888888888\n")

#fruits = ["sagir","rahu","amit","ravi"]
for index , fruit in enumerate(fruits,start=1):
    print(index,fruit)
