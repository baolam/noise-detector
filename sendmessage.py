import telegram
import cv2

TOKEN_ID = "5649686016:AAHTvRL-kmPedN02gXVICHeYD2G_F1AHgus"
CHANNEL_ID = 1755272924
bot = telegram.Bot(TOKEN_ID)

bot.send_photo(CHANNEL_ID, photo=open("example.png", "rb"), caption="Hello world")