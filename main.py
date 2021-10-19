from InstagramBot import InstagramBot

username = "dailymicio"
password = "micio2"
bot = InstagramBot("dailymicio", "micio2")
bot.login()

TotalLikes=0
TotalFollows=0
hashtags = ["russiangirl","polskagirl"]

for hashtag in hashtags:
  nLikes=0
  nFollows=0
  arrayLikesFollows =  bot.bot_by_hashtag(hashtag, 12, 4)      #hashtag, 1 like ogni 12 secondi, 1 possibilitá su 4 di seguire chi ha messo la foto(25% di probabilià)
  nLikes += arrayLikesFollows[0]
  nFollows += arrayLikesFollows[1]
  TotalLikes +=nLikes
  TotalFollows +=nFollows
  print("You put: " + str(nLikes) + " Likes and " + str(nFollows) +" Follows for the Hashtag: " + str(hashtag))

print("This session you put: " + str(TotalLikes) + " Likes and " + str(TotalFollows) +" Follows" )

bot.goToFollowing("dailymicio")
print("Start to unfollow " + str(1200) + " People")
bot.unFollow(1200)

bot.closeBrowser()
