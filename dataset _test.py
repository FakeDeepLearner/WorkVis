import pandas
df1 = pandas.read_csv("during_the_pandemic.csv")
df1.dropna(inplace= True)
print(df1.to_string(index=False))
print(df1.loc[3:7,"Industry/Month":"20-Jun"].to_string(index=False))   #Unless loc(), the values must be INTEGERS when using iloc())