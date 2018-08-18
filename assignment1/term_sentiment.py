import sys


def load_sent(filename):
    sent_file = open(filename)
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    return scores.items()


def load_tweet(filename):
    import json

    with open(filename) as f:
        tweets = f.readlines()

    return [json.loads(tweet) for tweet in tweets]


def tweet_score(tweet_words, existing_terms, sentiment_dict):
    term = 0
    score = 1
    found_terms = set(tweet_words).intersection(existing_terms)
    if len(found_terms) == 0:
        return 0
    else:
        tweet_scores = [x[score] for x in sentiment_dict if x[term] in found_terms]
        return sum(tweet_scores)


def main():
    """
    Computes the sentiment for the terms that do not appear in the file AFINN-111.txt.
    For example, if the word soccer always appears in proximity with positive words like great and fun,
    then we can deduce that the term soccer itself carries a positive sentiment.
    """
    sentiment_file = sys.argv[1]
    tweet_file = sys.argv[2]

    sentiment_dict = load_sent(sentiment_file)
    tweet_list = load_tweet(tweet_file)
    existing_terms = [x[0] for x in sentiment_dict]
    new_terms = {}

    for tweet in tweet_list:
        tweet_words = tweet["text"].split()
        non_sentiment_words = set(tweet_words).difference(existing_terms)

        for word in non_sentiment_words:
            if word not in new_terms.keys():
                new_terms[word] = tweet_score(tweet_words, existing_terms, sentiment_dict)
            else:
                existing_core = new_terms[word]
                new_terms[word] = existing_core + tweet_score(tweet_words, existing_terms, sentiment_dict)

    for key, item in new_terms.items():
        print key + " " + str(item)


if __name__ == '__main__':
    main()
