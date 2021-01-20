import click as ck
from qbitkit.io.file import csv, json, excel
from qbitkit.error import error as qbitkit_error

def __init__(self):
    none = None
class qbitctl:

    def get_support_status(self):
        qbitctl_support_status = 'experimental'
        qbitkit_error.Errors.support_status(feature_state=qbitctl_support_status,
                                            resource_name='qbitctl',
                                            additional_notes='For more information on forthcoming qbitctl support, see https://github.com/qbitkit/qbitkit/issues/4')
        return qbitctl_support_status

        qbitctl.get_support_status()
    def __init__(self):
        qbitctl.get_support_status()
    class functions:
        @ck.command()
        @ck.option('--fileType',
                   prompt='No File Type Specified.\nFile Type (example: csv, json, excel) :',
                   help='File type to use when loading data from a file.\nExamples: csv, json, excel')
        @ck.option('--filePath',
                   help='Path of file to use when loading data from a file.')
        def qbitctl(fileType,
                    filePath):
            if fileType == 'csv':
                df = csv.read(data_path=filePath)
            elif fileType == 'json':
                df = json.read(data_path=filePath)
            elif fileType == 'excel':
                df = excel.read(data_path=filePath)
            else:
                err = f"ERROR: File type {fileType} not found.\nTry specifying one of csv, json or excel."
                print(err)
            return None
