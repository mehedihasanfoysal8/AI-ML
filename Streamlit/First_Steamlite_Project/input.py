import streamlit as st
st.title("Input Widgets in Streamlit")

st.divider()
name = st.text_input("Enter your name", autocomplete="on", placeholder="Type your name here")

st.divider()
age = st.number_input("Enter our age", placeholder="Type your age", value=None)

st.divider()
press = st.button("Submit", width="stretch")

if press:
    if not name and age:
        st.error("Name and age is required")
    elif not name:
        st.error("Name is required")
    elif not age:
        st.error("Age is required")
    else:
        st.success("Form submitted successfully")
        st.write(f"Your name is {name} and age is {age}")