from asset_bundler.resolve_assets import get_asset_urls, get_asset_filenames
from asset_bundler import minify
from asset_bundler.s3_uploads import upload_assets

def start_bundler(options):
    print options
    return
    url = "http://coachsark.local/"
    base_dir = '/Users/cmwelsh/code/dev/coachsark/project/html/'
    base_url = 'http://coachsark.local/'

    asset_urls = get_asset_urls(url)
    asset_filenames = get_asset_filenames(base_dir, base_url, **asset_urls)

    minify.javascript(asset_filenames['script_filenames'])
    minify.styles(asset_filenames['style_filenames'])

    #upload_assets();