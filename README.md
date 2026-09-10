# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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


Absolutely. Here is the entire README in one go, so you can select everything, copy it, and paste it into Notepad.

I’ve also slightly cleaned it up so it accurately reflects what you actually built rather than making the project sound more advanced than it is. A README is meant to explain what the project does and how someone can use it. 

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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
Tech Stack
Python

LangChain

Hugging Face Sentence Transformers

ChromaDB

Ollama

Llama 3.2

Gradio

PyPDF

Project Structure
ragchatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
The PDF knowledge base is not included in this GitHub repository.

Main Components
rag.py
This file contains the main RAG pipeline.

It:

Loads the PDF using PyPDF

Splits the document into smaller chunks

Creates vector embeddings using Sentence Transformers

Stores the document chunks in ChromaDB

Retrieves relevant chunks using similarity search

Combines the retrieved context with the user's question

Sends the context and question to the local LLM

Generates the final answer

app.py
This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

Local LLM
This project uses Ollama to run the language model locally.

Ollama
└── llama3.2:3b
Using a local model allowed me to build and test the application without relying on a paid cloud LLM API.

Retrieval
The application uses embeddings to represent document chunks as numerical vectors.

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM
The retrieval stage helps the language model answer using information from the selected document rather than relying only on its general knowledge.

Setup
1. Clone the repository
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
For Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama
Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Add the PDF knowledge base
Place the required PDF inside:

data/
with the filename:

SN_MPF_Eng.pdf
The original PDF used during development is not included in this repository.

7. Run the chatbot
python app.py
The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

http://127.0.0.1:7860
Example Questions
You can ask questions related to the information contained in the PDF.

For example:

What are the three types of MPF scheme?
What is an employer sponsored scheme?
The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

What I Learned
This project gave me practical exposure to the workflow behind a RAG application.

RAG concepts
Document loading

Text chunking

Embeddings

Vector databases

Similarity search

Retrieval-Augmented Generation

Prompt construction

Local LLMs

Development workflow
Python virtual environments

Installing and managing dependencies

Working with files and folders

Running Python applications from PowerShell

Connecting a backend pipeline to a user interface

Using Ollama for local AI

Using Git

Creating commits

Pushing code to GitHub

Writing project documentation

Learning Journey
This project was built after attending a hands-on introductory session on:

RAG

AI Agents

Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
Current Limitations
This is an early learning version of the project.

Some areas that can be improved include:

Better retrieval quality

Source/page references for answers

More efficient vector database handling

Conversation memory

Support for multiple documents

Better error handling

Retrieval and answer evaluation

Improved chatbot UI

Public deployment

Future Improvements
Planned improvements include:

Avoid rebuilding the vector database every time the application starts

Add page/source citations to retrieved answers

Add support for multiple PDF documents

Add conversation memory

Improve retrieval quality

Add evaluation for retrieval and answer accuracy

Improve the Gradio interface

Deploy the chatbot publicly

Experiment with different embedding models

Compare different local LLMs

Key Takeaway
The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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
This project is part of my hands-on learning journey into AI engineering and software development.

Disclaimer
This repository is a learning project.

The original PDF knowledge source is not included in this repository.


### Now do only this

1. **Ctrl + A** in Notepad
2. Paste the entire README above
3. **Ctrl + S**
4. Close Notepad
5. In PowerShell run:

