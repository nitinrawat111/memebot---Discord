import requests
import discord
import os


client = discord.Client()
API_LINK = "https://meme-api.herokuapp.com/gimme/"


def getJsonFromAPI(memesCount):
  finalUrl = API_LINK + str(memesCount)
  requestData = requests.get(finalUrl)
  jsonData = requestData.json()
  return jsonData


def getRandomMemesUrls(memesCount):
  try:
    if(memesCount > 50):
      memesCount = 50
    jsonData = getJsonFromAPI(memesCount)
    memesList = jsonData["memes"]
    
    randomMemesUrls = []
    for i in range(memesCount):
      randomMemesUrls.append( memesList[i]["url"] )
    
    return randomMemesUrls
  except:
    return ["```\nRan into a problem :(\nPlease try again Later..```"]


async def sendMultipleMessages(messageList, channel):
  for eachMessage in messageList:
    await channel.send(eachMessage)


@client.event
async def on_ready():
  print("Logged in as " + client.user.name)


@client.event
async def on_message(message):
  if(message.author == client.user):
    return

  if(message.content == "$meme"):
    memesUrls = getRandomMemesUrls(memesCount = 1)
    await sendMultipleMessages(memesUrls, message.channel)

  if(message.content.startswith("$meme ")):
    if(message.content[6:].isdigit()):
      memesCount = int(message.content[6:])
      memesUrls = getRandomMemesUrls(memesCount)
      await sendMultipleMessages(memesUrls, message.channel)


client.run(os.environ['TOKEN'])