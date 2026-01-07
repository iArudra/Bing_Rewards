from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route("/list.txt")
def words():
    return send_from_directory(".", "list.txt")

app.run(debug=True)
