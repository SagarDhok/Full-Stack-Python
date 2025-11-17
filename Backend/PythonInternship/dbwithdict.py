import json

try:
    with open("data.json", "r") as f:
        dict = json.load(f)
except:
    dict = {}

while True:
    print(""" 
    1. Add
    2. View
    3. Update
    4. Delete
    5. Exit  
    """)
    
    ch = input("Enter Your Choice: ")

    if ch == "1":
        key = input("Enter Key: ")
        val = input("Enter Value: ")
        dict[key] = val
        json.dump(dict, open("data.json", "w"))
        print("Added")

    elif ch == "2":
        key = input("Enter Key to View: ")
        if key in dict:
            print("*"*30)
            print(f"{key}: {dict[key]}")
            print("*"*30)
        else:
            print("Not Found.")

    elif ch == "3":
        key = input("Enter Key to Update: ")
        if key in dict:
            val = input("Enter New Value: ")
            dict[key] = val
            json.dump(dict, open("data.json", "w"))
            print("Updated")
        else:
            print("Key not found.")

    elif ch == "4":
        key = input("Enter Key to Delete: ")
        if key in dict:
            del dict[key]
            json.dump(dict, open("data.json", "w"))
            print("Deleted")
        else:
            print("Key not found.")

    elif ch == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
