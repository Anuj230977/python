from telegram import Update  # Import Update for handling updates
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes  # Import necessary classes
from response_engine1 import handle_response, evaluate_math_expression  # Import custom function to handle responses
import os  # For accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from .env file

load_dotenv()  # Load environment variables from .env file

TOKEN = os.getenv("TOKEN")  # Get the bot token from environment variables
BOT_USERNAME = os.getenv("BOT_USERNAME")  # Get the bot username from environment variables

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your math and logic assistant. Ask me anything!")

async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type  # Get the type of chat (private or group)
    text: str = update.message.text  # Get the text of the message
    user_id = update.message.chat.id

    print(f'User ({user_id}) in {message_type}: "{text}"')  # Debugging output
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')  # Debugging output
     # Check if user is in math mode
    if context.user_data.get("awaiting_math"):
        context.user_data["awaiting_math"] = False  # Reset flag
        response = evaluate_math_expression(text)
        print(f'Response sent: "{response}"')
        await update.message.reply_text(response)
        return

    if message_type == 'group':
        if BOT_USERNAME in text:  # Check if the bot is mentioned
            new_text: str = text.replace(BOT_USERNAME, '').strip()  # Remove the bot's username
            response: str = handle_response(new_text)  # Generate a response using the custom function
        else:
            return  # If the bot is not mentioned, do nothing
    else:
        response: str = handle_response(text, context)  # Handle private messages directly

    print(f'Response sent: "{response}"')  # Debugging output
    await update.message.reply_text(response)  # Send the response back to the group

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update "{update}" caused error "{context.error}"')  # Log the error for debugging

if __name__ == "__main__":
    print("Starting bot...")  # Print a message indicating the bot is starting
    application = Application.builder().token(TOKEN).build()  # Create the bot application with the token
    application.add_handler(MessageHandler(filters.TEXT, handle_message))  # Add a message handler for text messages

    application.add_error_handler(error)  # Add the error handler

    print('Bot started successfully!')  # Print a success message
    application.run_polling(poll_interval=3)  # Start polling for updates