from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("registration.html")

@app.route('/submit', methods=['POST'])
def submit():
    fname = request.form['fname']
    lname = request.form['lname']
    age = request.form['age']
    phno = request.form['phno']
    return render_template("greetings.html", 
                           fname=fname, 
                           lname=lname, 
                           age=age, 
                           phno=phno)

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port=5000)
