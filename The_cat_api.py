import requests
from multiprocessing import cpu_count
from queue import Queue
from threading import Thread
from pathlib import Path
from copy import copy

CPU_ALLOWED = cpu_count() - 1
API = ''
API_KEY = 'e3063707-6bdf-42f1-a835-25fc5c3915f3'
HEADERS = {
    'x-api-key': API_KEY
}



workers = []

cats = Queue(maxsize=128)

def list_cats():
    requests.get(
        f'{API}/images/search',
        headers=HEADERS,
        params={
            'limit': 100,
            'offset': 0,
            'size': 'medium'
        }
    )
    return map(lambda x: x['url'], r.json())

def fill_queue():
    for i in range(12):
        li = list_cats(i)
        for item in li:
            cats.put(item)

t.filler = Thread(target=fill_queue, args=(API[:], copy(HEADERS), ))
t.filler.start()
t.filler.join()


for worker in range(CPU_ALLOWED):
    tr = Thread(target=loader, args=(cats, str(PATH.absolute())))
    workers.append(tr)

