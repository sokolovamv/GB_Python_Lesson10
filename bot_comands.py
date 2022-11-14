from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
from complex import Complex


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/help\n/rational\n/complex')

async def rational_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    sign = items[2]
    y = int(items[3])
    await update.message.reply_text(f'{x} {sign} {y} =  {result(x,sign,y)}')

def result(x,sign,y):
    if sign == '+':
        return x + y
    elif sign == '-':
        return x - y
    elif sign == '*':
        return x * y
    elif sign == '/':
        return x / y
    else:
        return "Бот не понимает тебя("


async def complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x_Re = int(items[1])
    if items[2] == '+':
        x_Im = int(items[3])
    elif items[2] == '-':
        x_Im = -1 * int(items[3])
    sign = items[6]
    y_Re = int(items[7])
    if items[8] == '+':
        y_Im = int(items[9])
    elif items[8] == '-':
        y_Im = -1 * int(items[9])
    x = Complex(x_Re,x_Im)
    y = Complex(y_Re,y_Im)
    await update.message.reply_text(f'{x} {sign} {y} =  {result(x,sign,y)}')

