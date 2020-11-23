import time
import telebot
from telebot import types
import json
import urllib3
import keep_alive



# Token
bot = telebot.TeleBot("[token]")



# Start
http = urllib3.PoolManager()
print("APIcord")
print("Logs:")

@bot.message_handler(commands=['nice'])
def nice(message):
	bot.reply_to(message, "Thank you! You're nice too 👍")

@bot.message_handler(commands=['start', 'help', 'commands', 'info'], func = lambda message: True)
def help(message):
  bot.reply_to(message, '𝗔𝗣𝗜𝗰𝗼𝗿𝗱 🎃\n𝗠𝗲𝗺𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀: /meme\n𝗜𝗺𝗮𝗴𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀: /img\n𝗙𝗮𝗰𝘁 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀: /fact\n𝗔𝗯𝗼𝘂𝘁 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀: /aboutabout\n𝗠𝗼𝗿𝗲 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀: /more')

@bot.message_handler(commands=['aboutabout'])
def aboutabout(message):
  bot.reply_to(message, "About the bot\nPrefix: No prefix\n/about: Credits\n/license: License\n/invite: Displays bot invite\n/privacy: Bot Privacy Policy\n/code: Source code\n/help: Displays commands\n/botstats: Bot stats")

@bot.message_handler(commands=['more'])
def more(message):
  bot.reply_to(message, "𝗠𝗼𝗿𝗲\n/𝚌𝚑𝚞𝚌𝚔𝚗𝚘𝚛𝚛𝚒𝚜: Random Chuck Norris Joke\n/say <words>: The bot something for you\n/hug: A hug, for you, my friend\n/delete <amount>: Delete message\n/purge <amount>: Delete message")
  #embed.add_field(name=prefix + "ft <language code> <text>", value="Fun Translations (https://funtranslations.com) \n For more info of the language codes enter here: https://funtranslations.com/api", inline=True)

