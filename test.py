import urllib2

response = urllib2.urlopen('http://lmubasketball.local/')
html = response.read()

from BeautifulSoup import BeautifulSoup          # For processing HTML

soup = BeautifulSoup(html)

script_tags = soup.findAll('script')

script_urls = []

for tag in script_tags:
    for attr in tag.attrs:
        if attr[0] == 'src':
            script_urls.append(attr[1])


from urlparse import urljoin

for url in script_urls:
    print urljoin("http://lmubasketball.local/", url)



link_tags = soup.findAll('link')

style_urls = []

for tag in link_tags:
    for attr in tag.attrs:
        if attr[0] == 'href':
            if '.css' in attr[1] or '.less' in attr[1]:
                print attr[1]
                style_urls.append(attr[1])


from urlparse import urljoin

for url in style_urls:
    print urljoin("http://lmubasketball.local/", url)