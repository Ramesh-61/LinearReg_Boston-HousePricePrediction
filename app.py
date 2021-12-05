#Importing necessary libraries
from flask import Flask, render_template, request
import pickle
import numpy
from flask_cors import cross_origin

#initializing the flask app


app=Flask(__name__)

#route to display the home page
@app.route('/', methods=['GET'])
@cross_origin()
def home_page():
    return render_template("index.html")

#route to show the predictions
@app.route('/predict', methods=['POST','GET'])
@cross_origin()
def prediction():
    if request.method == 'POST':
        try:
            # Read the inputs from the user
            rm = float(request.form['RM'])
            lstat = float(request.form['LSTAT'])
            filename = 'Linear_Reg_Model.pickle'
            #loading the model from the storage
            load_model=pickle.load(open(filename,'rb'))
            #prediction using the loaded_model
            prediction_price = load_model.predict([[rm, lstat]])
            print("Prediction is: ", prediction_price)
            return render_template('results.html', prediction_price=float(numpy.round(prediction_price[0], 2)))
        except Exception as e:
            print("The exception message is :", e)
            return "Something is wrong"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