```powershell
dir
You should now see README.md.

Don't git add, commit, or push yet. We'll inspect it first.




Ad
Ads do not influence the answers you get from ChatGPT. Your chats stay private. 
Learn about ads and personalization

I pasted this -# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

text
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

Yes — that is correct so far. You have pasted the first section of the README, including the RAG flow diagram.

GitHub will render the triple-backtick section as a formatted code/diagram block when the README is displayed. 

You don't need to redo anything.

Your current ending is:

Local LLM (Llama 3.2)
 ↓
Generated answer
Now continue with the rest of the README I gave you, starting exactly with:

## Tech Stack
Paste everything from there through:

## Disclaimer

This repository is a learning project.

The original PDF knowledge source is not included in this repository.
Then:

Ctrl + S

Close Notepad.

Run:

dir
Send me the output.

Don't commit/push yet. We'll verify the README first, then commit it as a separate Git change.


give it again

Absolutely — let's make this simple. Replace whatever is currently in README.md with this complete version in one paste.

GitHub recommends a README to explain a repository, and Markdown supports the headings, lists, links, and code blocks we're using here. 

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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
Tech Stack
Python

LangChain

Hugging Face Sentence Transformers

ChromaDB

Ollama

Llama 3.2

Gradio

PyPDF

Project Structure
ragchatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
The PDF knowledge base is not included in this GitHub repository.

Main Components
rag.py
This file contains the main RAG pipeline.

It:

Loads the PDF using PyPDF

Splits the document into smaller chunks

Creates vector embeddings using Sentence Transformers

Stores the document chunks in ChromaDB

Retrieves relevant chunks using similarity search

Combines the retrieved context with the user's question

Sends the context and question to the local LLM

Generates the final answer

app.py
This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

Local LLM
This project uses Ollama to run the language model locally.

Ollama
└── llama3.2:3b
Using a local model allowed me to build and test the application without relying on a paid cloud LLM API.

Retrieval
The application uses embeddings to represent document chunks as numerical vectors.

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM
The retrieval stage helps the language model answer using information from the selected document rather than relying only on its general knowledge.

Setup
1. Clone the repository
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
For Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama
Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Add the PDF knowledge base
Place the required PDF inside:

data/
with the filename:

SN_MPF_Eng.pdf
The original PDF used during development is not included in this repository.

7. Run the chatbot
python app.py
The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

http://127.0.0.1:7860
Example Questions
You can ask questions related to the information contained in the PDF.

For example:

What are the three types of MPF scheme?
What is an employer sponsored scheme?
The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

What I Learned
This project gave me practical exposure to the workflow behind a RAG application.

RAG Concepts
Document loading

Text chunking

Embeddings

Vector databases

Similarity search

Retrieval-Augmented Generation

Prompt construction

Local LLMs

Development Workflow
Python virtual environments

Installing and managing dependencies

Working with files and folders

Running Python applications from PowerShell

Connecting a backend pipeline to a user interface

Using Ollama for local AI

Using Git

Creating commits

Pushing code to GitHub

Writing project documentation

Learning Journey
This project was built after attending a hands-on introductory session on:

RAG

AI Agents

Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
Current Limitations
This is an early learning version of the project.

Some areas that can be improved include:

Better retrieval quality

Source/page references for answers

More efficient vector database handling

Conversation memory

Support for multiple documents

Better error handling

Retrieval and answer evaluation

Improved chatbot UI

Public deployment

Future Improvements
Planned improvements include:

Avoid rebuilding the vector database every time the application starts

Add page/source citations to retrieved answers

Add support for multiple PDF documents

Add conversation memory

Improve retrieval quality

Add evaluation for retrieval and answer accuracy

Improve the Gradio interface

Deploy the chatbot publicly

Experiment with different embedding models

Compare different local LLMs

Key Takeaway
The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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
This project is part of my hands-on learning journey into AI engineering and software development.

Disclaimer
This repository is a learning project.

The original PDF knowledge source is not included in this repository.


### After pasting

Do exactly these 3 things:

**1.** `Ctrl + S`  
**2.** Close Notepad  
**3.** Run:

```powershell
dir
You should see README.md.

Don't run git add yet. We'll check it first.

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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


Absolutely. Here is the entire README in one go, so you can select everything, copy it, and paste it into Notepad.

I’ve also slightly cleaned it up so it accurately reflects what you actually built rather than making the project sound more advanced than it is. A README is meant to explain what the project does and how someone can use it. 

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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
Tech Stack
Python

LangChain

Hugging Face Sentence Transformers

ChromaDB

Ollama

Llama 3.2

Gradio

PyPDF

Project Structure
ragchatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
The PDF knowledge base is not included in this GitHub repository.

Main Components
rag.py
This file contains the main RAG pipeline.

It:

Loads the PDF using PyPDF

Splits the document into smaller chunks

Creates vector embeddings using Sentence Transformers

Stores the document chunks in ChromaDB

Retrieves relevant chunks using similarity search

Combines the retrieved context with the user's question

Sends the context and question to the local LLM

Generates the final answer

app.py
This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

Local LLM
This project uses Ollama to run the language model locally.

Ollama
└── llama3.2:3b
Using a local model allowed me to build and test the application without relying on a paid cloud LLM API.

Retrieval
The application uses embeddings to represent document chunks as numerical vectors.

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM
The retrieval stage helps the language model answer using information from the selected document rather than relying only on its general knowledge.

