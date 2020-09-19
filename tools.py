import pandas as pd

excel_file = 'example.xlsx'
df = pd.read_excel(excel_file)

"""
cleaning data
"""
for column in df.columns :
    df[column] = df[column].str.replace(r'\W', "")
    # w in lowercase will remote all the letters and numbers, in capital case will remote the specials characters

df.to_excel("removed_characters.xlsx")
print(df)


