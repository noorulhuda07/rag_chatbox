from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaLLM


# ============================================================
# 1. LOAD THE PDF
# ============================================================

def load_documents():

    loader = PyPDFLoader("data/SN_MPF_Eng.pdf")

    documents = loader.load()

    print("Number of pages:", len(documents))

    return documents


# ============================================================
# 2. SPLIT THE PDF INTO CHUNKS
# ============================================================

def create_chunks(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    print("Number of chunks:", len(chunks))

    return chunks


# ============================================================
# 3. CREATE EMBEDDING MODEL
# ============================================================

def create_embedding_model():

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embedding_model


# ============================================================
# 4. CREATE VECTOR DATABASE
# ============================================================

def create_vector_store(chunks, embedding_model):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./chroma_db"
    )

    print("Vector database created successfully!")

    return vector_store


# ============================================================
# 5. CREATE LOCAL LLM
# ============================================================

def create_llm():

    llm = OllamaLLM(
        model="llama3.2:3b"
    )

    return llm


# ============================================================
# 6. ASK A QUESTION
# ============================================================

def ask_question(query, vector_store, llm):

    results = vector_store.max_marginal_relevance_search(
        query,
        k=3,
        fetch_k=10
    )

    context = "\n\n".join(
        result.page_content
        for result in results
    )

    prompt = f"""
You are an assistant that answers questions using the provided
document context.

Use ONLY the information in the context below to answer the question.

If the answer is not available in the context, say:

"The provided document context does not contain enough information
to answer this question."

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response


# ============================================================
# 7. BUILD THE RAG SYSTEM
# ============================================================

print("\nStarting RAG system...\n")

documents = load_documents()

chunks = create_chunks(documents)

embedding_model = create_embedding_model()

vector_store = create_vector_store(
    chunks,
    embedding_model
)

llm = create_llm()

print("\nRAG system is ready!\n")


# ============================================================
# 8. TEST THE RAG SYSTEM
# ============================================================

if __name__ == "__main__":

    query = "What are the three types of MPF scheme?"

    answer = ask_question(
        query,
        vector_store,
        llm
    )

    print("Question:")
    print(query)

    print("\nAnswer:")
    print(answer)
