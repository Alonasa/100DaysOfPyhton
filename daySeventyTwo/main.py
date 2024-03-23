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

wiped_df.insert(1, 'Spread', wiped_df['Mid-Career 90th Percentile Salary'].subtract(wiped_df['Mid-Career 10th '
                                                                                             'Percentile Salary']))
minimal_risk_salary = wiped_df['Spread'].idxmin()
maximal_risk_salary = wiped_df['Spread'].idxmax()
print(f'The minimal risk to become a low paid specialist have a {wiped_df["Undergraduate Major"][minimal_risk_salary]}')
print(f'The maximal risk to become a low paid specialist have a '
      f'{wiped_df["Undergraduate Major"][maximal_risk_salary]}')

sorted_salaries = wiped_df.sort_values('Spread', ascending=False)
salaries_spread_table = sorted_salaries[['Undergraduate Major', 'Spread']]
highest_potential = wiped_df.sort_values('Mid-Career 90th Percentile Salary', ascending=False)
highest_potential_table = highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head()
