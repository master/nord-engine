from django.conf import settings
import genshi.builder as bldr
from genshi.core import Markup
from creoleparser import parse_args


def header(args, body, isblock):
    return body


def compass(args, body, isblock):
    from compass import compass_url
    items = map(lambda s: s.split('|'), filter(None, body.splitlines()))
    return bldr.tag.img(src=compass_url(items, width=450, height=450))


def gmap(args, body, isblock):
    if not hasattr(settings, 'GMAP_KEY'):
        return bldr.tag.strong('Error: GMAP_KEY is not set').generate()
    return '<script type="text/javascript" src="http://www.google.com/jsapi?key=%s"></script>' \
           % getattr(settings, 'GMAP_KEY', False)


def html(args, body, isblock):
    return body


macros = {'html': html,
          'compass': compass,
          'gmap': gmap,
          'header': header,          
          }

def macro_func(macro_name, arg_string, body, isblock, environ):
    if macro_name in macros:
        return Markup(macros[macro_name](parse_args(arg_string), body, isblock))
