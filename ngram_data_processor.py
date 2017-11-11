import helpers
import os

#input_folder = 'F:/google-bigram-cooccurrence/downloads/google_ngrams/letters/'

input_folder = 'D:/data/letters/'


def remove_pos_tag(input_folder, files, output_folder='./output/'):
    ''' Go through the data, remove pos-tags and generate a modified output file to the same folder where this script was run.'''

    # list of pos-tags
    pos_tags = ['ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRON', 'PRT', 'VERB']

    for file in files:
        with open(input_folder + file, 'r', encoding='utf-8', errors='ignore') as input_file:
            if not os.path.exists(os.path.dirname(output_folder + file)):
                os.makedirs(os.path.dirname(output_folder + file))
            with open(output_folder + file, 'w', encoding='utf-8') as output_file:
                print(file)
                for line in input_file.readlines():
                    tokens = line.rstrip().split('\t')
                    output_line = ''
                    for word in tokens:
                        if '_' in word:
                            # skips _PRON_ etc. files, the pos-tag always in the end of the file
                            possible_pos_tag = word.split('_')[-1]
                            if possible_pos_tag in pos_tags:
                                word = word.replace('_' + possible_pos_tag, '')  # remove the pos-tag

                        output_line += (word + '\t')

                    output_line = output_line[:-2]  # remove the extra \t
                    output_line += '\n'
                    output_file.write(output_line)


def sum_occurencies(input_folder, files, output_folder='./output/'):
    ''' Find all the same entries in the files and sum their occurrencies.'''
    for file in files:
        with open(input_folder + file, 'r', encoding='utf-8', errors='ignore') as input_file:
            if not os.path.exists(os.path.dirname(output_folder + file)):
                os.makedirs(os.path.dirname(output_folder + file))
            with open(output_folder + file, 'w', encoding='utf-8') as output_file:
                print(file)
                for line in input_file.readlines():
                    tokens = line.rstrip().split('\t')
                    output_line = ''
                    for word in tokens:

                        output_line += (word + '\t')

                    output_line = output_line[:-2]  # remove the extra \t
                    output_line += '\n'
                    output_file.write(output_line)


if __name__ == "__main__":
    files = helpers.get_files(input_folder)

    remove_pos_tag(input_folder, files, output_folder='D:/data/letters_pos_removed/')
