# =============================================================================
# OS MODULE - OPERATING SYSTEM FUNCTIONS
# =============================================================================
# The os module provides functions to interact with the operating system
# Functions include: directory operations, file operations, path handling

import os

print("=" * 60)
print("OS MODULE - OPERATING SYSTEM FUNCTIONS")
print("=" * 60)

# ===== 1. GET CURRENT WORKING DIRECTORY =====
print("\n1. GET CURRENT WORKING DIRECTORY\n")

# Returns the current working directory path
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")


# ===== 2. LIST FILES AND DIRECTORIES =====
print("\n" + "=" * 60)
print("2. LIST FILES AND DIRECTORIES")
print("=" * 60 + "\n")

# List all files and directories in current folder
files_and_dirs = os.listdir()
print(f"Number of items: {len(files_and_dirs)}")
print("\nFiles and Directories:")
for item in files_and_dirs[:10]:  # Show first 10 items
    print(f"  - {item}")
if len(files_and_dirs) > 10:
    print(f"  ... and {len(files_and_dirs) - 10} more items")


# ===== 3. LIST SPECIFIC DIRECTORY =====
print("\n" + "=" * 60)
print("3. LIST SPECIFIC DIRECTORY")
print("=" * 60 + "\n")

# List items in specific directory
specific_dir = os.listdir('.')  # Current directory
print(f"Items in current directory ({len(specific_dir)}):")
for item in specific_dir[:5]:
    print(f"  - {item}")


# ===== 4. CHECK IF PATH EXISTS =====
print("\n" + "=" * 60)
print("4. CHECK IF PATH EXISTS")
print("=" * 60 + "\n")

# Check if file or directory exists
test_files = ['calculator.py', 'Decorator.py', 'nonexistent.txt']

for file in test_files:
    exists = os.path.exists(file)
    print(f"os.path.exists('{file}'): {exists}")


# ===== 5. CHECK IF IT'S FILE OR DIRECTORY =====
print("\n" + "=" * 60)
print("5. CHECK IF PATH IS FILE OR DIRECTORY")
print("=" * 60 + "\n")

items_to_check = ['calculator.py', 'classAndObject', '.git']

for item in items_to_check:
    if os.path.exists(item):
        is_file = os.path.isfile(item)
        is_dir = os.path.isdir(item)
        print(f"{item}:")
        print(f"  is_file: {is_file}, is_dir: {is_dir}")


# ===== 6. GET FILE SIZE =====
print("\n" + "=" * 60)
print("6. GET FILE SIZE")
print("=" * 60 + "\n")

test_file = 'calculator.py'
if os.path.exists(test_file):
    size = os.path.getsize(test_file)
    print(f"Size of '{test_file}': {size} bytes")


# ===== 7. GET FILE INFORMATION =====
print("\n" + "=" * 60)
print("7. GET FILE INFORMATION USING os.stat()")
print("=" * 60 + "\n")

if os.path.exists(test_file):
    stat_info = os.stat(test_file)
    print(f"File information for '{test_file}':")
    print(f"  Size: {stat_info.st_size} bytes")
    print(f"  Modified time: {stat_info.st_mtime}")
    print(f"  Access time: {stat_info.st_atime}")
    print(f"  Change time: {stat_info.st_ctime}")


# ===== 8. PATH OPERATIONS =====
print("\n" + "=" * 60)
print("8. PATH OPERATIONS")
print("=" * 60 + "\n")

path = 'python/tutorial/file.txt'

print(f"Path: '{path}'")
print(f"  basename: {os.path.basename(path)}")
print(f"  dirname: {os.path.dirname(path)}")
print(f"  join: {os.path.join('folder', 'subfolder', 'file.txt')}")
print(f"  split: {os.path.split(path)}")
print(f"  splitext: {os.path.splitext(path)}")


# ===== 9. CREATE AND REMOVE DIRECTORIES =====
print("\n" + "=" * 60)
print("9. CREATE AND REMOVE DIRECTORIES")
print("=" * 60 + "\n")

# Create directory (uncomment to use)
# os.mkdir('new_folder')
# print("Created 'new_folder'")

# Create nested directories
# os.makedirs('path/to/folder')
# print("Created nested directories")

# Remove directory
# os.rmdir('new_folder')
# print("Removed 'new_folder'")

print("(Commented out: use os.mkdir(), os.makedirs(), os.rmdir() to manage directories)")


