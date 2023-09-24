from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Weather Web App! Hackathon UMBC '23</h1>"

@app.route("/about")
def about():
    return "<h1>About</h1>"
    
if __name__ == '__main__':
    app.run(debug=True)