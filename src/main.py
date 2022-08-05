"""
# My first app
Here's our first attempt at using data to create a table:
"""
import time

import numpy as np
import pandas as pd
import streamlit as st

st.markdown("# Streamlit操作練習🔰")
st.markdown("---")
st.markdown("## データフレームの表示")
# データフレームの表示
dataframe = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))

st.markdown("## マップの表示")
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"])
st.map(map_data)

st.markdown("## 数値スライダー")
x = st.slider("x")  # 👈 this is a widget
st.write(x, "squared is", x * x)
print(x)

st.markdown("## 文字列入力ウィジェット")
st.text_input("Your name", key="name")
# 文字列を入力すると更新される
st.session_state.name


st.markdown("## チェックボックス")
if st.checkbox("Show dataframe"):
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    chart_data

st.markdown("## セレクトボックス")
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
option = st.selectbox("Which number do you like best?", df["first column"])
"You selected: ", option


# Add a selectbox to the sidebar:
st.sidebar.markdown("# サイドバー")
st.sidebar.markdown("サイドバーを作成するときは、st.sidebarとすればよい")
add_selectbox = st.sidebar.selectbox("How would you like to be contacted?", ("Email", "Home phone", "Mobile phone"))

# Add a slider to the sidebar:
add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))


st.markdown("## 2分割で")
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button("Press me!")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio("Sorting hat", ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


st.markdown("## 経過の表示")
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"...and now we're done!"
