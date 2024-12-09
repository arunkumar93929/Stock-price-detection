from flask import Flask, render_template, request
import utils

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=["POST"])
def predict():
    # Get input data from user
    Open = float(request.form.get("Open"))
    High = float(request.form.get("High"))
    Low = float(request.form.get("Low"))
    Volume = float(request.form.get("Volume"))

    # Preprocess input and make a prediction
    prediction = utils.preprocess(Open, High, Low, Volume)

    # Pass values for graph visualization
    return render_template(
        'prediction.html',
        prediction=prediction,
        open_price=Open,
        high_price=High,
        low_price=Low,
        volume=Volume
    )

if __name__ == "__main__":
    app.run(debug=True)
