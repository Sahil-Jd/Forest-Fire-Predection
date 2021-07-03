from flask import Flask, render_template, request
from flask_cors import cross_origin
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from joblib import dump, load
app = Flask(__name__,template_folder='Templates')
model = load('Forest_Fire_Predictionjp_Heroku.pkl')
@app.route("/",methods=['GET'])
@cross_origin()
def home():
	return render_template("index.html")

@app.route("/predict",methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        # latitude
        latitude =float(request.form['latitude'])
        # longitude
        longitude = float(request.form['longitude'])
        # brightness
        brightness = float(request.form['brightness'])
        # track
        track = float(request.form['track'])
        # acq_time
        acq_time = int(request.form['acq_time'])
        # confidence
        confidence = int(request.form['confidence'])
        daynight =(request.form['daynight'])
        if(daynight=='day'):
            daynight=1
        else:
            daynight=0	
        prediction=model.predict([[latitude,longitude,brightness,track,acq_time,confidence,daynight]])
        output=round(prediction[0],2)
        if output>0:
            return render_template('predictor.html',prediction_text="Frp value is  {}".format(output))
    else:
        return render_template('predictor.html')

if __name__=="__main__":
    app.run(debug=True)
