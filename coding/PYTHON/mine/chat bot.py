import openai

# Replace this with your actual OpenAI API key
openai.api_key = "YOUR_API_KEY"

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {e}"

def chatbot():
    print("🤖 ChatGPT Bot is ready! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye! 👋")
            break
        reply = chat_with_gpt(user_input)
        print("Bot:", reply)

if __name__ == "__main__":
    chatbot()
