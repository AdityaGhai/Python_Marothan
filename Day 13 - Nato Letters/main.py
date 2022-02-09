import pandas as pd

# Reading the csv
df = pd.read_csv("nato_phonetic_alphabet.csv")



#Converting dataframe into dictionary
df_dict = {row.letter:row.code for (index,row) in df.iterrows()}

#Creating a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
result = [df_dict[letter] for letter in word]
print(result)
