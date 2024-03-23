import pandas as pd

df = pd.read_csv('salaries_by_college_major.csv')
wiped_df = df.dropna().tail()

max_salary_idx = wiped_df['Starting Median Salary'].idxmax()
min_salary_idx = wiped_df['Starting Median Salary'].idxmin()
highest_paid = wiped_df['Undergraduate Major'][max_salary_idx]
lowest_paid = wiped_df['Undergraduate Major'][min_salary_idx]

print(wiped_df.loc[min_salary_idx])

print(
    f'The Lowest paid Graduation is {wiped_df["Undergraduate Major"][min_salary_idx]} with a salary '
    f'{wiped_df["Starting Median Salary"][min_salary_idx]}$.\n90% who gain 10+ years of experience'
    f'will get '
    f'{wiped_df["Mid-Career 90th Percentile Salary"][min_salary_idx]}$ per year.\n10% people with 10+y.e. earn '
    f'{wiped_df["Mid-Career 10th Percentile Salary"][min_salary_idx]}$ \n\n')
print(
    f'The Highest paid Graduation is {wiped_df["Undergraduate Major"][max_salary_idx]} with a salary '
    f'{wiped_df["Starting Median Salary"][max_salary_idx]}$.\n90% who gain 10+ years of experience'
    f'will get '
    f'{wiped_df["Mid-Career 90th Percentile Salary"][max_salary_idx]}$ per year.\n10% people with 10+y.e. earn '
    f'{wiped_df["Mid-Career 10th Percentile Salary"][max_salary_idx]}$ ')
