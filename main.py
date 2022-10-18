import csv
import json
from calculate_ngram import get_ngrams
from collections import defaultdict
import itertools


def extract_column_text(file_name: str, column_name: str):
    """
     Extracts all the text/value present in the specific column from a csv file
    :param file_name: csv file name
    :param column_name: column name to extract value
    :return: list
    """
    with open(file_name, "r") as f:
        reader = csv.DictReader(f)
        return [row[column_name] for row in reader]


def calculate_word_frequency(word_list: list):
    """
    Creates a dictionary with values from the list and map each value with their frequency
    :param word_list: list of words
    :return: dict
    """
    word_frequency = defaultdict(int)
    for word in word_list:
        word_frequency[word] += 1
    return word_frequency


def slice_dict(dict_to_slice: dict, slice_range=0):
    """
    slices the given dictionary
    :param dict_to_slice: dict to slice
    :param slice_range: slicing range
    :return: dict
    """
    return dict_to_slice if slice_range == 0 else dict(itertools.islice(dict_to_slice.items(), slice_range))


def sort_dict(dict_to_sort: dict, index: int, desc=False):
    """
    Sorts the dictionary on parameter passed by user
    :param dict_to_sort: dictionary to be sorted
    :param index: index of one of the value of a dictionary. this will be used as a sorting parameter
    :param desc: If true, sorting will be done in descending order.
    :return: dict
    """
    return dict(sorted(dict_to_sort.items(), key=lambda x: x[index], reverse=desc))


# def calculate_ngram(text_list, start_ngram, end_ngram):
#     for text in text_list:
#         text_ngram = {}
#         for n in range(start_ngram, end_ngram + 1):
#             text_ngram[n] = get_ngrams(n, text)

def calculate_ngram(text, ngram_number):
    return {text: get_ngrams(word, ngram_number) for word in text}


def dump_json(file_name: str, data: dict):
    with open(file_name, "w") as f:
        json.dump(data, f)


def dump_csv(filename, data_list: list, fieldnames: list):
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for text in data_list:
            writer.writerow(text)


def filter_words(word_list: list, keys_to_filter: dict):
    return [word for word in word_list if word in keys_to_filter]


def get_filtered_text(text_ngram: dict, filtered_two_ngram, filtered_three_ngram):
    filtered_text = []
    for text, ngram in text_ngram.items():
        two_ngram_list, three_ngram_list = ngram[2], ngram[3]
        filtered_text.extend(
            [{"word": word, "note": text} for word in filter_words(two_ngram_list, filtered_two_ngram)])
        filtered_text.extend(
            [{"word": word, "note": text} for word in filter_words(three_ngram_list, filtered_three_ngram)])
    return filtered_text


def main():
    text_list = extract_column_text("govt_url.csv", "Note")
    text_ngram = {}
    for text in text_list:
        text_ngram[text] = {2: get_ngrams(text, 2), 3: get_ngrams(text, 3)}

    two_ngram_list, three_ngram_list = [], []
    for ngram in text_ngram.values():
        two_ngram_list.extend(ngram.get(2))
        three_ngram_list.extend(ngram.get(3))

    two_ngram_frequency = calculate_word_frequency(two_ngram_list)
    three_ngram_frequency = calculate_word_frequency(three_ngram_list)
    two_ngram_sorted = sort_dict(two_ngram_frequency, desc=True, index=1)
    three_ngram_sorted = sort_dict(three_ngram_frequency, desc=True, index=1)
    two_ngram_sliced = slice_dict(two_ngram_sorted, slice_range=20)
    three_ngram_sliced = slice_dict(three_ngram_sorted, slice_range=20)

    dump_json("top_ngrams.json",
              {"top_20_two_ngram": two_ngram_sliced, "top_20_three_ngram": three_ngram_sliced})

    filtered_text = get_filtered_text(text_ngram, two_ngram_sliced, three_ngram_sliced)
    dump_csv("ngrams_text.csv", filtered_text, ["word", "note"])


if __name__ == "__main__":
    main()
