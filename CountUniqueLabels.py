import pandas as pd
import math
df = pd.read_csv(r'C:\Users\Krasser Ficker 2.0\Documents\Code\Bachelor\DataPreparation\Dataset\fake.csv')

print("Number of Labels: " + str(df.iloc[:,19].nunique()))
print("The labels are: " + str(df.iloc[:,19].unique()))