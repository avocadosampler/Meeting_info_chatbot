import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
LLM_MODEL = "google/gemini-2.5-flash"

# TO DO - set your client (we've seen this before, via OpenRouter)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = OPENROUTER_API_KEY)

def call_llm(user_prompt):
    """
    Sends a simple prompt to an LLM via OpenRouter
    and returns the model's response as text.
    """

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.3,
        max_tokens = 1000
    )

    return response.choices[0].message.content


#########################
########### HINT for RAG
#########################
# def generate_answer(query, context_chunks):
#     context = "\n\n".join(context_chunks)

#     # Placeholder for local LLM call
#     return f"""
# Based on the provided documents, here is what I found:

# {context}

# Question:
# {query}

# (Note: This is a stubbed response — replace with local LLM call.)
# """.strip()
