#!/usr/bin/python

import sys
import html
import re
import wikipedia

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer

import helpers

stop = set(stopwords.words('english'))
stemmer = SnowballStemmer('english')
tokenizer = RegexpTokenizer(r'\w+')  # remove all punctuation

xml_test_data = 'corpus_small.xml'

def linkify(words, word_to_be_disambiguated):
  
  head_link = wikipedia.page(word_to_be_disambiguated)
  head_link_url = head_link.url

  all_links = []

  for word in words:
    print("word: ", word)

    try:
        # Wikipedia will auto suggest closest page for the word 
        page = wikipedia.page(word)
        print("page: ", page)
        all_links.append(page.url)

    except:
        print("No wikipedia page found")
        continue


  return head_link_url, all_links

def wikify(xml_data_set):
  if xml_data_set:
    test_dict = helpers.parse_xml(xml_test_data)
    whole_set = []
    corpus = test_dict['corpus']['@lang']
    whole_set.append(corpus)

    # loop the every word from xml file
    for word in test_dict['corpus']['lexelt']:
      lexelt = word['@item']
      lex_set = []
      lex_set.append(lexelt)

      # loop every instance in the current lexeme
      for instance in word['instance']:
        instance_set = []
        word_to_be_disambiguated = instance['context']['head']
        #print("word_to_be_disambiguated: ", word_to_be_disambiguated)
        #print("\n")

        correct_sense = instance['answer']['@senseid']
        #print("correct_sense: ", correct_sense)
        #print("\n")  

        context = instance['context']['#text']
        #print("Context: ", context)
        #print("\n")

        # Remove html entities
        context = html.unescape(context)
        #print("Unescape context: ", context)
        #print("\n")

        # Remove tags
        context = re.sub(r"\[(.*?)\]+", "", context)
        #print("Regex context: ", context)
        #print("\n")

        # Tokenize
        context = tokenizer.tokenize(context)
        #print("Tokenized context: ", context)
        #print("\n")

        # Remove stopwords
        context = [x for x in context if x not in stop]
        print('Stopwordless context: ', context)
        #print("\n")

        links = linkify(context, word_to_be_disambiguated)
        #print("links: ", links)
        #print("\n")

        instance_set.append(correct_sense)
        instance_set.append(links)

        lex_set.append(instance_set)

        # TODO: find strings in original context and add wiki url?

      whole_set.append(lex_set)

    return whole_set

  else:
    print('No XML file provided')


