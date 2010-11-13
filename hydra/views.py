import urllib2
from docutils.core import publish_parts


def my_view(context, request):
    src = 'http://dl.dropbox.com/u/87045/p/blog.rst'
    html = rst2html(netcat(src))
    return {'html': html}


def rst2html(rst):
    html = publish_parts(
        rst,
        writer_name='html',
        settings_overrides={'initial_header_level': 2}
    )['html_body']
    return html


def netcat(url):
    return urllib2.urlopen(url).read()