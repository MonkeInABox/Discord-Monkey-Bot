import os
import discord
import random
from keep_alive import keep_alive
import requests

client = discord.Client()

photos = [
    "https://media.newyorker.com/photos/59095bb86552fa0be682d9d0/master/pass/Monkey-Selfie.jpg",
    "https://static.independent.co.uk/s3fs-public/thumbnails/image/2014/01/14/12/monkey-bananav3.jpg?quality=75&width=982&height=726&auto=webp",
    "https://images.ctfassets.net/cnu0m8re1exe/5ynx8V71ijv3ffOj29IVbU/e334276ebc9cd9ed2b7bbf9401113bf4/chimpmedia.jpg?fm=jpg&fl=progressive&w=660&h=433&fit=fill"
]

facts = [
    "Some monkeys live on the ground, while others live in trees.",
    "There are no monkeys in Antarctica.",
    "Albert II was the first monkey in space in 1949.",
    "Japanese Macaques Enjoy a Relaxing Hot Soak.",
    "A troop refers to a group of monkeys.",
    "The 23rd is getting closer! You better be ready!",
    "I am going to steal all of your personal data!"
]

story = "First blood was drawn by the Kasakela community on January 7, 1974, when a party of six adult Kasakela males consisting of Humphrey, Figan, Jomeo, Sherry, Evered, and Rodolf ambushed the isolated Kahama male Godi while he was feeding on a tree. This was the first time that any of the chimpanzees had been seen to deliberately kill a fellow male chimpanzee. After they had slain Godi, the victorious chimpanzees celebrated boisterously, throwing and dragging branches with hoots and screams. After Godi fell, De was taken out next, and then Hugh. Later on came the elderly Goliath. Throughout the war, Goliath had been relatively friendly with the Kasakela neighbors when encounters occurred. However, his kindness was not reciprocated and he was killed. Only three Kahama males remained: Charlie, Sniff, and Willy Wally, who was crippled from polio. Without a chance to strike back, Charlie was killed next. After his death, Willy Wally disappeared and was never found. The last remaining Kahama male, the young Sniff, survived for over a year. For some time it seemed as if he might escape into a new community or be welcomed back to the Kasakelas, but this did not occur. Sniff, too, fell to the Kasakela war band. Of the females from Kahama, one was killed, two went missing, and three were beaten and kidnapped by the Kasakela males. The Kasakela then succeeded in taking over the Kahama's former territory. These territorial gains were not permanent, however. With the Kahama gone, the Kasakela territory now butted up directly against the terristory of another chimpanzee community, called the Kalande. Cowed by the superior strength and numbers of the Kalande, as well as a few violent skirmishes along their border, the Kasakela quickly gave up much of their new territory. Furthermore, when they moved back northward, the Kasakela were harassed by Mitumba foragers, who also outnumbered the Kasakela community. Eventually hostilities died down and the regular order of things was restored."


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("monkeyHello"):
        await message.channel.send("Ooh ooh ahh ahh!")
    if message.content.startswith("monkeyFacts"):
        await message.channel.send(random.choice(facts))
    if message.content.startswith("monkeyPic"):
        await message.channel.send(random.choice(photos))
    if message.content.startswith("monkeyStory"):
        await message.channel.send(story)
    if message.content.startswith("monkeyHelp"):
        await message.channel.send(
            "monkeyHello, monkeyFacts, monkeyPic, monkeyStory, monkeyJohnLennon"
        )
    if message.content.startswith("monkeyJohnLennon"):
        await message.channel.send("kill john lennon kill john lennon")
        await message.channel.send(
            "https://i.ytimg.com/vi/xR3E_t3qjgA/hqdefault.jpg")
    if message.content.startswith("monkeyWiki"):
        n = requests.get("https://en.wikipedia.org/wiki/Special:Random")
        await message.channel.send(n)
    if message.content.startswith("monkeyMovie"):
        await message.channel.send(
            "https://media0.giphy.com/media/2FayTY8z5FsBbLLBS/200.gif")
    if message.content.startswith("monkeyDance"):
        await message.channel.send(
            "https://tenor.com/view/monkey-dance-swag-gif-14656700")
    if message.content.startswith("monkeyThrow"):
        await message.channel.send(
            "https://tenor.com/view/racoon-throw-monkey-gif-23872817")


keep_alive()
client.run(os.getenv("TOKEN"))
