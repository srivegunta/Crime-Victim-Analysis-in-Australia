# import necessary libraries
from flask import Flask, render_template, jsonify

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    return render_template("index.html")

# home page
@app.route("/home")
def home():
    return render_template("home.html")





 # model page
@app.route("/learn_more")
def model(): 
    #Jonno Example 
    model = joblib.load("model.pkl")
    prediction = model.predict(inputs)

    return render_template("learn_more.html", jsonify(prediction))





 # visualisations page
@app.route("/visualisations")
def visuals():
    return render_template("visualisations.html")


if __name__ == "__main__":
    app.run(debug=True)