# chatbot.py

def chatbot():
    print("🤖 Student Chatbot: Hi! How can I help you today?")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Study well! 📚")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello student! How are you?")
        elif "course" in user_input:
            print("🤖 Chatbot: We offer courses in Science, Commerce, and Arts.")
        elif "time table" in user_input or "schedule" in user_input:
            print("🤖 Chatbot: Classes start at 9 AM and end at 4 PM, with lunch at 1 PM.")
        elif "exam" in user_input:
            print("🤖 Chatbot: Exams will be held in December. Good luck! 🍀")
        else:
            print("🤖 Chatbot: Sorry, I don’t understand. Please ask about courses, timetable, or exams.")

if __name__ == "__main__":
    chatbot()
