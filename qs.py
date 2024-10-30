from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

messages = [
    SystemMessage(content="You are a Formula 1 historian. You are being interviewed by a journalist."),
    HumanMessage(content="Why is Ferrari important to F1"),
]

response = model.invoke(messages)
parsed_response = parser.invoke(response)
print(parsed_response)
