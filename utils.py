# utils.py
def preprocess(Open, High, Low, Volume):
    try:
        # Convert inputs to floats
        Open = float(Open)
        High = float(High)
        Low = float(Low)
        Volume = float(Volume)
        
        # Dummy prediction logic (Replace with your model's logic)
        # Example: average price as prediction
        predicted_price = (Open + High + Low) / 3
        
        return f"Predicted Price: {predicted_price:.2f}"
    except ValueError:
        return "Error: Invalid input. Please enter numeric values."
