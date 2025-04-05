import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.generator import generate_campaign

st.set_page_config(page_title="Marketing Campaign Generator", layout="centered")

st.title("📣 AI Marketing Campaign App")
st.write("Generate marketing messages tailored to different age groups using AI and LangChain.")

# age
age_group = st.selectbox("Select Target Age Group:", options=["Kids", "Adults", "Seniors"])

# tone
tone = st.selectbox("Select Message Tone:", options=["Professional", "Funny", "Emotional"])

# length
length = st.selectbox("Select Message Length:", options=["Short", "Medium", "Long"])


#  input the product
product = st.text_input("Enter the product or service name:")

# session_state for saveing the message
if "generated_message" not in st.session_state:
    st.session_state.generated_message = ""

# Buttons Generate , Regenerate
col1, col2 = st.columns(2)
generate = col1.button("🎯 Generate Campaign")
regenerate = col2.button("🔁 Regenerate")

# generate
if generate or (regenerate and product.strip()):
    if product.strip():
        with st.spinner("Generating your marketing campaign..."):
            st.session_state.generated_message = generate_campaign(age_group, product, tone, length)
        st.success("Campaign Generated Successfully!")
    else:
        st.warning("Please enter a product or service name.")

# Markdown 
if st.session_state.generated_message:
    st.markdown("### 🧠 Campaign Message:")
    st.markdown(st.session_state.generated_message, unsafe_allow_html=False)
