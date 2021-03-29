# dealing with files and error handling

filename = "orders.txt"

def open_and_read_file(filename):
    
    try:
        # built in method for opening files - open("filename")
        file = open(filename, "r+")
        print(f"{filename} opened!")
    except FileNotFoundError as err:
        print(err) # prints the error message to the console
        print(f"Could not find {filename}. Make sure your file exists...")
    else:
        # this only runs if the try didn't raise any exceptions
        # put data from file into a list
        orders = []
            
        for line in file.readlines():
            orders.append(line.strip("\n"))

        print(orders)

        file.write(write_to_file())

    finally:
        # always executes, regardless of errors
        print("I always run!")
        return file

def write_to_file():

    user_input = input("Add an item to the list\n")

    while True:
        confirm_input = input(f"Are you sure you want to add {user_input}\n")

        if confirm_input.lower() == 'yes':
            return "\n" + user_input
        else:
            user_input = input("Add an item to the list\n")

orders_file = open_and_read_file(filename)
orders_file.seek(0)

# wip
for line in orders_file.readlines():
    print(line.strip("\n"))

orders_file.close()