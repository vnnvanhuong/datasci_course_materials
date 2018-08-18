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


def main():
    """
    Compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet.
    The sentiment of a tweet is equivalent to the sum of the sentiment scores for each term in the tweet.
    Run: $ python2.7 tweet_sentiment.py AFINN-111.txt output.txt
    """
    sentiment_file = sys.argv[1]
    tweet_file = sys.argv[2]

    sentiment_dict = load_sent(sentiment_file)
    tweet_list = load_tweet(tweet_file)
    terms = [x[0] for x in sentiment_dict]

    term = 0
    score = 1

    for tweet in tweet_list:
        tweet_words = tweet["text"].split()
        found_terms = set(tweet_words).intersection(terms)
        if len(found_terms) == 0:
            print 0
        else:
            tweet_scores = [x[score] for x in sentiment_dict if x[term] in found_terms]
            print sum(tweet_scores)


if __name__ == '__main__':
    main()
