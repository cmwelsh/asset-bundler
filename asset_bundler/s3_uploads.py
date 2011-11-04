from boto.s3.connection import S3Connection
from boto.s3.key import Key

from asset_bundler.config import aws


def upload_assets():
    def uploadResultToS3(bucket,id,srcDir):
        c = boto.connect_s3()
        b = c.get_bucket(bucket)
        k = Key(b)
        for path,dir,files in os.walk(srcDir):
            for file in files:
                k.key = id + "/" + os.path.relpath(os.path.join(path,file),srcDir)
                k.set_contents_from_filename(os.path.join(path,file))
                b.set_acl('public-read', k.key)

    conn = S3Connection(aws.AWS_ACCESS_KEY, aws.AWS_SECRET_KEY)
    bucket = conn.get_bucket('row27')
    k = Key(bucket)
    k.key = 'assets/lmu/lmubasketball/20111104173422/js/site.min.gz.js'
    k.set_contents_from_filename('site.min.gz.js', policy='public-read', headers={'Content-Encoding': 'gzip'})