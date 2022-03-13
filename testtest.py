import streamlit as st
import pandas as pd
import numpy as np


st.title('テストサイト')

st.write('ここは日本の結婚率と離婚率のページです')


df = pd.DataFrame({
    '都道府県':['東京都','千葉県','神奈川県','埼玉県'],
    'lat':[1,2,3,4],
    'lot':[10,20,30,40]
})

st.table(df.style.highlight_max(axis=0))



df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']  
)
st.line_chart(df)



df = pd.DataFrame({
    'lat':[35.593063,35.6297363,35.5914658],
    'lon':[139.6776223,139.6898639,139.6688982]
    
})
st.map(df)


if st.checkbox('マンションデータ'):
     mrdata = pd.read_csv('20200806mr_data1.csv',encoding='utf-8')
     st.table(mrdata)