"""This module speaks with Telegram API"""
from telethon import TelegramClient


class Bot:
    """Implements API methods"""
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash

    async def send(self, usr, msg):
        """method to send message"""
        # Initialise telegram client with API codes
        async with TelegramClient('session_name', self.api_id, self.api_hash) as client:
            # Start the process
            await client.start()
            # Send the message
            await client.send_message(usr, msg)
