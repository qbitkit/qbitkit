import modin.pandas as pd


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