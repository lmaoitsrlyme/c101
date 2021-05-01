import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_files(self, file_from, file_to):
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)

        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = "sl.Av9pLemzczz4o8XSiUnJwwftRlH7e5sVRRMZb-NGZ-mzTL52X03l9oaD5cswUGVFXyKpS5YzDXEYnRtSWqA3zlY2iO9CRvo-SFxwSdiQtg6kIMzaoAv02TTXS0Va1C8-ul1IUdM"
    transferData = TransferData(access_token)

    file_from = input("enter the file path: ")
    file_to = input("enter the destination: ")
    transferData.upload_files(file_from, file_to)
    print("file has been uploaded")







main()