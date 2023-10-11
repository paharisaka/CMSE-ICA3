import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
Phase1 = pd.read_excel('Formatted Wide I69SB.xlsx', sheet_name = 'Phase1')
Phase2 = pd.read_excel('Formatted Wide I69SB.xlsx', sheet_name = 'Phase2')
Phase1_data = Phase1.drop('SL', axis = 1) 
Phase2_data = Phase2.drop('SL', axis = 1)
plt.figure(figsize=(24, 8))
sns.lineplot(data=Phase1_data.mean(), color='red', label='Phase 1- SFT Active (n=89)')
sns.lineplot(data=Phase2_data.mean(), color='green', label='Phase2- SFT Inactive (n=85)')
plt.ylim(56, 64)
plt.xlabel('Distance from the first LiDAR')
plt.ylabel('Speeds')
plt.title('Average Speed Profile')
st.pyplot(plt)
