# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd
from scipy import stats

data = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/total_merged_data.csv")

group_1 = data[data['variant_number'] == 0]  # Control group
group_2 = data[data['variant_number'] == 1]  # Treatment group

mean_group_1 = group_1['total_active_mins'].mean()
median_group_1 = group_1['total_active_mins'].median()

mean_group_2 = group_2['total_active_mins'].mean()
median_group_2 = group_2['total_active_mins'].median()

u_test = stats.mannwhitneyu(group_1['total_active_mins'], group_2['total_active_mins'], alternative='two-sided')

print("Group 1 (Control) - Mean:", mean_group_1, "Median:", median_group_1)
print("Group 2 (Treatment) - Mean:", mean_group_2, "Median:", median_group_2)
print("Mann-Whitney U Test result:", u_test)
