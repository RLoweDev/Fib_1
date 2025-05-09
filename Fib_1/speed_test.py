from fib import fib as fib_recursive
from fib_2 import fib as fib_binet
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Function to measure execution time of a function
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return end_time - start_time, result

# Function to generate random test cases
def generate_test_cases(num_cases, max_value):
    return [random.randint(1, max_value) for _ in range(num_cases)]

# Function to plot execution times
def plot_execution_times(n_values, times_recursive, times_binet):
    plt.figure(figsize=(10, 5))
    plt.plot(n_values, times_recursive, label='Recursive Fibonacci', marker='o')
    plt.plot(n_values, times_binet, label='Binet\'s Formula', marker='o')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Execution Time Comparison of Fibonacci Implementations')
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to save results to a CSV file
def save_results_to_csv(n_values, times_recursive, times_binet, filename='results.csv'):
    df = pd.DataFrame({
        'Input Size (n)': n_values,
        'Recursive Time (s)': times_recursive,
        'Binet Time (s)': times_binet
    })
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

# Main function to run the speed test
def run_speed_test(num_cases=10, max_value=30):
    n_values = generate_test_cases(num_cases, max_value)
    times_recursive = []
    times_binet = []

    for n in n_values:
        time_recursive, _ = measure_time(fib_recursive, n)
        time_binet, _ = measure_time(fib_binet, n)
        times_recursive.append(time_recursive)
        times_binet.append(time_binet)


    plot_execution_times(n_values, times_recursive, times_binet)
    save_results_to_csv(n_values, times_recursive, times_binet)

if __name__ == "__main__":
    run_speed_test()
# This script compares the execution time of two Fibonacci implementations:
# a recursive implementation and an implementation using Binet's formula.
# It generates random test cases, measures the execution time for each implementation,
