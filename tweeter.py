import tweepy
#import tweepy.Cursor as tweetFind

API_key = "bSh5wvnGDnoE0HShQjbLcDCj5"

API_secret_key = "mwyr7FEk1z54uqhqxRSnHCoEM9QgdNVfEPNofH6gU3VwIbgfcs"

Access_token = "2953318536-Pm32gN5okawo4lcZlzpIIxfzvRpAuPWIZcbP9lT"

Access_token_secret = "BYzfYILbGoVrCfPt2exw4JBLnDBP8eKWDETOftiO285Ff" 
auth = tweepy.OAuthHandler(API_key,API_secret_key)
auth.set_access_token(Access_token,Access_token_secret)

api = tweepy.API(auth)
data = input("Enter the Keyword: ")
search = tweepy.Cursor(api.search, q=data,result_type="recent", lang="en").items(5)
count = 1
for item in search:
	print("Tweet "+str(count))
	count = count+1
	print("Tweet text: "+item.text)
	print (item.created_at)

	print ("Retweet: "+str(item.retweet_count))

	# print the username who published the tweet
	print ("Username: "+item.user.name)

	# print the location of the user who published the tweet
	print ("Location: "+item.user.location)

	# print the language code of the tweet
	print (item.metadata['iso_language_code'])

	# print the search result type
	print (item.metadata['result_type'])

	# print the device/source from which the tweet has been published
	# e.g. Twitter for Android, Twitter for iPhone, Twitter Web Client, etc.
	print ("Device: "+item.source+"\n\n\n\n\n")