from google_ngram_downloader import readline_google_store

count = 0
word = 'something'
fname, url, records = next(readline_google_store(ngram_len=1, indices=word[0]))

try:
    record = next(records)

    while record.ngram != word:
        record = next(records)
        print(record.ngram)

    while record.ngram == word:
        count = count + record.match_count
        record = next(records)
        print(record.ngram)

except StopIteration:
    pass