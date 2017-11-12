import os
import xmltodict
import csv
import time

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

def parse_xml(file):
    # Parse the xml-file to
    try:
        fd = open(file)
        doc = xmltodict.parse(fd.read())
    except IOError:
        print('Couldn\'t find the test data')
    finally:
        fd.close()
        return doc


def write_results(data, folder='./', test_type='general'):
    ltime = time.localtime()


    filename = '{}_on_{}_{}_{}_at_{}_{}_{}.csv'.format(test_type, ltime.tm_mday, ltime.tm_mon,
                                                              ltime.tm_year,
                                                              ltime.tm_hour, ltime.tm_min, ltime.tm_sec)



    print(filename)

    with open(filename, 'w') as results:
        log_file = csv.writer(results, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for datarow in data:
            log_file.writerow(datarow)

