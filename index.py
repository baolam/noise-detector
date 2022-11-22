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
THRESHOLD = 45

stop = False
video = cv2.VideoCapture(1)
client = socketio.Client()
bot = telegram.Bot(TOKEN_ID)
ser = serial.Serial("COM7")

def get_time():
  _time = datetime.datetime.now()
  return '{}:{}:{}'.format(_time.hour, _time.minute, _time.second)

def send(noise):
  __ ,frame = video.read()
  frame = cv2.resize(frame, (HEIGHT, WIDTH))

  filename = "noise.png"
  cv2.imwrite(filename, frame)

  caption = "Vào lúc {}, thiết bị phát hiện có tiếng ồn với ngưỡng ước tính là {:.2f}%".format(get_time(), noise)
  bot.send_photo(CHANNEL_ID, photo=open(filename, "rb"), caption=caption)

def esp32():
  global stop
  while not stop:
    analog_value = ser.readline().decode("utf-8") \
      .replace('\n', '')
    analog_value = float(analog_value)
    analog_value = analog_value / 1023 * 100
    print ("Ngưỡng độ ồn là {:.2f}%".format(analog_value))
    data = {
      "time" : get_time(),
      "noise_value" : analog_value * 1023 / 100
    }
    if client.connected:
      client.emit("noise_value", data=data, namespace="/")
    if analog_value > THRESHOLD:
      send(analog_value)

mem = False
def socket():
  client.connect("http://localhost:4000", namespaces=["/"])

threading.Thread(name="Service for esp32", target=esp32).start()
threading.Thread(name="Service for client", target=socket).start()

try:
  while True:
    if not mem and client.connected:
      mem = True
      client.emit("threshold", THRESHOLD, namespace="/")
    if client.connected == False:
      mem = False

except KeyboardInterrupt:
  stop = True