from src.parser.parser import *


def main():
    print("Welcome to object transformer! Enter 'm' to see all the commands and 'e' to exit")
    mode = "manual"
    object_or_image = None
    image, h, w = initialize_image(image_path)

    while True:
        user_choice = (input("Please, choose your command: ")).lower()
        while not is_valid_input(user_choice, mode, object_or_image):
            print("Invalid input. Please, try again: ")
            user_choice = (input("Please, choose your command: ")).lower()

        if user_choice == "e":
            break
        elif user_choice == "m":
            print_menu()
        elif user_choice == "mode":
            mode, object_or_image = switch_mode(mode)
        elif user_choice == "change":
            object_or_image = ask_and_validate_object_or_image()
        else:
            process_command(user_choice, mode, image, h, w, object_or_image)

    print("Okay, bye!")
    return


main()
