import pandas as pd
import qbitkit.io.file as f
class frame:
    def get_frame(data=None):
        """Return a pandas DataFrame optionally populated with specified data from keyword arguments

        Keyword arguments:
        data -- specify data to populate the Pandas DataFrame with. (default None)"""
        df = pd.DataFrame(data=data)
        return df
    def save_frame(frame=get_frame(),
                   pth='data.csv',
                   file_type='csv'):
        """Save a specified Pandas DataFrame as a specified file type at a specified location.

        frame -- specify the dataframe that we will be saving to disk. (default get_frame())
        pth -- specify the path where you want to save the dataframe. (default 'data.csv')
        file_type -- what structure (type of file) to use when saving to disk. Can be one of 'csv', 'json', or 'excel'. (default 'csv')"""
        if file_type == 'csv':
            f.excel.write(data_path=pth,
                        df=frame)
        if file_type == 'json':
            f.excel.write(data_path=pth,
                        df=frame)
        if file_type == 'excel':
            f.excel.write(data_path=pth,
                        df=frame)
