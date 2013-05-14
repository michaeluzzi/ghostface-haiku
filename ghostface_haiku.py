import context_free
import context_free_reader
import oauth2 as oauth
import json

# twitter version
#haiku = "status="

# non-twitter version
haiku = ""

cfree1 = context_free.ContextFree()
context_free_reader.add_rules_from_file(cfree1, open("ghostface.grammar"))
line1 = cfree1.get_expansion('Five')
haiku += ' '.join(line1)
haiku += '\n'
print ' '.join(line1)

cfree2 = context_free.ContextFree()
context_free_reader.add_rules_from_file(cfree2, open("ghostface.grammar"))
line2 = cfree2.get_expansion('Seven')
haiku += ' '.join(line2)
haiku += '\n'
print ' '.join(line2)

cfree3 = context_free.ContextFree()
context_free_reader.add_rules_from_file(cfree3, open("ghostface.grammar"))
line3 = cfree3.get_expansion('Five')
haiku += ' '.join(line3)
print ' '.join(line3)

# for posting to twitter feed
#CONSUMER_KEY = "Your CONSUMER_KEY"
#CONSUMER_SECRET = "Your CONSUMER_SECRET"
#ACCESS_KEY = "Your ACCESS_KEY"
#ACCESS_SECRET = "Your ACCESS_SECRET"

#consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
#access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
#client = oauth.Client(consumer, access_token)

#tweet = "https://api.twitter.com/1.1/statuses/update.json"
#response, data = client.request(tweet, "POST", haiku)

#tweetResponse = json.loads(data)
#print tweetResponse