import gradio as gr

from rag import vector_store, llm, ask_question


def chat(message, history):

    response = ask_question(
        message,
        vector_store,
        llm
    )

    return response


demo = gr.ChatInterface(
    fn=chat,
    title="MPF RAG Chatbot",
    description="Ask questions about the MPF study notes."
)


demo.launch()