import streamlit as st
import pandas as pd
import csv
from mistralai import Mistral

# Initialize Mistral client with API key from Streamlit secrets
api_key = st.secrets.get("MISTRAL_API_KEY", "wCCxoz0TFWggsnciVVj4AsQVnjg75a5c")
client = Mistral(api_key=api_key)
model = "mistral-large-latest"

# Load FAQ data
@st.cache_data
def load_faq_data():
    faq_data = []
    with open('hbdb_banking_faqs (2) (1).csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            faq_data.append(row)
    return faq_data

# Create FAQ context string
@st.cache_data
def create_faq_context():
    faq_data = load_faq_data()
    context = "You are a helpful banking assistant for HBDB Bank. Here are the FAQs:\n\n"
    for faq in faq_data:
        context += f"Q: {faq['Question']}\nA: {faq['Answer']}\n\n"
    return context

# Function to get bot response
def get_bot_response(user_message):
    faq_context = create_faq_context()
    
    system_message = f"""{faq_context}

Use the FAQ information above to answer customer questions about HBDB Banking services.
Be helpful, professional, and accurate. If the question is not covered in the FAQs, 
provide general banking advice and suggest contacting HBDB customer service."""
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]
    
    response = client.chat.complete(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
        stream=True
    )
    
    return response

# Streamlit UI
st.set_page_config(page_title="HBDB Banking Bot", layout="wide")

st.title("🏦 HBDB Banking Assistant")
st.markdown("Welcome to HBDB Bank's AI-powered customer service bot. Ask me anything about our banking services!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if user_input := st.chat_input("Ask me about HBDB banking services..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Get bot response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            response = get_bot_response(user_input)
            
            for chunk in response:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    response_placeholder.write(full_response)
            
            # Add assistant message to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            response_placeholder.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Sidebar info
st.sidebar.markdown("""
---
### About HBDB Banking Bot
- **Model**: Mistral Large
- **Knowledge Base**: HBDB Banking FAQs
- **Available 24/7**

### Quick Topics
- Opening accounts
- Online banking
- Credit cards
- Loans and mortgages
- Transfers and payments
- Account management
""")
