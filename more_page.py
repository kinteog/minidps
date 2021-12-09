import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 

@st.cache
def load_data():
    diabetes_dataset=pd.read_csv('diabetes.csv')
    return diabetes_dataset

         


def show_more_page():
    st.title("Explore more page")

    st.write(
        """
    ### more info on data used to train the model
    """
    )
    st.subheader("Dataset Used To Train And Test The Model")

    

    result = load_data()
    
    with st.expander("View all Data Used To Train And Test The Model"):
        st.dataframe(result)

    st.subheader("The Distribution Of The Labelled Data On The Dataset")
    with st.expander("View The Distribution Of The Labelled Data"):
        diabetis_df= result['Outcome'].value_counts().to_frame()
        diabetis_df = diabetis_df.reset_index()
        st.dataframe(diabetis_df)
        p1 = px.pie(diabetis_df,names='index',values='Outcome')
        st.plotly_chart(p1,use_container_width=True)
    st.subheader("The Distribution Of The Labelled Data On The Dataset Based On Age")
    with st.expander("View The Distribution Of The Labelled Data Based on Age"):
        data = result.groupby(["Age"])["Outcome"].mean().sort_values(ascending=True)
        st.bar_chart(data)

    st.subheader("The Distribution Of The Labelled Data On The Dataset Based On Blood Pressure")
    with st.expander("View The Distribution Of The Labelled Data Based on Blood Pressure"):

        data = result.groupby(["BloodPressure"])["Outcome"].mean().sort_values(ascending=True)
        st.line_chart(data)
    

    