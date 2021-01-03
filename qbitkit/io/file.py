import pandas as pd
import os as pyos
from qbitkit.error import error as qbitkit_error

def get_support_status():
    fileIO_support_status = 'experimental'
    qbitkit_error.errors.support_status(feature_state=fileIO_support_status,
                                        resource_name='file I/O')
    return fileIO_support_status

get_support_status()

class csv:
    def read(data_path=None):
        """Read a CSV from a specified path.

        Args:
            data_path (str): specify a path to read CSV data from. (default None)
        Returns:
            pandas.DataFrame: Pandas DataFrame from the contents of the CSV file we read"""
        df = pd.read_csv(data_path)
        return df
    def write(data_path=None,
              df=pd.DataFrame()):
        """Write a CSV to a specified path.

        Args:
            data_path (str): specify a path to write the CSV data to. (default None)
        Returns:
            str: the path we wrote the CSV data to"""
        df.to_csv(data_path)
        return data_path

class json:
    def read(data_path=None):
        """Read JSON data from a file at a specified path.

        Args:
            data_path (str) specify a path to read JSON data from. (default None)
        Returns:
            pandas.DataFrame: Pandas DataFrame from the contents of the JSON file we read"""
        df = pd.read_json(data_path)
        return df

    def write(data_path=None,
              df=pd.DataFrame()):
        """Write JSON data to a file at a specified path.

        Args:
            data_path (str) specify a path to write JSON data to. (default None)
            df (pandas.DataFrame): DataFrame you wish to write to disk. (default pandas.DataFrame())
        Returns:
            str: the path you wrote the specified DataFrame to"""
        df.to_json(data_path)
        return data_path

class excel:
    def read(data_path=None):
        """Read Microsoft Office Excel data from a file at a specified path.

        Args:
            data_path (str): specify a path to read Microsoft Office Excel data from. (default None)
            df (pandas.DataFrame): DataFrame you wish to write to disk. (default pandas.DataFrame())
        Returns:
            str: the path you wrote the specified DataFrame to"""
        df = pd.read_excel(data_path)
        return df
    def write(data_path=None,
              df=pd.DataFrame()):
        """Write Microsoft Office Excel data to a file at a specified path.

        Args:
            data_path (str): specify a path to write Microsoft Office Excel data to. (default None)
            df (pandas.DataFrame): DataFrame you wish to write to disk. (default pandas.DataFrame())
        Returns:
            str: the path you wrote the specified DataFrame to."""
        df.to_(data_path)
        return data_path