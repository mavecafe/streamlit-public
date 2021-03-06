import streamlit as st
import pandas as pd
import numpy as np
import time

#サイドバーで表示
st.sidebar.write('プログレスバーの表示 Start!')

latest_iteration = st.sidebar.empty()
bar = st.sidebar.progress(0)

for i in range(100):
    latest_iteration.text(f'もうすぐ表示されます{i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

#サイドバーで表示
condition = st.sidebar.slider('いまのあなたの調子は',0,50,100)
st.sidebar.write('コンディション', condition)


#サイドバーで表示
select = st.sidebar.selectbox("どちらが欲しい",["大きい箱","小さい箱"])

if st.sidebar.button('open'):
    if select == '玉手箱':
        st.sidebar.write('空っぽでした！')
    else:
        st.sidebar.write('お宝でした！！！')

#サイドバーで表示
a = st.sidebar.text_input('入力してください','ここにどうぞ')
st.sidebar.write(a)







st.title('ゆっくりてすとさいと')

"""
### 使っているライブラリー

```
python
import streamlit as st/
import numpy as np/
import pandas as pd/
```

"""


"""
# 第１章　日本の住宅と人口問題

"""





df = pd.DataFrame({
    '都道府県':['東京都','千葉県','神奈川県','埼玉県'],
    'lat':[1,2,3,4],
    'lot':[10,20,30,40]
})

st.table(df.style.highlight_max(axis=0))



"""
## 乱数で表示
"""
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']  
)
st.line_chart(df)


"""
## マンションデータと地図
"""


df = pd.DataFrame({
    'lat':[35.593063,35.6297363,35.5914658],
    'lon':[139.6776223,139.6898639,139.6688982]
    
})
st.map(df)

# #mrdata3 = pd.read_csv('streamlit-public/20200806mr_data3.csv',encoding='utf-8')
# mrdata3 = pd.read_csv('20200806mr_data3.csv',encoding='utf-8')
# st.table(mrdata3)

#df3 = pd.DataFrame(mrdata3,columns=['lat','lon'])

#st.map(mrdata3)








if st.checkbox('マンションデータ'):
     #mrdata = pd.read_csv('streamlit-public/20200806mr_data1.csv',encoding='utf-8')
     mrdata = pd.read_csv('20200806mr_data1.csv',encoding='utf-8')
     st.table(mrdata)
     
     






#expander = st.expander('問い合わせ')
#PCの環境ではst.beta_expander　で公開はst.expander 
# expander = st.beta_expander('問い合わせ')
# expander.write('問い合わせ内容を書く')
# expander.write('問い合わせ内容を書く')
# expander.write('問い合わせ内容を書く')
# expander.write('問い合わせ内容を書く')


st.write('ここは日本の結婚率と離婚率のページです')

mariige = pd.read_csv('mariige.csv',encoding='utf-8')
#mariige = pd.read_csv('streamlit-public/mariige.csv',encoding='utf-8')
mariige.set_index("年", inplace=True)
#df = pd.DataFrame(oak)
st.line_chart(mariige)

st.bar_chart(mariige)



oak = pd.read_csv('oak.csv',encoding='utf-8')
oak.set_index("年月", inplace=True)
#df = pd.DataFrame(oak)
st.line_chart(oak)

st.bar_chart(oak)
