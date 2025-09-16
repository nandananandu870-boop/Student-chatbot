# chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello student! How are you?"
    elif "course" in user_input:
        return "We offer courses in Science, Commerce, and Arts."
    elif "time table" in user_input or "schedule" in user_input:
        return "Classes start at 9 AM and end at 4 PM, with lunch at 1 PM."
    elif "exam" in user_input:
        return "Exams will be held in December. Good luck! 🍀"
    elif "i want information about colleges" in user_input:  # ✅ new condition
        return "You can find college information on the official education board website."
    elif "bye" in user_input:
        return "Goodbye! Study well! 📚"
    else:
        return "Sorry, I don’t understand. Please ask about courses, timetable, or exams."
