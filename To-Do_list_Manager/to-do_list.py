import getpass as gp
def write_diary(username, key):
    message = input(f"Write a message in {username}_diary.txt: ")
    encrypted_message = ""
    try:
        with open(username+"_diary.txt", "a+") as file:
            for char in message:
                encrypted_message += chr(ord(char) ^ key)
            file.write(encrypted_message + "\n")
    except FileNotFoundError:
        print(f"No diary Found for {username}.")
    return print("Message written successfully.")

def read_diary(username, key):
    decrypted_message = ""
    try:
        with open(username+"_diary.txt", "r") as file:
            for line in file:
                for char in line:
                    line = line.strip()
                    decrypted_message += chr(ord(char) ^ key)
        print(decrypted_message)
    except FileNotFoundError:
        print(f"No diary found for {username}.")

username = input("Enter username: ")
password = int(gp.getpass("Enter password: "))

while True:
    file_name = username+"_diary.txt"
    try:
        if password == 1234 and file_name == 'Omkar_diary.txt':
            print("".center(40,"*"))
            print("1. Write to Diary")
            print("2. Read Diary")
            print("3. Exit")
            print("".center(40,"*"))

            choice = input("Enter your choice: ")

            if choice == "3":
                print("Thank you for using our app.")
                break

            if choice == '1':
                write_diary(file_name, password)

            elif choice == '2':
                read_diary(file_name, password)

            else:
                print("Enter right options to perform task.")
        else:
            print("Invalid password and username.")
            # break
    except FileNotFoundError:
        print(f"{file_name} is not found inthe directory!!")