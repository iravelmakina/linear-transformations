from .transformations_validation_visualization import *


def rotate_object_cv(points, angle, center=None):
    rotation_matrix = cv.getRotationMatrix2D(center, -angle, 1)
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    rotated_points = (cv.transform(np.array([points_homogeneous]), rotation_matrix))[0]
    print_and_visualize(rotated_points, "Rotated")


def scale_object_cv(points, scale_factor, center=None):
    scaling_matrix = cv.getRotationMatrix2D(center, 0, scale_factor)
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    scaled_points = (cv.transform(np.array([points_homogeneous]), scaling_matrix))[0]
    print_and_visualize(scaled_points, "Scaled")


def reflect_object_cv(points):
    axis = ask_and_validate_axis("reflect")
    if axis == "x":
        reflection_matrix = np.array([[1, 0, 0], [0, -1, 0]], dtype=np.float32)
    else:
        reflection_matrix = np.array([[-1, 0, 0], [0, 1, 0]], dtype=np.float32)
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    reflected_points = (cv.transform(np.array([points_homogeneous]), reflection_matrix))[0]
    print_and_visualize(reflected_points, f"Reflected relative to {axis}-axis")


def shear_object_cv(points, shear_factor):
    axis = ask_and_validate_axis("shear")
    if axis == "x":
        shearing_matrix = np.array([[1, shear_factor, 0], [0, 1, 0]], dtype=np.float32)
    else:
        shearing_matrix = np.array([[1, 0, 0], [shear_factor, 1, 0]], dtype=np.float32)
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    sheared_points = (cv.transform(np.array([points_homogeneous]), shearing_matrix))[0]
    print_and_visualize(sheared_points, f"Sheared relative to {axis}-axis")


def transform_object_cv(points):
    custom_matrix = ask_and_validate_matrix("n * 2", 2)
    custom_matrix = np.hstack([custom_matrix, np.zeros((custom_matrix.shape[0], 1))])
    points_homogeneous = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = (cv.transform(np.array([points_homogeneous]), custom_matrix))[0]
    print_and_visualize(transformed_points, "Custom transformed")
