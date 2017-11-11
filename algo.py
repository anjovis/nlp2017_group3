#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import helpers

from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
#from nltk import tokenizer.tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer

#ngram_freq_folder = 'C:/Users/anjovis/desktop/nlp2017_group3/data/letters/'
ngram_freq_folder = 'D:/data/letters_pos_removed/'
#ngram_freq_folder = 'F:/google-bigram-cooccurrence/downloads/google_ngrams/letters/'
xml_test_data = 'C:/Users/anjovis/Desktop/nlp2017_group3/corpus_small.xml'
#xml_test_data = 'C:/Users/eemel/Desktop/nlp2017_group3/corpus_small.xml'
# initialize nltk language processing functions
stop = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')
tokenizer = RegexpTokenizer(r'\w+')  # remove all punctuation

# the stopwords
'''
        stop = 
        {'the', 'these', 'where', 'both', 'but', 'nor', 'just', 'wasn', 'itself', 'hadn', 'their', 'or', 'so', 'then', 
        'isn', 'when', 'me', 'she', 'all', 'having', 'ours', 'on', 'he', 'has', 'am', 'are', 'mustn', 'again', 'own', 
        'who', 's', 'at', 'theirs', 'wouldn', 'needn', 'being', 'was', 'we', 'only', 'up', 'in', 'by', 'most', 'from', 
        'once', 'into', 'now', 'a', 'you', 'out', 'below', 'it', 'i', 'over', 'were', 'hasn', 'further', 'after', 
        'before', 'off', 'herself', 'is', 'll', 'during', 'through', 'such', 'y', 'as', 'here', 'of', 'same', 'for', 
        'couldn', 'ma', 'until', 'yourselves', 'other', 'those', 'yours', 'aren', 'mightn', 'what', 'why', 're', 'our', 
        'have', 'ourselves', 'her', 'if', 'won', 'few', 'm', 'didn', 'shan', 'be', 'should', 'his', 'whom', 'than', 
        'yourself', 'above', 'to', 'too', 'down', 've', 'themselves', 'can', 'doing', 'did', 'each', 'not', 'they', 
        'your', 'himself', 'don', 'been', 't', 'with', 'o', 'more', 'because', 'and', 'will', 'how', 'do', 'them', 
        'any', 'myself', 'no', 'an', 'about', 'ain', 'weren', 'there', 'between', 'doesn', 'against', 'this', 'some', 
        'very', 'its', 'hers', 'under', 'while', 'had', 'haven', 'that', 'shouldn', 'which', 'my', 'd', 'does', 'him'}

'''


