import os

folders=input("Enter the folder names with spaces :").split()
print(folders)

for files in folders:
    try:
     print(os.listdir(files))
    except FileNotFoundError:
     print("Chech your folder names again")

