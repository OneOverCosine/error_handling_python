# dealing with files and error handling

filename = "orders.txt"

def open_and_read_file(filename):
    
    try:
        # built in method for opening files - open("filename")
        file = open(filename)
        print(f"{filename} opened!")
    except FileNotFoundError as err:
        print(err) # prints the error message to the console
        print(f"Could not find {filename}. Make sure your file exists...")
    else:
        # this only runs if the try didn't raise any exceptions
        # put data from file into a list
        orders = file.readlines()
            
        for i in range(len(orders)):
            orders[i] = orders[i].replace("\n", "")

        print(orders)

    finally:
        # always executes, regardless of errors
        print("I always run!")


open_and_read_file(filename)