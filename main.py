from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_comands import *

app = ApplicationBuilder().token("5465627393:AAGsEo1BpUOOp95jrOCRHerYM_S4TVI8xRA").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("rational", rational_command))
app.add_handler(CommandHandler("complex", complex_command))
app.run_polling()