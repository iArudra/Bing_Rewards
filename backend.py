# from flask import Flask, jsonify
# app = Flask(__name__)
# from flask_cors import CORS
# CORS(app)
# @app.route("/get-link")
# def get_link():
#     url = "https://www.bing.com/search?q=worldlist%20&qs=n&form=QBRE&sp=-1&lq=0&pq=worldlist%20&sc=12-10&sk=&cvid=3F3E83801316472F9D5819DB688F76E5"
#     return jsonify({
#         "url": url
#     })

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/get-link")
def get_link():
    return jsonify({
        "url": "https://www.bing.com/search?q=worldlist"
    })

if __name__ == "__main__":
    app.run(debug=True)
