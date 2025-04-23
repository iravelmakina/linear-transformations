from src.transformations.manual_matrix_transformations import *
from src.transformations.cv_matrix_transformations import *
from src.transformations.cv_image_transformations import *
from src.objects import *
from .parser_validation import *


def process_object_command(user_choice, object_or_image, image, h, w):
    if object_or_image == "object":
        if user_choice == "1":
            print("Let's rotate the object!")
            points = ask_and_validate_object(object_dict, "rotate")
            angle = ask_and_validate_coefficient("angle")
            rotate_object_cv(points, angle)
        elif user_choice == "2":
            print("Let's scale the object!")
            points = ask_and_validate_object(object_dict, "scale")
            scale_factor = ask_and_validate_coefficient("scale factor")
            scale_object_cv(points, scale_factor)
        elif user_choice == "3":
            print("Let's reflect the object!")
            points = ask_and_validate_object(object_dict, "reflect")
            reflect_object_cv(points)
        elif user_choice == "4":
            print("Let's shear the object!")
            points = ask_and_validate_object(object_dict, "shear")
            shear_factor = ask_and_validate_coefficient("shear factor")
            shear_object_cv(points, shear_factor)
        elif user_choice == "5":
            print("Let's transform object with custom matrix!")
            points = ask_and_validate_object(object_dict, "transform")
            transform_object_cv(points)
        else:
            print("Unable to process the command. Please, try again.")
    elif object_or_image == "image":
        if image is None:
            return
        if user_choice == "6":
            print("Let's rotate the image!")
            angle = ask_and_validate_coefficient("angle")
            rotate_image_cv(image, h, w, angle)
        elif user_choice == "7":
            print("Let's scale the image!")
            scale_factor = ask_and_validate_coefficient("scale factor")
            scale_image_cv(image, h, w, scale_factor)
        elif user_choice == "8":
            print("Let's reflect the image!")
            axis = ask_and_validate_axis("reflect")
            reflect_image_cv(image, h, w, axis)
        elif user_choice == "9":
            print("Let's shear the image!")
            shear_factor = ask_and_validate_coefficient("shear factor")
            axis = ask_and_validate_axis("shear")
            shear_image_cv(image, h, w, shear_factor, axis)
        else:
            print("Unable to process the command. Please, try again.")


def process_manual_command(user_choice):
    if user_choice == "1":
        print("Let's rotate the object!")
        object_points = ask_and_validate_object(object_dict, "rotate", possible_3d=True)
        angle_in_degrees = ask_and_validate_coefficient("angle")
        rotate_object(object_points, angle_in_degrees)
    elif user_choice == "2":
        print("Let's scale the object!")
        object_points = ask_and_validate_object(object_dict, "scale", possible_3d=True)
        scale_factor = ask_and_validate_coefficient("scale factor")
        scale_object(object_points, scale_factor)
    elif user_choice == "3":
        print("Let's reflect the object!")
        object_points = ask_and_validate_object(object_dict, "reflect", possible_3d=True)
        reflect_object(object_points)
    elif user_choice == "4":
        print("Let's shear the object!")
        object_points = ask_and_validate_object(object_dict, "shear", possible_3d=True)
        shear_factor = ask_and_validate_coefficient("shear factor")
        shear_object(object_points, shear_factor)
    elif user_choice == "5":
        print("Let's transform object with custom matrix!")
        object_points = ask_and_validate_object(object_dict, "transform", possible_3d=True)
        transform_object(object_points)
    else:
        print("Unable to process the command. Please, try again.")


def process_command(user_choice, mode, image, h, w, object_or_image=None):
    if mode == "manual":
        process_manual_command(user_choice)
    elif mode == "opencv":
        if object_or_image is None or user_choice == "change":
            object_or_image = ask_and_validate_object_or_image()
        process_opencv_command(user_choice, object_or_image, image, h, w)


def process_opencv_command(user_choice, object_or_image, image, h, w):
    process_object_command(user_choice, object_or_image, image, h, w)


def print_menu():
    print("\nWelcome to the Object and Image Transformer! Here are your options:\n"
          "1. Rotate object: This option allows you to rotate an object by a specified angle.\n"
          "2. Scale object: This option allows you to scale an object by a specified factor.\n"
          "3. Reflect object relative to certain axis: This option allows you to reflect an object relative to the x or y axis.\n"
          "4. Shear object: This option allows you to shear an object along the x or y axis.\n"
          "5. Transform object with custom matrix: This option allows you to apply a custom transformation matrix to an object.\n"
          "6. Rotate image: This option allows you to rotate an image by a specified angle.\n"
          "7. Scale image: This option allows you to scale an image by a specified factor.\n"
          "8. Reflect image relative to certain axis: This option allows you to reflect an image relative to the x or y axis.\n"
          "9. Shear image: This option allows you to shear an image along the x or y axis.\n"
          "Enter 'm' to see this menu again.\n"
          "Enter 'e' to exit the program.\n"
          "Enter 'mode' to switch between manual and OpenCV modes.\n"
          "Enter 'change' to switch between transforming an object and an image in 'opencv' mode.\n")


def initialize_image(image_path):
    image = cv.imread(image_path)
    if image is None:
        print("Could not read the image.")
        return None, None, None
    else:
        h, w = image.shape[:2]
        return image, h, w


def switch_mode(current_mode):
    new_mode = "opencv" if current_mode == "manual" else "manual"
    print(f"Switched to {new_mode} mode.")
    if new_mode == "opencv":
        object_or_image = ask_and_validate_object_or_image()
        return new_mode, object_or_image
    else:
        return new_mode, None
