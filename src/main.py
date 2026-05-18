def calculate_bmi(weight_kg, height_m):
	if height_m <= 0:
		raise ValueError("height_m must be greater than 0")

	return weight_kg / (height_m * height_m)


def bmi_category(bmi):
	if bmi < 18.5:
		return "Underweight"
	if bmi < 25:
		return "Normal weight"
	if bmi < 30:
		return "Overweight"
	return "Obesity"


def main():
	weight_kg = float(input("Enter weight in kilograms: "))
	height_m = float(input("Enter height in meters: "))

	bmi = calculate_bmi(weight_kg, height_m)
	print(f"BMI: {bmi:.2f}")
	print(f"Category: {bmi_category(bmi)}")


if __name__ == "__main__":
	main()

