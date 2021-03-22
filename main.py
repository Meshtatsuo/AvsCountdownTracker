import discord
import os

client = discord.Client()
global gameCutDowns
global seasonCutDowns

global file_object



@client.event
async def on_ready():
        global seasonCutDowns
        global file_object
        print('We have logged in as {0.user}'.format(client))
        print('season tally read from file...'.format(client))
        file_object = open("seasontally.txt", "r")
        fileResult = file_object.readlines()
        file_object.close()
        seasonCutDowns = int(''.join(str(x) for x in fileResult))


@client.event
async def on_connect():
        print('Connection successful')
        global gameCutDowns
        global seasonCutDowns
        gameCutDowns = 0
        seasonCutDowns = 0


@client.event
async def on_disconnect():
        global file_object
        global seasonCutDowns
        with open('seasontally.txt', 'w'):
            pass
            write(SeasonTally)
@client.event
async def on_close():
        global file_object
        global seasonCutDowns
        with open('seasontally.txt', 'w'):
            pass
            write(SeasonTally)


@client.event
async def on_message(message):
    global gameCutDowns
    global seasonCutDowns

    if message.author == client.user:
        return

    if message.content.startswith('!seasontally'):
            print('command [!seasontally] received. Executing...'.format(client))
            if 'seasonCutDowns' in globals():
                await message.channel.send('Total cutdowns this season: ' + str(seasonCutDowns))
            else:
                seasonCutDowns = 0
                file_object = open("seasontally.txt","w")
                file_object.write(str(seasonCutDowns))
                file_object.close()
                await message.channel.send('Someone fucked up their code and I lost my tally so season cutdowns are now ' + str(seasonCutDowns))

    if message.content.startswith('!gametally'):
            print('command [!gametally] received. Executing...'.format(client))
            if 'gameCutDowns' in globals():
                await message.channel.send('Total cutdowns this game: ' + str(gameCutDowns))
            else:
                gameCutDowns = 0
                await message.channel.send('gameCutDowns not initialized, so now current game tally is ' + str(gameCutDowns))

    if message.content.startswith('!newgame'):
            print('command [!newgame] received. Executing...'.format(client))
            gameCutDowns = 0
            await message.channel.send('New game started, game cutdowns reset. GO AVS!')
            await message.channel.send(file=discord.File('goavsgo.gif'))


    if message.content.startswith('!cutdown'):
            print('command [!cutdown] received. Executing...'.format(client))
            if 'gameCutDowns' in globals():
                gameCutDowns += 1
                if 'seasonCutDowns' in globals():
                    seasonCutDowns += 1
                    file_object = open("seasontally.txt","w")
                    file_object.write(str(seasonCutDowns))
                    file_object.close()
                else:
                    seasonCutDowns = 1
                    file_object = open("seasontally.txt","w")
                    file_object.write(str(seasonCutDowns))
                    file_object.close()
                await message.channel.send(file=discord.File('cutdown.png'))
                await message.channel.send('C    U    T    D    O    W    N')
                await message.channel.send('Game Cutdown Tally: ' + str(gameCutDowns))
                await message.channel.send('Season Cutdown Tally: ' + str(seasonCutDowns))

            else:
                gameCutDowns = 1
                if 'seasonCutDowns' in globals():
                    seasonCutDowns += 1
                    file_object = open("seasontally.txt","w")
                    file_object.write(str(seasonCutDowns))
                    file_object.close()
                else:
                    seasonCutDowns = 1
                    file_object = open("seasontally.txt","w")
                    file_object.write(str(seasonCutDowns))
                    file_object.close()
                await message.channel.send(file=discord.File('cutdown.png'))
                await message.channel.send('C    U    T    D    O    W    N')
                await message.channel.send('Game Cutdown Tally: ' + str(gameCutDowns))
                await message.channel.send('Season Cutdown Tally: ' + str(seasonCutDowns))



client.run(os.getenv('TOKEN'))
