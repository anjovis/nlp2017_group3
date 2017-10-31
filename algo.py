#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import helpers

from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords

ngram_freq_folder = 'C:/Users/anjovis/desktop/nlp2017_group3/data/letters/'
xml_test_data = 'C:/Users/anjovis/Desktop/nlp2017_group3/data/corpora/english-group-lex-sample/train/corpus_small.xml'

stop = set(stopwords.words('english'))

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


def disambiguate_word(disambiguated_word, context):
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
            examples + example.split(' ')
        # print(sense.definition())
        definition = sense.definition().split(' ')
        # just concatenate the definition and all the examples
        signature = definition + examples

        # TODO form lemmas from words to get better accuracy
        # TODO remove marks and paragraphs from the context and signature.
        marks = '(){}[];.'


        # remove defined stopwords
        signature = [i for i in signature if i not in stop]
        #print('signature: ', signature)

        # form overlap between the context and the current sense
        overlap = [word for word in context if word in signature]
        #print('Overlap: ', overlap)

        # form score from the overlapped words
        score = 0
        for word in overlap:
            # get occurrences for every word with the disambiguated_word
            # divided by len(signature) not to give more weight because of a lengthy definition
            score = score + get_word_occurrences(word, disambiguated_word, files) / len(signature)

        scores.append([score, sense])

        #print(scores)

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
    # https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c
    for filename in files:
        f = open(ngram_freq_folder + filename, 'r', encoding='utf-8', errors='ignore')
        for line in f.readlines():
            tokens = line.rstrip().split('\t')
            # TODO remove POS-tag from the words in ngram-files
            if tokens[0] == word1 and tokens[1] == word2:
                #cooccurrences = int(tokens[2])
                # print(word1, word2, cooccurrences)
                # only one instance of a word pair in a file
                f.close()
                return cooccurrences
    return cooccurrences




if __name__ == "__main__":

    test_dict = helpers.parse_xml(xml_test_data)

    # word to be disambiguated
    #print(test_dict['corpus']['lexelt'][0]['instance'][0]['context']['head'])
    # the text of the context
    #print(test_dict['corpus']['lexelt']['instance'][0]['context']['#text'])
    # the correct senseid from WordNet of the context
    #print(test_dict['corpus']['lexelt']['instance'][0]['answer']['@senseid'])

    #for instance in test_dict['corpus'].items():
    #    print(instance['context'])

    # loop the every word from xml file
    for word in test_dict['corpus']['lexelt']:

        # loop every instance in the current lexeme
        for instance in word['instance']:
            word_to_be_disambiguated = instance['context']['head']
            context = instance['context']['#text']
            correct_sense = instance['answer']['@senseid']

            # TODO remove tags and quotes from context
            # make context into a list
            context = context.split(' ')
            context = [i for i in context if i not in stop]
            #print('context', context)

            predicted_sense = disambiguate_word(word_to_be_disambiguated, context)

            print('predicted_sense:', predicted_sense)
            print('correct_sense:', correct_sense)
            print('')







