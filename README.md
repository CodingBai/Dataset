# Student Competency Data Generation

This code generates synthetic multidimensional competency data for 200 students, primarily designed for research in team formation scenarios.

## Features

The tool simulates the following student capabilities (all normalized to the range [0, 1]):

- **Academic ability** (`academic`)
- **Programming ability** (`programming`)
- **Paper writing ability** (`writing`)
- **Mathematical ability** (`math`)
- **English proficiency** (`english`)

- **Communication skills** (`communication`)
- **Leadership ability** (`leadership`)
- **Cooperation skills** (`cooperation`)
- **Confidence** (`confidence`)

- **Personality** (`personality`) – 5-dimensional vector  
- **Learning styles** (`learning_style`) – 4-dimensional vector  

## Characteristics

- Uses realistic statistical distributions (e.g., normal and Beta distributions) to model student abilities.
- Introduces meaningful correlations between related competencies (e.g., programming and academic ability).
- All values are bounded within [0, 1], with higher values indicating stronger capabilities.
- Calibrated so that approximately 80% of students have `leadership ≥ 0.4`.
- Precision: 9 decimal places

## Usage

Run the script from the command line:

```bash
python generate_data.py
```
## Note
- The generated data is based on predefined statistical distributions; parameters can be adjusted according to specific requirements.
- Output data files will overwrite existing files with the same name.
- Ensure that the ../data directory exists in your project structure or that you have appropriate write permissions.
