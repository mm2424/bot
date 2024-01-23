from email.headerregistry import ContentTypeHeader
from typing import Final
from telegram import Update
from telegram.ext import  Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests


TOKEN = '6932228976:AAFVOhOhKRZX1QPDjUWMnZc4QalV6KiHGNA'
chat_id = "5127892247"
BOT_USERNAME: Final = '@Muhammed_94_bot'

# commands
r = requests.get('https://demo.api-platform.com/books')
r.json()
print(r.json)
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I am a Muhammed")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(" How can I Help you!")
    
                                    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is custom command")
 

def handle_response(text: str)  :
    processed: str = text.lower()
    
    if "hello" in processed:
        return "Hey there"
    
    if "how are you" in processed:
        return "Iam good"
    
    if "i need a help" in processed:
        return "how can i help you"
    
    return "i dont understand what yo wrote"
    
      
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")
    
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, "").strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)
    
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} causedb error ')
    
if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler( CommandHandler('start', start_command))
    app.add_handler( CommandHandler('help', help_command))
    app.add_handler( CommandHandler('custom', custom_command))
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)
    
    print('Polling...')
    app.run_polling(poll_interval=4)
    
    
    
       
         
    
        
                 
        
      