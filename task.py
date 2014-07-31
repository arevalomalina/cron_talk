import datetime
from twilio.rest import TwilioRestClient
import random
import sys
from sys import argv
import twitter


# @manager.command means you can run this function from the command line by typing
# python task.py hello
def send_text_reminder():

    phone_numbers = ['6505446088', '4156963852']
    jokes = ["I wouldn't buy anything with velcro... It's a total rip-off",
             "Where do you learn to make ice cream?  Sunday school",
             "Did you hear about the restaurant on the moon?  Great food, no atmosphere",
             "Don't trust atoms.  They make up everything,",
             "Why did the coffee file a police report?  It got mugged"]

    account = "AC98219002f598f68692de0a632d15568f"
    token = "4dc519054f2eaa118e79b2f897837956"
    client = TwilioRestClient(account, token)

    recipient_number = random.choice(phone_numbers)
    joke = random.choice(jokes)
    try:
        client.messages.create(
            to=recipient_number,
            from_="+16173402844",
            body=joke
            )
    except Exception as e:
        print e

def run_twitterbot():
    NGRAMS = int(argv[2])
    corpus = argv[3:]
    chain_dictionary = make_chains(corpus, NGRAMS)
    random_text = make_text(chain_dictionary,NGRAMS)
    post_to_twitter(random_text)

def make_chains(corpus, NGRAMS):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_chains = {}
    for files in corpus:
        words = open(files).read().split()
        for i in range(len(words) - NGRAMS):
            tuple_key = tuple(words[i:i+NGRAMS])
            value = words[i+NGRAMS]
            markov_chains[tuple_key] = markov_chains.get(tuple_key, []) + [value]   
    return markov_chains


def make_text(input_dictionary, NGRAMS):

    key_list = input_dictionary.keys()

    while True:
        random_tuple = random.choice(key_list)
        random_key_check = ord(random_tuple[0][0])
        if random_key_check < ord('a'):
            break

    random_list = list(random_tuple)

    for i in range(0, 20):
        loop_tuple = tuple(random_list[-NGRAMS:])
        next_word = random.choice(input_dictionary[loop_tuple])
        random_list.append(next_word)
        
    random_string = " ".join(random_list).strip(',";:')

    random_string += random.choice(["!", ".", "..."])

    return random_string

def post_to_twitter(random_text):
    api = twitter.Api(consumer_key='SyOShbVqxyr67ULZxLLNk9K3i',
                    consumer_secret='Gs5MHum4LFxJ4uxSH5VOJKgFG9kqPWVupMv8dE9leeosMSjIqT',
                    access_token_key='2572929330-YPMaWiqdSZNO5sBDVeqYnJ7tuhn1hfDwK5UzWuE', 
                    access_token_secret='Y2kCBuTrUAeeLMFnKxrTKqwAbp1h80ZrKpYjF4qYbr8ki')
    status = api.PostUpdate(random_text)


if __name__ == "__main__":
    command=argv[1]
    if command == "twitter":
        run_twitterbot()
    elif command == "send_text":
        send_text_reminder()
