import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
data = pd.read_csv('BikePedCrash.csv')
sns.set(rc={'figure.figsize':(20, 5)})
st.title("Ped-Bike Crash Analysis: Potential Trends")
selected_var = st.sidebar.selectbox("Select the Variable:", ["Locality", "BikeAgeGrp", "LightCond"])
filtered_data = data[selected_var]
st.subheader('Histogram')
sns.histplot(filtered_data, kde=True) 
plt.xlabel(selected_var)
plt.ylabel("Frequency")
st.pyplot()
