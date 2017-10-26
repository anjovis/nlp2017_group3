#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords


stop = set(stopwords.words('english'))
# the folder where the files are
#data_location = 'C:/Users/eemel/Desktop/NLP/Project/downloads/google_ngrams/2_cooccurrence/'
data_folder = 'C:/Users/anjovis/desktop/nlp2017_group3/data/letters/'
#filename = 'googlebooks-eng-all-2gram-20120701-do'
#filename_postfix = '.gz_2'



def get_word_occurrences(word1, word2, files):
    '''
    Format in files: yourself_ADJ	Calm_ADJ	47
                     context        disambiguated   co-occurrences
    '''

    cooccurrences = 0
    # https://stackoverflow.com/questions/12468179/unicodedecodeerror-utf8-codec-cant-decode-byte-0x9c
    for filename in files:
        f = open(data_folder + filename, 'r', encoding='utf-8', errors='ignore')
        for line in f.readlines():
            tokens = line.rstrip().split('\t')
            #print(tokens)
            # TODO remove POS-tag from the words in ngram-files
            if tokens[0] == word1 and tokens[1] == word2:
                cooccurrences = int(tokens[2])
                print(word1, word2, cooccurrences)
                # only one instance of a word pair in a file
                f.close()
                return cooccurrences
    return cooccurrences


def get_files(folder_location):
    ''' Return all files in a list in file location in reference to current directory. '''
    files = []
    for (path, dirnames, filenames) in os.walk(folder_location):
        for filename in filenames:
            files.append(filename)
            # if filename.startswith('googlebooks-eng-all-2gram-20120701'):
            #    files.append(filename)
        break  # no files from subfolders

    if len(files) == 0:
        print('No applicable data in the folder.')

    return files

if __name__ == "__main__":


    context = "Their multiscreen projections of slides and film loops have featured in orbital parties, at the Astoria and Heaven, in Rifat Ozbek's 1988/89 fashion shows, and at Energy's recent Docklands all-dayer. \
    From their residency at the Fridge during the first summer of love, Halo used slide and film projectors to throw up a collage of op-art patterns, film loops of dancers like E-Boy and Wumni, and unique fractals derived from video feedback. \
    &bquo;We're not aware of creating a visual identify for the house scene, because we're right in there. \
    We see a dancer at a rave, film him later that week, and project him at the next rave.&equo; \
    [hi]Ben Lewis [/hi] Halo can be contacted on 071 738 3248. [ptr][/p] [caption] \
    <head>Art</head>you can dance to from the creative group called Halo "
    #context = ['engine', 'buy', 'something', 'formula', 'money']
    context = context.split(' ')

    context = [i for i in context if i not in stop]
    print(context)
    disambiguated_word = 'art'

    files = get_files(data_folder)
    first_two_letters = disambiguated_word[:2]
    # apparently every other pair exists except qt

    # search only the relevant files
    # from 'googlebooks-eng-all-2gram-20120701-do.gz_1' to 'do'
    files = [file for file in files if file.split('-')[-1].split('.')[0] == first_two_letters]  #  from 'googlebooks-eng-all-2gram-20120701-do.gz_1' to do
    print('Files to be processed:', files)

    scores = []
    # get every word sense from WordNet
    for sense in wn.synsets(disambiguated_word):
        print(' ')
        print(sense)
        examples = []
        for example in sense.examples():
            examples + example.split(' ')
        #print(sense.definition())
        definition = sense.definition().split(' ')
        # just concatenate the definitions and all the examples
        signature = definition + examples


        # TODO remove marks and paragraphs from the context and signature.
        marks = '(){}[];.'
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

        # remove defined stopwords
        signature = [i for i in signature if i not in stop]
        print('signature: ', signature)

        score = 0

        # form sets to ease the processing. Now only one word in context and signature.
        # signature = set(signature)
        # context = set(context)

        # form overlap between the context and the current sense
        overlap = [word for word in context if word in signature]
        print('Overlap: ', overlap)

        # form score from the overlap

        for word in overlap:
            # get occurrences for every word with the disambiguated_word
            # divided by len(signature) not to give more weight because of a lengthy definition
            score = score + get_word_occurrences(word, disambiguated_word, files) / len(signature)

        scores.append([score, sense])

        print(scores)

    # loop through the scores to get the maximum
    correct_sense = [0, 'Initial string here']
    for i in scores:
        if i[0] > correct_sense[0]:
            correct_sense = i

    print('Final sense: ', correct_sense)

