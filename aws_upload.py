from boto3 import Session
from datetime import datetime

path1 = ""
path2 =""
file1 = "README1.md"
path_to_find_1 = "/Users/nhant/Desktop/customer/README1.md"
file2 = "README2.md"

def create_file_name(file_name):
    file_name_new = ""
    return file_name_new

def find_bucket(s3):

    bucket = s3.Bucket('backup')
    return bucket

def find_file_in_bucket(s3, bucket, file_name):
    today = datetime.now()

    month = today.month
    year = today.year

    bk_path = str(year) + "_" + str(month) + "/"
    bucket_name = s3.Bucket(bucket)

    for obj in bucket_name.objects.filter(Prefix=bk_path):
        full_key = obj.key
        splits = full_key.split('/')
        if file_name == splits[len(splits)-1]:
            print ("file available")
            return True
        else:
            continue

    print("can't find file" + file_name)
    return False

def upload_file_to_bucket(s3, bucket, file_name):
    today = datetime.now()

    month = today.month
    year = today.year

    bk_path = str(year) + "_" + str(month) + "/"
    bucket_name = s3.Bucket(bucket)

    try:
        s3.meta.client.upload_file(file_name, bucket, bk_path + file_name)
    except:
        print("upload error")

    print("upload success" + file_name)


def init_session(s3_key, s3_api):
    conn = Session( aws_access_key_id=s3_key, aws_secret_access_key=s3_api)
    s3 = conn.resource("s3")

    return s3

if __name__ == '__main__':
    try:
        s3 = init_session("", "")

    except:
        print ("some error")


    find1_bool = find_file_in_bucket(s3, "", file1)
    find2_bool = find_file_in_bucket(s3, "", file2)

    if find1_bool!= True:
        upload_file_to_bucket(s3, "", path_to_find_1)

    if find2_bool != True:
        upload_file_to_bucket(s3, "", "README2.md")

    print("exit")
    
