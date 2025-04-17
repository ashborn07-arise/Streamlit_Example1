import streamlit as st

st.title("This is first application")
st.header("Hello this is application")
st.subheader("This is a Subheader")
st.text("Welcome to the World of Streamlit")

names = st.text_input("enter your name")

if st.button("Submit"):
    st.write("hello",name)

if st.checkbox("Show Secret Message"):
    st.write("You discovered a hidden message")

option = st.selectbox("Choose your favorite language",["Python","Java","C++","JavaScripts"])

st.write("You Selected: ",option)

age = st.slider("Select your age:",1,100,25)
st.write("Your age is",age)
