# README for Simple Python Chatbot

## Overview

This project contains a simple rule-based chatbot implemented in Python. The chatbot interacts with users via the command line, responding to basic greetings and questions. It demonstrates fundamental Python programming concepts such as input handling, string matching, and control flow.

## Files

- [`chatbot.py`](chatbot.py): The main Python script containing the chatbot logic.
- [`example_conversation.txt`](example_conversation.txt): A sample conversation demonstrating how the chatbot interacts with a user.

## Features

- Greets the user and provides instructions.
- Responds to greetings like "hello" or "hi".
- Answers questions such as "how are you" and "what is your name".
- Offers help when prompted.
- Responds to thanks.
- Handles unrecognized input gracefully.
- Exits when the user types "bye".

## How It Works

The chatbot runs in a loop, waiting for user input. It converts the input to lowercase for easier matching and checks for specific keywords or phrases to determine the appropriate response.

Example interaction:
```
🤖 Chatbot: Hi! I'm your simple chatbot. Type 'bye' to exit.
You: hello
🤖 Chatbot: Hello there! How can I help you?
You: how are you
🤖 Chatbot: I'm just a bot, but I'm doing great! Thanks for asking.
You: bye
🤖 Chatbot: Goodbye! Have a nice day 😊
```

## Usage

1. **Requirements:**  
   - Python 3.x installed on your system.

2. **Running the Chatbot:**  
   Open a terminal in the project directory and run:
   ```sh
   python chatbot.py
   ```

3. **Interacting:**  
   - Type your messages after the `You:` prompt.
   - Type `bye` to exit the chatbot.

## Customization

You can add more responses or modify existing ones by editing the `chatbot.py` file. The chatbot uses simple `if-elif-else` statements to match user input.

## Example Conversation

See [`example_conversation.txt`](example_conversation.txt) for a sample chat session.

