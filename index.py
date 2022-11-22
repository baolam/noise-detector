import socketio
import cv2
import telegram
import threading
import datetime
import serial

TOKEN_ID = "5649686016:AAHTvRL-kmPedN02gXVICHeYD2G_F1AHgus"
CHANNEL_ID = 1755272924
WIDTH = 256
HEIGHT = 256

video = cv2.VideoCapture(0)
client = socketio.Client()
bot = telegram.Bot(TOKEN_ID)
ser = serial.Serial()

def get_time():
  _time = datetime.datetime.now()
  return '{}:{}:{}'.format(_time.hour, _time.minute, _time.second)

def send(noise):
  __ ,frame = video.read()
  frame = cv2.resize(frame, (HEIGHT, WIDTH))

  filename = "noise.png"
  cv2.imwrite(filename, frame)

  caption = "Vào lúc {}, thiết bị phát hiện có tiếng ồn với ngưỡng ước tính là {}%".format(get_time(), noise)
  bot.send_photo(CHANNEL_ID, photo=open(filename, "rb"), caption=caption)

def esp32():
  while True:
    analog_value = ser.readline().decode("utf-8") \
      .replace('\n', '')
    print(analog_value)

threading.Thread(name="Service for testing", target=esp32).start()
# client.connect("noise-detector.herokuapp.com", namespaces=["/"])