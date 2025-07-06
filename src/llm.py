from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

def initiate_llm():
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
    return llm
