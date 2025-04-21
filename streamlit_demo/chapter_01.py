import streamlit as st

st.title("Hello Streamlit")
st.subheader("This is a subheader")
st.text("This is a text")
st.write("This is a write")

chai = st.selectbox("Your favourite language", ["Java", "Python", "C++", "JavaScript"])
st.write(f"Your choose {chai}.Eccelent choice")
st.success("Your language is good")