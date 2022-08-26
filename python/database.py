import pandas as pd
import re

df = pd.read_csv('StandardTablesofFood CompositionInJapan.csv')

df['food_name'] = df['food_name'].replace(r"\（[^()]*\）", "")


df.to_csv('calorie.csv', index=False)