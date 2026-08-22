from dotenv import load_dotenv
import os

load_dotenv()

API_token = os.getenv("API_KEY")

print(API_token)