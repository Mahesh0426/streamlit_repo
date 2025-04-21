import streamlit as st

st.title("Chai Taste Poll")
col1, col2 = st.columns(2)

with col1:
    st.header("masala chai")
    vote1 = st.button("Vote for masala chai")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0qxSPgB4C3eNms1SUVIZ5Vs6gG0VIVDYxMw&s", width=200)
with col2:
    st.header("Ginger chai")
    vote2 = st.button("Vote for Ginger chai")
    st.image("https://t4.ftcdn.net/jpg/03/04/17/77/360_F_304177779_7k7ZnPxZPvr4T3rsIsJQrcL08Mwe5BM3.jpg", width=200)
if vote1:
    st.success("You voted for masala chai")
if vote2:
    st.success("You voted for Ginger chai")
elif vote2:
    st.success("You voted for Ginger chai")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala", "Ginger", "Lemon"])

st.write(f"Welcome,{name} ! and your chai is gettig ready {tea}")


with st.expander("Show chai making instrustion"):
    st.write("""
1. Open a gas stove
2. Boit water with tea
3. Add milk and spices
4. Server
        """)

st.markdown('### Welcome to chai App')
st.markdown('> This is a simple chai app to demonstrate streamlit')