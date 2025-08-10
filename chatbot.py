# Easy Predefined Chatbot with Multiple Question Matching

responses = {
    ("hi", "hello", "hey"): "Hello! 👋",
    ("how are you", "how r u", "how's going"): "I'm fine, thanks! 😊",
    ("bye", "goodbye", "see you"): "Goodbye! Take care! 👋"
}

while True:
    user = input("You: ").lower()
    if user == "exit":
        print("Chatbot: Bye!")
        break
    
    found = False
    for questions, answer in responses.items():
        if user in questions:
            print("Chatbot:", answer)
            found = True
            break
    
    if not found:
        print("Chatbot: I don't understand.")