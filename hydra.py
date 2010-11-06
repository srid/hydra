import socket
import datetime
import markdown2
import urllib2
from flask import Flask, Response, render_template

app = Flask(__name__)
app.debug = True
app_start = datetime.datetime.now()


@app.route('/')
def index():
    return "instance uptime: %s" % (datetime.datetime.now() - app_start)
    

@app.route('/src')
def expose_self():
    return Response(open(__file__).read(), mimetype='text/plain')
    

u = 'http://dl.dropbox.com/u/87045/p/{0}.md.txt'
@app.route('/p/<pagename>')
def render_page(pagename):
    url = u.format(pagename)
    html, title = md2html(netcat(url))
    return render_template(
        'page.html',
        html=html, markup_url=url)
    
    
def md2html(md):
    """Return HTML, title"""
    html = markdown2.markdown(md)
    pos1, pos2 = html.find('<h1>'), html.find('</h1>')
    title = html[pos1+4: pos2]
    return html, title

    
def netcat(url):
    return urllib2.urlopen(url).read()
    

if __name__ == '__main__':
    PROD = 'nfshost.com' in socket.gethostname()
    host, port = ('127.0.0.1', 80) if PROD else ('0.0.0.0', 8000)
    app.run(host=host, port=port)
