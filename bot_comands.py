from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
from complex import Complex

# Приветствие
async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

# Команда помощь, знать какие команды есть
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/help\n/rational\n/complex')

# работа с рациональными числами
async def rational_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = float(items[1])
    sign = items[2]
    y = float(items[3])
    await update.message.reply_text(f'{x} {sign} {y} =  {result(x,sign,y)}')

# работа с комплексными числами
async def complex_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x_Re = float(items[1])
    if items[2] == '+':
        x_Im = float(items[3])
    elif items[2] == '-':
        x_Im = -1 * float(items[3])
    sign = items[6]
    y_Re = float(items[7])
    if items[8] == '+':
        y_Im = float(items[9])
    elif items[8] == '-':
        y_Im = -1 * float(items[9])
    x = Complex(x_Re,x_Im)
    y = Complex(y_Re,y_Im)
    await update.message.reply_text(f'{x} {sign} {y} =  {result(x,sign,y)}')

# Арифместические действия
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




