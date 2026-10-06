from flask import Flask, render_template_string, request, redirect, session

app = Flask(__name__)
app.secret_key = "radha-secret-key"

USERNAME = "radha"
PASSWORD = "143"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>My Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f5f5f5;
            margin: 0;
            padding: 20px;
        }

        .box {
            max-width: 400px;
            margin: 80px auto;
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }

        h1 {
            text-align: center;
        }

        input {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 8px;
        }

        button {
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            border: none;
            border-radius: 8px;
            background: #333;
            color: white;
            font-size: 16px;
        }

        .error {
            color: red;
            text-align: center;
        }
    </style>
</head>

<body>

<div class="box">

{% if not session.get("logged_in") %}

    <h1>Login</h1>

    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>

    {% if error %}
        <p class="error">{{ error }}</p>
    {% endif %}

{% else %}

    <h1>Welcome!</h1>
    <p style="text-align:center;">You are successfully logged in.</p>

    <form action="/logout">
        <button type="submit">Logout</button>
    </form>

{% endif %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    error = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:
            session["logged_in"] = True
            return redirect("/")
        else:
            error = "Invalid username or password"

    return render_template_string(HTML, error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
