import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import numpy as np
import requests
import faiss
import pickle
from tqdm import tqdm

# Load environment variables
load_dotenv()

app = FastAPI(title="Mental Health RAG App")

# Initialize MistralAI client
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("MISTRAL_API_KEY not found in .env file")

client = MistralClient(api_key=api_key)

# Constants
CACHE_FILE = "embeddings_cache.pkl"
ARTICLE_URL = "https://www.medicalnewstoday.com/articles/154543"

def get_text_embeddings(inputs):
    embeddings_batch_response = client.embeddings(
        model="mistral-embed",
        input=inputs
    )
    return [data.embedding for data in embeddings_batch_response.data]

def run_mistral(user_message, model="mistral-medium"):
    messages = [
        ChatMessage(role="user", content=user_message)
    ]
    chat_response = client.chat(
        model=model,
        messages=messages
    )
    return chat_response.choices[0].message.content

# Load or create embeddings
if os.path.exists(CACHE_FILE):
    print("Loading cached embeddings...")
    with open(CACHE_FILE, "rb") as f:
        chunks, text_embeddings = pickle.load(f)
else:
    print("Fetching and processing text...")
    response = requests.get(ARTICLE_URL)
    text = response.text

    chunk_size = 400
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    batch_size = 10
    text_embeddings = []
    for i in tqdm(range(0, len(chunks), batch_size), desc="Creating embeddings"):
        batch = chunks[i:i+batch_size]
        embeddings = get_text_embeddings(batch)
        text_embeddings.extend(embeddings)

    text_embeddings = np.array(text_embeddings)

    with open(CACHE_FILE, "wb") as f:
        pickle.dump((chunks, text_embeddings), f)

# Create FAISS index
d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

@app.post("/rag")
async def rag_endpoint(question: str = Query(..., description="User's mental health question")):
    try:
        # Get question embedding
        question_embedding = np.array(get_text_embeddings([question]))

        # Search for relevant chunks
        D, I = index.search(question_embedding, k=2)
        retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

        # Prepare prompt
        prompt = f"""
        Context information is below.
        ---------------------
        {' '.join(retrieved_chunks)}
        ---------------------
        Given the context information and not prior knowledge, answer the query about mental health.
        Query: {question}
        Answer:
        """

        # Generate response using MistralAI
        response = run_mistral(prompt)

        return {"question": question, "answer": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)