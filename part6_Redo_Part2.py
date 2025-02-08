# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd
t1 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/data/t1_user_active_min.csv")
t2 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/data/t2_user_variant.csv")
t4 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/data/t4_user_attributes.csv")

merged_data = t1.merge(t2[['uid', 'variant_number']], on='uid')

# Add up the total miniutes per user
total_merged_data = merged_data.groupby(['uid', 'variant_number'], as_index=False)['active_mins'].sum()

# Rename the column to be 'total_active_mins'
total_merged_data.rename(columns={'active_mins': 'total_active_mins'}, inplace=True)


t4_agg = t4.groupby('uid', as_index=False)['gender'].sum()
t4_agg.rename(columns={'active_mins': 'total_active_mins'}, inplace=True)

# Merge with pre-update data
final_data = total_merged_data.merge(t4_agg, on='uid', how='left')

# Save the final dataset
final_data.to_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/merged_data_with_gender.csv", index=False)
