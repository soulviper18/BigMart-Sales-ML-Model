# BigMart-Sales-ML-Model
BigMart-Sales-ML-Model
Overview

A machine learning web application for predicting product sales at Big Mart outlets, powered by a pre-trained model and served via app.py.

Project Contents

model.pkl: Serialized predictive model (trained offline)

app.py: Python script to load the model and provide a simple interface (API or UI) for generating predictions

Installation & Usage

Clone the repository:

git clone https://github.com/vaishnavmohan1129/BigMart-Sales-ML-Model.git
cd BigMart-Sales-ML-Model


(Optional) Set up a virtual environment and install dependencies:

python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
pip install -r requirements.txt


Run the app:

python app.py


The app will start a local server—open the displayed URL in your browser to input features and get a sales prediction.
