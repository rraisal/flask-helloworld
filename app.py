from flask import Flask
app = Flask(__name__)

@app.route("/")
    def hello():
        return "Devops is not a goal, but a never ending process of continual improvement"

if __name__ == "__main__":
    app.run()
