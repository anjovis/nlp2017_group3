import helpers

input_folder = 'F:/google-bigram-cooccurrence/downloads/google_ngrams/letters/'

def remove_pos_tag(input_folder, files):
    # remove pos-tags from every file

    # list of pos-tags
    pos_tags = ['ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRON', 'PRT', 'VERB']

    for file in files:
        with open(input_folder + file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f.readlines():
                tokens = line.rstrip().split('\t')
                # TODO remove POS-tag from the words in ngram-files
                for word in tokens:
                    if '_' in word:
                        # skips _PRON_ etc. files, the pos-tag always in the end of the file
                        possible_pos_tag = word.split('_')[-1]
                        if possible_pos_tag in pos_tags:
                            word = word.replace('_' + possible_pos_tag, '')  # remove the pos-tag

def get_all_pos_tags(files):
    '''Information could be found in http://storage.googleapis.com/books/ngrams/books/datasetsv2.html,
    script not really needed. '''
    pos_tags = []
    # remove pos-tags from every file
    for file in files:
        # just stop this somewhere
        if file == 'googlebooks-eng-all-2gram-20120701-bo.gz_0':
            break
        print(file)

        with open(input_folder + file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f.readlines():
                tokens = line.rstrip().split('\t')
                for token in tokens:
                    if '_' in token:
                        test_case = token.split('_')[-1]
                        if test_case.isupper(): # get the last token on the list, the pos is always at the end of the word
                            pos_tags.append(test_case)
                            #print(test_case)
                    else:
                        continue
    # remove same occurrences
    pos_tags = set(pos_tags)
    pos_tags = list(pos_tags)
    return pos_tags

if __name__ == "__main__":
    files = helpers.get_files(input_folder)
    #print(files)
    #remove_pos_tag(files)
    possible_pos_tags = get_all_pos_tags(files)
    print(possible_pos_tags)