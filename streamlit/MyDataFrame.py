import streamlit as st
import pandas as pd

st.title("DataFrame Demo")

my_df = pd.DataFrame({"ID":[1111,1112] , "Name":["John", "G Lay"]})
st.write(my_df)
st.dataframe(my_df)

FileToOpen = 'Dataset.xlsx'
sheetName = 'Province_1'
df_province_1 = pd.read_excel(FileToOpen, sheet_name = sheetName)
st.write(df_province_1)

sheetName = 'Province_2'
df_province_2 = pd.read_excel(FileToOpen, sheet_name = sheetName)
st.write(df_province_2)

# st.write(df_province_1.head())

# st.write("Two ways to display data in column")

# st.dataframe(df_province_1["Province"]) #Suggested Way
# st.dataframe(df_province_1.Province)

# df_province_2['Density'] = round(df_province_2['Population (2017)'] / df_province_2['Area (km2)'])
# st.write(df_province_2)

# df_size = len(df_province_1)
# st.write("DataFrame Size:", df_size)

# df_province_1_col = list(df_province_1.columns)
# st.write(df_province_1_col)

# st.subheader("Get Uniques Values in A Column")
# st.write(df_province_1['Province'].unique())

# df_province_2 = df_province_2.drop(columns = ['Density'])
# st.write(df_province_2)

# df_province_2_mod = df_province_2[df_province_2.columns[[0,2,1]]]
# st.write(df_province_2_mod)

# st.subheader("Filter some rows")
# df_province_2_filter = df_province_2[(df_province_2['Population (2017)'] > 1000000) & (df_province_2['Area (km2)'] > 15000)]
# st.write(df_province_2_filter)

# st.subheader("Select some columns to create new dataframe")
# df_province_2_new = df_province_2[['Province', 'Population (2017)']]
# st.write(df_province_2_new)

st.subheader("Merge DataFrames")
df_merge = df_province_1.merge(df_province_2, on = 'Province', how = 'inner')
st.dataframe(df_merge)

st.subheader("Sort DataFrame")
df_merge.sort_values(['GDP (Billion BHT)'], ascending = [False], inplace = True)
st.write(df_merge)

# df_merge = df_merge.sort_values(['Province', 'GDP (Billion BHT)'], ascending=[True, True])
# st.dataframe(df_merge)

st.subheader("DataFrame to List")
province_list = df_province_1['Province'].to_list()
st.write(province_list)

st.subheader("Access all columns iteratively")
for index, row in df_province_1.iterrows():
    st.write(index, (row['Province']), (row['GDP (Billion BHT)']))