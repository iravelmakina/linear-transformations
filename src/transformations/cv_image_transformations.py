from .transformations_validation_visualization import *


def rotate_image_cv(image, h, w, angle):
    center = (w / 2, h / 2)
    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv.warpAffine(image, rotation_matrix, (w, h))
    display_and_close_image_cv("Rotated image", rotated_image)


def scale_image_cv(image, h, w, scale_factor):
    scaling_matrix = np.array([[scale_factor, 0, 0], [0, scale_factor, 0]], dtype=np.float32)
    scaled_image = cv.warpAffine(image, scaling_matrix, (int(w * scale_factor), int(h * scale_factor)))
    display_and_close_image_cv("Scaled image", scaled_image)


def reflect_image_cv(image, h, w, axis):
    if axis == "x":
        reflection_matrix = (
            np.array([[1, 0, 0], [0, -1, h]], dtype=np.float32))
    else:
        reflection_matrix = np.array([[-1, 0, w], [0, 1, 0]], dtype=np.float32)
    reflected_image = cv.warpAffine(image, reflection_matrix, (w, h))
    display_and_close_image_cv("Reflected image", reflected_image)


def shear_image_cv(image, h, w, shear_factor, axis):
    if axis == "x":
        shearing_matrix = np.array([[1, shear_factor, 0], [0, 1, 0]], dtype=np.float32)
    else:
        shearing_matrix = np.array([[1, 0, 0], [shear_factor, 1, 0]], dtype=np.float32)
    sheared_image = cv.warpAffine(image, shearing_matrix, (w, h))
    display_and_close_image_cv("Sheared image", sheared_image)
