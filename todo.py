todo = ["Practice Python", "Learn Arabic", "Get groceries"]
accepted_commands = {"add", "clear", "edit", "exit", "filename", "help", "load", "move", "remove", "save", "view"}
filename = None

def display_list(list):
    """Displays list arg in command line."""

    print("\nHello! Here is your current to-do list:")

    for index, value in enumerate(list):
        print(index + 1, value)

def add_command(list):
    """Appends a user input item to list arg."""

    item = input("What would you like to add?: ")
    list.append(item)
    print("Item added successfully!")

def clear_command(list):
    """Clears list arg."""

    list.clear()

def edit_command(list):
    """Updates user specificed list index with new user input item."""

    index = get_input_index("Which item number would you like to edit?: ", list)
    new_item = input(f"What would you like to change #{index + 1} to?: ")
    list[index] = new_item
    print("Item updated successfully!")

def help_command():
    """Displays list of valid commands on command line."""

    print("Use the following commands to manipulate your list:")
    print(sorted(accepted_commands))

def load_command(list):
    """Loads saved todo list based on user input filename."""

    global filename

    while(True):
        try:
            filename = input("Which file would you like to load?: ") + ".txt"

            with open(filename, "r", encoding="utf-8") as f:
                list.clear()
                
                for line in f:
                    list.append(line.rstrip())
        
            if (f.closed):
                print("File loaded successfully!")
                break
            else:
                print("File did not close correctly!")
                break

        except FileNotFoundError:
            print("Could not find your file, please try again.")

def move_command(list):
    """Moves user specified index item to new user specified index."""

    index_to_move = get_input_index("Which item number would you like to move?: ", list)
    index_to_replace = get_input_index("Where would you like to place it in the list?: ", list)

    item = list[index_to_move]
    list.pop(index_to_move)  
    list.insert(index_to_replace, item)

    print("Item moved successfully!")
  
def remove_command(list):
    """Removes item at user specified index."""

    index = get_input_index("Which item number would you like to remove?: ", list)
    list.pop(index)
    print("Item removed successfully!")

def save_command(list):
    """Saves todo list to user specified file."""

    global filename
    if filename is None:
        filename = input("Enter name of the file you'd like to save: ") + ".txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        for item in list:
            f.write(item + "\n")

    if (f.closed):
        print ("File saved successfully!")
    else:
        print("The file did not close correctly!")

def get_input_command():
    """Validates and returns user inputted command."""

    while(True):
        command = input("What would you like to do?: ")

        if command in accepted_commands:
            return command
        else:
            print("Please enter a valid command. Type 'help' for list of commands.\n")

def get_input_index(input_text, list):
    """Returns and validates user inputted index."""

    while(True):
        try:
            user_input = int(input(input_text))
        except ValueError:
            print("Please enter an integer!\n")
        
        index = user_input - 1
        if index in range(0, len(list)):
            return index
        else:
            print("Your list does not contain that item number!\n")

def process_command(command, list):
    """Takes arg command and calls appropriate proccessing function."""
    
    match command:
        case "add":
            add_command(list)
        case "clear":
            clear_command(list)
        case "edit":
            edit_command(list)
        case "filename":
            print(filename)
        case "help":
            help_command()
        case "load":
            load_command(list)
        case "move":
            move_command(list)
        case "remove":
            remove_command(list)
        case "save":
            save_command(list)
        case "view":
            display_list(list)

display_list(todo)

while(True):
    print()

    command = get_input_command()

    if command == "exit":
        break

    process_command(command, todo)

