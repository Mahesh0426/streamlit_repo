import streamlit as st

st.title("Chai Maker app")

if st.button("Make chai"):
    st.success("Your chai is ready")


add_sugar= st.checkbox("Do you want to add sugar?")

if add_sugar:
    st.success("Your chai is ready with sugar")
else:
    st.success("Your chai is ready without sugar")


st.title("check box")
tea_type = st.radio("Select your chai", ["Milk chai", "Non_Milk chai", "Almond-Milk chai"])
# st.write(f"You selected {tea_type}")
flavour = st.selectbox("Select flavour", ["Masala", "Ginder", "cardmom", "lemon", "Tulsi"])
st.write (f"You have Selected  '{flavour}' with '{tea_type}'")



st.title("Or if you want   multiple flavour choose from here ")
multi = st.multiselect("Select your chai", ["Masala", "Ginder", "cardmom", "lemon", "Tulsi"])
st.write(f"You  want to add  {multi} on your {tea_type}")

sugar = st.slider("Select your sugar level", 0, 5, 2)

cups = st.number_input("how many cups", min_value=1, max_value=10, step = 1)
st.write(f"Selected cups{cups}")

name = st.text_input("Enter your name")
if name :
    st.write(f"Welcome {name} ! Your chai is on the way. ")

dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth is {dob}")