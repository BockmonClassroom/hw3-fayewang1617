# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd
from scipy.stats import mannwhitneyu

cleaned_data = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/cleaned_data.csv")

group_1 = cleaned_data[cleaned_data['variant_number'] == 0]  # 0 for control
group_2 = cleaned_data[cleaned_data['variant_number'] == 1]  # 1 for treatment

mean_group_1 = group_1['total_active_mins'].mean()
median_group_1 = group_1['total_active_mins'].median()

mean_group_2 = group_2['total_active_mins'].mean()
median_group_2 = group_2['total_active_mins'].median()

print("Group 1 (Control):")
print(f"Mean: {mean_group_1}, Median: {median_group_1}")

print("Group 2 (Treatment):")
print(f"Mean: {mean_group_2}, Median: {median_group_2}")

u_stat, p_val_u = mannwhitneyu(group_1['total_active_mins'], group_2['total_active_mins'], alternative='two-sided')
print(f"Mann-Whitney U-test: U-statistic = {u_stat}, p-value = {p_val_u}")
