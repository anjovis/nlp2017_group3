import helpers

xml_test_data = 'C:/Users/eemel/Desktop/nlp2017_group3/data/corpora/english-group-lex-sample/train/corpus.xml'

test_dict = helpers.parse_xml(xml_test_data)

correct_senses = 0
all_senses = 0
no_overlap = 0
results = []


# loop the every word from xml file
words = []
for word in test_dict['corpus']['lexelt']:
    # loop every instance in the current lexeme
    words.append([len(word['instance']), word['@item']])


for item in sorted(words):
    print(item)