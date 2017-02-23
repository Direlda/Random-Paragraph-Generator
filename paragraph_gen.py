#! python3.6

"""This module is a random paragraph generator that uses a Context Free
Grammar to randomly generate the text of paragraphs.
"""

# Author: Thomas "Direlda"
# Ported to Python: 2017-02-21
# Last Revised: 2017-02-23
# Foxes are cool! ^.^;;~

import json
import random

def load_dictionary(filepath):
    """Load a JSON file into a dictionary."""
    with open(filepath) as dict_file:
        dictionary = json.load(dict_file)
    return dictionary

def rule_expander(dictionary, axiom):
    """ Take a dictionary of phrase structure rules and recurse through
        them using the axiom as the starting key. Return a list of
        parts of speech.
    """
    sentence_parts_speech = []
    if axiom in dictionary:
        outputs = dictionary[axiom]["outputs"]
        weights = dictionary[axiom]["weights"]
        expansion = random.choices(outputs, cum_weights=weights, k=1)
        expansion = expansion[0].split()
        for token in expansion:
            sentence_parts_speech.extend(rule_expander(dictionary, token))
    else:
        sentence_parts_speech.append(axiom)
    return sentence_parts_speech

def word_chooser(dictionary, parts_speech_list):
    """ Take a dictionary of words and a list of parts of speech and
        return a list of words in grammatical sentence order.
    """
    word_list = []
    for part_speech in parts_speech_list:
        word = random.choice(dictionary[part_speech])
        word_list.append(word)
    return word_list

def generate_sentences(max_sentences, axiom, rules_dict, lexicon_dict):
    """ Create a user-specified number of sentences and append to a txt
        file.
    """
    sentences = 0
    with open("generated_paragraphs.txt", "a") as text_file:
        text_file.write("\n")
        while sentences < max_sentences:
            sentence_parts_speech = rule_expander(rules_dict, axiom)
            sentence_words = word_chooser(lexicon_dict, sentence_parts_speech)
            sentence = " ".join(sentence_words)
            sentence = sentence.capitalize()
            text_file.write(sentence + ". ")
            sentences += 1

def generate_document(max_paragraphs, max_sentences, axiom, rules_dict,
                      lexicon_dict):
    """Generate a txt file with a user-specified number of paragraphs."""
    with open("generated_paragraphs.txt", "w") as text_file:
        print("A Generated Text", file=text_file)
    paragraphs = 0
    while paragraphs < max_paragraphs:
        generate_sentences(max_sentences, axiom, rules_dict, lexicon_dict)
        paragraphs += 1

def main():
    """Run the program."""
    max_sentences = int(input("How many sentences per paragraph? "))
    max_paragraphs = int(input("How many paragraphs? "))
    axiom = input("What is the starting axiom? Use 'TP' for full sentences. ")
    rule_path = input("What is the filepath for the rule dictionary? ")
    lexicon_path = input("What is the filepath for the lexical dictionary? ")

    rules_dict = load_dictionary(rule_path)
    lexicon_dict = load_dictionary(lexicon_path)
    generate_document(max_paragraphs, max_sentences, axiom, rules_dict,
                      lexicon_dict)

if __name__ == "__main__":
    main()
