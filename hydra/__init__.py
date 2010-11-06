import socket
import datetime
from flask import Flask
from hydra.views.pages import pages
from hydra.views.main import main

app = Flask(__name__)
app.debug = True
app_start = datetime.datetime.now()
app.register_module(pages)
app.register_module(main)


if __name__ == '__main__':
    PROD = 'nfshost.com' in socket.gethostname()
    host, port = ('127.0.0.1', 80) if PROD else ('0.0.0.0', 8000)
    app.run(host=host, port=port)