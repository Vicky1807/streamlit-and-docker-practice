import streamlit as st
import pandas as pd

st.title("Hello from Streamlit! 👋")

st.write("This is a simple web app running in Docker")

# Simple form
name = st.text_input("What's your name?")
if name:
    st.write(f"Nice to meet you, {name}! 😊")


# Simple slider
number = st.slider("Pick a number", 1, 100)
st.write(f"You picked: {number}")

# Simple form
Place = st.text_input("Where are you from?")
if Place:
    st.write(f"how's {Place}! , {name}.. 😊")

# Simple data
st.subheader("Sample Data")
data = {
    'Name': ['Alice', 'Bob', 'Charlie',name],
    'Age': [25, 30, 35, number],
    'City': ['NYC', 'LA', 'Chicago',Place]
}
df = pd.DataFrame(data)
st.dataframe(df)
