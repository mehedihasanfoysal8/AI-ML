
# print(res.text)
import streamlit as st
import google.generativeai as genai
import os

# API Key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    API_KEY = st.text_input("Enter API Key", type="password")

# Configure Gemini
if API_KEY:
    genai.configure(api_key=API_KEY)

st.title("🤖 Gemini AI App")

prompt = st.text_area("Enter your prompt")

if st.button("Generate", use_container_width=True):
    if not API_KEY:
        st.error("API Key required!")

    elif not prompt.strip():
        st.warning("Prompt required!")
        
    else:
        try:
            with st.spinner("Generating..."):
                model = genai.GenerativeModel("gemini-3-flash-preview")
                response = model.generate_content(prompt)

            st.success("Done!")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")