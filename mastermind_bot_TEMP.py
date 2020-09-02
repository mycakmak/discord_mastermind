# This discord bot template is developed by github/mycakmak
# Reach me at mycakmak1@gmail.com
# Bot language is in Turkish
import discord, random

BOT_TOKEN = "ENTER YOUR BOT TOKEN HERE"
game_status = 0
current_game_length = 0

def has_doubles(n):
    return len(set(str(n))) < len(str(n))

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global game_status
    global current_game_length
    global my_number

    if message.author == client.user:
        return

    if message.content.startswith("!avatar") and message.mentions:
        await message.channel.send(message.mentions[0].avatar_url)

    if message.content.startswith("!baslat"):
        if game_status == 1:
            await message.channel.send("Şu anda zaten " + str(current_game_length) + " basamaklı bir oyun oynanıyor. " + message.author.mention)
        elif len(message.content) < 7:
            await message.channel.send("Basamak sayısını girmediniz. " + message.author.mention)
        else:
            if message.content[7].isnumeric() and message.content[7] != 0:
                length_of_game = int(message.content[7])
                my_number = ''.join(random.sample("0123456789", length_of_game))
                game_status = 1
                current_game_length = length_of_game
                await message.channel.send("" + str(length_of_game) + " basamaklı bir sayı tuttum. " + message.author.mention)
                print("GAME ON:", my_number)
            else:
                await message.channel.send("Lütfen geçerli bir başlatma komutu giriniz. " + message.author.mention)

    if message.content.startswith("!") and message.content[1:].isnumeric():
        counter_plus = 0
        counter_minus = 0
        if game_status == 0:
            await message.channel.send("Oyun henüz başlamadı. " + message.author.mention)
        else:
            author_guess = message.content[1:current_game_length+1]
            if my_number == author_guess:
                await message.channel.send("Kazanan: " + message.author.mention + " :partying_face: :confetti_ball: :fireworks:")
                print("Kazanan: " + message.author.mention)
                game_status = 0
            elif has_doubles(author_guess):
                await message.channel.send("Tahmininde tekrar eden sayılar olmaması gerekiyor. " + message.author.mention)
            elif len(my_number) != len(author_guess):
                await message.channel.send("Tahmin edilen sayı " + str(len(my_number)) + " basamaklı." + message.author.mention)
            else:
                for x in range(current_game_length):
                    if author_guess[x]==my_number[x]:
                        counter_plus = counter_plus + 1
                    elif author_guess[x] in my_number:
                        counter_minus = counter_minus + 1
                await message.channel.send("" + str(author_guess) + ": " + "+" + str(counter_plus) + " -" + str(counter_minus))

    if message.content.startswith("!yardım"):
        await message.channel.send("Komutlar ! ile başlamaktadır. \n !baslat5 komutuyla oyun başlar, !12345 şeklinde tahmin yaparsınız." + message.author.mention)

client.run(BOT_TOKEN)
