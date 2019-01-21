import configparser
import json
import socket
import tweepy

config = configparser.ConfigParser()
config.read('config.ini')

CONSUMER_KEY = config['TWITTER']['CONSUMER_KEY']
CONSUMER_SECRET = config['TWITTER']['CONSUMER_SECRET']
ACCESS_TOKEN = config['TWITTER']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['TWITTER']['ACCESS_TOKEN_SECRET']

# custom StreamListener class
class TweetStreamListener(tweepy.StreamListener):

    def __init__(self, client_socket):
        self.client_socket = client_socket
    
    # passes data from statuses to the on_status method
    # not sure if this operates expected - want to return True regardless
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg["text"])
            # self.client_socket.send(msg["text"])
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        finally:
            return True

    # might want to handle 420 errors separately
    def on_error(status):
        print(status)
        # ensure stream stays connected in event of error
        return True

if __name__ == "__main__":

    # create a socket object
    s = socket.socket()

    # host = socket.gethostbyname(socket.gethostname())
    host = socket.gethostbyname("localhost")
    # use port number higher than 1024 to run as unprivileged user
    port = 1111
    s.bind((host, port))

    print("Listening on port: %s" % str(port))

    # wait for client connection
    # s.listen(5)
    # establish connection with client
    # client_socket, addr = s.accept()

    # print("Received request from: %s" % str(addr))

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # create stream
    client_socket = 3000
    tweet_stream = tweepy.Stream(auth, TweetStreamListener(client_socket))

    # start stream
    # example filter by "python", will eventually want to handle user submissions
    tweet_stream.filter(track=['python'])
