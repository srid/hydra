import datetime
from flask import Response, Module

main = Module(__name__)

app_start = datetime.datetime.now()

@main.route('/')
def index():
    return "instance uptime: %s" % (datetime.datetime.now() - app_start)
    

@main.route('/src')
def expose_self():
    return Response(open(__file__).read(), mimetype='text/plain')
    
