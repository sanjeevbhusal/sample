import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

ignore_words = set(stopwords.words('english'))


def get_ngrams(text, ngram_count):
    words = [word for word in text.split(" ") if word not in ignore_words]
    temp = zip(*[words[i:] for i in range(ngram_count)])
    ans = [' '.join(ngram) for ngram in temp]
    return ans
