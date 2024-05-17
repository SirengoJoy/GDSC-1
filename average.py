#write a program that tells the user to enter three numbers, 
#sums the numbers and calculates the average.

#num1 = input("Please enter the first number: ")
#num2 = input("Please enter the second number: ")
#num3 = input("Please enter the last number: ")
#print("Given numbers are:", num1,num2,num3)

def calc_average(num1, num2, num3):
    sum = num1 + num2+ num3
    average = sum/3
    return average

def main():
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    num3 = float(input("Please enter the third number: "))

    average = calc_average(num1, num2, num3)
    print("The average of the given numbers is:", average )
main()    
    
    




#total = (num1+num2+num3)
#avg = (num1+num2+num3)/3
#print("The sum of the given numbers is:", total)

#print("The average is:", avg)
