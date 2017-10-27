import tweepy
from credentials import *
from time import sleep
import sys


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def main(argv):
    message = str(argv[0:])
    notify_me(message)
    sys.exit(0)

def notify_me(message):
    api.send_direct_message(screen_name='babetoduarte', text=message)

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print("No message argument provided!")
        sys.exit(1)
