import sys
import re


def load_tweet(filename):
    import json

    with open(filename) as f:
        tweets = f.readlines()

    return [json.loads(tweet) for tweet in tweets]


def main():
    """
    Compute the term frequency histogram. The frequency of a term can be calculated as
    [# of occurrences of the term in all tweets]/[# of occurrences of all terms in all tweets]

    > Run: $ python frequency.py output.txt
    """
    tweet_file = sys.argv[1]
    tweet_list = load_tweet(tweet_file)
    all_terms = {}

    for tweet in tweet_list:
        tweet_words = tweet["text"].split()

        for word in tweet_words:
            exp = re.compile('^\w+$')
            if not re.search(exp, word):
                continue

            if word not in all_terms.keys():
                all_terms[word] = 1
            else:
                existing_core = all_terms[word]
                all_terms[word] = existing_core + 1

    all_freqs = [freq for key, freq in all_terms.items()]

    for key, freq in all_terms.items():
        print key + " " + str(freq/float(sum(all_freqs)))


if __name__ == '__main__':
    main()
