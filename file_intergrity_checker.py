import hashlib

# Used to look at files and directories
import os
# Used to add color
from termcolor import colored
# Create a delay to make the shell Gooey look better(It'll seem like its "computing" more)
import time

def get_hash(filename):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    return hashlib.sha256(data).hexdigest()



# Need try becuase it may not work if its the first time running the program(No stored hash)
def check_file_integrity(filename):  
    try:
        # If can't open/read, Raise a FileNotFoundError
        hash_value = open(stored_files_hashes, "r") # opens the stored hash in the read mode(Don't need to read the bytes("rb"))
        stored_hash = hash_value.read() # Reads the stored hash value and stores it as a string in stored_hash
        hash_value.close()

        if stored_hash == starting_hash:
            print()
            print("-------------------------------------------------------------------------------------------------")
            print()
            print(colored(f"File integrity of {filename} file is confirmed. The file has not been modified.", "green"))
            print()
            print(colored("-------------------------------------------------------------------------------------------------", "light_yellow"))
            print()
        else:
            print(colored(f"THE FILE {filename} HAS BEEN MODIFIED. THE HASH VALUES DO NOT MATCH.", "red"))
            print()
            print(colored("-------------------------------------------------------------------------------------------------", "light_yellow"))
            print()
    except FileNotFoundError: # Happens when the new .integrity file of a files hash does not exist yet.
        print(colored("File does not have a hash, create one", "cyan"))
        print()
        print(colored("-------------------------------------------------------------------------------------------------", "light_yellow"))
        print()

print(colored("---------------------------------------------File Integrity Checker---------------------------------------------", "yellow"))

while True:
    print(colored("0) Show all files in the directory\n", "blue"))
    print(colored("1) Create a file hash\n", "blue"))
    print(colored("2) Check file integrity\n", "blue"))
    print(colored("3) Exit\n", "red"))
    user_input = input("Enter your choice: ")

    if user_input == "0":
        time.sleep(1)
        print()
        print(colored("-------------------------------------------------------------------------------------------------", "light_yellow"))
        print()
        for i in os.listdir(): 
            if i == ".git": # git something you don't want to create a hash for, so show as red
                print(colored(i, "red"))
            elif i == "hashed_files":
                print(colored(i, "red")) # hashed_files is directory so show as red
            else:
                print(colored(i, "green")) # Shows all the files in the directory
        print()
        print(colored("-------------------------------------------------------------------------------------------------", "light_yellow"))
        print()
    elif user_input == "1":
        time.sleep(1)
    # Get the name of the file you are trying to check
        filename = input("Enter the name of the file you want to check: ")
        

    # Tells python which file to look at(adress)
        stored_files_hashes = "hashed_files/" + filename + ".integrity" 

        # Calls get_hash function and reads and gets hash and stores as a string in strating_hash 
        starting_hash = get_hash(filename)
        
        hash_value = open(stored_files_hashes, "w") # Opens the .integrity file in write mode to create it and write the hash value to it beucase Read does not create a file. 
        hash_value.write(starting_hash) # The current hash value of the file is added to the .integrity file
        hash_value.close()
        print(colored("-------------------------------------------------------------------------------------------------", "light_yellow"))
        print()
        print(colored(f"[Hash value created for {filename} and stored successfully.]", "green"))
        print()
        print(colored("-------------------------------------------------------------------------------------------------", "light_yellow"))       

    elif user_input == "2":
        time.sleep(1)
        # Creates new input so the user can check the integrity of multiple files
        print()
        file_check = input("Enter the name of the file you want to check: ")
        print()
        filename = file_check
        check_file_integrity(filename)
    elif user_input == "3":
        decision = input("Are you sure you want to exit? (y/n): ")
        if decision == "n":
            print()
            print(colored("-------------------------------------------------------------------------------------------------", "light_yellow"))
            print()
            continue
        elif decision == "y":
            print(colored("Exiting the program.", "red"))
            break
    else:
        print(colored("Invalid input. Select 0, 1, 2, or 3.", "red"))