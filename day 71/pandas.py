import pandas as pd
df = pd.read_csv("salaries_by_college_major.csv")

clean_df = df.dropna()
clean_df.columns