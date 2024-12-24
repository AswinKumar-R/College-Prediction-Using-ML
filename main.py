from flask import Flask, request, render_template
import pickle

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/handel_data", methods=["POST"])
def handel_data():
    student_name = request.form.get("student_name")
    sat_score = float(request.form.get("sat_score"))

    # Load model
    with open("single_linear.pk1", "rb") as file:
        model = pickle.load(file)

    # Predict GPA
    gpa_result = model.predict([[sat_score]])[0][0]

    # Render results page
    return render_template("predict.html", gpa_result=gpa_result, student_name=student_name)


if __name__ == "__main__":
    app.run(debug=True)
