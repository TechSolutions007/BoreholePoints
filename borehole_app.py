import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import numpy as np



st.title('911 Kwa Dukuza | Borehole Points Stanger')


url = "https://docs.google.com/spreadsheets/d/1lHI0ofOrxTorUrthTqJKafWbZgmPqf9QdeWyVotcbrQ/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

# Disable caching for data retrieval
@st.cache_data(ttl=1)
def fetch_data(url):
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn.read(spreadsheet=url)

fetch_data.clear()
st.cache_data.clear()
data = fetch_data(url)


# Display filtering options using columns
with st.expander("Filter Points", expanded=True):
    col1, col2 = st.columns([1, 2])
    with col1:
        selected_column = st.selectbox('Select Column', ['All'] + data.columns.tolist())
    with col2:
        selected_value = st.text_input('Search Term')

# Apply filters
#filtered_data = data
if selected_column != 'All':
     data = data[data[selected_column].str.contains(selected_value, case=False).fillna(False).astype(bool)]

#Display filtered DataFrame
st.dataframe(data,use_container_width=True,hide_index=True)


st.subheader('The community are urged to please be mindful and courteous to those that are making water available to you')
st.subheader('To add your name to the list to make water available to the community please contact Salim Tootla @ 083 662 8118')
