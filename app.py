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

st.title("💍 Ranikhet Wedspot Finder")
st.write("Discover trusted banquet halls, caterers, and tent services in Ranikhet.")

query = st.text_input("What are you looking for?", "banquet hall for 150 people")


# Filter using AI
if st.button("Find Options"):
    model = llm
    prompt = f"""
    You are helping a user find wedding services in Ranikhet.
    Vendor data: {vendors.to_dict(orient='records')}
    Based on the query: "{query}", suggest the 3 most relevant vendors with short descriptions.
    """
    response = model.invoke(prompt)
    st.write(response.content)

with st.expander("📋 View All Vendors"):
    for _, row in vendors.iterrows():
        # st.image(row["image_url"], width=200)
        st.subheader(row["Name"])
        st.write(f"📍 {row['Address']}")
        st.write(f"💰 {row['price_range']}")
        st.write(f"📲 {row['contact 1']}")
        st.write(f"📞 {row['contact 2']}")
        st.divider()