Setup
1. Clone the repository
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
For Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama
Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Add the PDF knowledge base
Place the required PDF inside:

data/
with the filename:

SN_MPF_Eng.pdf
The original PDF used during development is not included in this repository.

7. Run the chatbot
python app.py
The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

http://127.0.0.1:7860
Example Questions
You can ask questions related to the information contained in the PDF.

For example:

What are the three types of MPF scheme?
What is an employer sponsored scheme?
The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

What I Learned
This project gave me practical exposure to the workflow behind a RAG application.

RAG concepts
Document loading

Text chunking

Embeddings

Vector databases

Similarity search

Retrieval-Augmented Generation

Prompt construction

Local LLMs

Development workflow
Python virtual environments

Installing and managing dependencies

Working with files and folders

Running Python applications from PowerShell

Connecting a backend pipeline to a user interface

Using Ollama for local AI

Using Git

Creating commits

Pushing code to GitHub

Writing project documentation

Learning Journey
This project was built after attending a hands-on introductory session on:

RAG

AI Agents

Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
Current Limitations
This is an early learning version of the project.

Some areas that can be improved include:

Better retrieval quality

Source/page references for answers

More efficient vector database handling

Conversation memory

Support for multiple documents

Better error handling

Retrieval and answer evaluation

Improved chatbot UI

Public deployment

Future Improvements
Planned improvements include:

Avoid rebuilding the vector database every time the application starts

Add page/source citations to retrieved answers

Add support for multiple PDF documents

Add conversation memory

Improve retrieval quality

Add evaluation for retrieval and answer accuracy

Improve the Gradio interface

Deploy the chatbot publicly

Experiment with different embedding models

Compare different local LLMs

Key Takeaway
The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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
This project is part of my hands-on learning journey into AI engineering and software development.

Disclaimer
This repository is a learning project.

The original PDF knowledge source is not included in this repository.


### Now do only this

1. **Ctrl + A** in Notepad
2. Paste the entire README above
3. **Ctrl + S**
4. Close Notepad
5. In PowerShell run:

```powershell
dir
You should now see README.md.

Don't git add, commit, or push yet. We'll inspect it first.




Ad
Ads do not influence the answers you get from ChatGPT. Your chats stay private. 
Learn about ads and personalization

I pasted this -# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

text
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

Yes — that is correct so far. You have pasted the first section of the README, including the RAG flow diagram.

GitHub will render the triple-backtick section as a formatted code/diagram block when the README is displayed. 

You don't need to redo anything.

Your current ending is:

Local LLM (Llama 3.2)
 ↓
Generated answer
Now continue with the rest of the README I gave you, starting exactly with:

## Tech Stack
Paste everything from there through:

## Disclaimer

This repository is a learning project.

The original PDF knowledge source is not included in this repository.
Then:

Ctrl + S

Close Notepad.

Run:

dir
Send me the output.

Don't commit/push yet. We'll verify the README first, then commit it as a separate Git change.


give it again

Absolutely — let's make this simple. Replace whatever is currently in README.md with this complete version in one paste.

GitHub recommends a README to explain a repository, and Markdown supports the headings, lists, links, and code blocks we're using here. 

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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
Tech Stack
Python

LangChain

Hugging Face Sentence Transformers

ChromaDB

Ollama

Llama 3.2

Gradio

PyPDF

Project Structure
ragchatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
The PDF knowledge base is not included in this GitHub repository.

Main Components
rag.py
This file contains the main RAG pipeline.

It:

Loads the PDF using PyPDF

Splits the document into smaller chunks

Creates vector embeddings using Sentence Transformers

Stores the document chunks in ChromaDB

Retrieves relevant chunks using similarity search

Combines the retrieved context with the user's question

Sends the context and question to the local LLM

Generates the final answer

app.py
This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

Local LLM
This project uses Ollama to run the language model locally.

Ollama
└── llama3.2:3b
Using a local model allowed me to build and test the application without relying on a paid cloud LLM API.

Retrieval
The application uses embeddings to represent document chunks as numerical vectors.

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM
The retrieval stage helps the language model answer using information from the selected document rather than relying only on its general knowledge.

Setup
1. Clone the repository
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
For Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama
Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Add the PDF knowledge base
Place the required PDF inside:

data/
with the filename:

SN_MPF_Eng.pdf
The original PDF used during development is not included in this repository.

7. Run the chatbot
python app.py
The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

http://127.0.0.1:7860
Example Questions
You can ask questions related to the information contained in the PDF.

For example:

What are the three types of MPF scheme?
What is an employer sponsored scheme?
The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

What I Learned
This project gave me practical exposure to the workflow behind a RAG application.

RAG Concepts
Document loading

Text chunking

Embeddings

Vector databases

Similarity search

Retrieval-Augmented Generation

Prompt construction

Local LLMs

Development Workflow
Python virtual environments

Installing and managing dependencies

Working with files and folders

Running Python applications from PowerShell

Connecting a backend pipeline to a user interface

Using Ollama for local AI

Using Git

Creating commits

Pushing code to GitHub

Writing project documentation

Learning Journey
This project was built after attending a hands-on introductory session on:

RAG

AI Agents

Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
Current Limitations
This is an early learning version of the project.

Some areas that can be improved include:

Better retrieval quality

Source/page references for answers

More efficient vector database handling

Conversation memory

Support for multiple documents

Better error handling

Retrieval and answer evaluation

Improved chatbot UI

Public deployment

Future Improvements
Planned improvements include:

Avoid rebuilding the vector database every time the application starts

Add page/source citations to retrieved answers

Add support for multiple PDF documents

Add conversation memory

Improve retrieval quality

Add evaluation for retrieval and answer accuracy

Improve the Gradio interface

Deploy the chatbot publicly

Experiment with different embedding models

Compare different local LLMs

Key Takeaway
The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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
This project is part of my hands-on learning journey into AI engineering and software development.

Disclaimer
This repository is a learning project.

The original PDF knowledge source is not included in this repository.


### After pasting

Do exactly these 3 things:

**1.** `Ctrl + S`  
**2.** Close Notepad  
**3.** Run:

```powershell
dir
You should see README.md.

