# Slowness Diagram Generator

This repository contains a Python script that generates slowness diagrams for waves propagating at the interface of two different materials. The script calculates and visualizes wave slowness as a function of direction based on the materials' elastic properties.

## Features
- Computes and plots slowness diagrams for given materials

## Installation
Ensure you have Python installed, then install the required dependencies:

```bash
pip install numpy matplotlib tkinter
```

## Usage
Run the script with your desired material parameters:

```bash
python app.py
```

You can modify the material properties and wave types directly in the script or in the graphical interface with the executable

## Parameters
The script allows customization of:
- **Material properties**: Celerity of the material
- **Plot settings**: Customization of axes, labels, and colors

## Output
The script generates a slowness diagram that visualizes the wave propagation characteristics at the material interface.

## Example
An example output for two isotropic materials with given properties:

```python
# Define material properties
material1 = {
    'vl': 6000,
    'vt': 3200
}
material2 = {
    'vl': 5500,
    'vt': 3000
}
```

The resulting plot shows the slowness curves for the selected wave types.

## License
This project is licensed under the MIT License.

## Contact
For questions or improvements, feel free to open an issue or submit a pull request!
