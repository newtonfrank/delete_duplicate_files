# delete_duplicate_files


Python Duplicate File Remover
This Python program helps you find and delete duplicate files based on their content within a specified folder.

Features:
Finds duplicate files: Identifies files with the same content using SHA-256 hashing.
Confirms deletion: Asks for user confirmation before deleting duplicate files, preventing accidental data loss.

How to use:
Save the program: Save the provided Python code in a file named duplicate_remover.py.
Run the program: Open a terminal or command prompt and navigate to the directory where you saved the file. Then, run the following command:
python duplicate_remover.py
Enter folder path: The program will prompt you for the folder path where you want to find duplicates. Enter the desired path and press Enter.
Review and confirm: If duplicates are found, the program will list them along with their hash.
For each group of duplicates, it will ask for confirmation before deletion.
Answer "y" to delete or "n" to skip deletion for that group.
