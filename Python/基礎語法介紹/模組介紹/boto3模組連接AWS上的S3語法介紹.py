import boto3
import re
import sys
import os

class S3Helper(object):
    """
    需要下載boto3模塊
    """

    def __init__(self):
        self.access_key = S3_FILE_CONF.get("ACCESS_KEY")
        self.secret_key = S3_FILE_CONF.get("SECRET_KEY")
        self.region_name = S3_FILE_CONF.get("REGION_NAME")

        # 連接S3
        self.s3 = boto3.resource(
            service_name='s3',
            region_name=self.region_name,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        )

        self.client = boto3.client(
            service_name='s3',
            region_name=self.region_name,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
        )

    def download_file_s3(self, bucket_name, file_name, local_file):
        """
        從S3下載指定文件到本地
        需要本地運行程序的目錄下新建一個local_file完整目錄
        :param bucket_name: 桶名稱
        :param file_name: 要下載的文件，所在路徑
        :return: 下載完成返回True，下載出問題返回False，並打印錯誤
        """

        bucket = self.s3.Bucket(bucket_name)

        for obj in bucket.objects.all():
            if obj.key == file_name:
                p = re.compile(r'.*/(.*)')
                result = p.search(file_name).group(1)

                down_file = local_file + result
                try:
                    bucket.download_file(file_name, down_file)
                    return True
                except Exception as e:
                    print('出錯了：' + str(e))
                    return False

    def get_list_s3(self, bucket_name, file_name):
        """
        用來列舉出該目錄下的所有文件
        :param bucket_name: 桶名稱
        :param file_name: 要查詢的文件夾
        :return: 該目錄下所有文件列表
        """
        # 用來存放文件列表
        file_list = []

        response = self.client.list_objects_v2(
            Bucket=bucket_name,
            Delimiter='/',
            Prefix=file_name,
        )

        for file in response['Contents']:
            s = str(file['Key'])
            p = re.compile(r'.*/(.*)(\..*)')
            if p.search(s):
                s1 = p.search(s).group(1)
                s2 = p.search(s).group(2)
                result = s1 + s2
                file_list.append(result)
        return file_list

    def upload_file_s3(self, file_name, bucket, s3_dir):
        """
        上傳本地文件到s3指定文件夾下
        :param file_name: 本地文件路徑
        :param bucket: 桶名稱
        :param s3_dir:要上傳到的s3文件夾名稱
        :return: 上傳成功返回True，上傳失敗返回False，並打印錯誤
        """
        res = sys.platform
        p = re.compile(r'\w{1}')
        s = p.search(res).group()

        if s == 'w':
            p = re.compile(r'.*\\(.*)(\..*)')
        else:
            p = re.compile(r'.*/(.*)(\..*)')

        if p.search(file_name):
            s1 = p.search(file_name).group(1)
            s2 = p.search(file_name).group(2)
            file = s1 + s2
        s3_file = s3_dir + file

        try:
            self.s3.Object(bucket, s3_file).upload_file(file_name)
        except Exception as e:
            print('出錯了：' + str(e))
            return False
        return True


if __name__ == '__main__':
    S3_FILE_CONF = {
        "ACCESS_KEY": "你自己的",
        "SECRET_KEY": "你自己的",
        "REGION_NAME": "你自己的",

        "DOWN_BUCKET_NAME": "桶的名稱",
        "DOWN_FILE_NAME": "需要下載的s3的文件目錄",
        "DOWN_LOCAL_FILE": "你本地的目錄",

        "GET_BUCKET_NAME": "桶的名稱",
        "GET_FILE_NAME": "需要列表的目錄",

        "UPLOAD_FILE_NAME": "你本地要上傳的文件",
        "UPLOAD_BUCKET_NAME": "桶的名稱",
        "UPLOAD_S3_DIR": "S3需要上傳的目錄",
    }
    s3 = S3Helper()
    res = s3.download_file_s3(S3_FILE_CONF["DOWN_BUCKET_NAME"], S3_FILE_CONF["DOWN_FILE_NAME"], S3_FILE_CONF["DOWN_LOCAL_FILE"])
    print(res)
    file_list = s3.get_list_s3(S3_FILE_CONF["GET_BUCKET_NAME"], S3_FILE_CONF["GET_FILE_NAME"])
    print(file_list)
    res = s3.upload_file_s3(S3_FILE_CONF["UPLOAD_FILE_NAME"], S3_FILE_CONF["UPLOAD_BUCKET_NAME"], S3_FILE_CONF["UPLOAD_S3_DIR"])
    print(res)