
from itertools import count
from turtle import title
from telegram.ext import Filters
from telegram import Update
from telegram.ext import Updater, MessageHandler, CommandHandler, CallbackContext

list = \
    [
        "Диденко Д.Н., 43 года, Директор по логистике", 
        "Каруна Т.В., 35 лет, Финансовый директор", 
    ]

def start_program(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Привет, {update.effective_user.first_name}! Вы в базе сотрудников ООО Магнат, что планируете делать:")
    update.message.reply_text(f"Если хотите посмотреть список сотрудников, нажмите - L\nЕсли хотите удалить информацию о сотруднике, нажмите - D\nЕсли хотите добавить сотрудника, нажмите - W")
def UserMessage(update: Update, context: CallbackContext):
    if update.message.text == 'L':
        update.message.reply_text(f"Список сотрудников ООО Магнат:")
        for i in range(len(list)):
            update.message.reply_text(f"{i+1}. {list[i]}")
    if update.message.text == 'D':
        update.message.reply_text(f"Введите порядковый номер сотрудника")
    if update.message.text.isdigit() == True:
        count = int(update.message.text)
        list.pop((count-1))
        update.message.reply_text(f"Запись удалена!")
    if update.message.text == 'W':
        update.message.reply_text(f"Введите информацию о сотруднике")        
    if update.message.text.isdigit() != True and update.message.text !='L' and update.message.text !='D'and update.message.text !='W':
        list.append(update.message.text)
        update.message.reply_text(f"Запись добавлена!")          
    
updater = Updater("5521188367:AAHy85dyM-J4-6t9Cr5o2ZzxgMF-cREgYuQ")
updater.dispatcher.add_handler(CommandHandler("start", start_program))
updater.dispatcher.add_handler(MessageHandler(Filters.text, UserMessage))

print('Server start')
updater.start_polling()
updater.idle()