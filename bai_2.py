import pandas as pd
import streamlit as st
pd.options.display.max_rows = 2
data = pd.read_csv('data.csv')
# st.write(data)
# st.table(data)
st.dataframe(data)
st.dataframe(data.loc[[2,4]])
info = data.info()
st.write(info)
