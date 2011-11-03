from asset_bundler.get_url import get_url
from asset_bundler.html_extractor import HtmlExtractor

url = "http://lmubasketball.local/"

html = get_url(url)

extractor = HtmlExtractor(html, url)

script_urls = extractor.get_script_urls()

print '\n'.join(script_urls)

style_urls = extractor.get_style_urls()

print '\n'.join(style_urls)
