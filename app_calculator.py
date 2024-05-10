# Psuedocode

# Set x as the first inputted number and y as the second inputted number
#Define a function for Addition operation
# Define a function for Subtraction operation
# Define a function for the multiplication operation
# Define a function for the division operation
    # Raise an exception if the user prompted 0 for the second number
# Define a function to get the user's input by choosing an operation for their liking
    # Set Addition as 1
    # Set Subtraction as 2
    # Set Multiplication as 3
    # Set Division as 4
    # Prompt the user to enter their choice between number 1 to 4
    # Convert the input to integer
# Define a function to prompt the user to enter two numbers
    # Convert the user's input into float
    # Return a tuple for the entered numbers
# Define a function that performs the calculation based on the chosen operation
    # Call the chosen operation function
# Define a main function to execute the whole code
    # Display a message that the app has started
    # Enter a while loop until the user decided to exit the app
        # Use the user's choice function to get the chosen operation
        # Check if the operation choice is valid, if not display an error message and loop back to the prompt user again
        # Use the user's input of number function to get the user's entered numbers
        # Calculate the result using the calculate function
        # Display the result
        # Use ValueError exceptions and make the user to try again if there is an error
        # Ask the user if they want to try again
            # If no, display "Thank you!" and exit the program
            # if yes, loop back from the start.

def add(x, y): 
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("You cannot divide by zero.")
    return x / y

def user_operation():
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    return int(input("Enter your chosen operation. Please choose 1 to 4: "))

def user_numbers():
    num1 = float(input("Please enter a first number: "))
    num2 = float(input("Please enter a second number: "))
    return num1, num2

def calculate_numbers(operation, x, y):
    if operation == 1:
        return add(x, y)
    elif operation == 2:
        return subtract(x, y)
    elif operation ==  3: 
        return multiply(x, y)
    elif operation == 4: 
        return divide(x, y)

def run_calculator():
    print("Welcome to the Simple App Calculator!")
    print("This application supports the basic arithmetic operations.")

    while True: 
        try: 
            operation = user_operation()

            if operation < 1 or operation > 4: 
                print("Invalid operation. Please choose again. Thank you.")
                continue

            num1, num2 = user_numbers()