Don't run git add yet. We'll check it first.

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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


Absolutely. Here is the entire README in one go, so you can select everything, copy it, and paste it into Notepad.

I’ve also slightly cleaned it up so it accurately reflects what you actually built rather than making the project sound more advanced than it is. A README is meant to explain what the project does and how someone can use it. 

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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
Tech Stack
Python

LangChain

Hugging Face Sentence Transformers

ChromaDB

Ollama

Llama 3.2

Gradio

PyPDF

Project Structure
ragchatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
The PDF knowledge base is not included in this GitHub repository.

Main Components
rag.py
This file contains the main RAG pipeline.

It:

Loads the PDF using PyPDF

Splits the document into smaller chunks

Creates vector embeddings using Sentence Transformers

Stores the document chunks in ChromaDB

Retrieves relevant chunks using similarity search

Combines the retrieved context with the user's question

Sends the context and question to the local LLM

Generates the final answer

app.py
This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

Local LLM
This project uses Ollama to run the language model locally.

Ollama
└── llama3.2:3b
Using a local model allowed me to build and test the application without relying on a paid cloud LLM API.

Retrieval
The application uses embeddings to represent document chunks as numerical vectors.

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM
The retrieval stage helps the language model answer using information from the selected document rather than relying only on its general knowledge.

Setup
1. Clone the repository
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
For Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama
Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Add the PDF knowledge base
Place the required PDF inside:

data/
with the filename:

SN_MPF_Eng.pdf
The original PDF used during development is not included in this repository.

7. Run the chatbot
python app.py
The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

http://127.0.0.1:7860
Example Questions
You can ask questions related to the information contained in the PDF.

For example:

What are the three types of MPF scheme?
What is an employer sponsored scheme?
The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

What I Learned
This project gave me practical exposure to the workflow behind a RAG application.

RAG concepts
Document loading

Text chunking

Embeddings

Vector databases

Similarity search

Retrieval-Augmented Generation

Prompt construction

Local LLMs

Development workflow
Python virtual environments

Installing and managing dependencies

Working with files and folders

Running Python applications from PowerShell

Connecting a backend pipeline to a user interface

Using Ollama for local AI

Using Git

Creating commits

Pushing code to GitHub

Writing project documentation

Learning Journey
This project was built after attending a hands-on introductory session on:

RAG

AI Agents

Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
Current Limitations
This is an early learning version of the project.

Some areas that can be improved include:

Better retrieval quality

Source/page references for answers

More efficient vector database handling

