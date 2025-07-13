from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from response_engine import handle_response

import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

TOKEN: Final = os.getenv("TOKEN")
BOT_USERNAME: Final = os.getenv("BOT_USERNAME")

#commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am your bot. How can I assist you today?')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Here are the commands you can use:\n'
                                     '/start - Start the bot\n'
                                     '/help - Get help information\n'
                                     '/about - Learn more about this bot')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This bot is designed to assist you with various tasks. '
                                     'Feel free to ask me anything!')
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
        
    print('bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Upadate "{update}" caused error "{context.error}"')

if __name__ == '__main__':
    print('Starting bot...')
    app= Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('about', about_command))

    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #errors
    app.add_error_handler(error)

    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)