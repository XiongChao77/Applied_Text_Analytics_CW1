# YouTube Comment Analysis using NLP & Topic Modeling

## Project Overview

This project extracts YouTube video comments and performs:

-   Sentiment Analysis (Positive / Negative / Neutral)
-   Topic Modeling using LDA
-   WordCloud Visualization
-   Interactive Topic Visualization using pyLDAvis

The goal is to analyze audience opinions and discover hidden discussion
topics from user comments using Natural Language Processing (NLP).

------------------------------------------------------------------------

## Features

-   Fetch comments using YouTube Data API
-   Text preprocessing using NLTK
-   Sentiment analysis using:
    -   TextBlob
    -   VADER Sentiment
-   Topic Modeling using:
    -   Scikit-learn LDA
-   Word frequency visualization using:
    -   WordCloud
-   Interactive topic visualization using:
    -   pyLDAvis

------------------------------------------------------------------------

## Tech Stack

-   Python
-   Pandas
-   NumPy
-   NLTK
-   TextBlob
-   VADER Sentiment
-   Scikit-learn
-   WordCloud
-   pyLDAvis

------------------------------------------------------------------------

## Installation

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/XiongChao77/Applied_Text_Analytics_CW1
cd Applied_Text_Analytics_CW1
```

### 2️⃣ Create Virtual Environment (Recommended)

``` bash
python -m venv venv
```

Activate environment:

Mac/Linux

``` bash
source venv/bin/activate
```

Windows

``` bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Requirements

Make sure your requirements.txt includes:

google-api-python-client\
nltk\
textblob\
vaderSentiment\
wordcloud\
pyLDAvis==3.3.1\
pandas\
numpy\
scipy\
joblib\
scikit-learn\
funcy

------------------------------------------------------------------------

## YouTube API Setup

1.  Go to Google Cloud Console\
2.  Enable YouTube Data API v3\
3.  Generate an API Key\
4.  Add your API key inside your script:

``` python
API_KEY = "YOUR_API_KEY"
```

------------------------------------------------------------------------

## How to Run the Project

### 1. Data Preparation (Optional)

Open and run:

data_process/comments_cleaned.ipynb

Note: The processed data is already included in the `data/` directory, so this step is optional.

### 2. NLP Training & Analysis

Open and run:

data_process/comments_nlp.ipynb

------------------------------------------------------------------------

## NLP Workflow

1.  Fetch YouTube comments\
2.  Clean and preprocess text
    -   Remove URLs\
    -   Remove punctuation\
    -   Remove stopwords\
    -   Remove irrelevant words\
    -   Convert to lowercase\
3.  Perform Sentiment Analysis\
4.  Convert text to numerical format using CountVectorizer\
5.  Apply LDA for Topic Modeling\
6.  Visualize topics using pyLDAvis\
7.  Generate WordCloud for frequent words

------------------------------------------------------------------------

## Output

-   Sentiment distribution (Positive / Negative / Neutral)\
-   Top keywords per topic\
-   Interactive LDA topic visualization\
-   WordCloud visualization\
-   Processed dataset ready for ML tasks

------------------------------------------------------------------------

## Known Issues

-   pyLDAvis may cause dependency conflicts with sklearn versions.\
-   Large datasets may increase processing time.\
-   Ensure correct Python version compatibility.

------------------------------------------------------------------------
