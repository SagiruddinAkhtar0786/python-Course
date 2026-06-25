"""Simple generator example for square numbers."""

# Step 1: Define a generator function
# This function uses yield to return one result at a time.
# It does not create the whole list of squares at once.

def square_numbers(nums):
    for n in nums:
        # yield returns the current square and pauses the function
        yield n * n


# Step 4: This block runs only when this file is executed directly.
# If the file is imported into another module, this block is skipped.
if __name__ == "__main__":
    # Step 2: Prepare input values
    numbers = [1, 2, 3, 4, 5]
    print("Input numbers:", numbers)
    print("Squares:")

    # Step 3: Use the generator by iterating over it.
    # Each square is produced only when needed.
    for value in square_numbers(numbers):
        print(value, end=" ")
    print()

# Explanation:
# __name__ is a special Python variable.
# When you run this file directly, Python sets __name__ to "__main__."
# When you import this file, __name__ becomes the module name instead.
# So the code inside if __name__ == "__main__": is for direct execution only.
