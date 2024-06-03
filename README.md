<h2> Delhi House Pricing Prediction </h2>
This repository showcases a web application designed to predict house prices in Delhi, incorporating a machine learning model and a Flask backend. The project utilizes a RandomForestRegressor algorithm trained on a dataset of Delhi house prices and an interactive chatbot for additional assistance.

<b> Key Features: </b>

1. Web Interface:
- Developed an interactive and responsive web interface using HTML, CSS, and JavaScript.
- Utilized Bootstrap for styling to ensure a visually appealing and user-friendly layout.

2. Machine Learning Model:
- Trained a RandomForestRegressor model using scikit-learn on a dataset of Delhi house prices.
- Implemented data preprocessing techniques, including categorical encoding and outlier handling, to enhance model performance.

3. Flask Backend:
- Created a Flask server to handle incoming requests and seamlessly integrate the machine learning model for predictions.
- Established routes for rendering the home page and handling predictions based on user input.

4. Data Handling:
- Employed LabelEncoder for encoding categorical features, improving the model's ability to interpret location data.
- Conducted comprehensive data preparation, including log-transformations, to ensure robust model performance.

5. Chatbot Integration:
- Integrated a chatbot using NLP and deep learning to assist users with queries related to house pricing and application usage.
- Implemented the chatbot to provide real-time responses and enhance user engagement.

<b> Usage: </b>

Users input location, area, number of bedrooms, and toggle various amenities on the web page.
Upon form submission, JavaScript sends the data to the Flask server (/predict).
The Flask server uses the pre-trained ML model to predict the house price and returns the result.
The predicted price is displayed on the web page. 
A list of property dealers is also flashed on the screen to assist the user with prompt resolution of queries related to the location/property.
Users can interact with the chatbot for additional assistance and information.

<h2> Referential Screenshot </h2>

![Screenshot 2024-05-19 at 5 06 13 PM](https://github.com/pragatimehra/major-project-delhi/assets/92671158/7f1fd3da-f429-426e-b222-953104bf6c92)
