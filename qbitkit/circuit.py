import pandas as __pd__


class CircuitFrame:
    """The qbitkit CircuitFrame is an easy way to specify a quantum circuit using a familiar Pandas DataFrame.

    Args:
        df(pandas.DataFrame): (optional) Pandas DataFrame to use as the CircuitFrame"""

    def __init__(self,
                 df=None):
        # Create an empty DataFrame
        empty_dataframe = __pd__.DataFrame()

        # Check if no DataFrame was specified
        if type(df) is not type(empty_dataframe):
            # generate an empty dataframe
            self.df = empty_dataframe
        else:
            self.df = df

        # Remove empty DataFrame from memory
        del empty_dataframe
