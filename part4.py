# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/total_merged_data.csv")

group_1 = data[data['variant_number'] == 0]  # Control group
group_2 = data[data['variant_number'] == 1]  # Treatment group

# Box plot
plt.figure(figsize=(8, 6))
plt.boxplot(
    [group_1['total_active_mins'], group_2['total_active_mins']],  # Pass the actual values
    labels=['Group 1 (Control)', 'Group 2 (Treatment)'],
    showmeans=True
)
plt.title('Box Plot of Total Active Minutes by Group', fontsize=14)
plt.ylabel('Total Active Minutes', fontsize=12)
plt.xlabel('Groups', fontsize=12)
plt.show()
