# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd
from scipy.stats import mannwhitneyu

cleaned_data2 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/cleaned_data2.csv")

group_1 = cleaned_data2[cleaned_data2['variant_number'] == 0]  # 0 for control
group_2 = cleaned_data2[cleaned_data2['variant_number'] == 1]  # 1 for treatment

mean_group_1 = group_1['active_mins_diff'].mean()
median_group_1 = group_1['active_mins_diff'].median()

mean_group_2 = group_2['active_mins_diff'].mean()
median_group_2 = group_2['active_mins_diff'].median()

print("Group 1 (Control):")
print(f"Mean Change: {mean_group_1}, Median Change: {median_group_1}")

print("Group 2 (Treatment):")
print(f"Mean Change: {mean_group_2}, Median Change: {median_group_2}")

u_stat, p_val_u = mannwhitneyu(group_1['active_mins_diff'], group_2['active_mins_diff'], alternative='two-sided')
print(f"Mann-Whitney U-test: U-statistic = {u_stat}, p-value = {p_val_u}")
