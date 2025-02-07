"""
Approximates pi using the Leibniz series:
pi = 4 * sum((-1)^k / (2k+1), k=0..infinity)
"""
def approximate_pi(num_terms):
    """
    Approximate pi using the Leibniz series up to 'num_terms'.
    Parameters:
    -----------
    num_terms : int
    Number of terms to include in the approximation.
    Returns:
    --------
    float
    Approximation of pi.
    """
    pi_approx = 0.0
    for k in range(num_terms):
        pi_approx += ((-1)**k) / (2*k + 1)
    pi_approx *= 4
    return pi_approx

def main():
    terms_list = [1, 10, 100, 1000, 10000, 100000]
    for t in terms_list:
        val = approximate_pi(t)
        print(f"Using {t} terms, pi ~ {val:.6f}")

if __name__ == "__main__":
    main()