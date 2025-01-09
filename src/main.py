import os
from openai import OpenAI
from dotenv import load_dotenv
from rag_system import RAGSYTEM
import chainlit as cl


load_dotenv()


data_path = "./data"
openai_client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST= os.getenv("HOST")
PORT = os.getenv("PORT")

db_connection_str = f"dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={HOST} port={PORT}"

print("db_connection_str", db_connection_str)

rag_system = RAGSYTEM(openai_client, db_connection_str, data_path=data_path)



@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    
    user_query = message.content
    
    user_query_context = rag_system.semantic_search(user_query)
        
    final_response = rag_system.generate_response(user_query_context, user_query)
    
    # Send a response back to the user
    await cl.Message(
        content= final_response,
    ).send()
