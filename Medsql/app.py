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

@app.route('/doctor_portal')
def doctor_portal():
    return render_template('doctor_portal.html')

@app.route('/patient_portal')
def patient_portal():
    return render_template('patient_portal.html')

@app.route('/alert')
def alert():
    return render_template('alert.html')

@app.route('/TestResults')
def TestResults():
    return render_template('TestResults.html')




if __name__ == '__main__':
    app.run(debug=True)

