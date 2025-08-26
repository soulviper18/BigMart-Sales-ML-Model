from flask import Flask, request, render_template
import numpy as np
import pickle

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Helper function to safely convert to float
            def safe_float(value, default=0.0):
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return default

            # Extract form data and safely convert
            Item_Indentifier = safe_float(request.form.get("Item_Identifier", 0))
            Item_weight = safe_float(request.form.get("Item_weight", 0))
            Item_Fat_Content = safe_float(request.form.get("Item_Fat_Content", 0))
            Item_visibility = safe_float(request.form.get("Item_visibility", 0))
            Item_Type = safe_float(request.form.get("Item_Type", 0))
            Item_MPR = safe_float(request.form.get("Item_MPR", 0))
            Outlet_identifier = safe_float(request.form.get("Outlet_identifier", 0))
            Outlet_established_year = safe_float(request.form.get("Outlet_established_year", 0))

            # Mappings for categorical features
            outlet_size_map = {
                'Small': 1.0,
                'Medium': 2.0,
                'High': 3.0
            }

            outlet_location_map = {
                'Tier 1': 1.0,
                'Tier 2': 2.0,
                'Tier 3': 3.0
            }

            outlet_type_map = {
                'Ware House': 1.0,
                'Shop': 2.0,
                'Super Market': 3.0,
                'Hyper Mart': 4.0
            }

            Outlet_size = outlet_size_map.get(request.form.get("Outlet_size", ''), 0.0)
            Outlet_location_type = outlet_location_map.get(request.form.get("Outlet_location_type", ''), 0.0)
            Outlet_type = outlet_type_map.get(request.form.get("Outlet_type", ''), 0.0)

            # Forming the feature array
            features = np.array([[
                Item_Indentifier,
                Item_weight,
                Item_Fat_Content,
                Item_visibility,
                Item_Type,
                Item_MPR,
                Outlet_identifier,
                Outlet_established_year,
                Outlet_size,
                Outlet_location_type,
                Outlet_type
            ]], dtype=np.float32)

            prediction = model.predict(features)[0]
            return render_template('index.html', prediction=f'Predicted Sales: {prediction:.2f}')

        except Exception as e:
            return render_template('index.html', prediction=f"Error occurred: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
