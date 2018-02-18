import pandas as pd

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col = 0)
print(data.head())

print(data.tail())

print(data.shape)

import seaborn as sns


print(sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales'))
