# %%

# Example 2
# Write a Python class or set of functions that:
# Computes the ECDF 
# Has a method to compute any quantile without using Numpy
# Has a method to compute the Interquartile Range (IQR) -- the .25 quantile and the .75 quantile, which brackets 50% of the data -- and the whiskers: from the edges of the IQR
# Has a method to compute a five-number summary/boxplot: the whiskers, the minimum and maximum, the IQR and the median
# Compare your answers with sns.boxplot; making a boxplot yourself is kind of a pain, but you could make a 5-number summary visualization
# Anything outside the whiskers is an outlier; write a method that returns a Boolean vector indicating if the observations are outliers`


import math
import statistics
import numpy as np 
import pandas as pd 
import seaborn as sns


data = []
class Uncertainstats:
    # quantile 
    def percentile(self, x, percentile):
        n = len(x)
        idx = n * percentile / 100
        return sorted(x)[math.floor(idx)]
    
    #IQR
    def iqr(self, x):
        q1 = self.percentile(x, 25)
        q3 = self.percentile(x, 75)
        return {"q1": q1, "q3": q3, "iqr": q3 - q1}
    
    def whiskers(self, x):
        stat = self.iqr(x)
        lower = stat['q1'] - 1.5 * stat['iqr']
        upper = stat['q3'] + 1.5 * stat['iqr']
        return {'lower': lower, 'upper': upper}
    
    # five-number summary/boxplot
    def summary(self, x):
        return{'min':min(x),'max':max(x), 'median': statistics.median(x), 'whiskers': self.whiskers(x), 'iqr': self.iqr(x)}
    
    # outliers
    def outliers(self, x):
        whiskers_bound = self.whiskers(x)
        return(val < whiskers_bound['lower']) | (x > whiskers_bound['upper'] for val in x)

sns.boxplot(x, orient=h)
    




# %%
