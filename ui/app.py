from flask import Flask, render_template, request, jsonify
from main import main

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.to_dict()
        output = main(user_input)
        return jsonify(output)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
