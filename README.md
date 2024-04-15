<h1>Extractive Text-Summarization App using NLTK, using Streamlit</h1>

**NLP:**
It is the ability of a computer program to understand human language as it is spoken and written referred to as natural language. It is a component of artificial intelligence(AI).


<h2>Libraries used:</h2>

**1) re (RegEx or Regular Expression):**
This is the Python regular expression module, which is used for text cleaning/ preprocessing and pattern matching operations.


**2) NLTK (Natural Language Toolkit):**
NLTK is a popular Python library used for building Python programs that work with human language data for applying in statistical natural language processing (NLP). It contains text processing libraries for tokenization, parsing, classification, stemming, tagging and semantic reasoning.
Specifically, the following modules/components from NLTK are imported and used:
   - stopwords: This module provides a list of stopwords (common words like "the," "a," "is," etc.) that are often removed during text processing.
   - word_tokenize: This function tokenizes (splits) a given text into individual words.
   - sent_tokenize: This function tokenizes (splits) a given text into individual sentences.

*Installation:*

pip3 install nltk


**3) Streamlit:**
It is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps.

*Installation:*

pip3 install streamlit


**4) Heapq (Heap Queue):** 
This is a built-in Python module for implementing the heap queue algorithm (Priority Queue). In this code, it is used to select the top N sentences with the highest scores for the summary.


<h2>Processes involved in Extractive Text Summarization</h2>

1. Text cleaning 

2. Sentence tokenization

3. Word tokenization

4. Word-frequency table

5. Summarization


<h3>To run the file:</h3>

python -m streamlit run TextSummarizer.py
