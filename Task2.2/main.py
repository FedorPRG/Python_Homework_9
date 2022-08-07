import controller as c
from bot_command import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
app = ApplicationBuilder().token("5594628689:AAHhsScZKR68wbbv6ZuNkbrS2g8-6DfzyO8").build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("1", com_1_format))
app.add_handler(CommandHandler("2", com_2_family))
app.add_handler(CommandHandler("3", com_3_data))
app.add_handler(CommandHandler("4", com_4_data))
app.add_handler(CommandHandler("5", com_5_write))
app.add_handler(CommandHandler("first", com_1_viev_print1))
app.add_handler(CommandHandler("second", com_1_viev_print2))
app.add_handler(CommandHandler("family", com_2_search))
app.add_handler(CommandHandler("add", com_3_add))
app.add_handler(CommandHandler("del", com_4_del))
print('server start')
app.run_polling()