from asset_bundler.get_url import get_url
from asset_bundler.html_extractor import HtmlExtractor

def get_asset_urls(url):
    html = get_url(url)

    extractor = HtmlExtractor(html, url)

    script_urls = extractor.get_script_urls()
    style_urls = extractor.get_style_urls()

    return dict(script_urls=script_urls, style_urls=style_urls)

def get_asset_filenames(base_dir, base_url, script_urls, style_urls):
    def url_to_filename(url):
        # replace() is a dirty way to go here, but it should work okay
        return url.replace(base_url, base_dir)

    script_urls = filter(lambda url: url.startswith(base_url), script_urls)
    script_filenames = map(url_to_filename, script_urls)

    style_urls = filter(lambda url: url.startswith(base_url), style_urls)
    style_filenames = map(url_to_filename, style_urls)

    return dict(script_filenames=script_filenames, style_filenames=style_filenames)