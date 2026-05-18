# BMI Calculator App

This is a simple command-line BMI calculator written in Python.

It asks for:

- weight in kilograms
- height in meters

Then it calculates the BMI value and prints the weight category.

## Features

- Calculates BMI using the standard formula: weight / (height * height)
- Shows the BMI value rounded to 2 decimal places
- Displays a category:
	- Underweight
	- Normal weight
	- Overweight
	- Obesity

## Requirements

- Python 3

## Run The App

From the project root, run:

```bash
python src/main.py
```

If you are using the virtual environment in this workspace, run:

```bash
.venv/bin/python src/main.py
```

Example input:

```text
Enter weight in kilograms: 70
Enter height in meters: 1.75
```

Example output:

```text
BMI: 22.86
Category: Normal weight
```

## Run Tests

Run the unit tests with:

```bash
python -m unittest discover -s tests -v
```

Or, if using the virtual environment:

```bash
.venv/bin/python -m unittest discover -s tests -v
```

## Project Structure

```text
README.md
requirements.txt
src/
	main.py
tests/
	test_main.py
```

## Notes

- Height must be greater than 0.
- The app uses metric units for both weight and height.
