# ===== READING FROM FILE =====
print("===== READING =====")

# Method 1: Read entire file as one string
with open('myfile.txt', 'r') as f:
    content = f.read()
    print("Read all:", content)

# Method 2: Read one line at a time
with open('myfile.txt', 'r') as f:
    line = f.readline()
    print("Read one line:", line)

# Method 3: Read all lines as a list
with open('myfile.txt', 'r') as f:
    lines = f.readlines()
    print("Read all lines:", lines)

# Method 4: Loop through lines (best practice)
print("Loop through lines:")
with open('myfile.txt', 'r') as f:
    for line in f:
        print(line.strip())


# ===== WRITING TO FILE =====
print("\n===== WRITING =====")

# Use 'a' (append) to ADD to file, NOT 'w' (write overwrites!)
addLine = "I am a Java Developer ---"
with open("myfile.txt", 'a') as f:  # 'a' = append, 'w' = overwrite
    f.write("\n" + addLine)  # \n adds newline before text
    print("Data appended successfully!")

# Verify by reading again
print("\nFile content after appending:")
with open('myfile.txt', 'r') as f:
    print(f.read())