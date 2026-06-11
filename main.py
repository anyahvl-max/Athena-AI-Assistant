import google.generativeai as genai
genai.configure(api_key="AQ.Ab8RN6L7Ai7Wn0RcWDAxkzT3nStIWrXA_S4hAMZQtBD6vZoMOQ")
model = genai.GenerativeModel("gemini-2.5-flash")
print("AI Chatbot Ready!")
print("Type 'bye' to exit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot:Goodbye!")
        break
    
    response = model.generate_content(user_input)
    print("Bot:", response.text)
    print()  