Conversation memory

Support for multiple documents

Better error handling

Retrieval and answer evaluation

Improved chatbot UI

Public deployment

Future Improvements
Planned improvements include:

Avoid rebuilding the vector database every time the application starts

Add page/source citations to retrieved answers

Add support for multiple PDF documents

Add conversation memory

Improve retrieval quality

Add evaluation for retrieval and answer accuracy

Improve the Gradio interface

Deploy the chatbot publicly

Experiment with different embedding models

Compare different local LLMs

Key Takeaway
The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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
This project is part of my hands-on learning journey into AI engineering and software development.

Disclaimer
This repository is a learning project.

The original PDF knowledge source is not included in this repository.


### Now do only this

1. **Ctrl + A** in Notepad
2. Paste the entire README above
3. **Ctrl + S**
4. Close Notepad
5. In PowerShell run:

```powershell
dir
You should now see README.md.

Don't git add, commit, or push yet. We'll inspect it first.




Ad
Ads do not influence the answers you get from ChatGPT. Your chats stay private. 
Learn about ads and personalization

I pasted this -# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

text
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

Yes — that is correct so far. You have pasted the first section of the README, including the RAG flow diagram.

GitHub will render the triple-backtick section as a formatted code/diagram block when the README is displayed. 

You don't need to redo anything.

Your current ending is:

Local LLM (Llama 3.2)
 ↓
Generated answer
Now continue with the rest of the README I gave you, starting exactly with:

## Tech Stack
Paste everything from there through:

## Disclaimer

This repository is a learning project.

The original PDF knowledge source is not included in this repository.
Then:

Ctrl + S

Close Notepad.

Run:

dir
Send me the output.

Don't commit/push yet. We'll verify the README first, then commit it as a separate Git change.


give it again

Absolutely — let's make this simple. Replace whatever is currently in README.md with this complete version in one paste.

GitHub recommends a README to explain a repository, and Markdown supports the headings, lists, links, and code blocks we're using here. 

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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
Tech Stack
Python

LangChain

Hugging Face Sentence Transformers

ChromaDB

Ollama

Llama 3.2

Gradio

PyPDF

Project Structure
ragchatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
The PDF knowledge base is not included in this GitHub repository.

Main Components
rag.py
This file contains the main RAG pipeline.

It:

Loads the PDF using PyPDF

Splits the document into smaller chunks

Creates vector embeddings using Sentence Transformers

Stores the document chunks in ChromaDB

Retrieves relevant chunks using similarity search

Combines the retrieved context with the user's question

Sends the context and question to the local LLM

Generates the final answer

app.py
This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

Local LLM
This project uses Ollama to run the language model locally.

Ollama
└── llama3.2:3b
Using a local model allowed me to build and test the application without relying on a paid cloud LLM API.

Retrieval
The application uses embeddings to represent document chunks as numerical vectors.

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM
The retrieval stage helps the language model answer using information from the selected document rather than relying only on its general knowledge.

Setup
1. Clone the repository
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
For Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama
Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Add the PDF knowledge base
Place the required PDF inside:

data/
with the filename:

SN_MPF_Eng.pdf
The original PDF used during development is not included in this repository.

7. Run the chatbot
python app.py
The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

http://127.0.0.1:7860
Example Questions
You can ask questions related to the information contained in the PDF.

For example:

What are the three types of MPF scheme?
What is an employer sponsored scheme?
The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

What I Learned
This project gave me practical exposure to the workflow behind a RAG application.

RAG Concepts
Document loading

Text chunking

Embeddings

Vector databases

Similarity search

Retrieval-Augmented Generation

Prompt construction

Local LLMs

Development Workflow
Python virtual environments

Installing and managing dependencies

Working with files and folders

Running Python applications from PowerShell

Connecting a backend pipeline to a user interface

Using Ollama for local AI

Using Git

Creating commits

Pushing code to GitHub

Writing project documentation

Learning Journey
This project was built after attending a hands-on introductory session on:

RAG

AI Agents

Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
Current Limitations
This is an early learning version of the project.

Some areas that can be improved include:

Better retrieval quality

Source/page references for answers

More efficient vector database handling

Conversation memory

Support for multiple documents

Better error handling

Retrieval and answer evaluation

Improved chatbot UI

Public deployment

Future Improvements
Planned improvements include:

Avoid rebuilding the vector database every time the application starts

Add page/source citations to retrieved answers

Add support for multiple PDF documents

Add conversation memory

Improve retrieval quality

Add evaluation for retrieval and answer accuracy

Improve the Gradio interface

Deploy the chatbot publicly

Experiment with different embedding models

Compare different local LLMs

Key Takeaway
The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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
This project is part of my hands-on learning journey into AI engineering and software development.

Disclaimer
This repository is a learning project.

The original PDF knowledge source is not included in this repository.


### After pasting

Do exactly these 3 things:

**1.** `Ctrl + S`  
**2.** Close Notepad  
**3.** Run:

```powershell
dir
You should see README.md.

