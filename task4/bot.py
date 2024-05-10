def parse_input(user_input):
    """Parse bot command and arguments
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """Bot add command implementation
    """
    valid, message = validate_args(args, 2)
    if not valid:
        return message
    else:
        name, phone = args
        if name in contacts:
            return "Contact already exist pls use change command to modify"
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    """Bot change command implementation
    """
    valid, message = validate_args(args, 2)
    if not valid:
        return message
    else:
        name, phone = args
        if name not in contacts:
            return f"There is no contact with the name '{name}'"
        contacts[name] = phone
        return "Contact changed."

def get_all_contacts(args, contacts):
    """Bot all command implementation
    """
    valid, message = validate_args(args, 0)
    if not valid:
        return message
    else:
        return contacts

def get_phone_by_user(args, contacts):
    """Bot phone command implementation
    """
    valid, message = validate_args(args, 1)
    if not valid:
        return message
    else:
        name = args[0]
        if name not in contacts:
            return f"There is no contact with the name '{name}'"
        return contacts[name]


def validate_args(args, args_count):
    """validate arguments count
    """
    if len(args) != args_count:
        return False, f"Command should have '{args_count}' arguments."
    return True, None

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(get_all_contacts(args, contacts))        
        elif command == "phone":
            print(get_phone_by_user(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
