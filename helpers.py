import os

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