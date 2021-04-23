import pandas as __pd__


class Frame:
    def get_frame(data=None):
        """Return a pandas DataFrame optionally populated with specified data from keyword arguments

        Args:
            data (dict): specify data to populate the Pandas DataFrame with. (default None)
        Returns:
            pandas.DataFrame: Empty DataFrame or dataframe populated with data specified using the 'data' keyword argument."""
        # Create a DataFrame from specified data.
        df = __pd__.DataFrame(data=data)
        # Return generated DataFrame.
        return df

    def fill_nan(self=get_frame(),
                 value=0):
        """Fill NaN values with a specified value.

        Args:
            self(pandas.DataFrame): DataFrame to Fill NaN values on. (default get_frame())
            value(int): Value to replace NaN values with. (default 0)
        Returns:
            pandas.DataFrame: DataFrame with NaN values replaced with the specified value."""
        # Replace NaN values with the specified value.
        nan_values_replaced = self.fillna(value)
        # Return the DataFrame with NaN values replaced with the specified value.
        return nan_values_replaced
