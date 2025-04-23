from .transformations_validation_visualization import *


def rotate_object(object_points, angle_in_degrees):
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


def scale_object(object_points, scale_factor):
    scaled_object = scale_factor * object_points
    print_and_visualize(scaled_object, "Scaled")


def reflect_object(object_points):
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


def shear_object(object_points, shear_factor):
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


def transform_object(object_points):
    if is_2d_object(object_points):
        custom_matrix = ask_and_validate_matrix("n * 2", 2)
    elif is_3d_object(object_points):
        custom_matrix = ask_and_validate_matrix("n * 3", 3)
    else:
        print("Transformation for such an object is not supported.")
        return
    transformed_object = np.dot(custom_matrix, object_points.T).T
    print_and_visualize(transformed_object, "Transformed")
