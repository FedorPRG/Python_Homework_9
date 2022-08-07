from calendar import c
from turtle import update
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
#from log import log
import controller as c

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def com_1_format(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/first первый формат вывода\n\
/second второй формат вывода')

async def com_2_family(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Введите фамилию для поиска\n\
Формат ввода: /family Фамилия')

async def com_3_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Введите фамилию, имя, номер телефона, коментарий\n\
Формат ввода: /add Фамилия Имя номер коментарий')

async def com_4_data(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Введите фамилию для удаления\n\
Формат ввода: /del Фамилия')

async def com_1_viev_print1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    stroka=c.com_1_viev_print(1)
    await update.message.reply_text(f'{stroka}')

async def com_1_viev_print2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    stroka=c.com_1_viev_print(2)
    await update.message.reply_text(f'{stroka}')

async def com_2_search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    family = update.message.text
    family = family.split(' ')
    family = str(family[1])    
    stroka=c.com_2_search(family)
    await update.message.reply_text(f'{stroka}')

async def com_3_add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text
    data = data.split(' ')
    family = str(data[1])
    name=str(data[2])
    number=str(data[3])
    coment=str(data[4])
    c.com_3_add(family, name, number, coment)
    await update.message.reply_text('Контакт добавлен')

async def com_4_del(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text
    data = data.split(' ')
    family = str(data[1])
    stroka=c.com_4_del(family)
    await update.message.reply_text(f'{stroka}')

async def com_5_write(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    c.com_5_write()
    await update.message.reply_text('Справочник сохранен на сервере в phonebook.json')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #log(update, context)
    await update.message.reply_text(f'/1 Показать весь справочник (запись в файл)\n\
/2 Поиск номера телефона по фамилии\n\
/3 Добавить контакт\n\
/4 Удалить контакт\n\
/5 Запись справочника в phonebook.json\n\
/help')


