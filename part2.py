# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd
t1 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/data/t1_user_active_min.csv")
t2 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/data/t2_user_variant.csv")
merged_data = t1.merge(t2[['uid', 'variant_number']], on='uid')

# Add up the total miniutes per user
total_merged_data = merged_data.groupby(['uid', 'variant_number'], as_index=False)['active_mins'].sum()

# Rename the column to be 'total_active_mins'
total_merged_data.rename(columns={'active_mins': 'total_active_mins'}, inplace=True)

total_merged_data.to_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/total_merged_data.csv", index=False)
