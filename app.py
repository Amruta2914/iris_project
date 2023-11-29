from flask import Flask,jsonify
import pickle

app = Flask(__name__) # module name is in __name__ , object of flask is created


@app.route('/') # url is cretaed using .route method , 1st api
def index():
    return "deafult API"

@app.route('/predict') # decorator is used using @, so that w/o changing function definition we can add another functionality, 
def iris_pred():
     
    with open("model.pkl","rb") as model:
        ml_model = pickle.load(model)
    
    SepalLengthCm = 6 
    SepalWidthCm = 4.8
    PetalLengthCm = 5.2
    PetalWidthCm = 3.75

    result = ml_model.predict([[SepalLengthCm, SepalWidthCm,PetalLengthCm,PetalWidthCm]])
    if result[0] == 2:
        iris_flower = "Iris-virginica" 
    if result[0] == 0:
        iris_flower = "Iris-setosa"
    if result[0] == 1:
        iris_flower = "Iris-versicolor"  

    return iris_flower

@app.route('/welcome')
def index1():
    return "Welcome to Velocity"

if __name__ == "__main__":
    app.run(debug=True)