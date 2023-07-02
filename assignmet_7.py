def update_file(file="data.txt"):
    try:
        # Open the file in append mode
        f = open(file, "a")
        
        # Write data to the file
        roll_number = "12345"
        name = "Gauri"
        class_name = "SYCO"
        f.writelines([roll_number + "\n", name + "\n", class_name + "\n"])
                
        # Reopen the file in read mode
        f = open(file, "r")
        
        # Read and print the data from the file
        print(f.readlines())

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")

# Call the function
update_file()
