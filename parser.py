from part_one import *


def process_command(user_choice):
    match user_choice:
        case "1":
            print("Let's rotate the object!")
            rotate_object()
        case "2":
            print("Let's scale the object!")
            scale_object()
        case "3":
            print("Let's reflect the object!")
            reflect_object()
        case "4":
            print("Let's shear the object!")
            shear_object()
        case "5":
            print("Let's transform object with custom matrix!")
            transform_object()
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
    while True:
        user_choice = (input("Please, choose your command: ")).lower()
        while not is_valid_input(user_choice):
            print("Invalid input. Please, try again: ")
            user_choice = (input("Please, choose your command: ")).lower()

        if user_choice == "e":
            break
        elif user_choice == "m":
            print_menu()
        else:
            process_command(user_choice)
    print("Okay, bye!")
    return


main()

