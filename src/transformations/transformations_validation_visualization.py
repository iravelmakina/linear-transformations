import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def ask_and_validate_coefficient(prompt):
    value = input(f"Please, enter {prompt}: ").lower()
    while not is_float(value):
        print("Invalid input. Please, try again: ")
        value = input(f"Please, enter {prompt}: ").lower()
    return float(value)


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def ask_and_validate_axis(prompt, object_3d=False):
    valid_axes = ["x", "y"] if not object_3d else ["x", "y", "z"]
    axes = "x, y, z" if object_3d else "x, y"
    axis = input(f"Please, choose the axis you want to {prompt} the object relative to ({axes}): ").lower()
    while axis not in valid_axes:
        print("Invalid input. Please, try again: ")
        axis = input(f"Please, choose the axis you want to {prompt} the object relative to ({axes}): ").lower()
    return axis


def ask_and_validate_matrix(prompt, dimension):
    matrix = input(f"Please, enter your custom {prompt} matrix (rows separated by ';'): ")
    while not is_valid_matrix(matrix, dimension):
        print("Invalid input. Please, try again: ")
        matrix = input(f"Please, enter your custom {prompt} matrix: ")
    return np.array([list(map(float, row.split())) for row in matrix.split(';')])


def is_valid_matrix(matrix, dimension):
    rows = matrix.split(';')
    for row in rows:
        if len(elements := row.split()) != dimension:
            return False
        for element in elements:
            if not is_float(element):
                return False
    return True


def is_2d_object(object_points):
    return object_points.shape[1] == 2


def is_3d_object(object_points):
    return object_points.shape[1] == 3


def print_matrix(matrix, transformation_adjective):
    print(f"{transformation_adjective} matrix: ")
    for row in matrix:
        formatted_row = [round(float(element), 8) for element in row]
        print(formatted_row)


def visualize_object(object_points):
    if is_2d_object(object_points):
        x_list = [coordinates[0] for coordinates in object_points]
        y_list = [coordinates[1] for coordinates in object_points]
        plt.plot(x_list, y_list)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('2D Object')
        plt.show()
    elif is_3d_object(object_points):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x_list = [coordinates[0] for coordinates in object_points]
        y_list = [coordinates[1] for coordinates in object_points]
        z_list = [coordinates[2] for coordinates in object_points]
        plt.plot(x_list, y_list, z_list)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title('3D Object')
        plt.show()
    else:
        print("Visualization for such an object is not supported.")


def print_and_visualize(matrix, transformation_adjective):
    print_matrix(matrix, transformation_adjective)
    visualize_object(matrix)


def display_and_close_image_cv(title, image):
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()
