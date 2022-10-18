import csv
from calculate_ngram import get_ngrams
from collections import defaultdict

note_list = []
words_dict = defaultdict(int)

with open("govt_url.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        note_list.append(row["Note"])


for note in note_list:
    two_ngram = get_ngrams(note, 2)
    three_ngram = get_ngrams(note, 3)
    word_list = two_ngram + three_ngram
    for word in word_list:
        words_dict[word] += 1


