import click as ck
from qbitkit.io.file import csv, json, excel
class qbitctl():
    def __init__(self):
        print('WARNING: qbitctl is still in development. Use with caution and avoid usage in production environments.')
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