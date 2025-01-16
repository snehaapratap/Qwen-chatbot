from transformers import pipeline
import torch
from sty import fg

# set device to GPU if available
if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')
    
# set pipeline
pipe = pipeline(
    "text-generation", 
    "Qwen/Qwen2-1.5B", 
    device_map = device
)

def ask_question(message):
    # generate response
    response = pipe(
        message, 
        max_new_tokens = 128
    )[0]['generated_text'][-1]["content"]
    # trim response to the first occurrence of "\n"
    if response.find("\n") != -1:
        response = response[:response.index("\n") + 1]   
    # display response in yellow
    print(fg.yellow + response + fg.rs)

message = [
    {
        "role": "system",
        "content": """
        You are a friendly chatbot named Chatty
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

# ask introductory question
ask_question(message)

while True:
    # collect user input
    prompt = input("\nYour question:")
    # set user input as user message
    message[1]["content"] = prompt
    # stop loop if user types exit
    if prompt == "exit":
        break
    else:    
        # ask questions continuously
        ask_question(message)