import re
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

import pandas as pd

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words("english"))
ps = PorterStemmer()
tf = TfidfVectorizer()
 
class process_text:
    def __init__(self) -> None:
        pass
    def process(self, text):
        # Y_2 = []
        sentences = []
        sentences_processed = []
        sentences_processed_tw = []
        all_data = text.strip().split("\n")
        for n, line in enumerate(all_data):
            # Split <word>:<value> in each data line
            line_data = line.split(" ")[0:-1]
            # Init sentence
            sentence = ""
            for words_count in line_data:
                # Get words in a data line
                words = words_count.split(":")[0].split("_")
                # Get coresponding value of each word
                # count = int(words_count.split(":")[1])
                # Remove Digits
                # words = list(filter("<num>".__ne__, words))
                # Remove Additional Spaces and Characters.
                words = list(map(lambda x: re.sub(r'\`|\'|,|\.|\"', '', x), words))

                # if len(words) == 0:
                #     continue
                # words = words * count

                # Form a setence
                sentence += " ".join(words) + " "

                sentences.append(sentence)
                # Save coresponding label
                # Y_2.append(float(line.split(" ")[-1].split(":")[-1]))

            # At this point we have sentences
        for sentence in sentences:
            # Obtain work tokens
            tokenized_words = word_tokenize(sentence)
            # Remove stop words
            filtered_words = list(filter(lambda x: x not in stop_words, tokenized_words))
            # Stemming words (lematization is better but requires POS tagging which)
            stemmed_words = list(map(ps.stem, filtered_words))
            sentences_processed.append(" ".join(stemmed_words))

        # Create a dataframe for downstream analysis
        data = pd.DataFrame(data={'sentence': sentences_processed})
        return data , sentences_processed

# pre_proces = process_text()
# f = open('temp/text.txt')

# string = f.read()

# data, sentence = pre_proces.process(string)
# print(data.head(50))
