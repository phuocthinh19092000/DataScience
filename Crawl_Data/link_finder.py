from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url= base_url
        self.page_url= page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        #print(tag)
        if  tag == 'a' or tag  == 'link' :
            for (attribute1, value1) in attrs :
                if attribute1 == 'rel' and value1 == 'nofollow':
                    for (attribute2, value2) in attrs:
                        if attribute2 == 'href':
                            url = parse.urljoin(self.base_url, value2)
                            self.links.add(url)

    def page_link(self):
        return self.links

    def error(self, message):
        pass



#finder = LinkFinder('https://www.thenewboston.com/', 'thenewboston.com')
#finder.feed('<link class="FooterNavList__item-link" href="/guide/introduction">Documentation</link>')