# ===== 10. RENAME AND REMOVE FILES =====
print("\n" + "=" * 60)
print("10. RENAME AND REMOVE FILES")
print("=" * 60 + "\n")

# Rename file
# os.rename('old_name.txt', 'new_name.txt')

# Remove file
# os.remove('file_to_delete.txt')

print("(Commented out: use os.rename() and os.remove() for file operations)")

# List files in a specific directory
specific_path = "d:\\Python Tutorial"
files = os.listdir(specific_path)
print("Files in specified path:", files)


# ============================================
# 3. CHECK IF PATH EXISTS
# ============================================

# Check if a file or directory exists
file_path = "d:\\Python Tutorial\\Os_module.py"
if os.path.exists(file_path):
    print(f"'{file_path}' exists")
else:
    print(f"'{file_path}' does not exist")


# ============================================
# 4. CHECK IF IT'S A FILE OR DIRECTORY
# ============================================

if os.path.isfile(file_path):
    print(f"'{file_path}' is a file")

if os.path.isdir(specific_path):
    print(f"'{specific_path}' is a directory")


# ============================================
# 5. CHANGE DIRECTORY
# ============================================

# Change current working directory
# os.chdir("d:\\Python Tutorial")  # Uncomment to change directory
# print("Changed to:", os.getcwd())


# ============================================
# 6. CREATE DIRECTORIES
# ============================================

# Create a single new directory (fails if parent doesn't exist)
# os.mkdir("d:\\Python Tutorial\\NewFolder")

# Create directories recursively (creates parent directories too)
# os.makedirs("d:\\Python Tutorial\\NewFolder\\SubFolder", exist_ok=True)
# exist_ok=True prevents error if directory already exists


# ============================================
# 7. REMOVE FILES AND DIRECTORIES
# ============================================

# Remove a file (file must exist)
# os.remove("d:\\Python Tutorial\\temp_file.txt")

# Remove an empty directory
# os.rmdir("d:\\Python Tutorial\\EmptyFolder")

# Remove directory with contents (dangerous!)
# import shutil
# shutil.rmtree("d:\\Python Tutorial\\FolderWithFiles")


# ============================================
# 8. RENAME FILES AND DIRECTORIES
# ============================================

# Rename a file or directory
# os.rename("old_name.py", "new_name.py")


# ============================================
# 9. GET FILE INFORMATION
# ============================================

# Get file size in bytes
file_size = os.path.getsize(file_path)
print(f"File size: {file_size} bytes")

# Get file statistics (size, creation time, modification time, etc.)
file_stats = os.stat(file_path)
print("File Info:", file_stats)
print(f"Last modified: {file_stats.st_mtime}")


# ============================================
# 10. WALK THROUGH DIRECTORIES
# ============================================

# Walk through all subdirectories and files
for root, dirs, files in os.walk(specific_path):
    print(f"Directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print("---")


# ============================================
# 11. ENVIRONMENT VARIABLES
# ============================================

# Get all environment variables
all_env = os.environ
print("All environment variables:", dict(list(all_env.items())[:3]))  # Show first 3

# Get specific environment variable
username = os.environ.get("USERNAME", "Unknown")
print(f"Current user: {username}")


# ============================================
# 12. OPERATING SYSTEM NAME
# ============================================

# Get operating system name (posix, nt, java, etc.)
os_name = os.name
print(f"OS Name: {os_name}")

# Get system info (Windows)
system_info = os.system("systeminfo")


# ============================================
# 13. SEPARATE PATH COMPONENTS
# ============================================

# Split path into directory and filename
dir_path, filename = os.path.split(file_path)
print(f"Directory: {dir_path}")
print(f"Filename: {filename}")

# Split filename and extension
name, extension = os.path.splitext(filename)
print(f"Name: {name}, Extension: {extension}")


# ============================================
# 14. JOIN PATHS
# ============================================

# Join path components properly (handles / vs \ automatically)
new_path = os.path.join("d:\\Python Tutorial", "subfolder", "file.py")
print(f"Joined path: {new_path}")


# ============================================
# 15. GET ABSOLUTE PATH
# ============================================

# Convert relative path to absolute path
abs_path = os.path.abspath("Os_module.py")
print(f"Absolute path: {abs_path}")


# ============================================
# 16. PRACTICAL EXAMPLE: List all Python files
# ============================================

print("\n=== All Python files in current directory ===")
for file in os.listdir():
    if file.endswith(".py"):  # Check if file ends with .py
        print(f"- {file}")
