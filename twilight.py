from twython import TwythonStreamer
CONSUMER_KEY = "e0EfOjpo8DxrLpoySgyDBPz30"
CONSUMER_SECRET = "OL3SWGQG7ud1T2Yr6cUKqmT7vbCDasy756hxfbEbAYGRyo7aqN"
ACCESS_TOKEN = "44809869-KoEUfS0lHmTlEBEjgXesQzlbk6cgEs1dFfPeQh7fy"
ACCESS_TOKEN_SECRET = "vZNnkv2atcoPacopvXvRcY9qFqzYvvLXem8M9G8D1e8XT"

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            #print("@{}: {}".format(username, tweet))
            if username == 'netwookie':
                print(username)
                print(tweet)


stream = MyStreamer(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)
print('streaming')
stream.statuses.filter(track='vlan')
