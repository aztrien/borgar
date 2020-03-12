import discord
import math
import random
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Client active.')

@client.command()
async def info(ctx):
    c0 = '**Use . before each command.**\n.info: lists all current commands\n.ping: displays latency to bot server, wherever it is\n'
    c1 = '.8ball: magic 8 ball\n.poke: makes Norton mad\n.quad: does the quadratic formula, input format is .quad a b c\n'
    c2 = '.rps: plays Rock Paper Scissors against Norton\n'
    await ctx.send(f'{c0}{c1}{c2} More commands coming soon? I need more ideas. :pensive:\n')
    
@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def ball8(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def poke(ctx):
    await ctx.send('*loud screaming noises*')

@client.command()
async def quad(ctx, a = None, b = None, c = None):
    if a and b and c:
        a = float(a)
        b = float(b)
        c = float(c)
        if a == 0:
            await ctx.send('"a" value must not be zero.')
        else:
            delta = (math.pow(b, 2) - (4*a*c))
            if delta > 0:
                solution1 = (-b + math.sqrt(delta))/(2*a)
                solution2 = (-b - math.sqrt(delta))/(2*a)
                await ctx.send(f'Solutions: {solution1} , {solution2}')
            elif delta == 0:
                solution1 = (-b/(2*a))
                await ctx.send(f'Solution: {solution1}')
            else:
                await ctx.send('Answer is not real')
    else:
        await ctx.send('.quad needs an input in the form of `a b c`')

@client.command(aliases=['rockpaperscissors'])
async def rps(ctx, *, choice):
    actions = ['Paper',
               'Rock',
               'Scissors']
    if choice == 'Paper' or 'Rock' or 'Scissors':
        botchoice = random.choice(actions)
        if choice == botchoice:
            await ctx.send(f'{choice} vs. {botchoice}... Draw.')
        else:
            if choice == 'Paper':
                if botchoice == 'Rock':
                    await ctx.send(f'{choice} vs. {botchoice}... You win.')
                else: await ctx.send(f'{choice} vs. {botchoice}... Norton wins.')
            
            elif choice == 'Rock':
                if botchoice == 'Scissors':
                    await ctx.send(f'{choice} vs. {botchoice}... You win.')
                else: await ctx.send(f'{choice} vs. {botchoice}... Norton wins.')
            
            elif choice == 'Scissors':
                if botchoice == 'Paper':
                    await ctx.send(f'{choice} vs. {botchoice}... You win.')
                else: await ctx.send(f'{choice} vs. {botchoice}... Norton wins.')
    
    else: await ctx.send('Invalid input, you can enter either .rps Rock, .rps Scissors, or .rps Paper.')

client.run('NjcyNjMxMzQwNDAyODY4MjM1.Xk93MA.IVSUmw4J6fhGOExLONG47S82eyQ')

