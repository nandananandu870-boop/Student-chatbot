from flask import Flask, render_template, request, redirect, url_for, session
import chatbot

app = Flask(__name__)
app.secret_key = "mysecretkey"  # needed for session handling

# simple student login data
users = {
    "student1": "nandana",
    "student2": "123456"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["nandana"]
        password = request.form["123456"]
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("chat"))
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")

@app.route("/chat")
def chat():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("index.html", user=session["user"])

@app.route("/get", methods=["POST"])
def get_bot_response():
    if "user" not in session:
        return "Please login first!"
    user_message = request.form["msg"]
    return chatbot.chatbot_response(user_message)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
