import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import numpy as np



st.title('911 Kwa Dukuza | Borehole Points Stanger')


url = "https://docs.google.com/spreadsheets/d/1lHI0ofOrxTorUrthTqJKafWbZgmPqf9QdeWyVotcbrQ/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url)


# Filtering options
st.sidebar.header('Filter Points')
selected_column = st.sidebar.selectbox('Select Column', ['All'] + data.columns.tolist())
selected_value = st.sidebar.text_input('Search Term')

# Apply filters
filtered_data = data.copy()
if selected_column != 'All':
     filtered_data = filtered_data[filtered_data[selected_column].str.contains(selected_value, case=False).fillna(False).astype(bool)]

# Display filtered DataFrame
st.dataframe(filtered_data)


st.text('The community are urged to please be mindful and courteous to those that are making water available to you')
st.text('To add your name to the list to make water available to the community please contact Salim Tootla 083 662 8118')
