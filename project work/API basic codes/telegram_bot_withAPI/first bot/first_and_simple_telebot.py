# Import required modules
from datetime import datetime  # For working with dates and times
import pytz  # For timezone handling
import requests  # For making HTTP requests
from dotenv import load_dotenv  # For loading environment variables from .env file
import os  # For accessing environment variables


# Set timezone to Indian Standard Time
IST = pytz.timezone('Asia/Kolkata')  # Indian Standard Timezone
# Get current date and time in IST
raw_TS = datetime.now(IST)
curr_date = raw_TS.strftime("%d-%m-%Y")  # Format date as DD-MM-YYYY
curr_time = raw_TS.strftime("%H:%M:%S")  # Format time as HH:MM:SS (24-hour)


# Load environment variables from .env file
load_dotenv()
# Get the Telegram bot token from environment variable
telegram_auth_token = os.getenv("TELEGRAM_AUTH_TOKEN")
# Set the group ID or username (should be numeric chat ID for groups)
telegram_group_id = "Date_and_time_notifier"


# Create the message to send
msg = f"Message received on {curr_date} at {curr_time}"


# Function to send a message to the Telegram group using the bot
def send_msg_on_telegram(message):
    # Construct the Telegram API URL
    telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id=@{telegram_group_id}&text={message}"
    # Send a GET request to the Telegram API
    tel_resp = requests.get(telegram_api_url)

    # Check if the message was sent successfully
    if tel_resp.status_code == 200:
        print("INFO : Notification has been sent on Telegram")
    else:
        print("ERROR: Could not send Message")


# Call the function to send the message
send_msg_on_telegram(msg)
