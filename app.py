import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone https://github.com/UsergeTeam/Loader ok && cd ok && pip3 install -U -r requirements.txt && nohup bash run &")
