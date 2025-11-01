from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from llms.gemini import *
import streamlit as st
import pandas as pd


load_dotenv()

success_message =os.getenv("success_message")
print(success_message,end= '\n\n')


llm = chat_gemini_lite(
    temperature=0.2,
    max_tokens= 200,
    timeout=None,
    max_retries=2,
    )

vendors = pd.read_excel('data/vendors.xlsx')

## App header

st.markdown("""
    <style>
    .title-card {
        background-color: #1e1e22;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        margin-bottom: 30px;
    }
    .title-card h1 {
        color: #ff4b8b;
        font-size: 34px;
        font-weight: 700;
        margin-bottom: 8px;
    }
    .title-card p {
        color: #ccc;
        font-size: 18px;
        margin: 0;
    }
    [data-theme="light"] .title-card p {
        color: #333;
    }
    </style>

    <div class="title-card">
        <h1>💍 Ranikhet Wedspot Finder</h1>
        <p>Discover trusted banquet halls, caterers, and tent services in Ranikhet</p>
    </div>
""", unsafe_allow_html=True)


st.markdown("<h4 style='font-size:22px; font-weight:600;'>🔎 What are you looking for?</h4>", unsafe_allow_html=True)
query = st.text_input("", "banquet hall for 150 people", label_visibility="collapsed")



# Filter using AI

if st.button("✨ Find Best Options"):
    if not query.strip():
        st.warning("Please enter what you’re looking for.")
    else:
        st.info("Analyzing your query using AI...")
        # Take a manageable subset for the LLM

        prompt = f"""
        You are helping a user find wedding services in Ranikhet.
        Vendor data: {vendors.to_dict(orient='records')}
        Based on the query: "{query}", suggest the 3 most relevant vendors with short descriptions.
        """

        with st.spinner("Finding the best matches..."):
            try:
                response = llm.invoke(prompt)
                st.success("Here are the top results:")
                st.write(response.content)
            except Exception as e:
                st.error(f"⚠️ Something went wrong: {e}")

with st.expander("📋 View All Vendors"):
    for _, row in vendors.iterrows():
        # st.image(row["image_url"], width=200)
        st.subheader(row["Name"])
        st.caption(row.get("Address", "Address not available"))
        st.write(f"💰 Price Range: {row.get('price_range', 'N/A')}")
        st.write(f"📞 Contact: {row.get('contact 1', 'N/A')}")
        st.write(f"📞 Alt: {row.get('contact 2', 'N/A')}")
        st.divider()

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.markdown("Made with ❤️ for Ranikhet Weddings | Created by Lalit Singh")
