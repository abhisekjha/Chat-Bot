# GenAI-Bot

![GenAI-Bot](static/chatbot1.png)

## Introduction

**GenAI-Bot** is an AI-powered chatbot designed to provide personalized interactions and responses. The chatbot is built with a simple web interface that allows users to input messages and receive AI-generated responses in real-time.

## Features

- **Real-time Interaction**: Chat with the bot and get instant responses.
- **Simple and Intuitive UI**: User-friendly interface for a smooth chatting experience.
- **Customizable**: Modify the bot responses and user interface to fit specific needs.

## Installation

Follow these steps to set up and run the GenAI-Bot on your local machine.

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/abhisekjha/GenAI-Bot.git
    cd GenAI-Bot
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Get OPENAI API**

5. **Run the application**:
    ```bash
    python src/main.py
    ```

5. **Open your browser and navigate to** `http://127.0.0.1:5000` to start chatting with GenAI-Bot.

## Usage

- Open your browser and go to `http://127.0.0.1:5000`.
- Type your message in the input box and press Enter.
- The bot will respond with a message displayed in the chatbox.
