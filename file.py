# =============================================================================
# FILE OPERATIONS IN PYTHON
# =============================================================================
# Working with files: reading, writing, appending

print("=" * 60)
print("FILE OPERATIONS IN PYTHON")
print("=" * 60)

# ===== 1. READING FROM FILE =====
print("\n1. READING FROM FILE\n")

# Method 1: Read entire file as one string
print("Method 1: Read entire file")
with open('myfile.txt', 'r') as f:
    content = f.read()
    print(f"Content:\n{content}")

# Method 2: Read one line at a time
print("\n\nMethod 2: Read one line")
with open('myfile.txt', 'r') as f:
    line = f.readline()
    print(f"First line: {line}")

# Method 3: Read all lines as a list
print("\nMethod 3: Read all lines as list")
with open('myfile.txt', 'r') as f:
    lines = f.readlines()
    print(f"All lines: {lines}")

# Method 4: Loop through lines (BEST PRACTICE)
print("\nMethod 4: Loop through lines (best practice)")
print("Content:")
with open('myfile.txt', 'r') as f:
    for line in f:
        print(f"  {line.strip()}")  # strip() removes newline characters


# ===== 2. WRITING TO FILE =====
print("\n" + "=" * 60)
print("2. WRITING TO FILE")
print("=" * 60 + "\n")

# Use 'w' mode to OVERWRITE the entire file
# Use 'a' mode to APPEND (add) to the file

addLine = "I am a Java Developer ---"

print(f"Appending to file: '{addLine}'")
with open('myfile.txt', 'a') as f:  # 'a' = append mode
    f.write("\n" + addLine)

print("File updated!")


# ===== 3. CREATING NEW FILE =====
print("\n" + "=" * 60)
print("3. CREATING AND WRITING NEW FILE")
print("=" * 60 + "\n")

# Create a new file with 'w' mode
new_content = """This is a new file.
It contains multiple lines.
Each line is added using write() method.
"""

print("Creating newfile.txt...")
with open('newfile.txt', 'w') as f:
    f.write(new_content)

print("New file created and content written!")


# ===== 4. FILE MODES =====
print("\n" + "=" * 60)
print("4. FILE MODES")
print("=" * 60 + "\n")

print("""
File Modes:
  'r'   = Read (default) - file must exist
  'w'   = Write - creates file or overwrites existing
  'a'   = Append - adds to end of file
  'x'   = Create - creates file, error if exists
  'b'   = Binary mode (e.g., 'rb', 'wb')
  '+'   = Read and write (e.g., 'r+', 'w+')

Best Practice: Always use 'with' statement!
  with open('file.txt', 'r') as f:
      content = f.read()
      
This automatically closes the file.
""")


# ===== 5. CHECKING AND READING FILE =====
print("\n" + "=" * 60)
print("5. CHECKING AND READING FILE")
print("=" * 60 + "\n")

import os

# Check if file exists
if os.path.exists('myfile.txt'):
    print("myfile.txt exists!")
    with open('myfile.txt', 'r') as f:
        print("Current content:")
        print(f.read())
else:
    print("File does not exist!")
with open("myfile.txt", 'a') as f:  # 'a' = append, 'w' = overwrite
    f.write("\n" + addLine)  # \n adds newline before text
    print("Data appended successfully!")

# Verify by reading again
print("\nFile content after appending:")
with open('myfile.txt', 'r') as f:
    print(f.read())