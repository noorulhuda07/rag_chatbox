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
