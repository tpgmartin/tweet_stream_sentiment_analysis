import configparser
import tweepy

config = configparser.ConfigParser()
config.read('config.ini')

print(config['TWITTER']['CONSUMER_KEY'])