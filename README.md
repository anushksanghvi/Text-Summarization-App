**Extractive Text-Summarization App using NLTK, using Streamlit**

**NLP:**
It is the ability of a computer program to understand human language as it is spoken and written referred to as natural language. It is a component of artificial intelligence(AI).

There are two main phases to natural language processing: 

1.data preprocessing

2.algorithm development


**Libraries used**


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


**To run the file:**

python -m streamlit run TextSummarizer.py 
