# RAG Chatbox

A beginner-friendly Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a locally running LLM.

## Overview

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of relying only on the LLM's general knowledge, the application first retrieves relevant information from a PDF and then provides that information as context to the language model.

The project demonstrates the complete workflow:

```text
PDF
 ↓
Document Loading
 ↓
Text Chunking
 ↓
Embeddings
 ↓
ChromaDB
 ↓
Relevant Chunk Retrieval
 ↓
Context + Question
 ↓
Local LLM
 ↓
Answer
```

## Tech Stack

| Technology            | Purpose                 |
| --------------------- | ----------------------- |
| Python                | Application development |
| LangChain             | RAG pipeline            |
| PyPDF                 | PDF document loading    |
| Sentence Transformers | Text embeddings         |
| ChromaDB              | Vector database         |
| Ollama                | Local LLM runtime       |
| Llama 3.2             | Language model          |
| Gradio                | Chat interface          |

## Project Structure

```text
rag_chatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

> The original PDF knowledge base is not included in this repository.

## How It Works

### 1. Load the PDF

The application loads the PDF using PyPDF.

### 2. Split the Document

The extracted text is divided into smaller chunks so that relevant sections can be retrieved efficiently.

### 3. Create Embeddings

Each document chunk is converted into a numerical vector using a Sentence Transformer embedding model.

### 4. Store Embeddings

The embeddings and document chunks are stored in ChromaDB.

### 5. Retrieve Relevant Information

When the user asks a question, the application searches the vector database and retrieves the most relevant chunks using MMR retrieval.

### 6. Generate the Answer

The retrieved information and the user's question are provided to the local LLM.

```text
User Question
      ↓
Question Embedding
      ↓
Vector Search
      ↓
Relevant Chunks
      ↓
Retrieved Context
      ↓
Llama 3.2
      ↓
Generated Answer
```

## Main Components

### `rag.py`

Contains the main RAG pipeline:

* PDF loading
* Text splitting
* Embedding generation
* ChromaDB storage
* MMR retrieval
* Prompt construction
* LLM response generation

### `app.py`

Provides the Gradio chatbot interface.

The user's question is passed to the RAG pipeline and the generated response is displayed in the interface.

## Local LLM

This project uses Ollama to run the LLM locally.

```text
Ollama
└── llama3.2:3b
```

Using a local model makes it possible to experiment with the application without depending on a paid cloud LLM API.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install and run Ollama

Install Ollama and download the required model:

```bash
ollama pull llama3.2:3b
```

### 6. Add the PDF

Place the knowledge-base PDF in:

```text
data/SN_MPF_Eng.pdf
```

The PDF itself is not included in this repository.

### 7. Run the application

```bash
python app.py
```

The Gradio interface should be available at:

```text
http://127.0.0.1:7860
```

## Example Questions

You can ask questions such as:

* What are the three types of MPF scheme?
* What is an employer sponsored scheme?

The chatbot retrieves relevant information from the PDF and uses it as context when generating the answer.

## What I Learned

Through this project, I gained hands-on experience with:

* Retrieval-Augmented Generation
* Document loading and text chunking
* Embeddings
* Vector databases
* Semantic retrieval
* Prompt construction
* Local LLMs
* LangChain
* ChromaDB
* Ollama
* Gradio
* Python virtual environments
* Git and GitHub

More importantly, I learned how the individual components of a RAG system connect together to form a working application.

## Learning Journey

This project was built after attending an introductory hands-on session covering:

* RAG
* AI Agents
* Agentic AI

Instead of stopping at the demonstration, I reproduced the workflow locally to understand each component and how it works in practice.

The learning process was:

```text
Watch
  ↓
Follow
  ↓
Run Locally
  ↓
Understand
  ↓
Build Independently
```

## Current Limitations

This is an early learning version of the project.

Current limitations include:

* The vector database can be rebuilt when the application starts
* No source or page citations are displayed
* Only one PDF is supported
* Conversation memory is not implemented
* Retrieval quality can be improved
* There is no automated evaluation of retrieval or answer quality
* The application is not publicly deployed

## Future Improvements

Planned improvements include:

* Persisting the vector database
* Adding source and page citations
* Supporting multiple PDF documents
* Adding conversation memory
* Improving retrieval quality
* Evaluating retrieval and answer accuracy
* Improving the chatbot interface
* Experimenting with different embedding models
* Comparing different local LLMs
* Deploying the application publicly

## Key Takeaway

The main goal of this project was not simply to build a chatbot.

It was to understand the complete RAG pipeline:

```text
Document
   ↓
Chunks
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retrieval
   ↓
Context
   ↓
LLM
   ↓
Answer
   ↓
Chat Interface
```

This project represents my hands-on learning journey into RAG, local AI, and AI engineering.

## Disclaimer

This is a learning project.

The original PDF knowledge source is not included in this repository.
