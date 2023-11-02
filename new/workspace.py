import pandas as pd

# df = pd.read_csv('/Users/franco/Documents/GitHub/harmonia/full.csv')
# df.to_csv('1df.csv')
df1 = pd.read_csv('1df.csv')
df2 = pd.read_csv('2df.csv')
df3 = pd.read_csv('3df.csv')
df4 = pd.read_csv('4df.csv')
df5 = pd.read_csv('5df.csv')

df = pd.concat([df1, df2, df3, df4, df5], axis = 0)
df = df.drop_duplicates()
df.to_csv('full.csv')


# 1df: with juan's keys i first got <2000 from SOL
# 2df: with juan's keys i got <2000 from PLAZA DE CASTILLA
# 3df: with my keys i got <2500 from ATOCHA
# 4df: with my keys i got 25 from SAINZ DE BARANDA
# 5df: with juan's keys i got 200 from GREGORIO MARAÑON