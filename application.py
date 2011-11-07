from optparse import OptionParser

from asset_bundler import start_bundler

def parse_command_line():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-e", "--extract-url", dest="extract_url",
                      help="URL from which asset include order is extracted")
    parser.add_option("-u", "--base-url", dest="base_url",
        help="URL to your assets folder")
    parser.add_option("-d", "--base-dir", dest="base_dir",
        help="file path to your assets folder")
    
    (options, args) = parser.parse_args()

    if options.extract_url == None:
        parser.error('EXTRACT_URL is required')
    if options.base_url == None:
        parser.error('BASE_URL is required')
    if options.base_dir == None:
        parser.error('BASE_DIR is required')

    return options

def main():
    options = parse_command_line()
    start_bundler(options)

if __name__ == "__main__":
    main()