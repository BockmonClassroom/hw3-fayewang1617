# Name: Faye(Lifei) Wang
# Date: 02/06/2025

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


cleaned_data = pd.read_csv("/Users/faye/Documents/hw-5110/hw3-fayewang1617/cleaned_data.csv")

plt.figure(figsize=(10, 6))  # Set the figure size
sns.boxplot(x='variant_number', y='total_active_mins', data=cleaned_data)  # Box plot for active minutes by group
plt.title('Box Plot of Active Minutes by Group') 
plt.xlabel('Group (0=Control, 1=Treatment)') 
plt.ylabel('Active Minutes')  
plt.show()  