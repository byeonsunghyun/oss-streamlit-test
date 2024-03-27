import streamlit as st

x = st.slider("select a value")
st.write(x, 'is a square ', x * x)

st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this it the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')