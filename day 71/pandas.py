import pandas as pd
df = pd.read_csv("salaries_by_college_major.csv")

clean_df = df.dropna()
clean_df.columns

max_mid_carrer_10th = clean_df['Mid-Career Median Salary'].idxmax()
clean_df.loc[max_mid_carrer_10th]

min_start_carrer = clean_df['Starting Median Salary'].idxmin()
clean_df.loc[min_start_carrer]

mid_carrer = clean_df['Mid-Career Median Salary'].idxmin()
clean_df.loc[mid_carrer]

spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, "Spread", spread_col)
clean_df.head()