# Cynological Analyser

Cynological Analyser is a web application for the classification of canine breeds using a neural networks built for cynological analysis of canine breeds with the help of an image URL using TensorFlow. Once the breed is predicted, details about the breed is scraped from the internet using web scrapers.

The Machine Learning Model is built with TensorFlow and Keras Library in Google Colabs. The colab notebooks used for the model are included in the ```/colab-notebooks``` Directory.

## Stack Used
Machine Learning Model: `TensorFlow`, `Keras`

Web Scraping: `Beautiful Soup`

Front-End:  `HTML`, `CSS`, `JS`

Back-End:  `Flask`

## Documentation

### Quick Start
Clone the Repo: ```git clone https://github.com/theWellHopeErr/Cynological-Analyser```

Change Directory: ```cd Cynological-Analyser```

### Install Dependencies
Using requirements.txt: ```sudo pip install -r requirements.txt```

### Use Cynological Analyser
Export Flask App Path: ```export FLASK_APP=server.py```

Run App: ```flask run```
