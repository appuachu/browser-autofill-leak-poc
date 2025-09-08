from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print("=== Autofill Data Captured ===")
        for field, value in request.form.items():
            print(f"{field}: {value}")

        name = request.form.get("name")
        email = request.form.get("email")
        return render_template("success.html", name=name, email=email)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
