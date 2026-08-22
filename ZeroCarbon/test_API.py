from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    api_key = os.getenv("API_KEY")
)

response = client.chat.completions.create(
    model = "meta-llama/Llama-3.1-8B-Instruct",
    messages = [
        {
            "role": "user",
            "content": "You are an experienced sustainability consultant."
            "Plant Name: Mumbai Plant"
            "Net Emissions: 72,720 kg CO₂"
            "Distance From Net-Zero: 78%"
            "Status: Action Needed"
            "Generate a professional executive summary."
        }
    ]
)

print(response.choices[0].message.content)