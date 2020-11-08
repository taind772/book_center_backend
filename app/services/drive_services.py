from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class DriveServices:
    g_auth = GoogleAuth(settings_file='services/drive_config/settings.yaml')
    g_auth.LocalWebserverAuth()

    drive = GoogleDrive(g_auth)

    @classmethod
    def upload_to_drive(cls, file, name, content_type=None):
        drive_file = cls.drive.CreateFile({'title': name})
        drive_file.content = file
        if content_type is not None:
            drive_file['mimeType'] = content_type
        drive_file.Upload()
        drive_file.InsertPermission({
            'type': 'anyone',
            'role': 'reader'
        })
        return drive_file['alternateLink']