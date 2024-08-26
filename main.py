import streamlit as st
import pandas as pd

# Load the CSV data
data = pd.read_csv("https://media.githubusercontent.com/media/akshayonly/HMMER_DATA/main/data.csv")

# Title of the web app
st.title('NuoHMMER Data Viewer')

# Description of the app
st.markdown("""
The filtered data, shown below, is derived from the results of HMMER search result.

- **Option 1:** Enter an **Accession** to filter the data by Accession alone.
- **Option 2:** Enable the checkbox to filter by both **Accession** and **Subunit**.
- Use the dropdown menu to select the desired **Subunit** from the available options.

The filtered data will be displayed below. You can explore the dataset without downloading it.
""")

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
