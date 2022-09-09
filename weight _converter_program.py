weight = int(input("enter your weight: "))
unit = input("enter (L) for pounds or (K) for kilogram: ")
if unit.upper()=="L":
    converted = weight*0.45
    print(f"you are {converted}kg")
else:
    converted = weight//0.45
    print(f"you are {converted}lbs")

