import os
'''
from google_ngram_downloader import readline_google_store

name, url, records = next(readline_google_store(ngram_len=5))

next(records)
'''
def get_files_in_top_dir(file_location):
    ''' Return all files in a list in file location in reference to current directory. '''
    files = []

    for (path, dirnames, filenames) in os.walk(file_location):
        for filename in filenames:
            if filename.startswith(''):
                files.append(filename)
        break
    return files


files = get_files_in_top_dir('./')
print(files)