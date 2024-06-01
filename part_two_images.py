import cv2 as cv
import numpy as np

image = cv.imread("brain.jpg")
if image is None:
    print("Could not read the image.")
else:
    (h, w) = image.shape[:2]


def display_and_close(title, image):
    cv.imshow(title, image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def rotate_image(image, angle):
    center = (w // 2, h // 2)
    rotation_matrix = cv.getRotationMatrix2D(center, angle, 1)
    rotated_image = cv.warpAffine(image, rotation_matrix, (w, h))
    return rotated_image


def scale_image(image, scale_factor):
    scaling_matrix = np.array([[scale_factor, 0, 0], [0, scale_factor, 0]], dtype=np.float32)
    scaled_image = cv.warpAffine(image, scaling_matrix, (int(w * scale_factor), int(h * scale_factor)))
    return scaled_image


def reflect_image(image, axis):
    if axis == "x":
        reflection_matrix = (
            np.array([[1, 0, 0], [0, -1, h]], dtype=np.float32))
    elif axis == "y":
        reflection_matrix = np.array([[-1, 0, w], [0, 1, 0]], dtype=np.float32)
    reflected_image = cv.warpAffine(image, reflection_matrix, (w, h))
    return reflected_image


def shear_image(image, shear_factor, axis):
    if axis == "x":
        shearing_matrix = np.array([[1, shear_factor, 0], [0, 1, 0]], dtype=np.float32)
    elif axis == "y":
        shearing_matrix = np.array([[1, 0, 0], [shear_factor, 1, 0]], dtype=np.float32)
    sheared_image = cv.warpAffine(image, shearing_matrix, (w, h))
    return sheared_image

# ----------------------------------------------------------------------------------------------------------------------


rotated_image = rotate_image(image, 45)
scaled_image = scale_image(image, 1.5)
reflected_image_x = reflect_image(image, "x")
reflected_image_y = reflect_image(image, "y")
sheared_image_x = shear_image(image, 0.5, "x")
sheared_image_y = shear_image(image, 0.5,  "y")

display_and_close("Original image", image)
display_and_close('Rotated Image', rotated_image)
display_and_close('Scaled Image', scaled_image)
display_and_close('Reflected Image (relative to x-axis)', reflected_image_x)
display_and_close('Reflected Image (relative to y-axis)', reflected_image_y)
display_and_close('Sheared Image (relative to x-axis)', sheared_image_x)
display_and_close('Sheared Image (relative to y-axis)', sheared_image_y)

