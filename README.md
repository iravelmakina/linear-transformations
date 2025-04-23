# Linear Transformation Program

This repository contains a modular Python program for performing and visualizing linear transformations in both 2D and 3D spaces, including transformation of objects and images using both custom NumPy logic and OpenCV utilities.

---

## Project Overview

This project is divided into two parts:

### Part One: Manual Linear Transformations with NumPy

A matrix-based approach using NumPy and Matplotlib to apply transformations to 2D and 3D objects.

#### Features
- Object Visualization
  - Predefined 2D and 3D shapes (e.g., hare, swallow, custom shape)
  - Visualization using Matplotlib for clear transformation output
- Transformations Supported
  - Rotation
  - Scaling
  - Reflection
  - Shearing
  - Custom transformation matrices
- 3D Support
  - All transformations extended to 3D with visual feedback
- Educational Focus
  - Useful for exploring how matrix elements affect spatial transformations

---

### Part Two: Image & Object Transformations with OpenCV

Using OpenCV to perform fast and visually intuitive transformations on both object coordinates and images.

#### Features
- OpenCV Integration
  - Uses `cv.getRotationMatrix2D` and `cv.warpAffine` for image and point transformations
- Image Transformation Pipeline
  - Load sample image (e.g., `assets/brain.jpg`)
  - Apply transformations (rotate, scale, reflect, shear)
  - Display modified images using Matplotlib
- Object Transformation (OpenCV-based)
  - Coordinate transformation using homogeneous matrix operations

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/iravelmakina/linear-transformations.git
cd linear-transformations
```

### 2. Set up a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install numpy matplotlib opencv-python
```

---

## Project Structure

```
linear-transformations/
├── src/
│   ├── main.py
│   ├── objects.py
│   ├── parser/
│   │   ├── parser.py
│   │   └── parser_validation.py
│   ├── transformations/
│   │   ├── manual_matrix_transformations.py
│   │   ├── cv_matrix_transformations.py
│   │   ├── cv_image_transformations.py
│   │   └── transformations_validation_visualization.py
├── assets/
│   └── brain.jpg
├── requirements.txt
├── .gitattributes
├── .gitignore
└── README.md
```

---

## Usage

Run the program from the project root:

```bash
python src/main.py
```

Follow the terminal prompts to:
- Select between manual and OpenCV transformation modes
- Choose between object or image processing
- Apply transformations and view the results

---

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- OpenCV (`opencv-python`)

---

## Contributors

- [@iravelmakina](https://github.com/iravelmakina)

---

## License

This project is open-source under the **MIT License**.