if __name__ == "__main__":

  wikified = wikify(xml_test_data)
  print("wikified: ", wikified)

  test_results = [  
   [  
      'art.n',
      [  
         'art-0',
         ('https://en.wikipedia.org/wiki/Art',
         [  
            'https://en.wikipedia.org/wiki/They',
            'https://en.wikipedia.org/wiki/Multi-screen_video',
            'https://en.wikipedia.org/wiki/Film',
            'https://en.wikipedia.org/wiki/Party',
            'https://en.wikipedia.org/wiki/Heaven',
            'https://en.wikipedia.org/wiki/1988',
            'https://en.wikipedia.org/wiki/Fashion',
            'https://en.wikipedia.org/wiki/Energy',
            'https://en.wikipedia.org/wiki/Holocene',
            'https://en.wikipedia.org/wiki/Friday',
            'https://en.wikipedia.org/wiki/Summer',
            'https://en.wikipedia.org/wiki/Love',
            'https://en.wikipedia.org/wiki/Film',
            'https://en.wikipedia.org/wiki/Projector',
            'https://en.wikipedia.org/wiki/Throwing',
            'https://en.wikipedia.org/wiki/Collage',
            'https://en.wikipedia.org/wiki/Art',
            'https://en.wikipedia.org/wiki/Pattern',
            'https://en.wikipedia.org/wiki/Film',
            'https://en.wikipedia.org/wiki/Dance',
            'https://en.wikipedia.org/wiki/Like',
            'https://en.wikipedia.org/wiki/E_(mathematical_constant)',
            'https://en.wikipedia.org/wiki/Boy',
            'https://en.wikipedia.org/wiki/Fractal',
            'https://en.wikipedia.org/wiki/Video',
            'https://en.wikipedia.org/wiki/Feedback',
            'https://en.wikipedia.org/wiki/We',
            'https://en.wikipedia.org/wiki/Awareness',
            'https://en.wikipedia.org/wiki/Visual_system',
            'https://en.wikipedia.org/wiki/House',
            'https://en.wikipedia.org/wiki/Rights',
            'https://en.wikipedia.org/wiki/We',
            'https://en.wikipedia.org/wiki/Dance',
            'https://en.wikipedia.org/wiki/Rave',
            'https://en.wikipedia.org/wiki/Film',
            'https://en.wikipedia.org/wiki/Week',
            'https://en.wikipedia.org/wiki/Project',
            'https://en.wikipedia.org/wiki/Rave',
            'https://en.wikipedia.org/wiki/Ben',
            'https://en.wikipedia.org/wiki/Lewis',
            'https://en.wikipedia.org/wiki/Contactor',
            'https://en.wikipedia.org/wiki/020',
            'https://en.wikipedia.org/wiki/738',
            'https://en.wikipedia.org/wiki/BD_%2B17%C2%B0_3248',
            'https://en.wikipedia.org/wiki/Dance',
            'https://en.wikipedia.org/wiki/Group_(mathematics)'
         ]         )
      ],
      [  
         'art_gallery-0',
         ('https://en.wikipedia.org/wiki/Art',
         [  
            'https://en.wikipedia.org/wiki/Leeds',
            'https://en.wikipedia.org/wiki/Sport',
            'https://en.wikipedia.org/wiki/21_(number)',
            'https://en.wikipedia.org/wiki/Golf',
            'https://en.wikipedia.org/wiki/Sport',
            'https://en.wikipedia.org/wiki/Leisure',
            'https://en.wikipedia.org/wiki/Leaf',
            'https://en.wikipedia.org/wiki/Feeling',
            'https://en.wikipedia.org/wiki/Need',
            'https://en.wikipedia.org/wiki/Take',
            'https://en.wikipedia.org/wiki/Theatre',
            'https://en.wikipedia.org/wiki/Leeds',
            'https://en.wikipedia.org/wiki/4',
            'https://en.wikipedia.org/wiki/Leeds',
            'https://en.wikipedia.org/wiki/City',
            'https://en.wikipedia.org/wiki/1',
            'https://en.wikipedia.org/wiki/Oldest_people',
            'https://en.wikipedia.org/wiki/Music',
            'https://en.wikipedia.org/wiki/Country',
            'https://en.wikipedia.org/wiki/Home',
            'https://en.wikipedia.org/wiki/BBC',
            'https://en.wikipedia.org/wiki/Television',
            'https://en.wikipedia.org/wiki/Good',
            'https://en.wikipedia.org/wiki/Day',
            'https://en.wikipedia.org/wiki/Theatre',
            'https://en.wikipedia.org/wiki/Business',
            'https://en.wikipedia.org/wiki/Permanent',
            'https://en.wikipedia.org/wiki/Home',
            'https://en.wikipedia.org/wiki/Opera',
            'https://en.wikipedia.org/wiki/F.C._Copenhagen',
            'https://en.wikipedia.org/wiki/1',
            'https://en.wikipedia.org/wiki/Yorkshire',
            'https://en.wikipedia.org/wiki/Saying',
            'https://en.wikipedia.org/wiki/Brass',
            'https://en.wikipedia.org/wiki/May',
            'https://en.wikipedia.org/wiki/Still',
            'https://en.wikipedia.org/wiki/Brass',
            'https://en.wikipedia.org/wiki/Comes',
            'https://en.wikipedia.org/wiki/Nothing',
            'https://en.wikipedia.org/wiki/Brass',
            'https://en.wikipedia.org/wiki/1',
            'https://en.wikipedia.org/wiki/Summer',
            'https://en.wikipedia.org/wiki/Town_square',
            'https://en.wikipedia.org/wiki/Town',
            'https://en.wikipedia.org/wiki/Hall',
            'https://en.wikipedia.org/wiki/Park'
         ]         )
      ],
      [  
         'art-1',
         ('https://en.wikipedia.org/wiki/Art',
         [  
            'https://en.wikipedia.org/wiki/Pole_star',
            'https://en.wikipedia.org/wiki/Frederick_Page_(musician)',
            'https://en.wikipedia.org/wiki/Politics',
            'https://en.wikipedia.org/wiki/Shines',
            'https://en.wikipedia.org/wiki/Project',
            'https://en.wikipedia.org/wiki/Overcomer',
            'https://en.wikipedia.org/wiki/Art',
            'https://en.wikipedia.org/wiki/Life',
            'https://en.wikipedia.org/wiki/Power_set',
            'https://en.wikipedia.org/wiki/171',
            'https://en.wikipedia.org/wiki/Inch',
            'https://en.wikipedia.org/wiki/The_Seems',
            'https://en.wikipedia.org/wiki/Alex_Callinicos',
            'https://en.wikipedia.org/wiki/Mean',
            'https://en.wikipedia.org/wiki/Little',
            'https://en.wikipedia.org/wiki/Disclaimer',
            'https://en.wikipedia.org/wiki/Good',
            'https://en.wikipedia.org/wiki/Art',
            'https://en.wikipedia.org/wiki/Individual',
            'https://en.wikipedia.org/wiki/Good',
            'https://en.wikipedia.org/wiki/Throwing',
            'https://en.wikipedia.org/wiki/Soliloquy',
            'https://en.wikipedia.org/wiki/Force',
            'https://en.wikipedia.org/wiki/Strict',
            'https://en.wikipedia.org/wiki/Circumscribed_circle',
            'https://en.wikipedia.org/wiki/Reference',
            'https://en.wikipedia.org/wiki/Henri_Matisse',
            'https://en.wikipedia.org/wiki/Sense',
            'https://en.wikipedia.org/wiki/Boot',
            'https://en.wikipedia.org/wiki/Foot',
            'https://en.wikipedia.org/wiki/Art',
            'https://en.wikipedia.org/wiki/Sense',
            'https://en.wikipedia.org/wiki/Social',
            'https://en.wikipedia.org/wiki/Ideology',
            'https://en.wikipedia.org/wiki/Name',
            'https://en.wikipedia.org/wiki/Supposed_Former_Infatuation_Junkie',
            'https://en.wikipedia.org/wiki/Sensuous',
            'https://en.wikipedia.org/wiki/Rather_Be',
            'https://en.wikipedia.org/wiki/Aesthetics'
         ]         )
      ]
   ],
   [  
      'music.n',
      [  
         'art-0',
         ('https://en.wikipedia.org/wiki/Art',
         [  
            'https://en.wikipedia.org/wiki/They',
            'https://en.wikipedia.org/wiki/Multi-screen_video',
            'https://en.wikipedia.org/wiki/Film',
            'https://en.wikipedia.org/wiki/Party',
            'https://en.wikipedia.org/wiki/Heaven',
            'https://en.wikipedia.org/wiki/1988',
            'https://en.wikipedia.org/wiki/Fashion',
            'https://en.wikipedia.org/wiki/Energy',
            'https://en.wikipedia.org/wiki/Holocene',
            'https://en.wikipedia.org/wiki/Friday',
            'https://en.wikipedia.org/wiki/Summer',
            'https://en.wikipedia.org/wiki/Love',
            'https://en.wikipedia.org/wiki/Film',
            'https://en.wikipedia.org/wiki/Projector',
            'https://en.wikipedia.org/wiki/Throwing',
            'https://en.wikipedia.org/wiki/Collage',
            'https://en.wikipedia.org/wiki/Art',
            'https://en.wikipedia.org/wiki/Pattern',
            'https://en.wikipedia.org/wiki/Film',
            'https://en.wikipedia.org/wiki/Dance',
            'https://en.wikipedia.org/wiki/Like',
            'https://en.wikipedia.org/wiki/E_(mathematical_constant)',
            'https://en.wikipedia.org/wiki/Boy',
            'https://en.wikipedia.org/wiki/Fractal',
            'https://en.wikipedia.org/wiki/Video',
            'https://en.wikipedia.org/wiki/Feedback',
            'https://en.wikipedia.org/wiki/We',
            'https://en.wikipedia.org/wiki/Awareness',
            'https://en.wikipedia.org/wiki/Visual_system',
            'https://en.wikipedia.org/wiki/House',
            'https://en.wikipedia.org/wiki/Rights',
            'https://en.wikipedia.org/wiki/We',
            'https://en.wikipedia.org/wiki/Dance',
            'https://en.wikipedia.org/wiki/Rave',
            'https://en.wikipedia.org/wiki/Film',
            'https://en.wikipedia.org/wiki/Week',
            'https://en.wikipedia.org/wiki/Project',
            'https://en.wikipedia.org/wiki/Rave',
            'https://en.wikipedia.org/wiki/Ben',
            'https://en.wikipedia.org/wiki/Lewis',
            'https://en.wikipedia.org/wiki/Contactor',
            'https://en.wikipedia.org/wiki/020',
            'https://en.wikipedia.org/wiki/738',
            'https://en.wikipedia.org/wiki/BD_%2B17%C2%B0_3248',
            'https://en.wikipedia.org/wiki/Dance',
            'https://en.wikipedia.org/wiki/Group_(mathematics)'
         ]         )
      ],
      [  
         'art_gallery-0',
         ('https://en.wikipedia.org/wiki/Art',
         [  
            'https://en.wikipedia.org/wiki/Leeds',
            'https://en.wikipedia.org/wiki/Sport',
            'https://en.wikipedia.org/wiki/21_(number)',
            'https://en.wikipedia.org/wiki/Golf',
            'https://en.wikipedia.org/wiki/Sport',
            'https://en.wikipedia.org/wiki/Leisure',
            'https://en.wikipedia.org/wiki/Leaf',
            'https://en.wikipedia.org/wiki/Feeling',
            'https://en.wikipedia.org/wiki/Need',
            'https://en.wikipedia.org/wiki/Take',
            'https://en.wikipedia.org/wiki/Theatre',
            'https://en.wikipedia.org/wiki/Leeds',
            'https://en.wikipedia.org/wiki/4',
            'https://en.wikipedia.org/wiki/Leeds',
            'https://en.wikipedia.org/wiki/City',
            'https://en.wikipedia.org/wiki/1',
            'https://en.wikipedia.org/wiki/Oldest_people',
            'https://en.wikipedia.org/wiki/Music',
            'https://en.wikipedia.org/wiki/Country',
            'https://en.wikipedia.org/wiki/Home',
            'https://en.wikipedia.org/wiki/BBC',
            'https://en.wikipedia.org/wiki/Television',
            'https://en.wikipedia.org/wiki/Good',
            'https://en.wikipedia.org/wiki/Day',
            'https://en.wikipedia.org/wiki/Theatre',
            'https://en.wikipedia.org/wiki/Business',
            'https://en.wikipedia.org/wiki/Permanent',
            'https://en.wikipedia.org/wiki/Home',
            'https://en.wikipedia.org/wiki/Opera',
            'https://en.wikipedia.org/wiki/F.C._Copenhagen',
            'https://en.wikipedia.org/wiki/1',
            'https://en.wikipedia.org/wiki/Yorkshire',
            'https://en.wikipedia.org/wiki/Saying',
            'https://en.wikipedia.org/wiki/Brass',
            'https://en.wikipedia.org/wiki/May',
            'https://en.wikipedia.org/wiki/Still',
            'https://en.wikipedia.org/wiki/Brass',
            'https://en.wikipedia.org/wiki/Comes',
            'https://en.wikipedia.org/wiki/Nothing',
            'https://en.wikipedia.org/wiki/Brass',
            'https://en.wikipedia.org/wiki/1',
            'https://en.wikipedia.org/wiki/Summer',
            'https://en.wikipedia.org/wiki/Town_square',
            'https://en.wikipedia.org/wiki/Town',
            'https://en.wikipedia.org/wiki/Hall',
            'https://en.wikipedia.org/wiki/Park'
         ]         )
      ],
      [  
         'art-1',
         ('https://en.wikipedia.org/wiki/Art',
         [  
            'https://en.wikipedia.org/wiki/Pole_star',
            'https://en.wikipedia.org/wiki/Frederick_Page_(musician)',
            'https://en.wikipedia.org/wiki/Politics',
            'https://en.wikipedia.org/wiki/Shines',
            'https://en.wikipedia.org/wiki/Project',
            'https://en.wikipedia.org/wiki/Overcomer',
            'https://en.wikipedia.org/wiki/Art',
            'https://en.wikipedia.org/wiki/Life',
            'https://en.wikipedia.org/wiki/Power_set',
            'https://en.wikipedia.org/wiki/171',
            'https://en.wikipedia.org/wiki/Inch',
            'https://en.wikipedia.org/wiki/The_Seems',
            'https://en.wikipedia.org/wiki/Alex_Callinicos',
            'https://en.wikipedia.org/wiki/Mean',
            'https://en.wikipedia.org/wiki/Little',
            'https://en.wikipedia.org/wiki/Disclaimer',
            'https://en.wikipedia.org/wiki/Good',
            'https://en.wikipedia.org/wiki/Art',
            'https://en.wikipedia.org/wiki/Individual',
            'https://en.wikipedia.org/wiki/Good',
            'https://en.wikipedia.org/wiki/Throwing',
            'https://en.wikipedia.org/wiki/Soliloquy',
            'https://en.wikipedia.org/wiki/Force',
            'https://en.wikipedia.org/wiki/Strict',
            'https://en.wikipedia.org/wiki/Circumscribed_circle',
            'https://en.wikipedia.org/wiki/Reference',
            'https://en.wikipedia.org/wiki/Henri_Matisse',
            'https://en.wikipedia.org/wiki/Sense',
            'https://en.wikipedia.org/wiki/Boot',
            'https://en.wikipedia.org/wiki/Foot',
            'https://en.wikipedia.org/wiki/Art',
            'https://en.wikipedia.org/wiki/Sense',
            'https://en.wikipedia.org/wiki/Social',
            'https://en.wikipedia.org/wiki/Ideology',
            'https://en.wikipedia.org/wiki/Name',
            'https://en.wikipedia.org/wiki/Supposed_Former_Infatuation_Junkie',
            'https://en.wikipedia.org/wiki/Sensuous',
            'https://en.wikipedia.org/wiki/Rather_Be',
            'https://en.wikipedia.org/wiki/Aesthetics'
         ]         )
      ]
   ]
]

# TODO: loop wikified results to csv?
# results_out = open(xml_test_data + '_wikified.out', 'w')
# results_out.write(wikified)


# for x in test_results:
#   print("x: ", x) # lex set
#   print("x0: ", x[0]) # lexelt
#   print("x1: ", x[1]) # instance set
#   print("x10: ", x[1][0]) # sense id 
#   print("x11: ", x[1][1]) # links
#   print("x110: ", x[1][1][0]) # head link
#   print("x111: ", x[1][1][1]) # list of all links

#   for y in x[1][1][1]:
#     print("y: ", y) 
    # print("y0: ", y[0])
    # print("y1: ", y[1])
    # for z in y:
    #   print("z: ", z)