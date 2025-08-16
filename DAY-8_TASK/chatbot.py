def chatbot():
    print("🤖 Chatbot: Hi! I'm your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()  # Convert input to lowercase for easy matching

        # Exit condition
        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break

        # Rule-based responses
        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello there! How can I help you?")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just a bot, but I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("🤖 Chatbot: I'm a simple chatbot created using Python and if-else.")

        elif "help" in user_input:
            print("🤖 Chatbot: Sure! You can ask me about my name, how I am, or just say hello.")

        elif "thank you" in user_input or "thanks" in user_input:
            print("🤖 Chatbot: You're welcome! 😊")

        else:
            print("🤖 Chatbot: Sorry, I don't understand that yet.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
