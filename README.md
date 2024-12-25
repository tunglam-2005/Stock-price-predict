# Stock Price Prediction

## Overview
The **Stock Price Prediction** project aims to develop a predictive model that forecasts stock prices using historical data. This project utilizes various machine learning techniques to analyze stock market trends and generate accurate predictions.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Data Collection**: Fetches historical stock data from **investing.com**.
- **Data Preprocessing**: Cleans and prepares the data for analysis.
- **Model Selection**: Implements multiple machine learning algorithms: Linear Regression, ARIMA, and LSTM (Long Short-Term Memory) networks.
- **Visualization**: Provides visual insights into stock price trends, daily profit, liquidity, and model performance.
- **Prediction**: Generates future stock price predictions based on the trained models.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- TensorFlow/Keras (for deep learning models)
- Jupyter Notebook
- Streamlit (for creating stocks price prediction web app)

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/tunglam-2005/Stock-price-predict.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Open the Jupyter Notebook file located in the `notebooks` directory.
2. Run the cells sequentially to execute data preprocessing, model training, and prediction tasks.
3. Modify parameters as needed to experiment with different models or datasets.
4. Run Python file within `Stock price predict app` folder to open the web app:
   ```bash
   Streamlit run Stock_price_predict_app.py
   ```
   Or can go to this link to try this web app:
   ```bash
   https://stock-price-predict-jzmn3mpvk8ufpuenybvfkw.streamlit.app/
   ```

## Data Sources
The project uses historical stock price data from sources like:
- Yahoo Finance API
- Investing.com

## Model Training
The project includes scripts for training different models. The primary steps are:
1. Load and preprocess the data.
2. EDA is used to discover trends for stock price, stock profit, and volume (Amount of stock traded).
3. Engineering features for prediction.
4. Split the dataset into training and testing sets.
5. Train the selected model using the training set.
6. Evaluate model performance using Mean Squared Error, Mean Absolute Error and R² score.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to your branch (`git push origin feature/YourFeature`).
5. Open a pull request.
