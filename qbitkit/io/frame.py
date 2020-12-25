import pandas as pd
import qbitkit.io.file as f
class frame:
    def get_frame(data=None):
        df = pd.DataFrame(data=data)
        return df
    def save_frame(frame=get_frame(),
                   pth='data.csv',
                   file_type='csv'):
        if file_type == 'csv':
            f.excel.write(data_path=pth,
                        df=frame)
        if file_type == 'json':
            f.excel.write(data_path=pth,
                        df=frame)
        if file_type == 'excel':
            f.excel.write(data_path=pth,
                        df=frame)
