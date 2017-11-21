"# nlp2017_group3" 

Download google-ngram-downloader python module.
Run "google-ngram-downloader cooccurrence" to download the data.

Seperate only files that concern only words. In other words remove number and pos-tag files.
Extract files.
Update the path for the bi-gram data to config.py.
Update path for the test corpus to config.py. (Must be in the same format as the sample corpus.)
Update mappings and the results data to "config.py"

Navigate to root folder.
"pip install -r requirements.txt" to install dependencies.

4. Run either wikifier.py depending on the algorithm

Two files will be outputted to results folder. The "data_dump"-file records overlaps for all senses where as "output" has less information.


Folder structure:
- data folder contains the original senseval2 data (corpora-folder) and also the modified smaller datasets that we used
- src contains the algorithms and some helpful scripts to help with the manual labeling to WordNet 3.0
- results contains results that we previosly made