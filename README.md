"# nlp2017_group3" 

Instructions:
1. Install google-ngram-downloader https://pypi.python.org/pypi/google-ngram-downloader.
2. Run "google-ngram-downloader cooccurrence" to download the data.
3. Seperate only files that concern only words to a seperate folder. In other words remove number and pos-tag files. Also extract files.
4. Update the path for the bi-gram data to config.py.
5. Update path for the test corpus to config.py. (Must be in the same format as the sample corpus.)
6. Navigate to root folder and run "pip install -r requirements.txt" to install dependencies
7. Run one of the algorithms: wikipedia_google_books_bigram.py, wikipedia_simple_lesk.py or wn3_google_books_bigram. Note: only word "chair" usable for wikipedia related algorithms.

Two files will be outputted to the results folder. The "dump"-file records overlaps for all senses where as "output" has less information.

Folder structure:
- data folder contains the original senseval2 data (corpora-folder) and also the modified smaller datasets that we used
- src contains the algorithms and some helpful scripts to help with the manual labeling to WordNet 3.0
- results contains results that we previosly made