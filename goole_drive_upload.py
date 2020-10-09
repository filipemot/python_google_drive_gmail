from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#Login to Google Drive and create drive object
g_login = GoogleAuth()
drive = GoogleDrive(g_login)
# Importing os and glob to find all PDFs inside subfolder
import os


file = open('teste.txt')
fn = os.path.basename(file.name)
file_drive = drive.CreateFile({'title': fn })
file_drive.SetContentString(file.read())
file_drive.Upload()


permission = file_drive.InsertPermission({
                        'type': 'anyone',
                        'value': 'anyone',
                        'role': 'reader'})


print(file_drive['alternateLink'])