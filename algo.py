#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords


stop = set(stopwords.words('english'))
# the folder where the files are
#data_location = 'C:/Users/eemel/Desktop/NLP/Project/downloads/google_ngrams/2_cooccurrence/'
data_folder = 'C:/Users/anjovis/Desktop/disambiguation_using_google_ngrams/data/letters/'
#filename = 'googlebooks-eng-all-2gram-20120701-do'
#filename_postfix = '.gz_2'



def get_word_occurrences(word1, word2, files):
    '''
    :param word1:
    :param word2:
    :param files:
    :return:

    Format in files: yourself_ADJ	Calm_ADJ	47
                     context        disambiguated   co-occurrences

    '''



    # TODO search from correct files
    # the idea of sum is to check that the word-pair only exists once
    sum = 0
    # https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c
    for filename in files:
        cooccurrences = 0
        f = open(data_folder + filename, 'r', encoding='utf-8', errors='ignore')
        for line in f.readlines():
            tokens = line.rstrip().split('\t')
            #print(tokens)
            # TODO remove POS-tag from the words in ngram-files
            # TODO do they have to be exact?
            if tokens[0] == word1 and tokens[1] == word2:
                cooccurrences = int(tokens[2])
                sum = sum + cooccurrences
                print('cooccurrences: ', cooccurrences)
                # only one instance of a word pair in a file
                f.close()
                break
                # return cooccurrences
        f.close()
    print('Sum: ', sum)
    return sum

def get_files_in_top_dir(file_location):
    ''' Return all files in a list in file location in reference to current directory. '''
    files = []

    for (path, dirnames, filenames) in os.walk(file_location):
        for filename in filenames:
            if filename.startswith('googlebooks-eng-all-2gram-20120701'):
                files.append(filename)
        break
    return files

if __name__ == "__main__":

    disambiguated_word = 'car'
    files = get_files_in_top_dir(data_folder)
    first_two_letters = disambiguated_word[:2]
    # every other pair exists except qt


    # search only the relevant files
    # from 'googlebooks-eng-all-2gram-20120701-do.gz_1' to 'do'
    files = [file for file in files if file.split('-')[-1].split('.')[0] == first_two_letters]  # from 'googlebooks-eng-all-2gram-20120701-do.gz_1' to do
    print('Files to be processed:', files)

    scores = []
    # get every word sense from WordNet
    for sense in wn.synsets(disambiguated_word):
        print(sense)
        # sense.definition() + sense.examples()
        #print(sense.definition())
        definition = sense.definition().split(' ')
        #print(definition)
        # remove common english stopwords
        definition = [i for i in definition if i not in stop]
        print(definition)

        score = 0
        for context_word in definition:
            # get occurrences for every word with the disambiguated_word
            # divided by len(definition) not to give more weight because of a lengthy definition
            score = score + get_word_occurrences(context_word, disambiguated_word, files) / len(definition)

        scores.append([score, sense])

    print(scores)
    correct_sense = max(scores)
    print(max(scores))
