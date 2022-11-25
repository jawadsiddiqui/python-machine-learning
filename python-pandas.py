import pandas as pd

dftrain = pd.read_csv("/users/jsiddiqui/Documents/survey-2021.csv")

print(dftrain.head())


y_train = dftrain.pop('servived')
print(dftrain.head())

print(dftrain.loc[0])