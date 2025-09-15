from flask import Flask, render_template, request

app = Flask(__name__)

# Simple chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello student! How are you?"
    elif "course" in user_input:
        return "We offer courses in CSE, ISE, and EC."
    elif "time table" in user_input or "schedule" in user_input:
        return "Classes start at 9 AM and end at 4 PM, with lunch at 1 PM."
    elif "exam" in user_input:
        return "Exams will be held in December. Good luck! 🍀"
    elif "bye" in user_input:
        return "Goodbye! Study well! 📚"
    else:
        return "Sorry, I don’t understand. Please ask about courses, timetable, or exams."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.form["msg"]
    return chatbot_response(user_message)

if __name__ == "__main__":
    app.run(debug=True)
