"""
fibonacci.py
Computes the n-th Fibonacci number using an iterative approach.
Usage:
"""
def fibonacci(n):
    """
    Return the n-th Fibonacci number using an iterative approach.
    Parameters:
    -----------
    n : int
    The index of the Fibonacci sequence to compute.
    Returns:
    --------
    int
    The n-th Fibonacci number.
    """
    if n < 2:
        return n
    f_minus_two, f_minus_one = 0, 1
    for _ in range(2, n+1):
        current = f_minus_one + f_minus_two
        f_minus_two, f_minus_one = f_minus_one, current
    return f_minus_one
def main():
# Demonstrate first 5 Fibonacci numbers
    for i in range(20):
        print(f"F({i}) = {fibonacci(i)}")
if __name__ == "__main__":
    main()