Don't run git add yet. We'll check it first.

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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


Absolutely. Here is the entire README in one go, so you can select everything, copy it, and paste it into Notepad.

I’ve also slightly cleaned it up so it accurately reflects what you actually built rather than making the project sound more advanced than it is. A README is meant to explain what the project does and how someone can use it. 

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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
Tech Stack
Python

LangChain

Hugging Face Sentence Transformers

ChromaDB

Ollama

Llama 3.2

Gradio

PyPDF

Project Structure
ragchatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
The PDF knowledge base is not included in this GitHub repository.

Main Components
rag.py
This file contains the main RAG pipeline.

It:

Loads the PDF using PyPDF

Splits the document into smaller chunks

Creates vector embeddings using Sentence Transformers

Stores the document chunks in ChromaDB

Retrieves relevant chunks using similarity search

Combines the retrieved context with the user's question

Sends the context and question to the local LLM

Generates the final answer

app.py
This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

Local LLM
This project uses Ollama to run the language model locally.

Ollama
└── llama3.2:3b
Using a local model allowed me to build and test the application without relying on a paid cloud LLM API.

Retrieval
The application uses embeddings to represent document chunks as numerical vectors.

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM
The retrieval stage helps the language model answer using information from the selected document rather than relying only on its general knowledge.

Setup
1. Clone the repository
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
For Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama
Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Add the PDF knowledge base
Place the required PDF inside:

data/
with the filename:

SN_MPF_Eng.pdf
The original PDF used during development is not included in this repository.

7. Run the chatbot
python app.py
The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

http://127.0.0.1:7860
Example Questions
You can ask questions related to the information contained in the PDF.

For example:

What are the three types of MPF scheme?
What is an employer sponsored scheme?
The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

What I Learned
This project gave me practical exposure to the workflow behind a RAG application.

RAG concepts
Document loading

Text chunking

Embeddings

Vector databases

Similarity search

Retrieval-Augmented Generation

Prompt construction

Local LLMs

Development workflow
Python virtual environments

Installing and managing dependencies

Working with files and folders

Running Python applications from PowerShell

Connecting a backend pipeline to a user interface

Using Ollama for local AI

Using Git

Creating commits

Pushing code to GitHub

Writing project documentation

Learning Journey
This project was built after attending a hands-on introductory session on:

RAG

AI Agents

Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
Current Limitations
This is an early learning version of the project.

Some areas that can be improved include:

Better retrieval quality

Source/page references for answers

More efficient vector database handling

Conversation memory

Support for multiple documents

Better error handling

Retrieval and answer evaluation

Improved chatbot UI

Public deployment

Future Improvements
Planned improvements include:

Avoid rebuilding the vector database every time the application starts

Add page/source citations to retrieved answers

Add support for multiple PDF documents

Add conversation memory

Improve retrieval quality

Add evaluation for retrieval and answer accuracy

Improve the Gradio interface

Deploy the chatbot publicly

Experiment with different embedding models

Compare different local LLMs

Key Takeaway
The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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
This project is part of my hands-on learning journey into AI engineering and software development.

Disclaimer
This repository is a learning project.

The original PDF knowledge source is not included in this repository.


### Now do only this

1. **Ctrl + A** in Notepad
2. Paste the entire README above
3. **Ctrl + S**
4. Close Notepad
5. In PowerShell run:

