from part_one import *


def process_command(user_choice):
    match user_choice:
        case "1":
            print("Rotating the object...")
            rotate_object(hare)
            rotate_object(swallow)
        case "2":
            print("Scaling the object...")
            scale_object(hare)
            scale_object(swallow)
        case "3":
            print("Reflecting the object...")
            reflect_object(hare)
            reflect_object(swallow)
        case "4":
            print("Shearing the object...")
            shear_object(hare)
            shear_object(swallow)
        case "5":
            print("Transforming with custom matrix...")
            transform_object(hare)
            transform_object(swallow)
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
        else:
            process_command(user_choice)
    print("Okay, bye!")
    return


main()

