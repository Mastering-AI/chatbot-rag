
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


def store_data():
    print("db_connection_str", db_connection_str)

    rag_system = RAGSYTEM(openai_client, db_connection_str, data_path=data_path)
    rag_system.store_documents()
    print("Data stored successfully")
    

if __name__ == "__main__":
    store_data()