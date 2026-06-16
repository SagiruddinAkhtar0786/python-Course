# OS Module - Operating System Functions
# The os module provides functions to interact with the operating system

import os

# ============================================
# 1. GET CURRENT WORKING DIRECTORY
# ============================================

current_dir = os.getcwd()  # Returns the current working directory path
print("Current Directory:", current_dir)


# ============================================
# 2. LIST FILES AND DIRECTORIES
# ============================================

# List all files and directories in current folder
files_and_dirs = os.listdir()
print("Files and Directories:", files_and_dirs)

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
