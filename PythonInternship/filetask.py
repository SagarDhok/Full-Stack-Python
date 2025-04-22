
import os
filename = "data.txt"

def create_file():
    content = input("Enter Your content: ")
    with open(filename , "w") as f:
        f.write(content)
    print(f"File created: {filename }")


def read_file():
    try:
        with open(filename, "r") as f:
            print("File content : ",f.read())
    except FileNotFoundError:
        print("File Does Not Exists")

def delete_file():
    try:
        os.remove(filename)
        print("File deleted")
    except FileNotFoundError:
        print("File Does Not Exists")

def rename_file():
    new_name = input("Enter new filename: ")
    try:
        os.rename(filename, new_name)
        print(f"FIle Renamed Succesfully : {new_name}")
    except FileNotFoundError:
        print("File Does Not Exists")


def add_file():
    try:
        with open(filename, "a") as f:
            content = input("Enter content to add :")
            f.write("\n" + content)
            print("Content added")
    except FileNotFoundError:
        print("File Does Not Exists")


def main():
    while True:
        print("""   
                 1.Create File
                 2.Read File
                 3.Delete FIle
                 4.Rename File
                 5.Add content in exixting file
                 6.Exit
  """)

        ch = input("Enter Your Choice : ")

        if ch == "1":
            create_file()

        elif ch == "2":
            read_file()


        elif ch == "3":
            delete_file()

        elif ch == "4":
            rename_file()

        elif ch == "5":
            add_file()

        elif ch == "6":
            print("Exiting...")
            break

        else:
            print("Invalid ch. Please try again.")


main()
