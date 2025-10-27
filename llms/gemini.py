from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Gemini standard model
def chat_gemini_lite(temperature,max_tokens,timeout,max_retries):
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=temperature,
    max_tokens=max_tokens,
    timeout=timeout,
    max_retries= max_retries,
    api_key=os.getenv("GOOGLE_GENAI_API_KEY")
    )

    return llm

# Gemini Pro model for large database
def chat_gemini_pro(temperature,max_tokens,timeout,max_retries):
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=temperature,
    max_tokens=max_tokens,
    timeout=timeout,
    max_retries= max_retries,
    api_key=os.getenv("GOOGLE_GENAI_API_KEY")
    )
    
    return llm

# Gemini Image model
def chat_gemini_image(temperature,max_tokens,timeout,max_retries):
    llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-image",
    temperature=temperature,
    max_tokens=max_tokens,
    timeout=timeout,
    max_retries= max_retries,
    api_key=os.getenv("GOOGLE_GENAI_API_KEY")
    )
    
    return llm