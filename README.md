# Mental Health RAG Assistant

## Description
This is a Retrieval-Augmented Generation (RAG) based application designed to answer mental health-related questions. It uses the MistralAI API for language processing and embeddings, and FAISS for efficient similarity search. The application retrieves relevant information from a pre-processed mental health article and generates responses to user queries.

## Features
- RAG-based question answering on mental health topics
- Efficient information retrieval using FAISS
- Integration with MistralAI for natural language processing
- Caching of embeddings for improved performance
- Gradio-based web interface for easy interaction

## Installation

### Prerequisites
- Python
- A MistralAI API key

### Steps
1. Clone this repository
2. Install the required packages
3. Set up your MistralAI API key as an environment variable:
- For local development, create a `.env` file in the root directory and add:
  ```
  MISTRAL_API_KEY=your_api_key_here
  ```
- For Hugging Face Spaces, add the API key in the "Secrets" section under "Variables" in your Space settings.

## Usage

### Running Locally
Execute the following command:
