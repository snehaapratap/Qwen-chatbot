# Qwen Chatbot

Qwen Chatbot is an AI-powered conversational assistant built using the Qwen transformer model. This chatbot leverages advanced natural language processing (NLP) capabilities to deliver meaningful and intelligent conversations. It is packaged to run seamlessly in a Docker container for ease of setup and deployment.

---

## Features

- **Powered by Qwen Transformer**: Leverages advanced transformer-based AI for natural and intelligent interactions.
- **Ease of Deployment**: Dockerized for quick and consistent setup.
- **Flexible Access**: Interact through a web interface or API.

---

## Prerequisites

1. [Install Docker](https://docs.docker.com/get-docker/).
2. [Install Python 3.8+](https://www.python.org/downloads/) if you plan to run locally without Docker.

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/MariyaSha/chatbot_qwen.git
cd chatbot_qwen
docker build -t qwen-chatbot .
docker run -d -p 5000:5000 qwen-chatbot

