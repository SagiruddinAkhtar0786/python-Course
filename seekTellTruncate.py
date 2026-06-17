# =====================================================
# FILE POINTER METHODS: seek(), tell(), truncate()
# =====================================================

# First, create a test file
with open('test.txt', 'w') as f:
    f.write("Hello World! This is a test file.")

print("Original content: 'Hello World! This is a test file.'")
print("=" * 50)


# =====================================================
# 1. tell() - RETURNS CURRENT FILE POINTER POSITION
# =====================================================

print("\n1. TELL() - Current Position in File")
print("-" * 50)

with open('test.txt', 'r') as f:
    # Initially at position 0
    pos = f.tell()
    print(f"Position at start: {pos}")
    
    # Read 5 characters
    data = f.read(5)
    print(f"Read: '{data}'")
    
    # Check position after reading
    pos = f.tell()
    print(f"Position after reading 5 chars: {pos}")
    
    # Read more
    data = f.read(7)
    print(f"Read: '{data}'")
    
    pos = f.tell()
    print(f"Position after reading 7 more chars: {pos}")


# =====================================================
# 2. seek() - MOVE FILE POINTER TO SPECIFIC POSITION
# =====================================================

print("\n2. SEEK() - Move File Pointer to Specific Position")
print("-" * 50)

with open('test.txt', 'r') as f:
    # Seek to position 0 (start of file)
    f.seek(0)
    print("seek(0) - Go to beginning:")
    print(f"Position: {f.tell()}, Content: '{f.read(5)}'")
    
    # Seek to position 6 (skip "Hello ")
    f.seek(6)
    print(f"\nseek(6) - Skip 'Hello ':")
    print(f"Position: {f.tell()}, Content: '{f.read(5)}'")
    
    # Seek to position 13 (skip "Hello World! ")
    f.seek(13)
    print(f"\nseek(13) - Skip to 'This':")
    print(f"Position: {f.tell()}, Content: '{f.read(4)}'")
    
    # Seek to end of file (negative offset)
    f.seek(0, 2)  # 2 = end of file
    print(f"\nseek(0, 2) - Go to end:")
    print(f"Position: {f.tell()}, Content length")
    
    # Seek backward from end
    f.seek(-4, 2)  # 4 bytes from end
    print(f"\nseek(-4, 2) - Go 4 bytes from end:")
    print(f"Position: {f.tell()}, Content: '{f.read()}'")


# =====================================================
# 3. seek() PARAMETERS
# =====================================================

print("\n3. SEEK() - Parameter Meanings")
print("-" * 50)
print("""
seek(offset, whence)
- offset: number of bytes to move
- whence: reference point
  * 0 = beginning of file (default)
  * 1 = current position
  * 2 = end of file

Examples:
f.seek(10)      → Go to position 10 from start
f.seek(5, 0)    → Go to position 5 from start
f.seek(5, 1)    → Go 5 bytes forward from current position
f.seek(-5, 1)   → Go 5 bytes backward from current position
f.seek(0, 2)    → Go to end of file
f.seek(-10, 2)  → Go 10 bytes before end of file
""")


# =====================================================
# 4. truncate() - RESIZE FILE
# =====================================================

print("\n4. TRUNCATE() - Resize/Cut File")
print("-" * 50)

# Create a test file
with open('truncate_test.txt', 'w') as f:
    f.write("Hello World! This is a test file.")

with open('truncate_test.txt', 'r') as f:
    print(f"Original file: '{f.read()}'")

# Truncate to 5 characters (keep only "Hello")
with open('truncate_test.txt', 'r+') as f:
    f.truncate(5)

with open('truncate_test.txt', 'r') as f:
    print(f"After truncate(5): '{f.read()}'")

# Truncate to 0 (empty the file)
with open('truncate_test.txt', 'w') as f:
    f.write("123456789")

with open('truncate_test.txt', 'r+') as f:
    print(f"Before truncate(0): '{f.read()}'")
    f.seek(0)
    f.truncate(0)

with open('truncate_test.txt', 'r') as f:
    content = f.read()
    print(f"After truncate(0): '{content}' (empty file)")


# =====================================================
# 5. PRACTICAL EXAMPLES
# =====================================================

print("\n5. PRACTICAL EXAMPLES")
print("-" * 50)

# Example 1: Read file in reverse
print("\nExample 1: Read last 10 characters")
with open('test.txt', 'r') as f:
    f.seek(-10, 2)  # 10 bytes from end
    print(f"Last 10 chars: '{f.read()}'")

# Example 2: Replace character at specific position
print("\nExample 2: Replace character at position 6")
with open('test.txt', 'r') as f:
    print(f"Original: '{f.read()}'")

with open('test.txt', 'r+') as f:
    f.seek(6)  # Go to position 6 (W in World)
    f.write("w")  # Replace W with w

with open('test.txt', 'r') as f:
    print(f"After replace: '{f.read()}'")

# Example 3: Get file size using seek
print("\nExample 3: Get file size")
with open('test.txt', 'r') as f:
    f.seek(0, 2)  # Go to end
    file_size = f.tell()
    print(f"File size: {file_size} bytes")

# Example 4: Copy specific portion of file
print("\nExample 4: Copy bytes 6-11 to new file")
with open('test.txt', 'r') as f:
    f.seek(6)
    chunk = f.read(5)  # Read 5 bytes
    print(f"Chunk copied: '{chunk}'")
    
with open('chunk.txt', 'w') as f:
    f.write(chunk)

with open('chunk.txt', 'r') as f:
    print(f"Saved to chunk.txt: '{f.read()}'")


# =====================================================
# 6. MODES MATTER
# =====================================================

print("\n6. IMPORTANT: File Modes")
print("-" * 50)
print("""
For seek(), tell(), truncate():
- 'r'   : Read only (can't write/truncate)
- 'w'   : Write only (truncates file)
- 'r+'  : Read and write (CAN use truncate)
- 'a'   : Append only
- 'a+'  : Append and read

Use 'r+' mode when you need seek() + truncate()
""")


print("\n✓ All examples completed!")
