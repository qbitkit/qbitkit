import pandas as pd
import os as pyos
from qbitkit.error import error as qbitkit_error

def get_support_status(self):
    fileIO_support_status = 'experimental'
    qbitkit_error.errors.experimental_feature(feature_state=fileIO_support_status,
                                              resource_name='file I/O',
                                              additional_notes='For more information on forthcoming Elasticsearch support, see https://github.com/brianlechthaler/qbitkit/issues/4')
    return fileIO_support_status

get_support_status()

class csv:
    def read(data_path=None):
        """Read a CSV from a specified path.

        Keyword arguments:
        data_path -- specify a path to read CSV data from. (default None)"""
        df = pd.read_csv(data_path)
        return df
    def write(data_path=None,
              df=pd.DataFrame()):
        """Write a CSV to a specified path.

        Keyword arguments:
        data_path -- specify a path to write the CSV data to. (default None)"""
        df.to_csv(data_path)
        return data_path

class json:
    def read(data_path=None):
        """Read JSON data from a file at a specified path.

        Keyword arguments:
        data_path -- specify a path to read JSON data from. (default None)"""
        df = pd.read_json(data_path)
        return df

    def write(data_path=None,
              df=pd.DataFrame()):
        """Write JSON data to a file at a specified path.

        Keyword arguments:
        data_path -- specify a path to write JSON data to. (default None)"""
        df.to_json(data_path)
        return data_path

class excel:
    def read(data_path=None):
        """Read Microsoft Office Excel data from a file at a specified path.

        Keyword arguments:
        data_path -- specify a path to read Microsoft Office Excel data from. (default None)"""
        df = pd.read_excel(data_path)
        return df
    def write(data_path=None,
              df=pd.DataFrame()):
        """Write Microsoft Office Excel data to a file at a specified path.

        Keyword arguments:
        data_path -- specify a path to write Microsoft Office Excel data to. (default None)"""
        df.to_(data_path)
        return data_path

def file(direction='read',
         directory=pyos.getcwd(),
         filename='data',
         fileType='csv'):
    """High-level function for both reading and writing files.

    Keyword arguments:
    direction -- specify whether to 'read' or 'write' data. (default 'read')
    directory -- specify a directory from which to build a path to save a file to. (default pyos.getcwd())
    filename -- specify a filename to save the file to. Will be appended to the directory to form a path without an extension. (default 'data')
    fileType -- specify the type of file you wish to save the file in. choose from 'excel', 'csv' or 'json'. (default 'csv')"""
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