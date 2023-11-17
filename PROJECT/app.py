from flask import Flask,render_template,request
app = Flask(__name__)
import pickle
import numpy as np
import sklearn 

model = pickle.load(open("C:\\Users\\sanja\\Downloads\\zhc3zh\\ASD.pkl",'rb'))

@app.route('/')
def start():
    return render_template('Text.html')

@app.route('/login',methods =['POST'])

def login():
   
   A1 = request.form["A1"]
   A2 = request.form["A2"]
   A3 = request.form["A3"]
   A4 = request.form["A4"]
   A5 = request.form["A5"]
   A6 = request.form["A6"]
   A7 = request.form["A7"]
   A8 = request.form["A8"]
   A9 = request.form["A9"]
   A10= request.form["A10"]
   Age= request.form["Age"]
   Jundice = request.form["jd"]
   Autism= request.form["atm"]
   Used_app_before= request.form["app"]
   Result= request.form["res"]

   t =np.array([[int(A1),int(A2),int(A3),int(A4),int(A5),int(A6),int(A7),int(A8),int(A9),int(A10),float(Age),0,int(Jundice),int(Autism),int(Used_app_before),float(Result),5]])
   output =model.predict(t)
   print(output)

   return render_template("Text.html", y = "ASD detection result: "+str(np.round(output[0])))

if __name__ == '__main__' :
    app.run(debug=True)