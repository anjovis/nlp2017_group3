# set up the file paths to bigram folder and senseval2-format xml test data here
#ngram_freq_folder = 'C:/Users/anjovis/desktop/nlp2017_group3/data/letters/'
ngram_freq_folder = 'D:/data/letters/'
#ngram_freq_folder = 'F:/google-bigram-cooccurrence/downloads/google_ngrams/letters/'  # slash in the end required
xml_test_data = '../data/bar_chair_day.xml'

# Written only once to the output file
file_text = 'Description about the run'

wn17_to_wn30 = {
    'bar-0': 'barroom.n.01',  # the place where you drink
    'bar-3': 'measure.n.07',  # bar in music, indicates time
    'bar-5': 'bar.n.07',   # a unit for pressure
    'chair-0': 'chair.n.01',  # the thing where you sit on
    'day-0': 'day.n.01',
    'day-1': 'day.n.05',
    'day-3': 'day.n.02'
}

wn17_to_wikipedia = {
    'chair-0': 'chair-furniture'
}

plurals = ['bars', 'chairs', 'days']  # file used to remove plurals of the word to be disambiguated from the context

# from https://en.wikipedia.org/wiki/Chair_(disambiguation), 14.11.2017
# a list of senses in wikipedia disambiguation page

wikipedia_senses = [('chair-furniture',
           'A chair is a piece of furniture with a raised surface supported by legs, commonly used to seat a single person. Chairs are supported most often by four legs and have a back; however, a chair can have three legs or can have a different shape. Chairs are made of a wide variety of materials, ranging from wood to metal to synthetic material (e.g. plastic), and they may be padded or upholstered in various colors and fabrics, either just on the seat (as with some dining room chairs) or on the entire chair. Chairs are used in a number of rooms in homes (e.g. in living rooms, dining rooms, and dens), in schools and offices (with desks), and in various other workplaces. A chair without a back or arm rests is a stool, or when raised up, a bar stool. A chair with arms is an armchair; one with upholstery, reclining action, and a fold-out footrest is a recliner. A permanently fixed chair in a train or theater is a seat or, in an airplane, airline seat; when riding, it is a saddle or bicycle saddle; and for an automobile, a car seat or infant car seat. With wheels it is a wheelchair; or when hung from above, a swing. An upholstered, padded chair for two people is a \'loveseat\', while if it is for more than two person it is a couch, sofa, or settee; or if is not upholstered, a bench. A separate footrest for a chair, usually upholstered, is known as an ottoman, hassock, or pouffe.'
           ),

          (
              'chairman',
              'The chairman (also chairperson, chairwoman or chair) is the highest officer of an organized group such as a board, a committee, or a deliberative assembly. The person holding the office is typically elected or appointed by the members of the group. The chairman presides over meetings of the assembled group and conducts its business in an orderly fashion. When the group is not in session, the officer\'s duties often include acting as its head, its representative to the outside world and its spokesperson. In some organizations, this position is also called president (or other title), in others, where a board appoints a president (or other title), the two different terms are used for distinctly different positions.'
          ),

          ('chair-rail_chair',
           'The earliest rail chairs, made of cast iron and introduced around 1800, were used to fix and support cast-iron rails at their ends; they were also used to join adjacent rails. In the 1830s rolled T-shaped (or single-flanged T parallel rail) and I-shaped (or double-flanged T parallel or bullhead) rails were introduced; both required cast-iron chairs to support them. Originally, iron keys were used to wedge the rail into the vertical parallel jaws of the chair; these were superseded by entirely wooden keys. The wooden keys were formed from oak, steam softened and then compressed with hydraulic presses and stored in a drying house. When inserted into the chair, exposure to the wet atmosphere caused the key to expand, firmly holding the rail. The wedge may be on the inside or outside of the rail. In Britain they were usually on the outside. Chairs have been fixed to the sleeper using wooden spikes (trenails), screws, fang-bolts or spikesIn most of the world, flat-bottomed rail and baseplates became the standard. However, in Britain, bullhead rail-and-chairs remained in use until the middle of the twentieth century. They are now largely obsolete but can still be found on the London Underground, some sidings and at London Waterloo Platforms 1-4.'
           ),

          ('chair-entertainment',
           'Chair Entertainment Group, LLC (commonly referred to as Chair Entertainment, stylized as ChAIR) is an American video game developer based in Salt Lake City, Utah, and is a subsidiary of Epic Games.'
           ),

          ('chair-conformation',
           'A cyclohexane conformation is any of several three-dimensional shapes that a cyclohexane molecule can assume while maintaining the integrity of its chemical bonds. The internal angles of a flat regular hexagon are 120°, while the preferred angle between successive bonds in a carbon chain is about 109.5°, the tetrahedral angle. Therefore, the cyclohexane ring tends to assume certain non-planar (warped) conformations, which have all angles closer to 109.5° and therefore a lower strain energy than the flat hexagonal shape. The most important shapes are called chair, half-chair, boat, and twist-boat. The molecule can easily switch between these conformations, and only two of them—chair and twist-boat—can be isolated in pure form. Cyclohexane conformations have been extensively studied in organic chemistry because they are the classical example of conformational isomerism and have noticeable influence on the physical and chemical properties of cyclohexane.'
           ),

          ('electrical-chair',

           'Execution by electrocution, performed using an electric chair, is a method of execution originating in the United States in which the condemned person is strapped to a specially built wooden chair and electrocuted through electrodes fastened on the head and leg. This execution method, conceived in 1881 by a Buffalo, New York, dentist named Alfred P. Southwick, was developed throughout the 1880s as a "humane alternative" to hanging, and first used in 1890. This execution method has been used in the United States and, for a period of several decades, in the Philippines (its first use was in 1924, last in 1976). Historically, once the condemned person was attached to the chair, various cycles (differing in voltage and duration) of alternating current would be passed through the individual\'s body, in order to cause fatal damage to the internal organs (including the brain). The first, more powerful, jolt of electric current is intended to pass through the head and cause immediate unconsciousness and brain death. The second, less powerful, jolt is intended to cause fatal damage to the vital organs. Death may also be caused by electrical overstimulation of the heart. Although the electric chair has long been a symbol of the death penalty in the United States, its use is in decline due to the rise of lethal injection, which is widely believed to be a more humane method of execution. Although some states still maintain electrocution as a method of execution, today, it is only maintained as a secondary method that may be chosen over lethal injection at the request of the prisoner, except in Tennessee, where it may be used if the drugs for lethal injection are not available, without input from the prisoner. As of 2014, electrocution is an optional form of execution in Alabama, Florida, South Carolina, and Virginia. They allow the prisoner to choose lethal injection as an alternative method. In the state of Kentucky, the electric chair has been retired, except for those whose capital crimes were committed prior to March 31, 1998, and who choose electrocution; inmates who do not choose electrocution and inmates who committed their crimes after the designated date are executed by lethal injection. In the state of Tennessee, the electric chair is available for use if lethal injection drugs are unavailable, or otherwise, if the inmate so chooses and if their capital crime was committed before 1999. The electric chair is an alternate form of execution approved for potential use in Arkansas and Oklahoma if other forms of execution are found unconstitutional in the state at the time of execution. On February 8, 2008, the Nebraska Supreme Court determined that execution by electric chair was a "cruel and unusual punishment" under the state\'s constitution. This brought executions of this type to an end in Nebraska, the only remaining state to retain electrocution as its sole method of execution.'
           )]


