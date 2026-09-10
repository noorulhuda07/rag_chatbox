# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The goal was to understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works

```text
PDF
 ↓
Load document
 ↓
Split document into chunks
 ↓
Create embeddings
 ↓
Store embeddings in ChromaDB
 ↓
User asks a question
 ↓
Retrieve relevant chunks
 ↓
Retrieved context + question
 ↓
Local LLM (Llama 3.2)
 ↓
Generated answer
```

## Tech Stack

* Python
* LangChain
* Hugging Face Sentence Transformers
* ChromaDB
* Ollama
* Llama 3.2
* Gradio
* PyPDF

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

The PDF knowledge base is not included in this GitHub repository.

## Main Components

### `rag.py`

This file contains the main RAG pipeline.

It:

* Loads the PDF using PyPDF
* Splits the document into smaller chunks
* Creates vector embeddings using Sentence Transformers
* Stores document chunks in ChromaDB
* Retrieves relevant chunks using MMR retrieval
* Combines the retrieved context with the user's question
* Sends the context and question to the local LLM
* Generates the final answer

### `app.py`

This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

## Local LLM

This project uses Ollama to run the language model locally.

```text
Ollama
└── llama3.2:3b
```

Using a local model allowed the application to be tested without relying on a paid cloud LLM API.

## Retrieval

The application converts document chunks into numerical vectors called embeddings.

When a user asks a question:

```text
User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM
      ↓
Generate Answer
```

The retrieved information is provided to the language model as context so that the answer is grounded in the selected document.

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

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Ollama

Install Ollama and pull the required model:

```bash
ollama pull llama3.2:3b
```

### 6. Add the PDF knowledge base

Place the PDF inside:

```text
data/
```

with the filename:

```text
SN_MPF_Eng.pdf
```

The original PDF used during development is not included in this repository.

### 7. Run the chatbot

```bash
python app.py
```

The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

```text
http://127.0.0.1:7860
```

## Example Questions

* What are the three types of MPF scheme?
* What is an employer sponsored scheme?

The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

## What I Learned

This project gave me practical exposure to the workflow behind a RAG application.

### RAG Concepts

* Document loading
* Text chunking
* Embeddings
* Vector databases
* Retrieval-Augmented Generation
* Prompt construction
* Local LLMs

### Development Workflow

* Python virtual environments
* Installing and managing dependencies
* Working with files and folders
* Running Python applications from PowerShell
* Connecting a backend pipeline to a user interface
* Using Ollama for local AI
* Using Git
* Creating commits
* Pushing code to GitHub
* Writing project documentation

## Learning Journey

This project was built after attending a hands-on introductory session on:

* RAG
* AI Agents
* Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

```text
Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
```

## Current Limitations

This is an early learning version of the project.

Some areas that can be improved include:

* Better retrieval quality
* Source and page references for answers
* More efficient vector database handling
* Conversation memory
* Support for multiple documents
* Better error handling
* Retrieval and answer evaluation
* Improved chatbot UI
* Public deployment

## Future Improvements

* Avoid rebuilding the vector database every time the application starts
* Add page and source citations to retrieved answers
* Add support for multiple PDF documents
* Add conversation memory
* Improve retrieval quality
* Add evaluation for retrieval and answer accuracy
* Improve the Gradio interface
* Deploy the chatbot publicly
* Experiment with different embedding models
* Compare different local LLMs

## Key Takeaway

The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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

This project is part of my hands-on learning journey into AI engineering and software development.

## Disclaimer

This repository is a learning project.

The original PDF knowledge source is not included in this repository.
