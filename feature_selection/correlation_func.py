import numpy as np
import scipy
import pandas as pd

"""

This function toolbox contains function that does the single task of:

Measure the correlation between 1 independent column and 1 dependent column.

Different statistical correlation are used for differnent type of data (Categorical, Continuous, Ordinal)

All input are structured as such:

Pandas DataFrame of 2 columns: [independent_col, target_col]

The result are:

p_value or list of p_value, correlation (if applicable)

When applied on the large scale, these function should find useful correlation out of noise columns.

"""

# Chi Squared test are used for categorical vs categorical relationships
def chi_squared(test_df):
    pass

# One way anova is used for continuous vs categorical/ordinal relationships.
def anova(test_df):
    pass

# Logistic Regression is used for categorical vs continuous relationships.
def logistic(test_df):
    pass

# Linear Regression is used for continuous vs continuous relationships.
def linregress(test_df):
    pass

# Spearman Rank is used for ordinal vs ordinal relationships.
def spearman_rank(test_df):
    pass

# Whitney is used for ordinal vs categorical relationships.
def whitney_test(test_df):
    pass