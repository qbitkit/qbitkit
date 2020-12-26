import click as ck
class qbitctl():
    @ck.command()
    @ck.option('--fileType',
               prompt='No File Type Specified.\nFile Type (example: csv, json, excel) :',
               help='File type to use when loading data from a file.\nExamples: csv, json, excel')
    @ck.option('--filePath',
               help='Path of file to use when loading data from a file.')
    def qbitctl(fileType,
                filePath):
        msg = f"ERROR: qbitctl CLI Not implemented yet.\nFile Type: {fileType}\n File Path: {filePath}"
        print(msg)
        return msg