"""
Demonstrates a greedy algorithm for making change with a known set of coin
denominations (e.g., US currency: quarters=25, dimes=10, nickels=5, pennies=1).
"""
def coin_change_greedy(amount, denominations):
    """
    Return a list of coins that sum to 'amount' using a greedy approach.
    Assumes denominations is a sorted list (descending order).
    Parameters:
    -----------
    amount : int
    The total amount of change to make.
    denominations : list of ints
    Coin denominations, e.g., [25, 10, 5, 1] for quarters, dimes, nickels, pennies.
    Returns:
    --------
    list of ints
    The coins that sum to 'amount'. If the greedy approach fails to make exact change,
    the result might be suboptimal or incomplete in non-standard cases.
    """
    result = []
    remaining = amount
    for coin in denominations:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    # If 'remaining' is not zero, the greedy approach couldn't form exact change
    return result
    
def main():
# Example with US coin denominations
    denominations = [25, 10, 5, 1] # sorted descending
    amount = 87 # e.g., 87 cents
    coins_used = coin_change_greedy(amount, denominations)
    print(f"Making change for {amount} cents with denominations {denominations}:")
    print(f"Coins used: {coins_used} (total = {sum(coins_used)})")
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    