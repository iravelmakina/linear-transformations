def process_command(user_choice):
    match user_choice:
        case "1":
            print("Rotating the object...")
        case "2":
            print("Scaling the object...")
        case "3":
            print("Reflecting the object...")
        case "4":
            print("Shearing the object...")
        case "5":
            print("Transforming with custom matrix...")
        case _:
            print("Unable to process the command. Please, try again.")
            return


def print_menu():
    print("1. Rotate object\n"
          "2. Scale object\n"
          "3. Reflect relative to certain axis\n"
          "4. Shear the object\n"
          "5. Transform with custom matrix\n")


def is_valid_input(user_choice):
    return (user_choice.isdigit() and 0 < int(user_choice) < 6) or user_choice in ["m", "e"]


def main():
    print("Welcome to object transformer! Enter 'm' to see all the commands and 'e' to exit")
    user_choice = ""
    while user_choice != "e":
        user_choice = (input("Please, choose your command: ")).lower()
        while not is_valid_input(user_choice):
            print("Invalid input. Please, try again: ")
            user_choice = (input("Please, choose your command: ")).lower()

        if user_choice == "m":
            print_menu()
        elif user_choice == "e":
            print("Okay, bye!")
            return
        else:
            process_command(user_choice)


main()

