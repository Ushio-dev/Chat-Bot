from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def read_file():
    nuevo = ""
    
    with open("./datos.txt", "r") as file:
        for line in file:
            nuevo+= line + "\n"
    
    return nuevo


    
template = """
answer the question below in spanish.

Here is the information with products with this format name;link;price:
{list_info}

{context}

Question: {question}

Answer: 

"""

model = OllamaLLM(model="llama3", temperature=0.8)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
list_info = read_file()

def chat():
    print("welcome to the chat!")
    context = ""
    
    while True:
        question = input("You: ")
        if question == "stop":
            break
        
        result = chain.invoke({"list_info": list_info,"context": context, "question": question})
        print("Bot: ", result)
        context += f"Bot: {result}\nYou: {question}\n"
        

if __name__ == "__main__":
    chat()