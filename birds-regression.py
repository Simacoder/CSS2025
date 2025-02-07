# Import packages
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression

import os
os.chdir(r"C:\CSS2025")

#%%
# Import the data
animals = pd.read_csv('super-animals.csv')

#%%
# Create a data set that only contains the birds (subset)
birds = animals.loc[animals["Species"] == "Bird", :]

#%%
# Draw a scatterplot of the size vs the weight of the birds
sns.scatterplot(data = birds, x = "Size", y = "Weight")

#%%
# Do a log transformation on the size and the weight of the birds
birds_log_size = np.log(birds["Size"])
birds_log_weight = np.log(birds["Weight"])

# Draw a scatterplot
sns.scatterplot(x = birds_log_size, y = birds_log_weight)

#%%
# Correlation and regression analysis
y = np.array(birds_log_weight)
x = np.array(birds_log_size)
np.corrcoef(x, y)
x = x.reshape((-1, 1))
lrm = LinearRegression().fit(x, y)
lrm.intercept_
lrm.coef_
y_pred = lrm.predict(x)
e = y - y_pred
r_sq = lrm.score(x, y)