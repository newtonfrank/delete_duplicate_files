import hashlib
import os


def calculate_file_hash(filepath):
  """Calculates the SHA-256 hash of a file's content."""
  hasher = hashlib.sha256()
  with open(filepath, 'rb') as f:
    for chunk in iter(lambda: f.read(4096), b''):
      hasher.update(chunk)
  return hasher.hexdigest()


def find_duplicate_files(root_folder):
  """Finds duplicate files based on their hash."""
  duplicates = {}
  for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
      filepath = os.path.join(dirpath, filename)
      file_hash = calculate_file_hash(filepath)
      if file_hash in duplicates:
        duplicates[file_hash].append(filepath)
      else:
        duplicates[file_hash] = [filepath]
  return duplicates


def delete_duplicates(duplicates, confirm=True):
  """Deletes duplicate files, prompting confirmation before deletion."""
  for file_hash, filepaths in duplicates.items():
    if len(filepaths) > 1:
      if confirm:
        print(f"Found duplicates with hash {file_hash}:")
        for filepath in filepaths[1:]:
          print(filepath)
        answer = input("Delete these duplicates? (y/n): ")
        if answer.lower() != 'y':
          continue
      for filepath in filepaths[1:]:
        os.remove(filepath)
        print(f"Deleted: {filepath}")


if __name__ == "__main__":
  root_folder = input("Enter the folder path: ")
  duplicates = find_duplicate_files(root_folder)
  if duplicates:
    delete_duplicates(duplicates)
  else:
    print("No duplicate files found.")
