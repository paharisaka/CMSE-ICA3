import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title("Ped-Bike Crash Analysis: Potential Trends")

#st.set_option('deprecation.showPyplotGlobalUse', False)
data = pd.read_csv('BikePedCrash.csv')

st.subheader('Introduction')
st.write('This project aims to look at factors that have impacts in causing fatal ped-bike crashes. State agencies and Departments of Transportation (DOTs) can benefit from these type of evaluations in order to minimize fatal crashes and eventually move towards zero deaths caused due to traffic crashes.')
st.markdown("### Do you want to see the dataset?")
show = st.selectbox("", ["No", "Yes"])
if show == "Yes":
    st.write(data)
    
selected_var = st.selectbox("### Select the Variable:", ["Locality", "BikeAgeGrp", "LightCond"])

filtered_data = data[selected_var]
sns.set(rc={'figure.figsize':(20, 5)})
st.subheader('Histogram')
figure1 = sns.histplot(filtered_data, kde=True) 
plt.xlabel(selected_var)
plt.ylabel("Frequency")
st.pyplot(fig = figure1.get_figure())
