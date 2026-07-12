import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from flask import Flask,request,jsonify,render_template

application = Flask(__name__)
app=application

ridge_model=pickle.load(open('models/ridge.pkl','rb'))
StandardScaler=pickle.load(open('models/scaler.pkl','rb'))



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        temperature = float(request.form['Temperature'])
        rh = float(request.form['RH'])
        ws = float(request.form['Ws'])
        rain = float(request.form['Rain'])
        ffmc = float(request.form['FFMC'])
        dmc = float(request.form['DMC'])
        isi = float(request.form['ISI'])
        classes = int(request.form['Classes'])
        region = int(request.form['Region'])    

        new_data_scaled = StandardScaler.transform([[
            temperature,
            rh,
            ws,
            rain,
            ffmc,
            dmc,
            isi,
            classes,
            region
        ]])
        result=ridge_model.predict(new_data_scaled)

        return render_template('home.html',results=result[0])
 
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")