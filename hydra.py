import socket
import datetime
import markdown2
import urllib2
from flask import Flask, Response

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
    html = ''.join([
        '<style type="text/css">'
        'body {font-family: Arial, Helvetica, sans-serif; margin: 5% 24%; background-color: #eeeeee; line-height: 160%; color: #5A4735;}'
        'h1,h2,h3 {font-family: Georgia, "Times New Roman", Times, serif; letter-spacing: 2px; color: #284907;}'
        'a,a:hover,a:visited {color: brown; text-decoration: none;}'
        'a:hover {text-decoration: underline;}'
        '</style>',
        '<title>' + title + '</title>',
        html,
        '<hr />',
        '<a href="{0}">View markdown source</a>'.format(url),
        '<br />', '<br />',
        '<span style="font-size: 60%; color: #888888;">Powered by <a href="http://flask.pocoo.org/">Flask</a>, '
        '<a href="http://blog.nearlyfreespeech.net/2010/04/03/pools-arbitrary-http-servers-resource-reservation-and-scalability/"'
        '>NFS Pools</a>, Dropbox, Komodo and ExpanDrive; '
        '<a href="/src">view site source</a>'
    ])
    return html
    
    
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
