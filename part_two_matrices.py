import cv2 as cv
import numpy as np

import part_one
import objects as obj


def rotate_points_cv(points, angle, center=None):
    if center is None:
        center = (np.mean(points[:, 0]), np.mean(points[:, 1]))
    rotation_matrix = cv.getRotationMatrix2D(center, -angle, 1)
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    rotated_points = cv.transform(np.array([points_homogeneous]), rotation_matrix)
    return rotated_points[0]


def scale_points_cv(points, scale_factor, center=None):
    scaling_matrix = cv.getRotationMatrix2D(center, 0, scale_factor)
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    scaled_points = cv.transform(np.array([points_homogeneous]), scaling_matrix)
    return scaled_points[0]


def reflect_points_cv(points, axis):
    if axis == "x":
        reflection_matrix = np.array([[1, 0, 0], [0, -1, 0]], dtype=np.float32)
    else:
        reflection_matrix = np.array([[-1, 0, 0], [0, 1, 0]], dtype=np.float32)
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    reflected_points = cv.transform(np.array([points_homogeneous]), reflection_matrix)
    return reflected_points[0]


def shear_points_cv(points, shear_factor, axis):
    if axis == "x":
        shearing_matrix = np.array([[1, shear_factor, 0], [0, 1, 0]], dtype=np.float32)
    else:
        shearing_matrix = np.array([[1, 0, 0], [shear_factor, 1, 0]], dtype=np.float32)
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    sheared_points = cv.transform(np.array([points_homogeneous]), shearing_matrix)
    return sheared_points[0]


def transform_points_cv(points, custom_matrix):
    custom_matrix = np.hstack([custom_matrix, np.zeros((custom_matrix.shape[0], 1))])
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = cv.transform(np.array([points_homogeneous]), custom_matrix)
    return transformed_points[0]

# ----------------------------------------------------------------------------------------------------------------------


rotated_hare = rotate_points_cv(obj.hare, 45)
part_one.print_and_visualize(rotated_hare, "Rotated")

scaled_swallow = scale_points_cv(obj.swallow, 1.5)
part_one.print_and_visualize(scaled_swallow, "Scaled Hare")

reflected_hare = reflect_points_cv(obj.hare, "y")
part_one.print_and_visualize(reflected_hare, "Reflected Hare")

sheared_swallow = shear_points_cv(obj.swallow, 0.5, "x")
part_one.print_and_visualize(sheared_swallow, "Sheared Hare")

custom_matrix = np.array([[0.5, 0.5], [0, 1]])  # Example custom transformation matrix
transformed_hare = transform_points_cv(obj.hare, custom_matrix)
part_one.print_and_visualize(transformed_hare, "Custom Transformed Hare")

