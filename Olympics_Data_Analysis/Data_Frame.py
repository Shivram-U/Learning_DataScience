import pandas as pd

DataFrame = pd.read_csv('C:\\OneDrive\\Software\\Work_Spaces\\System_WorkSpace\\CODE\\A2.Programming_Languages\\Python\\Data_Science\\Data_Frame and Analysis\\train-100.csv')

#print(DataFrame)
#print("Statistical Parameters")
#print("Mean: ",DataFrame.Height.mean())
#print("Mode: ",DataFrame.Height.mode())
#print("Median: ",DataFrame.Height.median())
#print("Variance: ",DataFrame.Height.median())
#print("Standard Deviation: ",DataFrame.Height.median())
Mean = DataFrame.Height.mean()
Mode = DataFrame.Height.mode()
Median = DataFrame.Height.median()
Stddev = DataFrame.Height.std()
Variance = DataFrame.Height.var()
S=Mean-5*Stddev
B=Mean+5*Stddev
print(DataFrame)
print(S,B)
print(DataFrame[DataFrame.Height>B])
print(DataFrame[DataFrame.Height<S])

s = DataFrame[(DataFrame.Height>60) & (DataFrame.Height<65)]
#print(s)
print(s.shape)
print()