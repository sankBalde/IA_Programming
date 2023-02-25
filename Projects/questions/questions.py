import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    files = dict()
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename)) as f:
            files[filename] = f.read()

    return files


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    list_tokens = []
    for word in nltk.word_tokenize(document):
        if word.isalpha():
            list_tokens.append(word.lower())
    """Filter out punctuation and stopwords (common words that are unlikely to be useful for querying). 
    Punctuation is defined as any character in string.punctuation (after you import string). 
    Stopwords are defined as any word in nltk.corpus.stopwords.words("english")."""
    final_list = []
    for word in list_tokens:
        if word not in nltk.corpus.stopwords.words("english"):
            for char in word:
                if char not in string.punctuation:
                    final_word = word
                else:
                    final_word = word.replace(char, "")
            final_list.append(final_word)
    return final_list


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    words = set()
    idfs = dict()
    for doc in documents:
        words.update(documents[doc])
    for word in words:
        nbr_doc_with_word = sum(word in documents[doc] for doc in documents)
        if nbr_doc_with_word > 0:
            idfs[word] = math.log(len(documents) / nbr_doc_with_word)
    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    filenames_list = []
    tfids = dict()
    """Files should be ranked according to the sum of tf-idf values 
    for any word in the query that also appears in the file. 
    Words in the query that do not appear in the file should not 
    contribute to the file’s score."""
    for file in files:
        sum_tfids = 0
        for word in query:
            if word in files[file]:
                try:
                    sum_tfids += files[file].count(word) * idfs[word]
                except KeyError:
                    pass
        tfids[file] = sum_tfids
    
    """Recall that tf-idf for a term is computed by multiplying 
    the number of times the term appears in the document by the IDF value for that term."""
    for file in sorted(tfids, key=tfids.get, reverse=True):
        filenames_list.append(file)
    return filenames_list[:n]

def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    # To hold scores of each sentences
    sentences_score = dict()
    
    # Give each score a 'matching word measure' score and 'query term density' score
    for sentence in sentences:

        # every sentence gonna have 2 kinda score
        score = {'matching word measure': 0, 'query term density': 0}

        # count how many word matches to calculate query term density
        matched_words = 0

        for word in query:
            if word in sentences[sentence]:
                score['matching word measure'] += idfs[word]
                matched_words += 1

        # calculate query term density    
        score['query term density'] = matched_words / len(sentences[sentence])

        # set the calculated score for the sentence to its dictionary
        sentences_score[sentence] = score

    # ranking the sentences based on their matching word measure scores first then query term density scores
    ranked_sentences = sorted(sentences_score, key = lambda k: (sentences_score[k]['matching word measure'], sentences_score[k]['query term density']), reverse = True)

    # will take only the top N sentences
    top_n = ranked_sentences[:n]

    return top_n
    
    


if __name__ == "__main__":
    main()
