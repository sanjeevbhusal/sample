import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')

ignore_words = set(stopwords.words('english'))
ignore_words_project_specific = ["Note", "added", "--"]
ignore_words.update(ignore_words_project_specific)


def is_date(text):
    return re.search("./../..", text) or re.search("././..", text) or re.search("..:..", text)


def get_ngrams(text, ngram_count):
    words = [word for word in text.split() if word not in ignore_words and not is_date(word)]
    temp = zip(*[words[i:] for i in range(ngram_count)])
    ans = [" ".join(ngram) for ngram in temp]
    return ans
