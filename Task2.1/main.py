
from bot_command import*
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("5225273947:AAHN_W0RfVUTsAbKfxCpMC9qvh0GR-mkyFw").build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("eval", my_eval))

print('server start')
app.run_polling()