# =============================================================================
# FILE POINTER METHODS: seek(), tell(), truncate()
# =============================================================================
# These methods control file pointer position and file size
# seek(): Move to specific position
# tell(): Get current position
# truncate(): Resize file

print("=" * 60)
print("FILE POINTER METHODS: seek(), tell(), truncate()")
print("=" * 60)

# ===== SETUP: CREATE TEST FILE =====
with open('test.txt', 'w') as f:
    f.write("Hello World! This is a test file.")

print("Original content: 'Hello World! This is a test file.'\n")


# ===== 1. tell() - RETURNS CURRENT FILE POINTER POSITION =====
print("=" * 60)
print("1. tell() - GET CURRENT FILE POINTER POSITION")
print("=" * 60 + "\n")

# tell() returns the byte position in the file

with open('test.txt', 'r') as f:
    # Initially at position 0
    pos = f.tell()
    print(f"Position at start: {pos}")
    
    # Read 5 characters
    data = f.read(5)
    print(f"Read 5 characters: '{data}'")
    
    # Check position after reading
    pos = f.tell()
    print(f"Position after read(5): {pos}")
    
    # Read 7 more characters
    data = f.read(7)
    print(f"Read 7 more characters: '{data}'")
    
    pos = f.tell()
    print(f"Position after read(7): {pos}")


# ===== 2. seek() - MOVE FILE POINTER TO SPECIFIC POSITION =====
print("\n" + "=" * 60)
print("2. seek() - MOVE FILE POINTER TO SPECIFIC POSITION")
print("=" * 60 + "\n")

# seek(offset, whence) moves to specified position
# whence: 0=start, 1=current, 2=end

with open('test.txt', 'r') as f:
    # Seek to position 0 (start of file)
    f.seek(0)
    print("seek(0) - Go to beginning:")
    print(f"  Position: {f.tell()}, Content: '{f.read(5)}'")
    
    # Seek to position 6 (skip "Hello ")
    f.seek(6)
    print(f"\nseek(6) - Skip 'Hello ':")
    print(f"  Position: {f.tell()}, Content: '{f.read(5)}'")
    
    # Seek to position 13
    f.seek(13)
    print(f"\nseek(13) - Goto 'This':")
    print(f"  Position: {f.tell()}, Content: '{f.read(4)}'")
    
    # Seek to end of file (0 bytes from end)
    f.seek(0, 2)  # 2 = end of file
    print(f"\nseek(0, 2) - Go to end:")
    print(f"  Position: {f.tell()}")
    
    # Seek backward from end
    f.seek(-4, 2)  # 4 bytes before end
    print(f"\nseek(-4, 2) - Go 4 bytes before end:")
    print(f"  Position: {f.tell()}, Content: '{f.read()}'")


# ===== 3. SEEK() PARAMETERS =====
print("\n" + "=" * 60)
print("3. SEEK() PARAMETERS EXPLAINED")
print("=" * 60 + "\n")

print("""
seek(offset, whence):
  offset: Number of bytes to move
  whence: Reference point
    * 0 = Beginning of file (DEFAULT)
    * 1 = Current position
    * 2 = End of file

Examples:
  f.seek(10)      → Go to byte 10 from start
  f.seek(5, 0)    → Go to byte 5 from start
  f.seek(5, 1)    → Go 5 bytes forward from current
  f.seek(-5, 1)   → Go 5 bytes backward from current
  f.seek(0, 2)    → Go to end of file
  f.seek(-10, 2)  → Go 10 bytes before end
""")


# ===== 4. truncate() - RESIZE/CUT FILE =====
print("\n" + "=" * 60)
print("4. truncate() - RESIZE OR CUT FILE")
print("=" * 60 + "\n")

# Create a test file
with open('truncate_test.txt', 'w') as f:
    f.write("Hello World! This is a test file.")

with open('truncate_test.txt', 'r') as f:
    print(f"Original file: '{f.read()}'")

# Truncate to 5 characters (keep only "Hello")
with open('truncate_test.txt', 'r+') as f:  # r+ allows read and write
    f.truncate(5)

with open('truncate_test.txt', 'r') as f:
    print(f"After truncate(5): '{f.read()}'")

# Truncate to 0 (empty the file)
with open('truncate_test.txt', 'w') as f:
    f.write("123456789")

with open('truncate_test.txt', 'r+') as f:
    f.truncate(0)

with open('truncate_test.txt', 'r') as f:
    content = f.read()
    print(f"After truncate(0): '{content}' (empty file)")


# ===== 5. PRACTICAL EXAMPLES =====
print("\n" + "=" * 60)
print("5. PRACTICAL EXAMPLES")
print("=" * 60 + "\n")

# Example 1: Read last 10 characters
print("Example 1: Read last 10 characters")
with open('test.txt', 'r') as f:
    f.seek(-10, 2)  # 10 bytes from end
    print(f"  Last 10 chars: '{f.read()}'")

# Example 2: Replace character at specific position
print("\nExample 2: Replace character at position 6")
with open('test.txt', 'r') as f:
    print(f"  Original: '{f.read()}'")

with open('test.txt', 'r+') as f:
    f.seek(6)  # Go to position 6 (W in World)
    f.write("w")  # Replace W with w

with open('test.txt', 'r') as f:
    print(f"  After replace: '{f.read()}'")

# Example 3: Get file size using seek
print("\nExample 3: Get file size using seek")
with open('test.txt', 'r') as f:
    f.seek(0, 2)  # Go to end
    file_size = f.tell()
    print(f"  File size: {file_size} bytes")

# Example 4: Copy specific portion of file
print("\nExample 4: Copy bytes 6-11 to new file")
with open('test.txt', 'r') as f:
    f.seek(6)
    chunk = f.read(5)  # Read 5 bytes
    print(f"  Chunk: '{chunk}'")

with open('chunk.txt', 'w') as f:
    f.write(chunk)

with open('chunk.txt', 'r') as f:
    print(f"  Saved to chunk.txt: '{f.read()}'")


# ===== 6. FILE MODES IMPORTANT FOR seek/truncate =====
print("\n" + "=" * 60)
print("6. FILE MODES (IMPORTANT)")
print("=" * 60 + "\n")

print("""
For seek(), tell(), truncate() to work:

  'r'   = Read only (can't write/truncate)
  'w'   = Write only (truncates file on open)
  'r+'  = Read and write (CAN use truncate)
  'a'   = Append only
  'a+'  = Append and read
  'rb'  = Binary read
  'r+b' = Binary read/write

⚠️ Use 'r+' mode when you need both seek() and truncate()!
""")

print("\n✓ All examples completed!")
