from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('frontpage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/Signup')
def Signup():
    return render_template('Signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

