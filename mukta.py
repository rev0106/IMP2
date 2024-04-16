from flask import Flask, render_template , redirect ,session

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/hb")
def about():
    return render_template('hb.html')

if __name__ == '__main__':
    app.run(debug=True)