import pandas as pd

df1 = pd.read_csv('new/df.csv')
df2 = pd.read_csv('new/df_2.csv')
df3 = pd.read_csv('new/df_3.csv')


full_df = pd.concat([df1, df2, df3], axis = 0)
full_df = full_df.drop_duplicates()
# print(full_df)
full_df.to_csv('full.csv')