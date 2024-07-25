import twitterbot as tb
import secret, sys

# fetches the hashtag from command line argument
#user = sys.argv[1]
# fetches the credentials dictionary
# using get_credentials function
credentials = secret.get_credentials()
# initialize the bot with your credentials
bot = tb.InstagramBot(credentials['email'], credentials['password'], credentials['username'])
# logging in

#bot.gmail_login()

bot.instagram_login()

bot.join_livestream("https://www.instagram.com/dale_shots")