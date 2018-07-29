print("How many kilometers did you want to convert?")
kms = input()
miles = float(kms) / 1.609344
miles = round(miles, 2)
print(f"{kms} kilometres is equal to {miles} miles")