```powershell
dir
You should now see README.md.

Don't git add, commit, or push yet. We'll inspect it first.




Ad
Ads do not influence the answers you get from ChatGPT. Your chats stay private. 
Learn about ads and personalization

I pasted this -# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

text
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

Yes — that is correct so far. You have pasted the first section of the README, including the RAG flow diagram.

GitHub will render the triple-backtick section as a formatted code/diagram block when the README is displayed. 

You don't need to redo anything.

Your current ending is:

Local LLM (Llama 3.2)
 ↓
Generated answer
Now continue with the rest of the README I gave you, starting exactly with:

## Tech Stack
Paste everything from there through:

## Disclaimer

This repository is a learning project.

The original PDF knowledge source is not included in this repository.
Then:

Ctrl + S

Close Notepad.

Run:

dir
Send me the output.

Don't commit/push yet. We'll verify the README first, then commit it as a separate Git change.


give it again

Absolutely — let's make this simple. Replace whatever is currently in README.md with this complete version in one paste.

GitHub recommends a README to explain a repository, and Markdown supports the headings, lists, links, and code blocks we're using here. 

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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
Tech Stack
Python

LangChain

Hugging Face Sentence Transformers

ChromaDB

Ollama

Llama 3.2

Gradio

PyPDF

Project Structure
ragchatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
The PDF knowledge base is not included in this GitHub repository.

Main Components
rag.py
This file contains the main RAG pipeline.

It:

Loads the PDF using PyPDF

Splits the document into smaller chunks

Creates vector embeddings using Sentence Transformers

Stores the document chunks in ChromaDB

Retrieves relevant chunks using similarity search

Combines the retrieved context with the user's question

Sends the context and question to the local LLM

Generates the final answer

app.py
This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

Local LLM
This project uses Ollama to run the language model locally.

Ollama
└── llama3.2:3b
Using a local model allowed me to build and test the application without relying on a paid cloud LLM API.

Retrieval
The application uses embeddings to represent document chunks as numerical vectors.

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM
The retrieval stage helps the language model answer using information from the selected document rather than relying only on its general knowledge.

Setup
1. Clone the repository
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment
For Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama
Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Add the PDF knowledge base
Place the required PDF inside:

data/
with the filename:

SN_MPF_Eng.pdf
The original PDF used during development is not included in this repository.

7. Run the chatbot
python app.py
The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

http://127.0.0.1:7860
Example Questions
You can ask questions related to the information contained in the PDF.

For example:

What are the three types of MPF scheme?
What is an employer sponsored scheme?
The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

What I Learned
This project gave me practical exposure to the workflow behind a RAG application.

RAG Concepts
Document loading

Text chunking

Embeddings

Vector databases

Similarity search

Retrieval-Augmented Generation

Prompt construction

Local LLMs

Development Workflow
Python virtual environments

Installing and managing dependencies

Working with files and folders

Running Python applications from PowerShell

Connecting a backend pipeline to a user interface

Using Ollama for local AI

Using Git

Creating commits

Pushing code to GitHub

Writing project documentation

Learning Journey
This project was built after attending a hands-on introductory session on:

RAG

AI Agents

Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
Current Limitations
This is an early learning version of the project.

Some areas that can be improved include:

Better retrieval quality

Source/page references for answers

More efficient vector database handling

Conversation memory

Support for multiple documents

Better error handling

Retrieval and answer evaluation

Improved chatbot UI

Public deployment

Future Improvements
Planned improvements include:

Avoid rebuilding the vector database every time the application starts

Add page/source citations to retrieved answers

Add support for multiple PDF documents

Add conversation memory

Improve retrieval quality

Add evaluation for retrieval and answer accuracy

Improve the Gradio interface

Deploy the chatbot publicly

Experiment with different embedding models

Compare different local LLMs

Key Takeaway
The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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
This project is part of my hands-on learning journey into AI engineering and software development.

Disclaimer
This repository is a learning project.

The original PDF knowledge source is not included in this repository.


### After pasting

Do exactly these 3 things:

**1.** `Ctrl + S`  
**2.** Close Notepad  
**3.** Run:

```powershell
dir
You should see README.md.

Don't run git add yet. We'll check it first.

# RAG Chatbox

A beginner-built Retrieval-Augmented Generation (RAG) chatbot that answers questions from a PDF knowledge base using a local Large Language Model (LLM).

## What is this project?

This project was built as a hands-on learning project to understand how a RAG application works from end to end.

Instead of asking an AI model to answer only from its general knowledge, the application first searches for relevant information from a PDF knowledge base and then provides that retrieved information to a local language model to generate an answer.

The project helped me understand the practical workflow behind a RAG application, from loading a document to creating a working chatbot interface.

