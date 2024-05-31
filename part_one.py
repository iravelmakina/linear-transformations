import matplotlib.pyplot as plt
import numpy as np

hare = np.array(
    [[5, 1], [6, 2], [6, 3], [5, 6], [4, 7], [5, 8], [6, 8], [8, 9], [9, 9], [7, 8], [9, 8], [6, 7], [7, 6], [9, 6],
     [11, 5], [12, 3], [12, 2], [13, 3], [12, 1], [7, 1], [8, 2], [9, 2], [8, 3], [6, 1], [5, 1]])

swallow = np.array(
    [[-5, 4], [-7, 4], [-9, 6], [-11, 6], [-12, 5], [-14, 5], [-12, 4], [-14, 3], [-12, 3], [-11, 2], [-10, 2],
     [-9, 1], [-9, 0], [-8, -2], [0, -3], [3, -2], [19, -2], [4, 0], [19, 4], [4, 2], [2, 3], [6, 9], [10, 11],
     [3, 11], [1, 10], [-5, 4]])

shape = np.array([[0, 0, 0], [1, 2, 1], [2, 3, 1], [3, 3, 0], [2, 2, -1], [1, 0, -1], [0, -1, 0],
                  [-1, -2, 1], [-2, -3, 1], [-3, -3, 0], [-2, -2, -1], [-1, 0, -1], [0, 0, 0]])

object_dict = {"hare": hare, "swallow": swallow, "shape": shape}


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


def ask_and_validate_object(object_dict, prompt):
    object_choice = input(f"Please, choose the object you want to {prompt}: ").lower()
    while object_choice not in ["hare", "swallow", "shape"]:
        print("Invalid input. Please, try again: ")
        object_choice = input(f"Please, choose the object you want to {prompt}: ").lower()
    return object_dict[object_choice] # OK


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
        print("Visualization for such an object is not supported.")


def print_and_visualize(matrix, transformation_adjective):
    print_matrix(matrix, transformation_adjective)
    visualize_object(matrix)


def rotate_object():
    object_points = ask_and_validate_object(object_dict, "rotate")
    angle_in_degrees = ask_and_validate_coefficient("angle")
    angle_in_radians = angle_in_degrees * np.pi / 180

    if is_2d_object(object_points):
        rotation_matrix = np.array([[np.cos(angle_in_radians), -np.sin(angle_in_radians)],
                                    [np.sin(angle_in_radians), np.cos(angle_in_radians)]])
        rotated_object = np.dot(rotation_matrix, object_points.T).T
    elif is_3d_object(object_points):
        axis = ask_and_validate_axis("rotate", object_3d=True)
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
    else:
        print("Rotation for such an object is not supported.")
        return
    print_and_visualize(rotated_object, "Rotated")


def scale_object():
    object_points = ask_and_validate_object(object_dict, "scale")
    scale_factor = ask_and_validate_coefficient("scale factor")
    scaled_object = scale_factor * object_points
    print_and_visualize(scaled_object, "Scaled") # OK


def reflect_object():
    object_points = ask_and_validate_object(object_dict, "reflect")
    if is_2d_object(object_points):
        axis = ask_and_validate_axis("reflect")
        if axis == "x":
            transformation_matrix = np.array([[1, 0], [0, -1]])
        else:
            transformation_matrix = np.array([[-1, 0], [0, 1]])
    elif is_3d_object(object_points):
        axis = ask_and_validate_axis("reflect", object_3d=True)
        if axis == "x":
            transformation_matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])
        elif axis == "y":
            transformation_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])
        else:
            transformation_matrix = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])
    else:
        print("Reflection for such an object is not supported.")
        return
    reflected_object = np.dot(transformation_matrix, object_points.T).T
    print_and_visualize(reflected_object, f"Reflected relative to {axis}-axis")


def shear_object():
    object_points = ask_and_validate_object(object_dict, "shear")
    shear_factor = ask_and_validate_coefficient("shear factor")
    if is_2d_object(object_points):
        axis = ask_and_validate_axis("shear")
        if axis == "x":
            shear_matrix = np.array([[1, shear_factor], [0, 1]])
        else:
            shear_matrix = np.array([[1, 0], [shear_factor, 1]])
    elif is_3d_object(object_points):
        axis = ask_and_validate_axis("shear", object_3d=True)
        if axis == "x":
            shear_matrix = np.array([[1, shear_factor, shear_factor], [0, 1, 0], [0, 0, 1]])
        elif axis == "y":
            shear_matrix = np.array([[1, 0, 0], [shear_factor, 1, shear_factor], [0, 0, 1]])
        else:
            shear_matrix = np.array([[1, 0, 0], [0, 1, 0], [shear_factor, shear_factor, 1]])
    else:
        print("Shearing for such an object is not supported.")
        return
    sheared_object = np.dot(shear_matrix, object_points.T).T
    print_and_visualize(sheared_object, f"Sheared relative to {axis}-axis")


def transform_object():
    object_points = ask_and_validate_object(object_dict, "transform")
    if is_2d_object(object_points):
        custom_matrix = ask_and_validate_matrix("n * 2", 2)
    elif is_3d_object(object_points):
        custom_matrix = ask_and_validate_matrix("n * 3", 3)
    else:
        print("Transformation for such an object is not supported.")
        return
    transformed_object = np.dot(custom_matrix, object_points.T).T
    print_and_visualize(transformed_object, "Transformed")
