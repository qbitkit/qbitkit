import pandas as __pd__
from qbitkit.error import error as __qbitkit_error__


def get_support_status():
    fileIO_support_status = 'experimental'
    __qbitkit_error__.Errors.support_status(feature_state=fileIO_support_status,
                                            resource_name='file I/O')
    return fileIO_support_status


get_support_status()


class Csv:
    def read(data_path=None):
        """Read a CSV from a specified path.

        Args:
            data_path (str): specify a path to read CSV data from. (default None)
        Returns:
            pandas.DataFrame: Pandas DataFrame from the contents of the CSV file we read"""
        # Read a DataFrame from the specified path.
        df = __pd__.read_csv(data_path)
        # Return the DataFrame.
        return df
    def write(data_path=None,
              df=__pd__.DataFrame()):
        """Write a CSV to a specified path.

        Args:
            data_path (str): specify a path to write the CSV data to. (default None)
        Returns:
            str: the path we wrote the CSV data to"""
        # Write a CSV file to the specified path.
        df.to_csv(data_path)
        # Return the path the data was written to.
        return data_path


class Json:
    def read(data_path=None):
        """Read JSON data from a file at a specified path.

        Args:
            data_path (str) specify a path to read JSON data from. (default None)
        Returns:
            pandas.DataFrame: Pandas DataFrame from the contents of the JSON file we read"""
        # Read a JSON file from the specified path.
        df = __pd__.read_json(data_path)
        # Return the DataFrame.
        return df

    def write(data_path=None,
              df=__pd__.DataFrame()):
        """Write JSON data to a file at a specified path.

        Args:
            data_path (str) specify a path to write JSON data to. (default None)
            df (pandas.DataFrame): DataFrame you wish to write to disk. (default pandas.DataFrame())
        Returns:
            str: the path you wrote the specified DataFrame to"""
        # Write a JSON file to the specified path.
        df.to_json(data_path)
        # Return the path the JSON data was written to.
        return data_path


class Excel:
    def read(data_path=None):
        """Read Microsoft Office Excel data from a file at a specified path.

        Args:
            data_path (str): specify a path to read Microsoft Office Excel data from. (default None)
            df (pandas.DataFrame): DataFrame you wish to write to disk. (default pandas.DataFrame())
        Returns:
            str: the path you wrote the specified DataFrame to"""
        # Read an Excel (XLSX) file from the specified path.
        df = __pd__.read_excel(data_path)
        # Return the DataFrame.
        return df

    def write(data_path=None,
              df=__pd__.DataFrame()):
        """Write Microsoft Office Excel data to a file at a specified path.

        Args:
            data_path (str): specify a path to write Microsoft Office Excel data to. (default None)
            df (pandas.DataFrame): DataFrame you wish to write to disk. (default pandas.DataFrame())
        Returns:
            str: the path you wrote the specified DataFrame to."""
        # Write an Excel (XLSX) file to the specified path.
        df.to_(data_path)
        # Return the path the Excel (XLSX) file was written to.
        return data_path
