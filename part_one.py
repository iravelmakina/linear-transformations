import matplotlib.pyplot as plt
import numpy as np

hare = np.array(
    [[5, 1], [6, 2], [6, 3], [5, 6], [4, 7], [5, 8], [6, 8], [8, 9], [9, 9], [7, 8], [9, 8], [6, 7], [7, 6], [9, 6],
     [11, 5], [12, 3], [12, 2], [13, 3], [12, 1], [7, 1], [8, 2], [9, 2], [8, 3], [6, 1], [5, 1]])

swallow = np.array(
    [[-5, 4], [-7, 4], [-9, 6], [-11, 6], [-12, 5], [-14, 5], [-12, 4], [-14, 3], [-12, 3], [-11, 2], [-10, 2],
     [-9, 1], [-9, 0], [-8, -2], [0, -3], [3, -2], [19, -2], [4, 0], [19, 4], [4, 2], [2, 3], [6, 9], [10, 11],
     [3, 11], [1, 10], [-5, 4]])


def visualize_object(object_points):
    x_list = [coordinates[0] for coordinates in object_points]
    y_list = [coordinates[1] for coordinates in object_points]
    plt.plot(x_list, y_list)
    plt.show()


def rotate_object(object_points):
    angle_in_degrees = input("Please, enter angle for rotation: ")  # validation
    angle_in_radians = float(angle_in_degrees) * np.pi / 180
    rotation_matrix = np.array(
        [[np.cos(angle_in_radians), -np.sin(angle_in_radians)],  # it works vice versa without transposing though
         [np.sin(angle_in_radians), np.cos(angle_in_radians)]])
    rotated_object = np.dot(rotation_matrix, object_points.T).T
    visualize_object(rotated_object)


def scale_object(object_points):  # validation
    scale_factor = float(input("Please, enter desired scaling coefficient: "))
    scaled_object = scale_factor * object_points
    visualize_object(scaled_object)


def reflect_object(object_points):
    transformation_matrix_x = np.array([[1, 0], [0, -1]])
    transformation_matrix_y = np.array([[-1, 0], [0, 1]])

    reflected_x_axis = np.dot(transformation_matrix_x, object_points.T).T
    reflected_y_axis = np.dot(transformation_matrix_y, object_points.T).T
    visualize_object(reflected_x_axis)
    visualize_object(reflected_y_axis)


def shear_object(object_points):
    shear_factor = float(input("Please, enter desired shear coefficient: "))
    shear_matrix_x = np.array([[1, shear_factor], [0, 1]])
    shear_matrix_y = np.array([[1, 0], [shear_factor, 1]])

    sheared_x_axis = np.dot(shear_matrix_x, object_points.T).T
    sheared_y_axis = np.dot(shear_matrix_y, object_points.T).T
    visualize_object(sheared_x_axis)
    visualize_object(sheared_y_axis)


def transform_object(object_points):
    custom_matrix = input("Please, enter your custom 2 * n matrix: ")
    custom_matrix = np.array([list(map(float, row.split())) for row in custom_matrix.split(';')])
    transformed_object = np.dot(custom_matrix, object_points.T).T
    visualize_object(transformed_object)