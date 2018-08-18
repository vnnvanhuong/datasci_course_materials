import sys


def load_tweet(filename):
    import json

    with open(filename) as f:
        tweets = f.readlines()

    return [json.loads(tweet) for tweet in tweets]


def main():
    """
    Computes the ten most frequently occurring hashtags

    > Run: $ python2.7 top_ten.py output.txt
    """
    tweet_file = sys.argv[1]
    tweet_list = load_tweet(tweet_file)
    hashtags = {}

    for tweet in tweet_list:
        if "entities" not in tweet.keys() or "hashtags" not in tweet["entities"].keys():
            continue

        hts = tweet["entities"]["hashtags"]

        for ht in hts:
            if "text" not in ht.keys():
                continue

            ht_name = ht["text"]
            if ht_name not in hashtags.keys():
                hashtags[ht_name] = 1
            else:
                current_freq = hashtags[ht_name]
                hashtags[ht_name] = current_freq + 1
    count = 1
    for key, freq in hashtags.items():
        if count <= 10:
            print key + " " + str(freq)
            count = count + 1


if __name__ == '__main__':
    main()
