from storages.backends.s3boto3 import S3Boto3Storage

class DocStorage(S3Boto3Storage):
    bucket_name = 'uolst-tracker'
    custom_domain = '{}.s3.amazonaws.com'.format(bucket_name)
    location = 'docs'
    file_overwrite = False