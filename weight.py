#this is a weight converter program
#converts weight from kilograms to pounds

def Kilograms_to_pounds(weight):
    new_weight = weight * 2.2
    return new_weight

weight = float(input("Enter your weight in kilograms: "))
weight_in_pounds = Kilograms_to_pounds(weight)
print(f"Your weight in pounds is: {weight_in_pounds} lbs")