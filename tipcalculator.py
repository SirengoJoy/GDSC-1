#a program that asks the user for their tip percentage sums up the tip amount with the actual bill
#and outputs the total amount

def calculate_tip(bill_amt, tip_percentage):
    tip_amt = bill_amt * tip_percentage/100
    return tip_amt

def main():
    bill_amt = float(input("Enter your meal amount: "))
    tip_percentage = int(input("Enter your tip percentage: "))

    tip_amt = calculate_tip(bill_amt, tip_percentage)
    total_amt = bill_amt + tip_amt

    print(f"Your meal was Ksh {bill_amt:.2f} and your tip was Ksh {tip_percentage:.2f}")
    print(f"Your total amount is: Ksh {total_amt:.2f}")
main()
    






