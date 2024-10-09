import streamlit as st
import pandas
data = {
    "series_1":[1,2,3,4,5],
    "series_2":[22,33,44,55,66]
}
df = pandas.DataFrame(data)
st.title("My first app")
st.subheader("Introducincg streamlit")
st.write("""my first app""")
st.write(df)
st.line_chart(df)

myslider =st.slider("celsius")
st.write(myslider,"in fyreheint is",myslider * 9/5 + 32)