def disambiguate_word(disambiguated_word, context, verbose=False):
    # form the files that are to be searched
    files = helpers.get_files(ngram_freq_folder)
    first_two_letters = disambiguated_word[:2]  # apparently every pair of letters exists
    # search only the relevant files
    # from 'googlebooks-eng-all-2gram-20120701-do.gz_1' to 'do'
    files = [file for file in files if file.split('-')[-1].split('.')[
        0] == first_two_letters]  # from 'googlebooks-eng-all-2gram-20120701-do.gz_1' to do
    # print('Files to be processed:', files)


    # Sense with the highest score is considered best.
    scores = []
    # get every word sense from WordNet
    for sense in wn.synsets(disambiguated_word):
        #print(' ')
        #print(sense)
        examples = []
        for example in sense.examples():
            examples += tokenizer.tokenize(example)
        # print(sense.definition())
        definition = tokenizer.tokenize(sense.definition())

        # get hyponyms and hypernyms for the sense to get larger overlap

        hypernyms = []
        for hypernym in sense.hypernyms():
            hypernyms += tokenizer.tokenize(hypernym.definition())
            for example in hypernym.examples():
                hypernyms += tokenizer.tokenize(example)

        #print('hypernyms: ', hypernyms)

        hyponyms = []
        for hyponym in sense.hyponyms():
            hyponyms += tokenizer.tokenize(hyponym.definition())
            for example in hyponym.examples():
                hyponyms += tokenizer.tokenize(example)

        #print('hyponyms: ', hyponyms)

        # just concatenate the definition and all the examples
        signature = definition + examples + hypernyms + hyponyms
        #print('signature: ', signature)

        # retain the information of the original word in stemming
        # signature format: [(stem1, word1), (stem2, word2)...]
        # stem the words in signature
        signature = [(stemmer.stem(word), word) for word in signature]


        #for index, pair in signature:
        #    for w in stop:
        #        if w == pair[0]:
        #            continue
        #    signature[index] = pair

        # remove defined stopwords based on the stemmed word
        without_stopwords = []  # helper variable
        for pair in signature:
            if pair[0] in stop:
                continue
            else:
                without_stopwords.append(pair)

        signature = without_stopwords

        #print('signature: ', signature)

        # form overlap between the context and the current sense
        overlap = []
        for w1 in context:
            for w2 in signature:
                # TODO handle
                if w1[0] == w2[0]:
                    # Append the original non-stemmed word. Words are not stemmed in ngram-coocurence data.
                    overlap.append(w1[1])  # Use context base-word on default.

        #overlap = [word for word in context if word in signature]

        if verbose:
            print('Sense: ', sense, 'Overlap: ', overlap)

        # form score from the overlapped words
        score = 0
        for word in overlap:
            # get occurrences for every word with the disambiguated_word
            # divided by len(signature) not to give more weight because of a lengthy definition
            score = score + get_word_occurrences(word, disambiguated_word, files) / len(signature)

        scores.append([score, sense])

        # print(scores)

    # loop through the scores to get the maximum
    predicted_sense = [0, 'Initial string here']
    for i in scores:
        if i[0] > predicted_sense[0]:
            predicted_sense = i

    #print('Final sense: ', predicted_sense)

    return predicted_sense


def get_word_occurrences(word1, word2, files):
    '''
    Format in files: yourself_ADJ	Calm_ADJ	47
                     context        disambiguated   co-occurrences
    '''

    cooccurrences = 0
    for filename in files:
        try:
            f = open(ngram_freq_folder + filename, 'r', encoding='utf-8', errors='ignore')
        except:
            print('Check path.')
            f.close()
            return
        finally:
            for line in f.readlines():
                tokens = line.rstrip().split('\t')
                if tokens[0] == word1 and tokens[1] == word2:
                    cooccurrences = int(tokens[2])
                    # print(word1, word2, cooccurrences)
                    # only one instance of a word pair in a file
                    f.close()
                    return cooccurrences
    return cooccurrences


if __name__ == "__main__":

    test_dict = helpers.parse_xml(xml_test_data)

    # loop the every word from xml file
    for word in test_dict['corpus']['lexelt']:
        # loop every instance in the current lexeme
        for instance in word['instance']:
            word_to_be_disambiguated = instance['context']['head']
            context = instance['context']['#text']
            correct_sense = instance['answer']['@senseid']

            # TODO remove tags and quotes from context
            # can be produce errors by giving weigth to senses that happen to have the keyword
            # format context to a list
            context = tokenizer.tokenize(context)

            # remove the word to be disambiguated: it doesn't provide any information for the context
            context = [w for w in context if w not in [word_to_be_disambiguated, word_to_be_disambiguated.lower()]]

            # stem the words but retain the information of the original word
            context = [(stemmer.stem(word), word) for word in context]

            #print(context)
            # remove defined stopwords based on the stemmed word
            without_stopwords = []  # helper variable
            for pair in context:
                if pair[0] in stop:
                    continue
                else:
                    without_stopwords.append(pair)

            context = without_stopwords

            #print('context', context)

            predicted_sense = disambiguate_word(word_to_be_disambiguated, context, verbose=True)

            print('word_to_be_disambiguated: ', word_to_be_disambiguated)
            print('predicted_sense:', predicted_sense)
            print('correct_sense:', correct_sense)
            print('')

            # TODO write results to csv






