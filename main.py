import csv
import json
from calculate_ngram import get_ngrams
from collections import defaultdict

note_list = []
two_ngram_words_dict = defaultdict(int)
three_ngram_words_dict = defaultdict(int)

with open("govt_url.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        note_list.append(row["Note"])

for note in note_list:
    two_ngram = get_ngrams(note, 2)
    three_ngram = get_ngrams(note, 3)
    for word in two_ngram:
        two_ngram_words_dict[word] += 1
    for word in three_ngram:
        three_ngram_words_dict[word] += 1
top_20_two_ngram = dict(sorted(two_ngram_words_dict.items(), key=lambda x: x[1], reverse=True)[:20])
top_20_three_ngram = dict(sorted(three_ngram_words_dict.items(), key=lambda x: x[1], reverse=True)[:20])

with open("ngrams.json", "w") as f:
    json.dump({"top_20_two_ngram": top_20_two_ngram, "top_20_three_ngram": top_20_three_ngram}, f, indent=4)

