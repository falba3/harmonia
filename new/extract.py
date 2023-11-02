from ast import literal_eval # for converting string of list to list
import pandas as pd

with open('info', 'r') as file:
    data = file.readlines()
    data = literal_eval(data[0]) # '[]' string -> list

# print(len(data[0]))
# print(type(data))
# print(len(data))

df = pd.DataFrame(columns = list(data[0].keys()))
for record in data:
    df.loc[len(df)] = record # adding each entry as a row

df.to_csv('df.csv')

# Used to extract the old string!!!
