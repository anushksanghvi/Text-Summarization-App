import re
import streamlit as st

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

import heapq


def nltk_summarizer(docx):
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(docx)
    freqTable = {}

    print(words)    # Print word tokens
    print()

    # Count word frequency
    for word in words:
        word = word.lower()
        if word not in stopWords:
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
  
    # Normalize word frequency
    max_freq = max(freqTable.values())
    for word in freqTable.keys():
        freqTable[word] = (freqTable[word]/max_freq)

    # Calculate sentence scores
    sentence_list = sent_tokenize(docx)
    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in freqTable.keys():
                if len(sent.split(' ')) < 30:      # filtering condition in order to exclude very long sentences from the scoring process.
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = freqTable[word]
                    else:
                        sentence_scores[sent] += freqTable[word] # total number of length of words

    # print(sentence_list)
    # print()
    print(sentence_scores)      

    # Get top sentences for summary
    summary_sentences = heapq.nlargest(8, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    return summary


def main():
    st.title("Text Summarizer App")
    activities = ["Summarize Via Text"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == 'Summarize Via Text':
        st.subheader("Text Summary using NLTK")
        article_text = st.text_area("Enter Text Here","Type here")

        #cleaning of input text
        article_text = re.sub(r'\\[[0-9]*\\]', ' ',article_text)
        article_text = re.sub('[^a-zA-Z.,]', ' ',article_text)
        article_text = re.sub(r"\b[a-zA-Z]\b",'',article_text)
        article_text = re.sub("[A-Z]\Z",'',article_text)
        article_text = re.sub(r'\s+', ' ', article_text)

        summary_choice = "NLTK"
        if st.button("Summarize Via Text"):
            summary_result = nltk_summarizer(article_text)
            
            st.write(summary_result)

            # Display lengths of original text and summary text
            st.write("Original Text Length:", len(article_text))
            st.write("Summary Text Length:", len(summary_result))

            # st.write(word_tokenize(article_text))
            
main()
