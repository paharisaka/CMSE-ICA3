import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
st.set_option('deprecation.showPyplotGlobalUse', False)
#********************************************************************************************************
st.title("Evaluation of Fatal Pedestrian-Bicyclist (Ped-Bike) Crashes in North Carolina")
#********************************************************************************************************
data = pd.read_csv('BikePedCrash.csv')
st.subheader('Introduction')
st.write('Pedestrians and bicyclists are among the vulnerable road users (along with motorized two-wheelers) who are more likely to get into fatal crashes as compared to car drivers. They are referred to as such because they do not have enough protection through an outside shield, and risk sustaining a greater injury in any collision with a vehicle. This project aims to look at few of the factors that have impacts in causing fatal ped-bike crashes. State agencies and Departments of Transportation (DOTs) can benefit from these type of evaluations in order to minimize fatal crashes and eventually move towards zero deaths caused due to traffic crashes.')
#********************************************************************************************************
st.subheader('Variables in the Dataset')
st.write(' - BikeDir: Direction of travel of bicyclists as compared to direction of travel of traffic.')
st.write(' - CrashAlcoh: Were the vehicle drivers intoxicated from alcohol during the time of crash?')
st.write(' - WeekdayOrWeekend: Day of occurrence of the crash in terms of weekend or weekday.')
st.write(' - CrashLoc: Location of Crash (whether or not the crash occurred in the intersection).')
st.write(' - Developmen: Type of development of the area of crash.')
st.write(' - LightCond: Light Condition at the location of crash.')
st.write(' - Locality: Locality of crash in terms of Urban, Mixed or Rural locality.')
st.write(' - RdSurface: Road Surface Conditions.')
st.write(' - RuralUrban: Road Context in terms of rural or urban roads.')
st.write(' - SpeedLimit: Speed Limit at the location of crash.')
#********************************************************************************************************
st.markdown("### Do you want to see the raw dataset?")
show = st.selectbox("", ["No", "Yes"])
if show == "Yes":
    st.write(data)
#********************************************************************************************************
st.subheader("EDA and Evaluation of Trends")    
#********************************************************************************************************
selected_var = st.radio("Select a Variable", ["CrashAlcoh", "WeekdayOrWeekend", "Locality", "LightCond", "RdSurface","Developmen", "RuralUrban", "SpeedLimit", "CrashLoc", "BikeDir"])
filtered_data = data[selected_var]
sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(16, 6))
sns.histplot(filtered_data, kde=True, color="skyblue", element="bars", fill=True)
plt.xlabel(selected_var, fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.title(f"Histogram and KDE Plot for {selected_var}", fontsize=16)
st.pyplot(fig)
#********************************************************************************************************
st.write('From the histograms, from a traffic safety perspective, we can observe some clear trends for some variables. The variables "SpeedLimit", "CrashLoc", and especially "BikeDir" show some trends that may factor for fatal ped-bike crashes. We now look in to the interactive plots between these three particular variables.')
#********************************************************************************************************
st.subheader("Interactive Plot")
#********************************************************************************************************
fig = px.sunburst(data, path=['BikeDir', 'CrashLoc', 'SpeedLimit'], title='Nested Pie Chart')
st.plotly_chart(fig)
#********************************************************************************************************
