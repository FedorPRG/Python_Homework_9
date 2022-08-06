from turtle import update
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from log import log

async def my_eval(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    msg = update.message.text
    msg = msg.split(' ')
    msg = str(msg[1])
    exp=eval(msg)
    log(update, context,exp)
    await update.message.reply_text(f'{msg}={exp}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/eval 2.7+3.5\n/help')

