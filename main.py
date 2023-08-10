import re
from collections import Counter


def count_words(text) :
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)
    return word_count


def average_sentence_length(text) :
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    sentence_lengths = [len(re.findall(r'\b\w+\b', sentence)) for sentence in sentences]

    if len(sentence_lengths) > 0 :
        average_length = sum(sentence_lengths) / len(sentence_lengths)
        return average_length
    else :
        return 0


def most_common_phrases(text, num_phrases=5) :
    words = re.findall(r'\b\w+\b', text.lower())
    phrases = [words[i :i + 2] for i in range(len(words) - 1)]
    phrase_count = Counter(tuple(phrase) for phrase in phrases)

    return phrase_count.most_common(num_phrases)


def count_letter_frequency(text) :
    letters = re.findall(r'[a-zA-Z]', text.lower())
    letter_count = Counter(letters)
    return letter_count


if __name__ == "__main__" :
    file_path = "sample_text_file.txt"

    try :
        with open(file_path, "r") as file :
            sample_text = file.read()
    except FileNotFoundError :
        print(f"Nie można znaleźć pliku: {file_path}")
        exit()

    print("Słowa i ich wystąpienia:")
    word_count = count_words(sample_text)
    for word, count in word_count.items() :
        print(f"{word}: {count}")

    print("\nŚrednia długość zdań:")
    avg_length = average_sentence_length(sample_text)
    print(f"{avg_length:.2f} słów na zdanie")

    print("\nNajczęściej występujące wyrażenia:")
    common_phrases = most_common_phrases(sample_text)
    for phrase, count in common_phrases :
        print(f"{', '.join(phrase)}: {count}")

    print("\nCzęstotliwość występowania liter:")
    letter_frequency = count_letter_frequency(sample_text)
    for letter, count in letter_frequency.items() :
        print(f"{letter}: {count}")