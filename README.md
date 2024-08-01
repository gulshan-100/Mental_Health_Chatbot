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
This will start a Gradio interface, typically accessible at `http://localhost:7860`.

### Deploying on Hugging Face Spaces
1. Create a new Space on Hugging Face and choose Gradio as the SDK.
2. Upload the `app.py` and `requirements.txt` files to your Space.
3. Add your MistralAI API key as a secret in the Space settings.
4. The Space will automatically build and deploy your application.

## How It Works
1. The application loads or creates embeddings for chunks of a mental health article.
2. When a user submits a question, the app finds the most relevant chunks using FAISS.
3. These chunks and the user's question are sent to MistralAI to generate a contextually relevant answer.
4. The answer is displayed to the user through the Gradio interface.

## Configuration
- `CACHE_FILE`: Name of the file to store embeddings (default: "embeddings_cache.pkl")
- `ARTICLE_URL`: URL of the mental health article used for information retrieval

## Troubleshooting
- If you encounter an error related to the API key, ensure it's correctly set in your environment variables or Hugging Face Space secrets.
- For issues with embedding creation, check your internet connection and MistralAI API status.

## Contributing
Contributions to improve the application are welcome. Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License
[Specify your license here, e.g., MIT License]

## Acknowledgements
- MistralAI for providing the language model and embedding capabilities
- FAISS library for efficient similarity search
- Gradio for the web interface framework
