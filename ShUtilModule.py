"""
SHUTIL MODULE - High-level File Operations
Used for copying, moving, deleting, and archiving files/directories
"""

import shutil
import os

print("=" * 60)
print("1. COPY FILES")
print("=" * 60)

# Create a source file for demonstration
source_file = "source.txt"
with open(source_file, "w") as f:
    f.write("This is source content")

# shutil.copy() - Copies file content (preserves metadata partially)
shutil.copy(source_file, "copy_of_source.txt")
print("✓ shutil.copy() - Copied file")

# shutil.copy2() - Copies file AND preserves metadata (timestamps, etc.)
shutil.copy2(source_file, "copy2_of_source.txt")
print("✓ shutil.copy2() - Copied file with metadata")


print("\n" + "=" * 60)
print("2. COPY DIRECTORIES (RECURSIVELY)")
print("=" * 60)

# Create a test directory with files
test_dir = "test_source_dir"
os.makedirs(test_dir, exist_ok=True)
with open(os.path.join(test_dir, "file1.txt"), "w") as f:
    f.write("File 1")
with open(os.path.join(test_dir, "file2.txt"), "w") as f:
    f.write("File 2")

# shutil.copytree() - Copies entire directory recursively
shutil.copytree(test_dir, "test_dir_copy")
print("✓ shutil.copytree() - Copied entire directory with contents")


print("\n" + "=" * 60)
print("3. MOVE/RENAME FILES AND DIRECTORIES")
print("=" * 60)

# shutil.move() - Moves file or directory
shutil.move("copy_of_source.txt", "moved_file.txt")
print("✓ shutil.move() - Moved file to new location")

# Rename by moving to same directory with different name
shutil.move("moved_file.txt", "renamed_file.txt")
print("✓ Renamed file using move()")


print("\n" + "=" * 60)
print("4. DELETE DIRECTORIES (RECURSIVE)")
print("=" * 60)

# shutil.rmtree() - Removes entire directory tree
shutil.rmtree("test_dir_copy")
print("✓ shutil.rmtree() - Deleted entire directory tree")


print("\n" + "=" * 60)
print("5. DISK SPACE INFORMATION")
print("=" * 60)

# shutil.disk_usage() - Returns disk space info
usage = shutil.disk_usage(".")
print(f"Total: {usage.total / (1024**3):.2f} GB")
print(f"Used: {usage.used / (1024**3):.2f} GB")
print(f"Free: {usage.free / (1024**3):.2f} GB")


print("\n" + "=" * 60)
print("6. CREATE ARCHIVES (ZIP, TAR, etc.)")
print("=" * 60)

# shutil.make_archive() - Creates compressed archive
# Format: (output_filename, format, directory_to_archive)
shutil.make_archive("backup", "zip", test_dir)
print("✓ shutil.make_archive() - Created ZIP archive")

# Other formats: 'tar', 'gztar', 'bztar', 'xztar'


print("\n" + "=" * 60)
print("7. EXTRACT ARCHIVES")
print("=" * 60)

# shutil.unpack_archive() - Extracts archive
shutil.unpack_archive("backup.zip", "backup_extracted")
print("✓ shutil.unpack_archive() - Extracted archive")


print("\n" + "=" * 60)
print("8. COPYING FILE PERMISSIONS")
print("=" * 60)

# shutil.copystat() - Copies permissions and timestamps only (no content)
shutil.copystat(source_file, "renamed_file.txt")
print("✓ shutil.copystat() - Copied permissions and metadata")


print("\n" + "=" * 60)
print("9. WHICH COMMAND (Find executables in PATH)")
print("=" * 60)

# shutil.which() - Finds where a command is located
python_path = shutil.which("python")
print(f"Python location: {python_path}")


print("\n" + "=" * 60)
print("CLEANUP - Removing test files")
print("=" * 60)

# Clean up test files
for file in ["source.txt", "copy2_of_source.txt", "renamed_file.txt", "backup.zip"]:
    if os.path.exists(file):
        os.remove(file)

if os.path.exists("test_source_dir"):
    shutil.rmtree("test_source_dir")

if os.path.exists("backup_extracted"):
    shutil.rmtree("backup_extracted")

print("✓ Test files cleaned up")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
copy()        → Copy file content
copy2()       → Copy file + metadata
copytree()    → Copy entire directory
move()        → Move/rename files or directories
rmtree()      → Delete directory recursively
disk_usage()  → Check disk space
make_archive()→ Create ZIP/TAR archives
unpack_archive() → Extract archives
copystat()    → Copy only permissions/timestamps
which()       → Find command location
""")
