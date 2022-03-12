import streamlit as st
import pandas as pd

st.title('テストサイト')

st.write('ここは日本の結婚率と離婚率のページです')


df = pd.DataFrame({
    '都道府県':['東京都','千葉県','神奈川県','埼玉県'],
    'lat':[1,2,3,4],
    'lot':[10,20,30,40]
})

st.table(df.style.highlight_max(axis=0))