import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv("https://media.githubusercontent.com/media/akshayonly/HMMER_DATA/main/data.csv")

# Title of the web app
st.title('NuoHMMER Data Viewer')

# User input: Accession
accession = st.text_input('Enter Accession:', placeholder='U00096.3')

accession = accession.upper()

# Generate the list of all unique subunits
all_subunits = sorted(data['Subunit'].unique())

# Checkbox to enable slicing by Subunit
use_subunit = st.checkbox('Select Specific Subunit')

if use_subunit:
    # Dropdown menu for selecting a Subunit
    subunit = st.selectbox('Select Subunit:', all_subunits)

    # Filter the data based on Accession and Subunit
    filtered_data = data[(data['Accession'] == accession) & (data['Subunit'] == subunit)]
else:
    # Filter the data based on Accession only
    filtered_data = data[data['Accession'] == accession]

# Display the filtered data
st.write('Filtered Data:')
st.dataframe(filtered_data)

st.markdown(
    """
    <style>
    [data-testid="stElementToolbar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
