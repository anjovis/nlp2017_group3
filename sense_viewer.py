import sys
import helpers
from nltk.corpus import wordnet as wn



bar_senses = wn.synsets(sys.argv[1])


for sense in bar_senses:
    print(sense.name(), ':', sense.definition())
    print(sense.examples())
    print(' ')
