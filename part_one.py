import matplotlib.pyplot as plt
import numpy as np

hare = np.array(
    [[5, 1], [6, 2], [6, 3], [5, 6], [4, 7], [5, 8], [6, 8], [8, 9], [9, 9], [7, 8], [9, 8], [6, 7], [7, 6], [9, 6],
     [11, 5], [12, 3], [12, 2], [13, 3], [12, 1], [7, 1], [8, 2], [9, 2], [8, 3], [6, 1], [5, 1]])

swallow = np.array(
    [[-5, 4], [-7, 4], [-9, 6], [-11, 6], [-12, 5], [-14, 5], [-12, 4], [-14, 3], [-12, 3], [-11, 2], [-10, 2],
     [-9, 1], [-9, 0], [-8, -2], [0, -3], [3, -2], [19, -2], [4, 0], [19, 4], [4, 2], [2, 3], [6, 9], [10, 11],
     [3, 11], [1, 10], [-5, 4]])

bird = np.array([[0, 0, 0], [1, 2, 1], [2, 3, 1], [3, 3, 0], [2, 2, -1], [1, 0, -1], [0, -1, 0],
                 [-1, -2, 1], [-2, -3, 1], [-3, -3, 0], [-2, -2, -1], [-1, 0, -1], [0, 0, 0]])

object_dict = {"hare": hare, "swallow": swallow, "bird": bird}


# func to validate integer input
def ask_and_validate_input(prompt):
    value = input(f"Please, enter {prompt}: ").lower()
    while not value.isdigit():
        print("Invalid input. Please, try again: ")
        value = input(f"Please, enter {prompt}: ").lower()
    return value


# func to choose object
def choose_object(object_dict, prompt):
    object_choice = input(f"Please, choose the object you want to {prompt}: ").lower()
    while object_choice not in ["hare", "swallow", "bird"]:
        print("Invalid input. Please, try again: ")
        object_choice = input("Please, choose the object you want to {prompt}: ").lower()
    return object_dict[object_choice]


def is_2d_object(object_points):
    return object_points.shape[1] == 2


def is_3d_object(object_points):
    return object_points.shape[1] == 3


def print_matrix(matrix, transformation_adjective):
    print(f"{transformation_adjective} matrix: ")
    for row in matrix:
        print(row)


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
        print("Visualization for such an object is not supported.")  # OK


def print_and_visualize(matrix, transformation_adjective):
    print_matrix(matrix, transformation_adjective)
    visualize_object(matrix)

# ----------------------------------------------------------------------------------------------------------------------


def rotate_object():
    object_points = choose_object(object_dict, "rotate")
    angle_in_degrees = ask_and_validate_input("angle")
    angle_in_radians = float(angle_in_degrees) * np.pi / 180

    if is_2d_object(object_points):
        rotation_matrix = np.array([[np.cos(angle_in_radians), -np.sin(angle_in_radians)],
                                    [np.sin(angle_in_radians), np.cos(angle_in_radians)]])
        rotated_object = np.dot(rotation_matrix, object_points.T).T
        print_and_visualize(rotated_object, "Rotated")
    elif is_3d_object(object_points):
        axis = input("Please, choose the axis you want to rotate the object around (x, y, z): ").lower()
        while axis not in ["x", "y", "z"]:
            print("Invalid input. Please, try again: ")
            axis = input("Please, choose the axis you want to rotate the object around (x, y, z): ").lower()

        if axis == "x":
            rotation_matrix = np.array([[1, 0, 0],
                                      [0, np.cos(angle_in_radians), -np.sin(angle_in_radians)],
                                      [0, np.sin(angle_in_radians), np.cos(angle_in_radians)]])
        elif axis == "y":
            rotation_matrix = np.array([[np.cos(angle_in_radians), 0, -np.sin(angle_in_radians)],
                                      [0, 1, 0],
                                      [np.sin(angle_in_radians), 0, np.cos(angle_in_radians)]])
        else:
            rotation_matrix = np.array([[np.cos(angle_in_radians), -np.sin(angle_in_radians), 0],
                                      [np.sin(angle_in_radians), np.cos(angle_in_radians), 0],
                                      [0, 0, 1]])

        rotated_object = np.dot(rotation_matrix, object_points.T).T
        print_and_visualize(rotated_object, "Rotated")
    else:
        print("Rotation for such an object is not supported.")
        return


def scale_object():
    object_points = choose_object(object_dict, "scale")
    scale_factor = ask_and_validate_input("scale factor")
    scaled_object = scale_factor * object_points
    print_and_visualize(scaled_object, "Scaled") # OK


def reflect_object(object_points):
    transformation_matrix_x = np.array([[1, 0], [0, -1]])
    transformation_matrix_y = np.array([[-1, 0], [0, 1]])

    reflected_x_axis = np.dot(transformation_matrix_x, object_points.T).T
    reflected_y_axis = np.dot(transformation_matrix_y, object_points.T).T
    print_matrix(reflected_x_axis, "Reflected relative to x-axis")
    visualize_object(reflected_x_axis)
    print_and_visualize(reflected_y_axis, "Reflected relative to y-axis")


def shear_object(object_points):
    shear_factor = ask_and_validate_input("shear factor")
    shear_matrix_x = np.array([[1, shear_factor], [0, 1]])
    shear_matrix_y = np.array([[1, 0], [shear_factor, 1]])

    sheared_x_axis = np.dot(shear_matrix_x, object_points.T).T
    sheared_y_axis = np.dot(shear_matrix_y, object_points.T).T
    print_matrix(sheared_x_axis, "Sheared relative to x-axis")
    visualize_object(sheared_x_axis)
    print_and_visualize(sheared_y_axis, "Sheared relative to y-axis")


def transform_object(object_points):
    custom_matrix = input("Please, enter your custom 2 * n matrix: ")  # validation
    custom_matrix = np.array([list(map(float, row.split())) for row in custom_matrix.split(';')])
    transformed_object = np.dot(custom_matrix, object_points.T).T
    print_and_visualize(transformed_object, "Transformed")
