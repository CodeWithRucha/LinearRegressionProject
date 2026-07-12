# Algerian Forest Fire Prediction App

This project is a Flask web application that predicts the fire-related target value for Algerian forest fire data using a trained machine learning model. The app takes user input for environmental and forest conditions and returns a prediction through a simple web interface.

## Project Overview

The application uses:
- Flask for the web interface
- scikit-learn for model inference
- pandas and numpy for data handling
- a pre-trained Ridge Regression model and scaler stored in the models folder

## Features

- User-friendly web form for input values
- Prediction based on important fire-related features
- Responsive HTML templates for input and result display

## Input Features

The app expects the following inputs:
- Temperature
- RH (Relative Humidity)
- Ws (Wind Speed)
- Rain
- FFMC
- DMC
- ISI
- Classes
- Region

## Project Structure

- application.py - Flask app and prediction logic
- templates/ - HTML pages for the frontend
- models/ - trained model and scaler files
- notebooks/ - EDA and model training notebooks
- requirements.txt - Python dependencies

## Installation

1. Create a virtual environment
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

```bash
python application.py
```

Then open your browser and go to:
```text
http://127.0.0.1:5000/
```

## Notes

This project is designed for demonstration and deployment of a machine learning prediction app using Flask. The model files are loaded from the models directory when the app starts.
