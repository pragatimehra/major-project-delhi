<h2>Delhi House Pricing Prediction</h2>

This repository showcases a web application designed to predict house prices in Delhi, incorporating a machine learning model and a Flask backend. The project utilizes a RandomForestRegressor algorithm trained on a dataset of Delhi house prices and an interactive chatbot for additional assistance.

<b>Key Features:</b>

<div style="margin-bottom: 20px;">
    <h3>🏠 Web Interface</h3>
    <ul>
        <li>Developed an interactive and responsive web interface using HTML, CSS, and JavaScript.</li>
        <li>Utilized Bootstrap for styling to ensure a visually appealing and user-friendly layout.</li>
    </ul>
</div>

<div style="margin-bottom: 20px;">
    <h3>📈 Machine Learning Model</h3>
    <ul>
        <li>Trained a RandomForestRegressor model using scikit-learn on a dataset of Delhi house prices.</li>
        <li>Implemented data preprocessing techniques, including categorical encoding and outlier handling, to enhance model performance.</li>
    </ul>
</div>

<div style="margin-bottom: 20px;">
    <h3>⚙️ Flask Backend</h3>
    <ul>
        <li>Created a Flask server to handle incoming requests and seamlessly integrate the machine learning model for predictions.</li>
        <li>Established routes for rendering the home page and handling predictions based on user input.</li>
    </ul>
</div>

<div style="margin-bottom: 20px;">
    <h3>📊 Data Handling</h3>
    <ul>
        <li>Employed LabelEncoder for encoding categorical features, improving the model's ability to interpret location data.</li>
        <li>Conducted comprehensive data preparation, including log-transformations, to ensure robust model performance.</li>
    </ul>
</div>

<div style="margin-bottom: 20px;">
    <h3>🤖 Chatbot Integration</h3>
    <ul>
        <li>Integrated a chatbot using NLP and deep learning to assist users with queries related to house pricing and application usage.</li>
        <li>Implemented the chatbot to provide real-time responses and enhance user engagement.</li>
    </ul>
</div>
<b> Usage: </b>

Users input location, area, number of bedrooms, and toggle various amenities on the web page.
Upon form submission, JavaScript sends the data to the Flask server (/predict).
The Flask server uses the pre-trained ML model to predict the house price and returns the result.
The predicted price is displayed on the web page. 
A list of property dealers is also flashed on the screen to assist the user with prompt resolution of queries related to the location/property.
Users can interact with the chatbot for additional assistance and information.

<h2> Referential Screenshot </h2>

![Screenshot 2024-05-19 at 5 06 13 PM](https://github.com/pragatimehra/major-project-delhi/assets/92671158/7f1fd3da-f429-426e-b222-953104bf6c92)


## Prerequisites
Make sure you have Python 3.12 or later installed on your system.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/delhi-project.git
   cd delhi-project
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv delhi-project-package
   ```

3. Activate the virtual environment:
    > On macOS/Linux:
    ```bash
    source delhi-project-package/bin/activate
    ```
    > On Windows:
    ```bash
    delhi-project-package\Scripts\activate
    ```

4. Install the required packages:
    ```bash
    pip install Flask==2.3.2
    pip install scikit-learn==1.3.0
    pip install numpy==1.26.4
    pip install scipy==1.14.1
    pip install joblib==1.4.2
    pip install threadpoolctl==3.5.0
    pip install nltk==3.7
    ```
5. Download the NLTK data required for the project:
   ```bash
   import nltk
   nltk.download('punkt')
   ```
## Running the application
  ```bash
  python3 app.py
  ```
