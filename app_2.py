import flask
from flask import Flask, request,jsonify, render_template
import pickle

app=flask.Flask(__name__)
app.config["DEBUG"]=False

from flask_cors import CORS, cross_origin
CORS(app)

@app.route('/')
@cross_origin()

def home():
    return '<h> Hey how may I help you <\h>'
@app.route('/predict',methods=["GET"])
def predict():
	from sklearn.externals import joblib
	model= joblib.load('sales_predicting_model.ml')
	prediction_sales=model.predict([[0.504531,0.000000,0.186516,1.000000,0.1,0.112747,0.2,0.3]])
	return str(prediction_sales)

if __name__=="__main__":
	app.run(debug=True)