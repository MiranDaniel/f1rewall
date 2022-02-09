import requests
import multiprocessing
import threading


def get():
    requests.get("http://localhost:8080/")


while True:
    multiprocessing.Process(target=get).start()
    threading.Thread(target=get).start()
