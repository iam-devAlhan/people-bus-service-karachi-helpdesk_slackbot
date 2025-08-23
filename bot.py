import requests
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

dataset = pd.read_csv("notebook/People_Bus_Service_Scraped_Data.csv")

def ask_bot(user_input):
    prompt = f"""You are a helpdesk assistant for Bus Service. Given the data provided to you, your task is to provide info to customer regarding bus stops. If you don't know just say Sorry this is not in my information!

    {dataset}

    Rules:
    1. Don't try to assume things from your own
    2. Help people by answering their questions only
    3. Answer should be concise and clear


    Answer:
    """
    payload = {
        "model": "llama-3.1-8b-instant",  
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 300
    }

    r = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    if r.status_code == 200:
        response = r.json()["choices"][0]["message"]["content"]
        return response
    else:
        msg = "Error:" + r.status_code + r.text
        return msg
