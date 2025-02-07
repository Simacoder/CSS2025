# CHPC Summer School 2025
# Probability & Statistics: Categorical Data & Probability
# On your own (exercise): Titanic

# Import packages and functions

import numpy as np
from scipy.stats import chi2_contingency

# Give the contingency table with observed counts			

ctTitanic = np.array([[122, 203], [167, 118], [528, 178], [673, 212]])

# Do the test for independence

chi2_contingency(ctTitanic)