import streamlit as st
import pandas as pd

st.title("Simple Data Dashboard")

upload_file = st.file_uploader("Choose a data file", type="csv")

if upload_file is not None:
    st.write("File Uploaded Successfully")
    df = pd.read_csv(upload_file) 
    st.subheader("Data Preview")
    st.write(df.sample(10))
    st.write(df.shape)
    st.subheader("Data Summary")
    st.write(df.describe())
    st.subheader("Filtered Data")
    column = df.columns.tolist()
    selected_column = st.selectbox("Select a column",column)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select a Value", unique_values)
    # show filtered dataframe wrt above selected value and selected column
    filtered_df = df[df[selected_column]==selected_value]
    st.write(filtered_df)
    # plot a graph: Choose x and y axis
    x_column = st.selectbox("Select x column",column)
    y_column = st.selectbox("Select y column",column)
    if st.button("Plot the Graph"):
        st.line_chart(filtered_df,x=x_column,y=y_column)
else:
    st.write("Waiting for file upload...")

    


