"""
Computes Fibonacci numbers using memoization (top-down DP).
"""
def fib_memo(n, cache=None):
    """
    Return the n-th Fibonacci number using a memoized (top-down) DP approach.
    Parameters:
    -----------
    n : int
    The Fibonacci index to compute (F_0=0, F_1=1).
    cache : dict or None
    A dictionary mapping int -> int to store previously computed Fib values.
    Returns:
    --------
    int
    The n-th Fibonacci number.
    """
    if cache is None:
        cache = {}

    if n < 2:
        return n
    if n in cache:
        return cache[n]
    # Compute and store in cache
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    return cache[n]

def main():
    tests = [0, 1, 5, 10, 20, 30]
    for t in tests:
        print(f"Fib({t}) = {fib_memo(t)}")
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    
    
    