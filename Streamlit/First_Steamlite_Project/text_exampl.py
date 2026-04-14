import streamlit as st

st.title("This app base on Steamlite", anchor=False, width="content")


st.markdown("""
Mehedi Hasan Foysal  
Class
""") 
st.latex(r"a^2 + b^2 = c^2")
st.code("cout << Hello << endl;", language='cpp')

st.json({"name": "Foysal", "age": 20})

st.caption("This is a caption")

st.title("This is a title", anchor=False)

st.success("This is a success message")