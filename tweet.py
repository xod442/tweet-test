import tweepy

CONSUMER_KEY = "e0EfOjpo8DxrLpoySgyDBPz30"
CONSUMER_SECRET = "OL3SWGQG7ud1T2Yr6cUKqmT7vbCDasy756hxfbEbAYGRyo7aqN"
ACCESS_TOKEN = "44809869-KoEUfS0lHmTlEBEjgXesQzlbk6cgEs1dFfPeQh7fy"
ACCESS_TOKEN_SECRET = "vZNnkv2atcoPacopvXvRcY9qFqzYvvLXem8M9G8D1e8XT"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Testing....this time with passion!"
api.update_status(status=status)
