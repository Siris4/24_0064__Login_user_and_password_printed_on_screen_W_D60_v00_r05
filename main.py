from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Ensure this template exists and is correct

@app.route("/login", methods=["GET", "POST"])
def receive_data():
    error = None
    username = None
    password = None
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Username: {username}, Password: {password}")  # Debug print
        if valid_login(username, password):
            return_message = log_the_user_in(username, password)
            print(f"Returning from login: {return_message}")  # Debug print
            return return_message
        else:
            error = "Invalid username and/or password"
            print(f"Error: {error}")  # Debug print
    response = render_template("login.html", error=error, username=username, password=password)
    print(f"Rendering login page: {response}")  # Debug print
    return response

def valid_login(username, password):
    # Simple logic for demonstration purposes
    valid = username == "gav4" and password == "gav4"
    print(f"Validation result for {username}: {valid}")  # Debug print
    return valid

def log_the_user_in(username, password):
    # Function requires both username and password
    return_message = f"<h1>Welcome {username}! You are successfully logged in, with the password {password}."
    print(f"Login successful for {username}: {return_message}")  # Debug print
    return return_message


if __name__ == "__main__":
    app.run(debug=True)
