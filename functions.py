# def is_power_greater_than_5000(base, exponent):
#     # Calculate the result of base raised to the power of exponent
#     result = base ** exponent
    
#     # Check if the result is greater than 5000
#     if result > 5000:
#         return True
#     else:
#         return False


def is_power_greater_than_5000(base, exponent):
 
    # Calculate the result of base raised to the power of exponent
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

def main():
    # Prompt the user to enter the base and exponent
    base_input = input("Enter the base number: ")
    exponent_input = input("Enter the exponent: ")
    
    try:
        # Convert the inputs to integers
        base = int(base_input)
        exponent = int(exponent_input)
        
        # Call the function with user inputs and print the result
        result = is_power_greater_than_5000(base, exponent)
        print("Result:", result)
    
    except ValueError:
        print("Please enter valid integer values for base and exponent.")

# Execute the main function
if __name__ == "__main__":
    main()
