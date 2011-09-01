import re
from creoleparser.dialects import create_dialect, creole11_base
from creoleparser.core import Parser, fragmentize
from creoleparser.elements import SimpleElement, PreBlock, URLLink, Heading
import genshi.builder as bldr


class AnchorLink(URLLink):
    def re_string(self):
        protocol = r'^\s*(()'
        rest_of_url = r'#.*?)\s*'
        alias = r'(' + re.escape(self.delimiter) + r' *(.*?))? *$'
        return protocol + rest_of_url + alias

    def href(self,mo):
        return mo.group(1)


class HeadingName(Heading):
    def __init__(self, tag, name_tag, token):
        super(Heading,self).__init__(tag, token)
        self.name_tag = name_tag
        self.tags = tag
        self.regexp = re.compile(self.re_string(),re.MULTILINE)
         
    def _build(self,mo,element_store, environ):
        heading_tag = self.tags[len(mo.group(1))-1]
        return bldr.tag.__getattr__(self.name_tag)(
            bldr.tag.__getattr__(heading_tag)(
                fragmentize(mo.group(2),
                            self.child_elements,
                            element_store, environ)),
            name=mo.group(2))


def dialect_base(wiki_root):
    from macros import macro_func

    Creole11Base = creole11_base(wiki_links_base_url=wiki_root,
                                 macro_func=macro_func)

    class Base(Creole11Base):
        simple_element = SimpleElement(token_dict = {
            '**':'strong','//':'em',',,':'sub',
            '^^':'sup','__':'u','##':'code',
            '<>':'center','``':'blockquote'})
        anchor_link = AnchorLink('a', '|')
        headings = HeadingName(['h1','h2','h3','h4','h5','h6'],'a','=')

        def __init__(self):
            super(Base,self).__init__()
            self.link.child_elements = [self.anchor_link] + self.link.child_elements
            
    return Base


def wikify(text, wiki_root):
    parser = Parser(dialect_base(wiki_root))
    return parser.render(text)
