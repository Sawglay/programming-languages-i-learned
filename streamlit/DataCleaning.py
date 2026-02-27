import streamlit as st
import pandas as pd

st.title('Data Cleaning')
FileToOpen = 'Dataset.xlsx'
sheetName = 'Missing_Values'
df_missing = pd.read_excel(FileToOpen, sheet_name = sheetName)
st.dataframe(df_missing)

# df_missing_clean = df_missing.dropna()
# st.dataframe(df_missing_clean)

# df_missing_clean = df_missing.dropna(subset=['Model'])
# st.dataframe(df_missing_clean)

# df_missing_clean = df_missing.fillna(0)
# st.dataframe(df_missing_clean)

# df_missing_clean = df_missing.fillna(df_missing["Width(mm)"].median())
# st.dataframe(df_missing_clean)

df_missing_clean = df_missing.dropna()
df_missing_clean = df_missing_clean.drop_duplicates()
st.dataframe(df_missing_clean)
