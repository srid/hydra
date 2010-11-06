from flask import Module, render_template
import markdown2
import urllib2

pages = Module(__name__)


u = 'http://dl.dropbox.com/u/87045/p/{0}.md.txt'
@pages.route('/p/<pagename>')
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