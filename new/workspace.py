import pandas as pd

# df = pd.read_csv('/Users/franco/Documents/GitHub/harmonia/full.csv')
# df.to_csv('1df.csv')
df1 = pd.read_csv('1df.csv')
df2 = pd.read_csv('2df.csv')
df3 = pd.read_csv('3df.csv')

df = pd.concat([df1, df2, df3], axis = 0)
df = df.drop_duplicates()
df.to_csv('full.csv')

# 1df.csv = with juan's keys i first got <2000 from SOL
# 2df.csv = with juan's keys i got <2000 from PLAZA DE CASTILLA
# 3df.csv = with my keys i got <2500 from ATOCHA