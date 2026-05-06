from openai import OpenAI
from dotenv import load_dotenv
import os

from app.rag.vector_store import collection

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_question(question):

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    context = "\n".join(
        results["documents"][0]
    )

    prompt = f"""
    Answer ONLY using this context:

    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content