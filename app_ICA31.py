import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


df_cancer = pd.read_csv('data.csv')

def Plot():
    st.header("Worst radius, smoothness and concavity for beningn and malignant tumors")
    sd = st.selectbox(
        "Select a Plot", #Drop Down Menu Name
        [
            "Radius Plot", #First option in menu
            "Smoothness Plot",   #Second option in menu
            "Concavity Plot"  #Third option in menu
        ]
    )

    fig = plt.figure(figsize=(12, 6))

    if sd == "Radius Plot":
        sns.boxplot(data=df_cancer, x="diagnosis", y="radius_worst", hue="diagnosis")
        plt.title("Comparing the Worst Radius of Tumors by Diagnosis")
        plt.xlabel("Diagnosis")
        plt.ylabel("Worst Radius")
        plt.show()
    
    elif sd == "Smoothness Plot":
        fig = sns.FacetGrid(df_cancer, col="diagnosis", hue="diagnosis")
        fig.map(sns.scatterplot, "smoothness_worst", "radius_worst", alpha=0.5)
        fig.add_legend()
        plt.show()

    elif sd == "Concavity Plot":
        sns.kdeplot(data=df_cancer, x="radius_worst", y="concavity_worst", hue="diagnosis")
        plt.title("Comparing Radius and Concavity")
        plt.xlabel("Radius")
        plt.ylabel("Concavity")
        plt.show()

    st.pyplot(fig)

page = st.sidebar.selectbox(
    "Select a Page",
    [
        "Plotting cancer graphs" #New Page
    ]
)
Plot()
