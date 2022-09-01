import pandas as pd

netflixDataFrame = pd.read_csv("netflix_titles.csv")
result = netflixDataFrame.head()
result = netflixDataFrame.columns

result = netflixDataFrame.dropna(axis = 1)
result = netflixDataFrame.fillna(value="-",inplace=True)
result = netflixDataFrame.info()
print(result)