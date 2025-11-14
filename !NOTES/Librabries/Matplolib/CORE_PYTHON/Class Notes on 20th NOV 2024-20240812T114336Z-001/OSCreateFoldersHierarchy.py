#Creating Folders Hierarchy
#OSCreateFoldersHierarchy.py
import os
try:
    os.makedirs("Apple\\Mango\\Banana")
    print("Folders Hierarchy Created--verify")
except FileExistsError:
    print("Folders Hierarchy Alerady Exist")