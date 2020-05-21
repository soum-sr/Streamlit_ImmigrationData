import streamlit as st
import numpy as np 
import pandas as pd 

st.title('Immigration to Canada')
df_ca = pd.read_excel('Canada.xlsx',sheet_name='Canada by Citizenship',skiprows=range(20), skipfooter=2)
df_ca.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace= True)


st.write("""### Dataset""")
st.write(df_ca.head(15))


df_ca['Total'] = df_ca.iloc[:, 9:43].sum(axis=1)


st.write("""### Dataset Description""")
st.write(df_ca.describe())

# Setting 'Country' as index
df_ca.set_index('Country', inplace=True)

# Converting column names to string
df_ca.columns = list(map(str, df_ca.columns))

# list of years for ease of use in future
years = list(map(str, range(1980,2014)))

# Plotting Immigration from India
india_df = df_ca.loc['India', years]
india_df.index = india_df.index.map(int)

st.write("""### Immigration from India""")
st.line_chart(india_df)
