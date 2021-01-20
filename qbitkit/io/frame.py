import pandas as __pd__
import qbitkit.io.file as __f__


class Frame:
    def get_frame(data=None):
        """Return a pandas DataFrame optionally populated with specified data from keyword arguments

        Args:
            data (dict): specify data to populate the Pandas DataFrame with. (default None)
        Returns:
            pandas.DataFrame: Empty DataFrame or dataframe populated with data specified using the 'data' keyword argument."""

        df = __pd__.DataFrame(data=data)
        return df

    def save_frame(frame=get_frame(),
                   pth='data.csv',
                   file_type='csv'):
        """Save a specified Pandas DataFrame as a specified file type at a specified location.

        Args:
            frame (pandas.DataFrame): specify the dataframe that we will be saving to disk. (default get_frame())
            pth (str): specify the path where you want to save the dataframe. (default 'data.csv')
            file_type (str): what structure (type of file) to use when saving to disk. Can be one of 'csv', 'json', or 'excel'. (default 'csv')
        Returns:
            str: path the data was written to"""
        if file_type == 'csv':
            __f__.excel.write(data_path=pth,
                              df=frame)
        if file_type == 'json':
            __f__.excel.write(data_path=pth,
                              df=frame)
        if file_type == 'excel':
            __f__.excel.write(data_path=pth,
                              df=frame)
        return pth

    def fill_nan(self=get_frame(),
                 value=0):
        """Fill NaN values with a specified value.

        Args:
            self(pandas.DataFrame): DataFrame to Fill NaN values on. (default get_frame())
            value(int): Value to replace NaN values with. (default 0)
        Returns:
            pandas.DataFrame: DataFrame with NaN values replaced with the specified value."""
        nan_values_replaced = self.fillna(value)
        return nan_values_replaced
