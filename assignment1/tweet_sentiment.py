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
    sentiment_file = sys.argv[1]
    tweet_file = sys.argv[2]

    sentiment_dict = load_sent(sentiment_file)
    tweet_list = load_tweet(tweet_file)
    terms = [x[0] for x in sentiment_dict]

    for tweet in tweet_list:
        encoded_tweet = tweet["text"]
        words = encoded_tweet.split()
        scores = set(words).intersection(terms)
        if len(scores) == 0:
            print 0
        else:
            total = [x[1] for x in sentiment_dict if x[0] in scores]
            print sum(total)


if __name__ == '__main__':
    main()
