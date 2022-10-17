import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

ignore_words = set(stopwords.words('english'))

def generate_ngrams(string, ngram_count):
    string_list = [string for string in string.split(" ") if string not in ignore_words]
    resulting_list = []
    length = len(string_list)
    index = 0
    while True:
        if (index + ngram_count) > length:
            break
        resulting_list.append(" ".join(string_list[index:index + ngram_count]))
        index += 1

    return resulting_list


def get_ngrams(string, ngram_count):
    total_ngrams = []
    for i in range(1, ngram_count + 1):
        n_grams = generate_ngrams(string, i)
        total_ngrams.append(n_grams)

    return total_ngrams


print(get_ngrams("The sun rises in the east",3))

