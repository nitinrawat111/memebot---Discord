import requests
import discord
import os


client = discord.Client()
API_LINK = "https://meme-api.herokuapp.com/gimme"


def getJsonFromAPI():
  requestData = requests.get(API_LINK)
  jsonData = requestData.json()
  return jsonData


def getRandomMemeUrl():
  try:
    jsonData = getJsonFromAPI()
    randomMemeURL = jsonData["url"]
    return randomMemeURL
  except:
    return "```\nRan into a problem :(\nPlease try again Later..```"


@client.event
async def on_ready():
  print("Logged in as " + client.user.name)


@client.event
async def on_message(message):
  if(message.content == "$meme"):
    randomMemeURL = getRandomMemeUrl()
    await message.channel.send(randomMemeURL)

client.run(os.environ['TOKEN'])