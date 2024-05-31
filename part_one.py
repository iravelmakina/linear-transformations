import matplotlib.pyplot as plt
import numpy as np


class Object:
    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.dimension = points.shape[1]

    def __str__(self):
        return f"{self.dimension}D object '{self.name}' with points:\n{self.points}"

    def visualize(self):
        if self.dimension == 2:
            self._visualize_2d()
        elif self.dimension == 3:
            self._visualize_3d()
        else:
            print("Visualization for such an object is not supported.")

    def _visualize_2d(self):
        x_list = [coordinates[0] for coordinates in self.points]
        y_list = [coordinates[1] for coordinates in self.points]
        plt.plot(x_list, y_list)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'2D Object: {self.name}')
        plt.show()

    def _visualize_3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x_list = [coordinates[0] for coordinates in self.points]
        y_list = [coordinates[1] for coordinates in self.points]
        z_list = [coordinates[2] for coordinates in self.points]
        ax.plot(x_list, y_list, z_list)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title(f'3D Object: {self.name}')
        plt.show()


class Transformer:
    @staticmethod
    def rotate(object):
        angle_in_degrees = ask_and_validate_coefficient("angle")
        angle_in_radians = angle_in_degrees * np.pi / 180

        if object.dimension == 2:
            rotation_matrix = np.array([[np.cos(angle_in_radians), -np.sin(angle_in_radians)],
                                        [np.sin(angle_in_radians), np.cos(angle_in_radians)]])
        elif object.dimension == 3:
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
        else:
            print("Rotation for such an object is not supported.")
            return

        object.points = np.dot(object.points, rotation_matrix.T)
        print_matrix(object.points, "Rotated")
        object.visualize()

    @staticmethod
    def scale(object):
        scale_factor = ask_and_validate_coefficient("scale factor")
        scaled_object = scale_factor * object.points
        print_matrix(scaled_object, "Scaled")
        object.points = scaled_object
        object.visualize()

    @staticmethod
    def reflect(object):
        if object.dimension == 2:
            axis = ask_and_validate_axis("reflect")
            if axis == "x":
                transformation_matrix = np.array([[1, 0], [0, -1]])
            else:
                transformation_matrix = np.array([[-1, 0], [0, 1]])
        elif object.dimension == 3:
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
        reflected_object = np.dot(object.points, transformation_matrix.T)
        print_matrix(reflected_object, f"Reflected relative to {axis}-axis")
        object.points = reflected_object
        object.visualize()

    @staticmethod
    def shear(object):
        shear_factor = ask_and_validate_coefficient("shear factor")
        if object.dimension == 2:
            axis = ask_and_validate_axis("shear")
            if axis == "x":
                shear_matrix = np.array([[1, shear_factor], [0, 1]])
            else:
                shear_matrix = np.array([[1, 0], [shear_factor, 1]])
        elif object.dimension == 3:
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
        sheared_object = np.dot(object.points, shear_matrix.T)
        print_matrix(sheared_object, f"Sheared relative to {axis}-axis")
        object.points = sheared_object
        object.visualize()

    @staticmethod
    def transform(object):
        if object.dimension == 2:
            custom_matrix = ask_and_validate_matrix("n * 2", 2)
        elif object.dimension == 3:
            custom_matrix = ask_and_validate_matrix("n * 3", 3)
        else:
            print("Transformation for such an object is not supported.")
            return
        transformed_object = np.dot(object.points, custom_matrix.T)
        print_matrix(transformed_object, "Transformed")
        object.points = transformed_object
        object.visualize()


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
    while object_choice not in object_dict:
        print("Invalid input. Please, try again: ")
        object_choice = input(f"Please, choose the object you want to {prompt}: ").lower()
    return object_dict[object_choice]


def print_matrix(matrix, transformation_adjective):
    print(f"{transformation_adjective} matrix: ")
    for row in matrix:
        print(row)


hare = np.array(
    [[5, 1], [6, 2], [6, 3], [5, 6], [4, 7], [5, 8], [6, 8], [8, 9], [9, 9], [7, 8], [9, 8], [6, 7], [7, 6], [9, 6],
     [11, 5], [12, 3], [12, 2], [13, 3], [12, 1], [7, 1], [8, 2], [9, 2], [8, 3], [6, 1], [5, 1]])
hare = Object("hare", hare)

swallow = np.array(
    [[-5, 4], [-7, 4], [-9, 6], [-11, 6], [-12, 5], [-14, 5], [-12, 4], [-14, 3], [-12, 3], [-11, 2], [-10, 2],
     [-9, 1], [-9, 0], [-8, -2], [0, -3], [3, -2], [19, -2], [4, 0], [19, 4], [4, 2], [2, 3], [6, 9], [10, 11],
     [3, 11], [1, 10], [-5, 4]])
swallow = Object("swallow", swallow)

shape = np.array([[0, 0, 0], [1, 2, 1], [2, 3, 1], [3, 3, 0], [2, 2, -1], [1, 0, -1], [0, -1, 0],
                  [-1, -2, 1], [-2, -3, 1], [-3, -3, 0], [-2, -2, -1], [-1, 0, -1], [0, 0, 0]])
shape = Object("bird", shape)