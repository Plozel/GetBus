from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/schedule/')
def schedule():
    return render_template('schedule.html')

if __name__ == '__main__':
    app.run(debug=True)
