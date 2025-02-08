# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd

data = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/total_merged_data.csv")

while True:
    Q1 = data['total_active_mins'].quantile(0.25)
    Q3 = data['total_active_mins'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    data_cleaned = data[(data['total_active_mins'] >= lower_bound) & (data['total_active_mins'] <= upper_bound)]
    
    if data_cleaned.shape[0] == data.shape[0]: 
        break
    
    data = data_cleaned  
    
data_cleaned.to_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/cleaned_data.csv", index=False)
