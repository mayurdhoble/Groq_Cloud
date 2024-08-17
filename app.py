import streamlit as st
from groq import Groq

# Streamlit app configuration
st.set_page_config(page_title="Fast Language Model Importance", layout="wide")

def get_groq_models():
    """Fetches the list of available Groq models securely (implementation details omitted)."""
    # Replace this with the actual logic to retrieve Groq models from a secure source
    # (e.g., API call, environment variable).
    return ["llama-3.1-8b-instant","llama-3.1-70b-versatile","llama3-8b-8192", "llama-guard-3-8b","llama3-70b-8192", "Mixtral-8x7b-32768", "Gemma-7b-it", "Gemma2-9b-it", "Whisper-large-v3"]  # Example models

# Get the list of models
available_models = get_groq_models()

# API key input from user (securely store outside the app)
api_key = st.sidebar.text_input("Groq API Key", type="password")


try:
        client = Groq(api_key=api_key)

        # User prompt input
        user_prompt = st.text_input("Ask a question about fast language models:", key="prompt")

        # Model selection with informative message if Groq connection fails
        selected_model = st.sidebar.selectbox("Choose a Groq Model", available_models if available_models else ["(Fetching models...)"])

        if user_prompt:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_prompt,
                    }
                ],
                model=selected_model,
            )
        if st.button("Get the answer"):
                st.write(chat_completion.choices[0].message.content)

except Exception as e:
        st.error(f"An error occurred: {e}")
