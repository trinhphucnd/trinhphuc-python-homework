from flask import Flask,render_template

app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:hieght>')
def bmi(weight,hieght):
    bmi_ = ((weight*10000)/(hieght*hieght))
    return render_template('bmi.html',bmi_ = bmi_)
    
if __name__ == "__main__":
    app.run(debug=True)
