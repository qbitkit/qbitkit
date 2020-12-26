import pandas as pd
import os as pyos

class csv:
    def read(data_path=None):
        df = pd.read_csv(data_path)
        return df
    def write(data_path=None,
              df=pd.DataFrame()):
        df.to_csv(data_path)
        return data_path

class json:
    def read(data_path=None):
        df = pd.read_json(data_path)
        return df

    def write(data_path=None,
              df=pd.DataFrame()):
        df.to_json(data_path)
        return data_path

class excel:
    def read(data_path=None):
        df = pd.read_excel(data_path)
        return df
    def write(data_path=None,
              df=pd.DataFrame()):
        df.to_(data_path)
        return data_path

def file(direction='read',
         directory=pyos.getcwd(),
         filename=None,
         fileType='csv',
         df=pd.DataFrame(),
         fileExt=None):

    if filename == None:
        print('ERROR: No file name specified. Please specify a file name.')
        return None

    if fileType == 'excel':
        fileExt = 'xlsx'
    elif fileType == None:
        fileExt = None
        print(f'WARNING: No file extension value specified for fileType {fileType}')
    else:
        fileExt = fileType

    fullPath = f"{directory}{pyos.path}{filename}.{fileExt}"
    exists = pyos.path.exists(fullPath)

    if direction == 'read':
        print(f'INFO: Reading a {fileType} file from {fullPath}')
        if fileType == 'csv':
            df = csv.read(data_path=fullPath)
        elif fileType == 'json':
            df = json.read(data_path=fullPath)
        elif fileType == 'excel':
            df = csv.read(data_path=fullPath)
        else:
            df = pd.DataFrame()
            print(f'ERROR: Invalid fileType {fileType}. Returning empty dataframe.')
        return df
    elif direction == 'write':
        print(f'INFO: Writing a {fileType} file to {fullPath}')
        if fileType == 'csv':
            csv.write(data_path=fullPath)
        elif fileType == 'json':
            json.write(data_path=fullPath)
        elif fileType == 'excel':
            excel.write(data_path=fullPath)