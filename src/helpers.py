import os
import xmltodict
import time

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

def parse_xml(file):
    # Parse the xml-file to
    try:
        fd = open(file)
        doc = xmltodict.parse(fd.read())
    except IOError:
        print('Couldn\'t find the test data')
    finally:
        fd.close()
        return doc


def write_results(data, folder='./', test_type='general'):
    ltime = time.localtime()

    filename = '{}_on_{}_{}_{}_at_{}_{}_{}.csv'.format(test_type, ltime.tm_mday, ltime.tm_mon,
                                                              ltime.tm_year,
                                                              ltime.tm_hour, ltime.tm_min, ltime.tm_sec)
    #print(filename)

    with open(filename, 'w') as results:
        results.write(data)

def get_word_occurrences(word1, word2, folder, files):
    '''
    :param word1: either the word that is to be disambiguated or word from the overlap
    :param word2: either the word that is to be disambiguated or word from the overlap
    :param files: A list of strings that represent the filenames.
    :return:
    '''

    first_two_letters = word2.lower()[:2]  # apparently every pair of letters exists
    # search only the relevant files
    # from 'googlebooks-eng-all-2gram-20120701-do.gz_1' to 'do'
    word2_files = [file for file in files if file.split('-')[-1].split('.')[
        0] == first_two_letters]  # from 'googlebooks-eng-all-2gram-20120701-do.gz_1' to do
    # print('Files to be processed:', files)

    # check "word2 word1 co-occurence"
    cooccurrences = check_word_occurence(word1, word2, folder, word2_files)

    # check "word1 word2 co-occurence" aka. the other half of the bi-gram
    first_two_letters = word1.lower()[:2]
    word1_files = [file for file in files if file.split('-')[-1].split('.')[
        0] == first_two_letters]

    cooccurrences += check_word_occurence(word2, word1, folder, word1_files)

    return cooccurrences


def check_word_occurence(word1, word2, folder, files):
    '''
        Format in files: yourself_ADJ	Calm_ADJ	47
                         word1        word2   co-occurrences
    '''
    cooccurrences = 0
    for file in files:
        #print(file)
        with open(folder + file, 'r', encoding='utf-8', errors='ignore') as f:

            for line in f.readlines():
                tokens = line.rstrip().split('\t')

                if tokens[0] == word1 and tokens[1] == word2:
                    cooccurrences = int(tokens[2])
                    # print(word1, word2, cooccurrences)
                    # only one instance of a word pair in a file
                    return cooccurrences

    return cooccurrences