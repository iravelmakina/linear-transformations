from part_one import *


class CommandParser:
    def __init__(self, object_dict):
        self.object_dict = object_dict
        self.current_object = None
        self.transformer = None

    @staticmethod
    def print_menu():
        print("1. Rotate object\n"
              "2. Scale object\n"
              "3. Reflect relative to certain axis\n"
              "4. Shear the object\n"
              "5. Transform with custom matrix\n"
              "6. Change current object\n")

    @staticmethod
    def is_valid_input(user_choice):
        return (user_choice.isdigit() and 0 < int(user_choice) < 7) or user_choice in ["m", "e"]

    def ask_and_validate_object(self):
        object_choice = input(f"Please, choose the object (available options: {', '.join(self.object_dict.keys())}): ").lower()
        while object_choice not in self.object_dict:
            print("Invalid input. Please, try again: ")
            object_choice = input(f"Please, choose the object (available options: {', '.join(self.object_dict.keys())}): ").lower()
        self.current_object = self.object_dict[object_choice]
        self.transformer = Transformer()
        print(f"Current object set to {self.current_object.name}")

    def process_command(self, user_choice):
        if not self.current_object and user_choice != "6":
            self.ask_and_validate_object()

        match user_choice:
            case "1":
                print("Let's rotate the object!")
                self.transformer.rotate(self.current_object)
            case "2":
                print("Let's scale the object!")
                self.transformer.scale(self.current_object)
            case "3":
                print("Let's reflect the object!")
                self.transformer.reflect(self.current_object)
            case "4":
                print("Let's shear the object!")
                self.transformer.shear(self.current_object)
            case "5":
                print("Let's transform the object with custom matrix!")
                self.transformer.transform(self.current_object)
            case "6":
                print("Let's change the current object!")
                self.ask_and_validate_object()
            case _:
                print("Unable to process the command. Please, try again.")
                return


object_dict = {"hare": hare, "swallow": swallow, "bird": shape}


def main():
    print("Welcome to object transformer! Enter 'm' to see all the commands and 'e' to exit")
    command_parser = CommandParser(object_dict)
    user_choice = ""
    while user_choice != "e":
        user_choice = (input("Please, choose your command: ")).lower()
        while not command_parser.is_valid_input(user_choice):
            print("Invalid input. Please, try again: ")
            user_choice = (input("Please, choose your command: ")).lower()

        if user_choice == "m":
            command_parser.print_menu()
        else:
            command_parser.process_command(user_choice)
    print("Okay, bye!")
    return


main()

hare = np.array(
    [[5, 1], [6, 2], [6, 3], [5, 6], [4, 7], [5, 8], [6, 8], [8, 9], [9, 9], [7, 8], [9, 8], [6, 7], [7, 6], [9, 6],
     [11, 5], [12, 3], [12, 2], [13, 3], [12, 1], [7, 1], [8, 2], [9, 2], [8, 3], [6, 1], [5, 1]])
hare = Object("hare", hare)

swallow = np.array(
    [[-5, 4], [-7, 4], [-9, 6], [-11, 6], [-12, 5], [-14, 5], [-12, 4], [-14, 3], [-12, 3], [-11, 2], [-10, 2],
     [-9, 1], [-9, 0], [-8, -2], [0, -3], [3, -2], [19, -2], [4, 0], [19, 4], [4, 2], [2, 3], [6, 9], [10, 11],
     [3, 11], [1, 10], [-5, 4]])
swallow = Object("swallow", swallow)

shape = np.array([[0, 0, 0], [1, 2, 1], [2, 3, 1], [3, 3, 0], [2, 2, -1], [1, 0, -1], [0, -1, 0],
                  [-1, -2, 1], [-2, -3, 1], [-3, -3, 0], [-2, -2, -1], [-1, 0, -1], [0, 0, 0]])
shape = Object("bird", shape)