## How RAG works in this project

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
## Tech Stack

- Python
- LangChain
- Hugging Face Sentence Transformers
- ChromaDB
- Ollama
- Llama 3.2
- Gradio
- PyPDF

## Project Structure

```text
ragchatbox/
│
├── data/
│   └── SN_MPF_Eng.pdf
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
Main Components
rag.py

This file contains the main RAG pipeline.

It:

Loads the PDF using PyPDF
Splits the document into smaller chunks
Creates vector embeddings using Sentence Transformers
Stores the document chunks in ChromaDB
Retrieves relevant chunks using similarity search
Combines the retrieved context with the user's question
Sends the context and question to the local LLM
Generates the final answer
app.py

This file provides the chatbot interface using Gradio.

The user's question is passed from the web interface to the RAG pipeline, and the generated answer is displayed back in the chatbot.

Local LLM

This project uses Ollama to run the language model locally.

Ollama
└── llama3.2:3b

Using a local model allowed me to build and test the application without relying on a paid cloud LLM API.

Retrieval

The application uses embeddings to represent document chunks as numerical vectors.

When a user asks a question:

User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Find Relevant Chunks
      ↓
Send Relevant Context to LLM

The retrieval stage helps the language model answer using information from the selected document rather than relying only on its general knowledge.

Setup
1. Clone the repository
git clone https://github.com/noorulhuda07/rag_chatbox.git
cd rag_chatbox
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment

For Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install Ollama

Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Add the PDF knowledge base

Place the required PDF inside:

data/

with the filename:

SN_MPF_Eng.pdf

The original PDF used during development is not included in this repository.

7. Run the chatbot
python app.py

The Gradio application will start locally.

Open the local URL shown in the terminal.

Usually:

http://127.0.0.1:7860
Example Questions

You can ask questions related to the information contained in the PDF.

For example:

What are the three types of MPF scheme?
What is an employer sponsored scheme?

The chatbot retrieves relevant sections from the document and uses them as context for the generated answer.

What I Learned

This project gave me practical exposure to the workflow behind a RAG application.

RAG Concepts
Document loading
Text chunking
Embeddings
Vector databases
Similarity search
Retrieval-Augmented Generation
Prompt construction
Local LLMs
Development Workflow
Python virtual environments
Installing and managing dependencies
Working with files and folders
Running Python applications from PowerShell
Connecting a backend pipeline to a user interface
Using Ollama for local AI
Using Git
Creating commits
Pushing code to GitHub
Writing project documentation
Learning Journey

This project was built after attending a hands-on introductory session on:

RAG
AI Agents
Agentic AI

Instead of stopping at the session, I reproduced the workflow locally to understand what each component actually does.

The goal was to move from:

Watching someone build
        ↓
Following the steps
        ↓
Running it locally
        ↓
Understanding each component
        ↓
Building and modifying independently
Current Limitations

This is an early learning version of the project.

Some areas that can be improved include:

Better retrieval quality
Source/page references for answers
More efficient vector database handling
Conversation memory
Support for multiple documents
Better error handling
Retrieval and answer evaluation
Improved chatbot UI
Public deployment
Future Improvements

Planned improvements include:

Avoid rebuilding the vector database every time the application starts
Add page/source citations to retrieved answers
Add support for multiple PDF documents
Add conversation memory
Improve retrieval quality
Add evaluation for retrieval and answer accuracy
Improve the Gradio interface
Deploy the chatbot publicly
Experiment with different embedding models
Compare different local LLMs
Key Takeaway

The main purpose of this project was not just to build a chatbot.

It was to understand how the individual components of a RAG system connect:

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

This project is part of my hands-on learning journey into AI engineering and software development.

Disclaimer

This repository is a learning project.

The original PDF knowledge source is not included in this repository.


**Important:** The ` ```text ` and ` ```bash ` and ` ```powershell ` lines are supposed to be there. They are Markdown formatting that makes the README look nice on GitHub. GitHub officially supports these fenced code blocks. :contentReference[oaicite:0]{index=0} 

### So your immediate action is ONLY:

1. Open `README.md` in Notepad.
2. Go to the end where you currently have **`Generated answer`**.
3. Paste the entire block above.
4. Press **Ctrl + S**.
5. **Do not run Git commands yet.**

Then tell me **“done”** and we'll check it together before committing anything.
can we sdit it in github directly, cause notepad
