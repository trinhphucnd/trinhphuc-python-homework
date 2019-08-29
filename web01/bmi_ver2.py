from flask import Flask,render_template

app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:hieght>')
def bmi(weight,hieght):
    bmi_ = ((weight*10000)/(hieght*hieght))
    str_bmi = str(bmi_)
    if bmi_< 16: 
        return 'BMI : ' + str_bmi +  "  => Severely underweight"
    
    elif 16<= bmi_< 18.5: 
        return 'BMI : ' + str_bmi +  "   => Underweight"

    elif 18.5 <= bmi_< 25: 
        return 'BMI : ' + str_bmi +  "  => Normal"
    elif 25 <= str_bmi< 30: 
        return 'BMI : ' + str_bmi +  "  => Overweight"
    else: 
        return 'BMI : ' + str_bmi +  "  => Obese"

    
if __name__ == "__main__":
    app.run(debug=True)
