import json
from tkinter.messagebox import RETRY
import requests

def obterUsuarios():
    r = requests.get('http://127.0.0.1:5000/getUsers')

    return json.loads(r.content)

def getProjetos():
    r = requests.get('http://127.0.0.1:5000/getProjetos')

    return json.loads(r.content)