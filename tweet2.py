from twython import Twython

CONSUMER_KEY = "e0EfOjpo8DxrLpoySgyDBPz30"
CONSUMER_SECRET = "OL3SWGQG7ud1T2Yr6cUKqmT7vbCDasy756hxfbEbAYGRyo7aqN"
ACCESS_TOKEN = "44809869-KoEUfS0lHmTlEBEjgXesQzlbk6cgEs1dFfPeQh7fy"
ACCESS_TOKEN_SECRET = "vZNnkv2atcoPacopvXvRcY9qFqzYvvLXem8M9G8D1e8XT"


twitter = Twython(
                    CONSUMER_KEY,
                    CONSUMER_SECRET,
                    ACCESS_TOKEN,
                    ACCESS_TOKEN_SECRET
)
message = 'Bummer I broke it.....wookieware.com'

twitter.update_status(status=message)

print("Tweeted: "+ message)
