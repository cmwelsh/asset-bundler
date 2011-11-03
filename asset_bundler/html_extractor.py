from BeautifulSoup import BeautifulSoup
from urlparse import urljoin

class HtmlExtractor:
    def __init__(self, html, url):
        self.html = html
        self.url = url
        self.soup = BeautifulSoup(html)

    def get_script_urls(self):
        script_tags = self.soup.findAll('script')

        script_urls = []

        for tag in script_tags:
            for attr in tag.attrs:
                if attr[0] == 'src':
                    script_urls.append(attr[1])

        script_urls = map(
            lambda url: urljoin(self.url, url),
            script_urls
        )

        return script_urls


    def get_style_urls(self):
        link_tags = self.soup.findAll('link')

        style_urls = []

        for tag in link_tags:
            for attr in tag.attrs:
                if attr[0] == 'href':
                    if '.css' in attr[1] or '.less' in attr[1]:
                        style_urls.append(attr[1])

        style_urls = map(
            lambda url: urljoin(self.url, url),
            style_urls
        )

        return style_urls