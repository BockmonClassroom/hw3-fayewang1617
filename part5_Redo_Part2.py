# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd
t1 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/data/t1_user_active_min.csv")
t2 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/data/t2_user_variant.csv")
t3 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/data/t3_user_active_min_pre.csv")

merged_data = t1.merge(t2[['uid', 'variant_number']], on='uid')

# Add up the total miniutes per user
total_merged_data = merged_data.groupby(['uid', 'variant_number'], as_index=False)['active_mins'].sum()

# Rename the column to be 'total_active_mins'
total_merged_data.rename(columns={'active_mins': 'total_active_mins'}, inplace=True)


# Compute total pre-update active minutes per user
t3_agg = t3.groupby('uid', as_index=False)['active_mins'].sum()
t3_agg.rename(columns={'active_mins': 'active_mins_pre'}, inplace=True)

# Merge with pre-update data
final_data = total_merged_data.merge(t3_agg, on='uid', how='left')

# Fill NaN values in active_mins_pre with 0 (in case some users had no pre-update activity recorded)
final_data['active_mins_pre'] = final_data['active_mins_pre'].fillna(0)

# Compute active minutes difference (Post - Pre)
final_data['active_mins_diff'] = final_data['total_active_mins'] - final_data['active_mins_pre']

# Save the final dataset
final_data.to_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/updated_total_merged_data.csv", index=False)
