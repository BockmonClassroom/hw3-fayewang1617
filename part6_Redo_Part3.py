# Name: Faye(Lifei) Wang
# Date: 02/07/2025

import pandas as pd
from scipy.stats import mannwhitneyu

cleaned_data3 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/cleaned_data3.csv")

group_male = cleaned_data3[cleaned_data3['gender'] == 'male']
group_female = cleaned_data3[cleaned_data3['gender'] == 'female']

mean_group_male = group_male['total_active_mins'].mean()
median_group_male = group_male['total_active_mins'].median()

mean_group_female = group_female['total_active_mins'].mean()
median_group_female = group_female['total_active_mins'].median()

print("Group Male:")
print(f"Mean Total Active Minutes: {mean_group_male}, Median Total Active Minutes: {median_group_male}")

print("Group Female:")
print(f"Mean Total Active Minutes: {mean_group_female}, Median Total Active Minutes: {median_group_female}")

u_stat, p_val_u = mannwhitneyu(group_male['total_active_mins'], group_female['total_active_mins'], alternative='two-sided')
print(f"Mann-Whitney U-test: U-statistic = {u_stat}, p-value = {p_val_u}")
