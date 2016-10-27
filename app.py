from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    with open('date.txt') as f:
        date = f.read()
    return date

if __name__ == "__main__":
    app.run(host='0.0.0.0')
