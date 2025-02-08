# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cleaned_data2 = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/cleaned_data2.csv")

plt.figure(figsize=(10, 6))  # Set the figure size
sns.boxplot(x='variant_number', y='active_mins_diff', data=cleaned_data2)  # Box plot for change in active minutes
plt.title('Box Plot of Active Minutes Difference by Group')  
plt.xlabel('Group (0=Control, 1=Treatment)')  
plt.ylabel('Change in Active Minutes (Post - Pre)')  
plt.show()
