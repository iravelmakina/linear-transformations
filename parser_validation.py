def is_valid_input(user_choice, mode, object_or_image):
    if mode == "manual":
        return (user_choice.isdigit() and 1 <= int(user_choice) <= 5) or user_choice in ["m", "e", "mode"]
    elif mode == "opencv":
        return (user_choice.isdigit() and ((object_or_image == "object" and 1 <= int(user_choice) <= 5) or (
                object_or_image == "image" and 6 <= int(user_choice) <= 9))) or user_choice in ["m", "e", "mode",
                                                                                                "change"]


def ask_and_validate_object_or_image():
    choice = input("Do you want to transform an object or an image? (object/image): ").lower()
    while choice not in ["object", "image"]:
        print("Invalid input. Please, try again.")
        choice = input("Do you want to transform an object or an image? (object/image): ").lower()
    return choice


def ask_and_validate_object(object_dict, prompt, possible_3d=False):
    valid_objects = ["hare", "swallow"] if not possible_3d else ["hare", "swallow", "shape"]
    object_choice = input(f"Please, choose the object you want to {prompt}: ").lower()
    while object_choice not in valid_objects:
        print("Invalid input. Please, try again: ")
        object_choice = input(f"Please, choose the object you want to {prompt}: ").lower()
    return object_dict[object_choice]