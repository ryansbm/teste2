from main import *
import os
import boto3
import botocore


class S3bucket(QMainWindow):

    def bucket():
        pass
        # s3 = boto3.resource('s3')
        # bucket = s3.Bucket('sbmdatabases')

        os.system(
            'aws s3 cp s3://buildsbm/carbon/carbon-hml-backend.zip C:/Users/ryans/OneDrive/Documentos/BucketDownloads')
