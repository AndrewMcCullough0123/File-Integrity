import hashlib

# Used to look at files and directories
import os
# Used to add color
import termcolor
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
            print(f"File integrity of {filename} file is confirmed. The file has not been modified.")
            print()
            print("-------------------------------------------------------------------------------------------------")
            print()
        else:
            print(f"THE FILE {filename} HAS BEEN MODIFIED. THE HASH VALUES DO NOT MATCH.")
            print()
            print("-------------------------------------------------------------------------------------------------")
            print()
    except FileNotFoundError: # Happens when the new .integrity file of a files hash does not exist yet.
        print("File does not have a hash, create one")
        print()
        print("-------------------------------------------------------------------------------------------------")
        print()

print("---------------------------------------------File Integrity Checker---------------------------------------------")

while True:
    print("0) Show all files in the directory\n")
    print("1) Create a file hash\n")
    print("2) Check file integrity\n")
    print("3) Exit\n")
    user_input = input("Enter your choice: ")

    if user_input == "0":
        time.sleep(1)
        print()
        print("-------------------------------------------------------------------------------------------------")
        print()
        print(os.listdir()) # Shows all the files in the directory
        print()
        print("-------------------------------------------------------------------------------------------------")
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
        print("-------------------------------------------------------------------------------------------------")
        print()
        print(f"[Hash value created for {filename} and stored successfully.]")
        print()
        print("-------------------------------------------------------------------------------------------------")
        print()

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
            print("-------------------------------------------------------------------------------------------------")
            print()
            continue
        elif decision == "y":
            print("Exiting the program.")
            break
    else:
        print("Invalid input. Select 0, 1, 2, or 3.")