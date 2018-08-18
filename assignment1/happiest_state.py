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


def tweet_score(tweet, existing_terms, sentiment_dict):
    if "text" not in tweet.keys():
        return 0

    term = 0
    score = 1
    tweet_words = tweet["text"].split()
    found_terms = set(tweet_words).intersection(existing_terms)
    if len(found_terms) == 0:
        return 0
    else:
        tweet_scores = [x[score] for x in sentiment_dict if x[term] in found_terms]
        return sum(tweet_scores)


def get_states():
    return {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }


def find_state_abbr(state_name, states):
    for abbr, name in states.items():
        if name == state_name:
            return abbr


def main():
    """
    Returns the name of the happiest state as a string.
    Print the two letter state abbreviation of the state with the highest average tweet sentiment to stdout.

    > Run: $ python2.7 happiest_state.py AFINN-111.txt output.txt
    """
    sentiment_file = sys.argv[1]
    tweet_file = sys.argv[2]

    sentiment_dict = load_sent(sentiment_file)
    tweet_list = load_tweet(tweet_file)
    existing_terms = [x[0] for x in sentiment_dict]
    existing_states = get_states()
    scored_states = {}

    for tweet in tweet_list:
        t_score = tweet_score(tweet, existing_terms, sentiment_dict)

        if "user" not in tweet.keys() or "location" not in tweet["user"].keys():
            continue

        state_abbr = find_state_abbr(tweet["user"]["location"], existing_states)

        if state_abbr is None:
            continue

        if state_abbr not in scored_states.keys():
            scored_states[state_abbr] = t_score
        else:
            existing_core = scored_states[state_abbr]
            scored_states[state_abbr] = existing_core + t_score

    happiest_state, highest_score = "", 0
    for state, score in scored_states.items():
        if score > highest_score:
            happiest_state = state

    print happiest_state


if __name__ == '__main__':
    main()
