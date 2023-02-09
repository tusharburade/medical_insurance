from flask import Flask,render_template,jsonify,request,redirect,url_for
from project_app.utils import MedicalInsurance
import config
app = Flask(__name__)
@app.route("/")
def hello_flask():
    print("welcome")
    return render_template('login.html')

@app.route ("/result / <name>")
def result (name):
    return f"Hello {name}"

@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        data = request.form
        name = data['name']
        print('Name : ',name)
        return redirect(url_for("result", name = name))
    

@app.route("/predict_charges",methods = ["POST","GET"])
def get_insurance_charges():
    if request.method == "POST":
        data = request.form
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']
        med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
        charges = med_ins.get_predicted_charges()
        return jsonify ({'Result':f"Predicted medical insurance charges are : {charges}"})


app.run()