def fib(input):
    if input == 1 or input == 2:
        output = 1
    else:
        output = fib(input - 1) + fib(input - 2)
    return output

def main():
    while True:
        try:
            user_input = int(input("Enter a number (1 or greater): "))
            if user_input < 1:
                raise ValueError("Input must be a positive integer.")
            print(f"The Fibonacci number for {user_input} is {fib(user_input)}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")
        if input("Press Enter to continue or type 'exit' to quit: ") == 'exit':
            break
    print("Exiting the program.")
# # This code calculates the Fibonacci number for a given input using recursion.
# # It uses a simple recursive function to compute Fibonacci numbers.
# # This is less efficient than Binet's formula for large inputs due to its exponential time complexity.
if __name__ == "__main__":
    main()