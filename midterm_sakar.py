import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
st.set_option('deprecation.showPyplotGlobalUse', False)
#********************************************************************************************************
st.sidebar.title("Content")
#********************************************************************************************************
data = pd.read_csv('BikePedCrash.csv')
option = st.sidebar.radio("Select an option", ["Background and Data", "Data Visualization", "Conclusion and Recommendations"])
if option == "Background and Data":
    st.markdown("# Fatal Pedestrian-Bicyclist (Ped-Bike) Crash Trends")
    st.header('Introduction')
    st.write('Pedestrians and bicyclists are among the vulnerable road users (along with motorized two-wheelers) who are more likely to get into fatal crashes as compared to car drivers. They are referred to as such because they do not have enough protection through an outside shield, and risk sustaining a greater injury in any collision with a vehicle. This project aims to look at few of the factors that have impacts in causing fatal ped-bike crashes. The webapp will help in visualizing the roadway contexts, demographics as well as the effects of various other factors that may have been observed in fatal ped-bike crashes, which may eventually assist in knowing the trends of the causes of ped-bike crashes, and eventually leading steps to avoid roadway mishaps. State agencies and Departments of Transportation (DOTs) can benefit from these type of evaluations in order to minimize fatal crashes and eventually move towards zero deaths caused due to traffic crashes.')
    #********************************************************************************************************
    st.subheader('Dataset')
    st.write('BikePedCrash Data, an open-access public dataset was used in order to work with the graphics that may be related with this project. This dataset contains the information regarding every police-reported ped-bike crashes from the year 2007 to 2019 in the state of North Carolina. All the variables in this dataset are categorical, and are listed below:')
    st.write(' - Bike_Direction: Direction of travel of bicyclists as compared to direction of travel of traffic.')
    st.write(' - Crash_Alcohol_Involved: Were the vehicle drivers intoxicated from alcohol during the time of crash?')
    st.write(' - Weekday_Or_Weekend: Day of occurrence of the crash in terms of weekend or weekday.')
    st.write(' - Crash_Location: Location of Crash (whether or not the crash occurred in the intersection).')
    st.write(' - Development: Type of development of the area of crash.')
    st.write(' - Light_Conditions: Light Condition at the location of crash.')
    st.write(' - Locality: Locality of crash in terms of Urban, Mixed or Rural locality.')
    st.write(' - Road_Surface: Road Surface Conditions.')
    st.write(' - Rural_Or_Urban: Road Context in terms of rural or urban roads.')
    st.write(' - SpeedLimit: Speed Limit at the location of crash.')
    #********************************************************************************************************
    st.markdown("### Do you want to see the raw dataset?")
    show = st.selectbox("", ["No", "Yes"])
    if show == "Yes":
        st.write(data)
#********************************************************************************************************
if option == "Data Visualization":
    st.markdown("# Fatal Pedestrian-Bicyclist (Ped-Bike) Crash Trends")
    st.header("Evaluation of Trends")    
    #********************************************************************************************************
    selected_var = st.radio("Here, we will be looking at the frequency distributions for the variables in the dataset, and come up with some potential trends that may come up. To do so, select a variable from the following:", ["Crash_Alcohol_Involved", "Weekday_Or_Weekend", "Locality", "Light_Conditions", "Road_Surface","Development", "SpeedLimit", "Rural_Or_Urban", "Crash_Location", "Bike_Direction"])
    filtered_data = data[selected_var]
    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(16, 6))
    sns.histplot(filtered_data, kde=True, color="skyblue", element="bars", fill=True)
    plt.xlabel(selected_var, fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.title(f"Histogram and KDE Plot for {selected_var}", fontsize=16)
    st.pyplot(fig)
    #********************************************************************************************************
    st.write('From the histograms, from a traffic safety perspective, we can observe some clear trends for some variables. We can see a clear discrepancy on presence of a variable that may contribute to fatal ped-bike crashes. The variables "RuralUrban", "CrashLoc", and especially "BikeDir" show some trends that may factor for fatal ped-bike crashes. We now look in to the interactive plots between these three particular variables.')
    #********************************************************************************************************
    st.subheader("Interactive Plot")
    st.write('The following nested pie chart demonstrates a the amount of instances during which we observe the fatal ped-bike crashes for the variables "Rural_Or_Urban", "Crash_Location" and "Bike_Direction".')
    #********************************************************************************************************
    fig = px.sunburst(data, path=['Bike_Direction', 'Rural_Or_Urban', 'Crash_Location'], title='Nested Pie Chart Demonstrating the Preliminary Data')
    st.plotly_chart(fig)
#********************************************************************************************************
if option == "Conclusion and Recommendations":
    st.markdown("# Fatal Pedestrian-Bicyclist (Ped-Bike) Crash Trends")
    st.header("Preliminary Estimation")
    st.write("From this dataset, following may be taken into consideration before conducting a statistical analysis and finally coming to a conclusion:")
    message = """
    - The direction at which bicyclist travel may have an impact not only on the severity of the crashes, but the frequency of the crashes itself. Bicyclists may be rear-ended from the traffic from the same direction, which eventually may lead to a severe crash.
    - Rural settings, by default, do not have plenty of traffic control features in order to accommodate pedestrians and bicyclists, as they are primarily designed for passenger cars and heavy trucks. The fatal crash trends show that rural roads are not very safe for ped-bike safety in terms of infrastructures provided, as rural settings generally have a lesser amount of bicycle users as compared to urban contexts.
    - On the other hand, fatal crashes observed in urban settings may be contributed mostly towards the volume of ped-bikers and the traffic congestion itself.
    - The location of fatal crashes are observed to be more in Non-Intersection (Midblock) areas rather than in intersection, maybe due to the lack of any signs that may aware the motorists of the presence of ped-bikers at those road segments, as opposed to intersections, where either the ped-biker or the motorists are required to either stop or yield for each other.
    """
    st.markdown(message)      
    #********************************************************************************************************
    st.header("Recommendations")
    st.write('Following recommendations may be made from the preliminary analysis alone:')    
    st.write('- Roads with bike lanes or shoulders can be intermittently provided with direction markers in order to prevent blindside rear-end hits to the ped-bikers from motorists.')
    image_url = "http://content.bikeroar.com/system/content/000/427/676/large/bike_lane_road_marking_and_sign_2.jpg?1523587685"
    st.image(image_url, caption="Bike Lane With Direction Marker (Credit: bikeroar.com)", use_column_width=True)
    st.write('Rural settings and midblock sections may be provided with the warning pedestrian or bicyclist crossing signs intermittently for the drivers to insure they are not driving in a monotonous manner, and look out for vulnerable road users.')
    image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6OP7hmfH4veYRGgVh8b8fmFB-s579E2-trzUFJ7cKjeJ6i4WACt8EGlCA4b_Us9X_ZWQ&usqp=CAU"
    st.image(image_url, caption="Pedestrian Crossing Warning Sign(Credit: shutterstock.com)", use_column_width=True)
    st.write('Ultimately, the given dataset may be converted into binary dataset and a multinomial regression models may be generated eventually in order to quantify the fatal crash frequency that may be attributed to the variables in this dataset.')