# a list of extended stopwords
stop_extended = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost",
                 "alone", "along", "already", "also", "although", "always", "am", "among", "amongst", "amoungst",
                 "amount",
                 "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway", "anywhere", "are", "around",
                 "as", "at", "back", "be", "became", "because", "become", "becomes", "becoming", "been", "before",
                 "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both",
                 "bottom", "but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de",
                 "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either",
                 "eleven", "else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone",
                 "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first",
                 "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further",
                 "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter",
                 "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however",
                 "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep",
                 "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile",
                 "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself",
                 "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone",
                 "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto",
                 "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per",
                 "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems",
                 "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so",
                 "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such",
                 "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence",
                 "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv",
                 "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to",
                 "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up",
                 "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence",
                 "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether",
                 "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with",
                 "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]

# the stopwords from nltk
'''
        stop = 
        {'yourself', 'again', 'should', 'over', 'with', 'd', 'the', 'once', 'ours', 't', 'herself', 'those', 'o', 'ain',
         'how', 'into', 'on', 'be', 'but', 'is', 'other', 'a', 'which', 's', 'mightn', 'here', 'by', 'some', 'no', 
         'between', 'its', 'up', 'below', 'only', 'aren', 'mustn', 'it', 'her', 'own', 'been', 'while', 'further', 
         'weren', 'yourselves', 'our', 'did', 'not', 'both', 'after', 'we', 'has', 'of', 'y', 'out', 'so', 'under', 
         'theirs', 'during', 'don', 'in', 'isn', 'this', 'me', 'down', 'then', 'too', 'if', 'before', 'about', 'where', 
         'any', 'these', 'such', 'against', 'most', 'when', 'hasn', 'being', 'or', 'for', 'same', 'than', 'few', 
         'because', 'them', 'just', 'until', 'won', 'haven', 'didn', 'myself', 'why', 'an', 'am', 'i', 'through', 'nor', 
         'needn', 'who', 'does', 'couldn', 'shan', 'yours', 'hadn', 'do', 'will', 'they', 'itself', 'doesn', 're', 
         'his', 'wasn', 'wouldn', 'you', 'above', 'very', 'my', 'were', 'at', 'ma', 'him', 'whom', 'there', 'she', 
         'that', 'ourselves', 'from', 'shouldn', 'now', 'have', 'doing', 'what', 'and', 'll', 'your', 'hers', 'was', 
         'as', 'all', 've', 'themselves', 'he', 'more', 'can', 'having', 'himself', 'their', 'to', 'each', 'm', 'off', 
         'are', 'had'}
'''