@bot.message_handler(commands=['img'], func=lambda message: True)
def img(message):
  something = message.text
  if something == "/img coffee":
    jdat = (http.request('GET', 'https://coffee.alexflipnote.dev/random.json'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "𝗛𝗲𝗿𝗲 𝘆𝗼𝘂 𝗵𝗮𝘃𝗲 𝘆𝗼𝘂𝗿 𝗰𝗼𝗳𝗳𝗲𝗲\n" + jsdata['file'])
  elif something == "/img dog":
    jdat = (http.request('GET', 'https://dog.ceo/api/breeds/image/random'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "𝗔 𝗱𝗼𝗴𝗴𝗼! :𝗗\nI wish you'll like this uwu\n" + jsdata['message'])
  elif something == "/img cat":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/cat'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "𝗔 𝗰𝗮𝘁! :𝗗\nkittens & adult kittens\n" + jsdata['link'])
  elif something == "/img panda":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "𝗽 𝗮 𝗻 𝗱 𝗮\n" + jsdata['link'])
  elif something == "/img red panda":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/red_panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "𝗿𝗲𝗱 𝗽𝗮𝗻𝗱𝗮 :)\n" + jsdata['link'])
  elif something == "/img bird":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/birb'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "*𝗯𝗶𝗿𝗱 𝘀𝗼𝘂𝗻𝗱𝘀.𝗺𝗽𝟯*\n" + jsdata['link'])
  elif something == "/img fox":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/fox'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "𝗙𝗶𝗻𝗻𝗲𝗴𝗮𝗻 𝗙𝗼𝘅 𝗮𝗽𝗿𝗼𝘃𝗲𝘀 𝗶𝘁.\n(I think)" + jsdata['link'])
  elif something == "koala":
    jdat = (http.request('GET', 'https://some-random-api.ml/img/koala'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "𝗮\n" + jsdata['link'])
  else:
    bot.reply_to(message, "Image commands\nPrefix: /img\n/img coffee: Random coffee image\n/img dog: Random dog image\n/img cat: Random cat image\nimg panda: Random panda image\n/img red panda: Random red panda image\n/img bird: Random bird image\n/img fox: Random fox image\n/img koala: Random koala image")

@bot.message_handler(commands=['gmeme'], func=lambda message: True)
def gmeme(message):
  one = message.text
  if one.endswith(".jpg"):
    img_type = ".jpg"
  elif one.endswith(".jpeg"):
    img_type = ".jpeg"
  elif one.endswith(".webp"):
    img_type = ".webp"
  elif one.endswith(".png"):
    img_type = ".png"
  elif one.endswith(".gif"):
    img_type = ".gif"
  else:
    bot.reply_to("error, image type not found")
  two = one.replace("/gmeme ", "https://api.memegen.link/images/custom/", 1)
  three = two.replace(" ", "/", 1)
  four = three.replace(" ", img_type + "?background=", 1)
  bot.reply_to(message, "𝗬𝗼𝘂𝗿 𝗺𝗲𝗺𝗲 𝗶𝘀 𝗿𝗲𝗮𝗱𝘆!\n" + four)

@bot.message_handler(commands=['gm'], func=lambda message: True)
def gm(message):
  one = message.text
  if one.endswith(".jpg"):
    img_type = ".jpg"
  elif one.endswith(".jpeg"):
    img_type = ".jpeg"
  elif one.endswith(".webp"):
    img_type = ".webp"
  elif one.endswith(".png"):
    img_type = ".png"
  elif one.endswith(".gif"):
    img_type = ".gif"
  else:
    bot.reply_to("error, image type not found")
  two = one.replace("/gm ", "https://api.memegen.link/images/custom/", 1)
  three = two.replace(" ", "/", 1)
  four = three.replace(" ", img_type + "?background=", 1)
  bot.reply_to(message, "𝗬𝗼𝘂𝗿 𝗺𝗲𝗺𝗲 𝗶𝘀 𝗿𝗲𝗮𝗱𝘆!\n" + four)
  
@bot.message_handler(commands=['fact'], func=lambda message: True)
def fact(message):
  not_not_important = message.text
  factstuff = not_not_important.replace("/fact ", "")
  if factstuff == "cat":
    jdat = (http.request('GET', 'https://catfact.ninja/fact'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "Did you know...\n" + jsdata['fact'])
  elif factstuff == "dog":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/dog'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "Did you know...\n" + jsdata['fact'])
  elif factstuff == "panda":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/panda'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "Did you know...\n" + jsdata['fact'])
  elif factstuff == "fox":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/fox'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "Did you know...\n" + jsdata['fact'])
  elif factstuff == "bird":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/bird'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "Did you know...\n" + jsdata['fact'])
  elif factstuff == "koala":
    jdat = (http.request('GET', 'https://some-random-api.ml/facts/koala'))
    jsdata = (json.loads(jdat.data.decode('utf-8')))
    bot.reply_to(message, "Did you know...\n" + jsdata['fact'])
  elif factstuff == "DEL":
    bot.reply_to(message, "Discord Extreme List, i don't know who is but, sounds like a nice name :)")
  elif factstuff == "bots.gg":
    bot.reply_to(message, "It's a very good Discord bot list, 70/10")
  elif factstuff == "discord.bots.gg":
    bot.reply_to(message, "It's a very good Discord bot list, 70/10")
  else:
    bot.reply_to(message, "Facts\nPrefix: /fact\n/fact cat: Random cat fact\n/fact dog: Random dog fact\n/fact panda: Random panda fact\n/fact fox: Random fox fact\n/fact bird: Random bird fact\n/fact koala: Random koala fact")

@bot.message_handler(commands=['say'], func=lambda message: True)
def echox(message):
  mtext = message.text
  printer = mtext.replace("/say", "", 1)
  bot.reply_to(message, printer)

@bot.message_handler(commands=['echo'], func=lambda message: True)
def echox(message):
  mtext = message.text
  printer = mtext.replace("/echo", "", 1)
  bot.reply_to(message, printer)

keep_alive.keep_alive()
bot.polling()
