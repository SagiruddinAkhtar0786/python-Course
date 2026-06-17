# =============================================================================
# LOOPING WITH BREAK STATEMENT
# =============================================================================
# Loops iterate over sequences
# break statement exits the loop early

print("=" * 60)
print("LOOPING WITH BREAK STATEMENT")
print("=" * 60)

# ===== 1. ITERATE THROUGH STRING =====
print("\n1. ITERATE THROUGH STRING\n")

name = "sagiruddin"

print(f"String: '{name}'")
print("Characters (separated by space):")
for n in name:
    print(n, end=" ")
print("\n")


# ===== 2. ITERATE THROUGH LIST WITH BREAK =====
print("=" * 60)
print("2. ITERATE THROUGH LIST WITH BREAK")
print("=" * 60 + "\n")

list1 = [1, 2, 3, 4, 5]
print(f"List: {list1}")
print("Iterating (break when finding 3):")

for i in list1:
    print(f"  {i}")
    if i == 3:
        print("  Found 3, breaking the loop")
        break

print("Loop ended\n")


# ===== 3. ITERATE THROUGH STRING LIST WITH BREAK =====
print("=" * 60)
print("3. ITERATE THROUGH STRING LIST WITH BREAK")
print("=" * 60 + "\n")

string1 = ["sagir", "sag", "sagi", "sagiru", "sagirudd", "sagiruddin"]
print(f"List of strings: {string1}")
print("Searching for 'sagiru':")

for s in string1:
    print(f"  {s}")
    if s == "sagiru":
        print("  Found 'sagiru', breaking the loop")
        break

print("Search complete\n")


# ===== 4. CONTINUE STATEMENT =====
print("=" * 60)
print("4. CONTINUE STATEMENT")
print("=" * 60 + "\n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")
print("Printing only even numbers (skip odd):")

for num in numbers:
    if num % 2 != 0:  # If odd number
        continue  # Skip to next iteration
    print(f"  {num}")


# ===== 5. NESTED LOOPS WITH BREAK =====
print("\n" + "=" * 60)
print("5. NESTED LOOPS WITH BREAK")
print("=" * 60 + "\n")

print("Nested loop (break when finding 3):")
for i in range(1, 4):
    for j in range(1, 5):
        print(f"  i={i}, j={j}")
        if j == 3:
            print("  Found j=3, breaking inner loop")
            break
    print(f"Inner loop complete for i={i}\n")


# ===== 6. FOR-ELSE WITH BREAK =====
print("=" * 60)
print("6. FOR-ELSE WITH BREAK")
print("=" * 60 + "\n")

print("Loop with break (else will NOT execute):")
for num in [1, 2, 3, 4, 5]:
    if num == 3:
        print(f"  Found {num}, breaking")
        break
else:
    print("  Loop completed normally (no break)")

print("\nLoop without break (else WILL execute):")
for num in [1, 2, 4, 5]:
    print(f"  Processing {num}")
else:
    print("  Loop completed normally (no break)")


# ===== 7. SEARCHING IN NESTED STRUCTURE =====
print("\n" + "=" * 60)
print("7. SEARCHING IN NESTED STRUCTURE")
print("=" * 60 + "\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 5
found = False

print(f"Matrix: {matrix}")
print(f"Searching for {target}...")

for row in matrix:
    for element in row:
        if element == target:
            print(f"  Found {target} at position {matrix.index(row)}, {row.index(element)}")
            found = True
            break
    if found:
        break

if not found:
    print(f"  {target} not found in matrix")
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