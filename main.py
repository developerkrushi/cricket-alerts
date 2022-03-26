"""This is the main program"""
import asyncio
from lib.telegram import Bot
from lib.api import fetch_data
import time

API_URL = 'https://www.yourapi.com'
API_ID = '12345678'
API_HASH = '7e7dufhe78ehjd8ej8wuwjw8euiwjw8w'

if __name__ == "__main__":
    while True:
        try:
            data = fetch_data(API_URL)
            bot = Bot(API_ID, API_HASH)

            loop = asyncio.get_event_loop()
            loop.run_until_complete(bot.send('+91 1234567890', data))
            loop.close()
            # Sleep for 1 Hr and send alerts again
            time.sleep(3600)
            
        except KeyboardInterrupt:
            break
