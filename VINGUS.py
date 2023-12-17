
#------------------------------------------------------------------------
#-------------------------------------------------------------------------------

Q1
def sum_of_squares_if_odd(num1, num2):
    if num1 % 2 == 1 and num2 % 2 == 1:
        sum_of_squares = num1**2 + num2**2
        print(f"The sum of squares of {num1} and {num2} is: {sum_of_squares}")
    else:
        print("Calculation not performed. Both numbers should be odd.")

# Get user input for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Call the function with user input
sum_of_squares_if_odd(num1, num2)




Q2


def calculate_factorial(number):
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return
    elif number == 0:
        print("The factorial of 0 is 1")
        return

    factorial = 1
    i = 1

    while i <= number:
        factorial *= i
        i += 1

    print(f"The factorial of {number} is: {factorial}")

# Get user input for the number
num = int(input("Enter a number to find its factorial: "))

# Call the function with user input
calculate_factorial(num)






Q4


def restaurant_bill_calculator():
    try:
        # Get user input
        num_people = int(input("Enter the number of people: "))
        cost_per_meal = float(input("Enter the cost of each meal: $"))
        sales_tax_percentage = float(input("Enter the sales tax percentage: "))
        tip_percentage = float(input("Enter the tip percentage: "))

        # Calculate total cost of food
        total_food_cost = num_people * cost_per_meal

        # Calculate total sales tax
        total_sales_tax = (sales_tax_percentage / 100) * total_food_cost

        # Calculate total tip amount
        total_tip_amount = (tip_percentage / 100) * total_food_cost

        # Calculate total bill amount
        total_bill_amount = total_food_cost + total_sales_tax + total_tip_amount
        # Calculate total bill amount per person
        bill_per_person = total_bill_amount / num_people

        # Display the results
        print("\nSummary:")
        print(f"Total Cost of Food: ${total_food_cost:.2f}")
        print(f"Total Sales Tax: ${total_sales_tax:.2f}")
        print(f"Total Tip Amount: ${total_tip_amount:.2f}")
        print(f"Total Bill Amount: ${total_bill_amount:.2f}")
        print(f"Bill Amount Per Person: ${bill_per_person:.2f}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Call the function to calculate the restaurant bill

