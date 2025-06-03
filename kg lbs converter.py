print()
weight = float(input("Enter the amount in kilograms that you'd like to convert to pounds: "))
pounds = weight * 2.20462
print()
print(f"{weight} kg is equal to {pounds:.2f} lbs." , "\n")
new_weight = float(input("Enter the amount in pounds that you'd like to convert to kilograms: "))
kilograms = new_weight / 2.20462
print()
print(f"{new_weight} lbs is equal to {kilograms:.2f} kg" , "\n")
#Empty print() lines added for visual clarity.
#Perhaps second_weight would be a better name that new_weight?