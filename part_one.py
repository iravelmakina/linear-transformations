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
