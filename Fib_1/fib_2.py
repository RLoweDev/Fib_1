from math import sqrt

phi = (1 + sqrt(5)) / 2

def fib(input):
    output = round((phi ** input - (1 - phi) ** input) / sqrt(5))
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
# # This code calculates the Fibonacci number for a given input using Binet's formula.
# # It uses the golden ratio to compute Fibonacci numbers in constant time.
if __name__ == "__main__":
    main()