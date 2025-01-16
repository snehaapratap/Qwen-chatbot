from transformers import pipeline
import torch
from sty import fg

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')
    
pipe = pipeline(
    "text-generation", 
    "Qwen/Qwen2-1.5B", 
    device_map = device
)

def ask_question(message):
    response = pipe(
        message, 
        max_new_tokens = 128
    )[0]['generated_text'][-1]["content"]
    if response.find("\n") != -1:
        response = response[:response.index("\n") + 1]   
    print(fg.yellow + response + fg.rs)

message = [
    {
        "role": "system",
        "content": """
        You are a friendly chatbot named Gwen
        """
    },
    {
        "role": "user", 
        "content": """
        Please introduce yourself and add
        'how can I help you today?' at
        the end of the response
        """
    }
]

ask_question(message)

while True:
    prompt = input("\nYour question:")
    message[1]["content"] = prompt
    if prompt == "exit":
        break
    else:    
        ask_question(message)