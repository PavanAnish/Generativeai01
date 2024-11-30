from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatMessagePromptTemplate

template="""
Answer the Question Below,

Here is the conversation history : {context}

Questions : {question}

Answer :"""
model = OllamaLLM(model="llama3")
prompt = ChatMessagePromptTemplate.from_template(template)
chain = prompt | model

def handle_conv():
    context=""
    print("Welcome to the AI Chatbot! Type 'exit' to quit ")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:",result)
        context +=f"\nUser: {user_input}\nAI: {result}"
if __name__ == "__main__":
   print("hi")
    handle_conv()

