import discord, random, time

topics = ['eggs','trees','music','animals', 'vehicles',
            'historical figures','social media']
copy_of_topics = []
copy_of_topics = topics

coin = ['heads','tails']

cats = ['CAT.png','CAT2.jpg']

coles = ['cole1','cole2','cole3','cole4','cole5','cole6','cole7','cole8','cole9','cole10']

jokes = {'Why did Susie fall off of the swing?':"Because she had been suffering from narcolepsy her whole life, and at that particular moment it kicked in.",
         "What's sad about four white people driving off of a cliff?":"They were my friends.",
         "A man walks into a bar.":"He is an alcoholic and is ruining his family.", "Why was the boy sad?":"Because he had a frog stapled to his face.",
         "Why did the bike fall over?":"Because it had a negligent owner who didn't wash or oil his bike, resulting in a gear failure which collpased the bike."}

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
                                                    
        if message.content.startswith('c!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if message.content.startswith('c!topic'):
            if len(copy_of_topics) > 0:
                the_pick = random.choice(copy_of_topics)
                copy_of_topics.remove(the_pick)
                await message.channel.send("The topic is..."+the_pick+"! Good luck!")
            else:
                await message.channel.send("You've run out of original topics! Please DM the admin to add more.")

        if message.content.startswith('c!joke'):
            joke, punchline = random.choice(list(jokes.items()))
            await message.channel.send(joke)
            time.sleep(3)
            await message.channel.send(punchline)

        if message.content.startswith('c!help'):
            await message.channel.send("So far, I can greet you (c!hello), give you a topic for puns (c!topic), tell you a joke (c!joke), show you a picture of a gorgeous cat (c!cat), and flip a coin or roll a die (c!flip or c!roll <number of sides>).")

        if message.content.startswith('c!roll'):
            user_input = message.content.split()
            if len(user_input) > 1:
                try:
                    the_roll = random.randint(1, int(user_input[1]))
                    await message.channel.send("You rolled a "+ str(the_roll)+".")
                except ValueError:
                    await message.channel.send("Number not recognized. Please try again.")

        if message.content.startswith('c!flip'):
            coin_flip = random.choice(coin)
            await message.channel.send('The virtual coin landed on '+coin_flip+".")

        if message.content.startswith('c!cat'):
            the_cat = random.choice(cats)
            await message.channel.send('Cat:', file=discord.File(the_cat))

        if message.content.startswith('c!cole'):
            the_cole = random.choice(coles)
            await message.channel.send('Cole:', file=discord.File(the_cole))
            
        if message.content.startswith('c!spam'):                                                     
            command = message.content.split()
            command.pop(0)

            try:
                number = int(command[0])
                if number > 15:
                    await message.channel.send("While this is a spam bot, please limit the amount of times a message is sent so that it does not exceed 15.")
                else:
                    command.pop(0)
                
                    print_string = ''
                    for i in command:
                        print_string += i
                        print_string += ' '

                    for i in range(number):
                        await message.channel.send(print_string)
            except ValueError:
                await message.channel.send("Number not recognized. Please try again")
            
client = MyClient()
client.run('NDk2MTY4NDA0MDQyOTA3NjQ4.DpMvHg.O01P5QAwRi2OoR0t4vCEUqIGXBs')
